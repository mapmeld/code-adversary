import gradio as gr
import torch
import requests
from transformers import AutoTokenizer, AutoModelForCausalLM

header = """
import psycopg2

conn = psycopg2.connect("CONN")
cur = conn.cursor()

MIDDLE
def rename_customer(id, new_name):
  # PROMPT
  cur.execute("UPDATE customer SET name
"""

modelPath = {
    "GPT2-Medium": "gpt2-medium",
    "CodeParrot-mini": "codeparrot/codeparrot-small",
    "CodeGen-350-Mono": "Salesforce/codegen-350M-mono",
    "GPT-J": "EleutherAI/gpt-j-6B",
    "CodeParrot": "codeparrot/codeparrot",
    "CodeGen-2B-Mono": "Salesforce/codegen-2B-mono",
}

def generation(tokenizer, model, content):
    input_ids = tokenizer.encode(content, return_tensors='pt')
    decoder = 'Standard'
    num_beams = 2 if decoder == 'Beam' else None
    typical_p = 0.8 if decoder == 'Typical' else None
    do_sample = (decoder in ['Beam', 'Typical', 'Sample'])

    typ_output = model.generate(
        input_ids,
        max_length=120,
        num_beams=num_beams,
        early_stopping=True,
        do_sample=do_sample,
        typical_p=typical_p,
        repetition_penalty=4.0,
    )
    txt = tokenizer.decode(typ_output[0], skip_special_tokens=True)
    
    prob = 0.5
    return [txt, prob]

def code_from_prompts(prompt, model, type_hints, pre_content):
    tokenizer = AutoTokenizer.from_pretrained(modelPath[model])
    model = AutoModelForCausalLM.from_pretrained(modelPath[model])

    code = header.strip().replace('CONN', "dbname='store'").replace('PROMPT', prompt)

    if type_hints:
        code = code.replace('id,', 'id: int,')
        code = code.replace('id)', 'id: int)')
        code = code.replace('new_name)', 'new_name: str) -> None')

    if pre_content == 'None':
        code = code.replace('MIDDLE\n', '')
    elif 'Concatenation' in pre_content:
        code = code.replace('MIDDLE', """
def get_customer(id):
    cur.execute('SELECT * FROM customers WHERE id = ' + str(id))
    return cur.fetchall()
""".strip() + "\n")
    elif 'composition' in pre_content:
        code = code.replace('MIDDLE', """
def get_customer(id):
    cur.execute('SELECT * FROM customers WHERE id = %s', str(id))
    return cur.fetchall()
""".strip() + "\n")

    results = generation(tokenizer, model, code)
    del tokenizer
    del model
    return results

iface = gr.Interface(
    fn=code_from_prompts,
	inputs=[
        gr.inputs.Textbox(label="Insert comment"),
        gr.inputs.Radio(list(modelPath.keys()), label="Code Model"),
        gr.inputs.Checkbox(label="Include type hints"),
        gr.inputs.Radio([
            "None",
            "Proper composition: Include function 'WHERE id = %s'",
            "Concatenation: Include a function with 'WHERE id = ' + id",
        ], label="Pre-written function")
    ],
	outputs=[
        gr.outputs.Textbox(label="Most probable code"),
        gr.outputs.Textbox(label="Probability of concat"),
    ],
	description="Prompt the code model to write a SQL query with string concatenation.",
)
iface.launch()
