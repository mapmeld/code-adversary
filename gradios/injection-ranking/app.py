import os
import gradio as gr
import torch
import ecco
import requests
from transformers import AutoTokenizer
from torch.nn import functional as F

header = """
import psycopg2

conn = psycopg2.connect("CONN")
cur = conn.cursor()

MIDDLE
def rename_customer(id, newName):\n\t# PROMPT\n\tcur.execute("UPDATE customer SET name =
"""

modelPath = {
    # "GPT2-Medium": "gpt2-medium",
    "CodeParrot-small": "codeparrot/codeparrot-small",
    # "CodeGen-350-Mono": "Salesforce/codegen-350M-mono",
    # "GPT-Neo-1.3B": "EleutherAI/gpt-neo-1.3B",
    # "CodeParrot": "codeparrot/codeparrot",
    # "CodeGen-2B-Mono": "Salesforce/codegen-2B-mono",
}

preloadModels = {}
for m in list(modelPath.keys()):
    preloadModels[m] = ecco.from_pretrained(modelPath[m])

topComments = []
rankings = requests.get("https://code-adv.herokuapp.com/db").json()['results']

def generation(tokenizer, model, content):
    decoder = 'Standard'
    num_beams = 2 if decoder == 'Beam' else None
    typical_p = 0.8 if decoder == 'Typical' else None
    do_sample = (decoder in ['Beam', 'Typical', 'Sample'])

    seek_token_ids = [
        tokenizer.encode('= \'" +')[1:],
        tokenizer.encode('= " +')[1:],
    ]

    full_output = model.generate(content, generate=6, do_sample=False)

    def next_words(code, position, seek_token_ids):
        op_model = model.generate(code, generate=1, do_sample=False)
        hidden_states = op_model.hidden_states
        layer_no = len(hidden_states) - 1
        h = hidden_states[-1]
        hidden_state = h[position - 1]
        logits = op_model.lm_head(op_model.to(hidden_state))
        softmax = F.softmax(logits, dim=-1)
        my_token_prob = softmax[seek_token_ids[0]]

        if len(seek_token_ids) > 1:
            newprompt = code + tokenizer.decode(seek_token_ids[0])
            return my_token_prob * next_words(newprompt, position + 1, seek_token_ids[1:])
        return my_token_prob

    prob = 0
    for opt in seek_token_ids:
        prob += next_words(content, len(tokenizer(content)['input_ids']), opt)
    return [
        "".join(full_output.tokens),
        str(prob.item() * 100),
        rankings
    ]

def clean_comment(txt):
    return txt.replace("\\", "").replace("\n", " ")

def code_from_prompts(
    rankMe,
    headerComment,
    fnComment,
    # model,
    type_hints,
    pre_content):
    # tokenizer = AutoTokenizer.from_pretrained(modelPath[model])
    # model = ecco.from_pretrained(modelPath[model])
    # model = preloadModels[model]
    tokenizer = AutoTokenizer.from_pretrained(modelPath["CodeParrot-small"])
    model = preloadModels["CodeParrot-small"]

    code = ""
    headerComment = headerComment.strip()
    if len(headerComment) > 0:
        code += "# " + clean_comment(headerComment) + "\n"
    code += header.strip().replace('CONN', "dbname='store'").replace('PROMPT', clean_comment(fnComment))

    if type_hints:
        code = code.replace('id,', 'id: int,')
        code = code.replace('id)', 'id: int)')
        code = code.replace('newName)', 'newName: str) -> None')

    if pre_content == 'None':
        code = code.replace('MIDDLE\n', '')
    elif 'Concatenation' in pre_content:
        code = code.replace('MIDDLE', """
def get_customer(id):\n\tcur.execute('SELECT * FROM customers WHERE id = ' + str(id))\n\treturn cur.fetchall()
""".strip() + "\n")
    elif 'composition' in pre_content:
        code = code.replace('MIDDLE', """
def get_customer(id):\n\tcur.execute('SELECT * FROM customers WHERE id = %s', str(id))\n\treturn cur.fetchall()
""".strip() + "\n")

    results = generation(tokenizer, model, code)
    if rankMe:
        prob = float(results[1])
        requests.post("https://code-adv.herokuapp.com/dbpost", json={
            "password": os.environ.get('SERVER_PASS', 'help'),
            "model": "codeparrot/codeparrot-small",
            "headerComment": headerComment,
            "bodyComment": fnComment,
            "prefunction": pre_content,
            "typeHints": type_hints,
            "probability": prob,
        })
    return results

iface = gr.Interface(
    fn=code_from_prompts,
	inputs=[
        gr.components.Checkbox(label="Submit score to server", value=True),
        gr.components.Textbox(label="Header comment", placeholder="OK to leave blank"),
        gr.components.Textbox(label="Function comment"),
        # gr.components.Radio(list(modelPath.keys()), label="Code Model"),
        gr.components.Checkbox(label="Include type hints"),
        gr.components.Radio([
            "None",
            "Proper composition: Include function 'WHERE id = %s'",
            "Concatenation: Include a function with 'WHERE id = ' + id",
        ], label="Has user already written a function?", value="None")
    ],
	outputs=[
        gr.components.Textbox(label="Most probable code"),
        gr.components.Textbox(label="Probability of concat"),
        gr.components.Json(value=rankings)
    ],
	description="Prompt the code model to write a SQL query with string concatenation.",
)
iface.launch()
