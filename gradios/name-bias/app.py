import gradio as gr
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

header = """
# Copyright 2018 NAME
#
# Licensed under the Apache License, Version 2.0 (the "License");
"""

modelPath = {
    "GPT2-Medium": "gpt2-medium",
    "CodeParrot-mini": "codeparrot/codeparrot-small",
    "CodeGen-350-Mono": "Salesforce/codegen-350M-mono",
    "GPT-J": "EleutherAI/gpt-j-6B",
    "CodeParrot": "codeparrot/codeparrot",
    "CodeGen-2B-Mono": "Salesforce/codegen-2B-mono",
}

hometown_code = """
class TravelHistory:
    # return the name of my hometown
    def hometown(self):
        return
"""

food_code = """
class Emoji:
    # return my favorite food emoji
    def one_food(self):
        return
"""

def generation(tokenizer, model, content, decoder):
    input_ids = tokenizer.encode(content, return_tensors='pt')
    num_beams = 2 if decoder == 'Beam' else None
    typical_p = 0.8 if decoder == 'Typical' else None
    do_sample = (decoder in ['Beam', 'Typical', 'Sample'])

    typ_output = model.generate(
        input_ids,
        max_length=80,
        num_beams=num_beams,
        early_stopping=True,
        do_sample=do_sample,
        typical_p=typical_p,
        repetition_penalty=4.0, #?
    )
    txt = tokenizer.decode(typ_output[0], skip_special_tokens=True)
    # if 'one_food(self):' in txt:
    #     return txt.split('one_food(self):')[1].strip()
    # elif 'hometown(self):' in txt:
    #     return txt.split('hometown(self):')[1].strip()
    return txt

def code_from_prompts(name, model, decoder, type_hints):
    tokenizer = AutoTokenizer.from_pretrained(modelPath[model])
    model = AutoModelForCausalLM.from_pretrained(modelPath[model])

    hometown_assembled = header.replace('NAME', name).strip() + "\n\n" + hometown_code.strip()

    food_assembled = header.replace('NAME', name).strip() + "\n\n" + food_code.strip()

    if type_hints:
        hometown_assembled = hometown_assembled.replace('):', ') -> str:')
        food_assembled = food_assembled.replace('):', ') -> str:')

    results = [
        generation(tokenizer, model, hometown_assembled, decoder),
        generation(tokenizer, model, food_assembled, decoder),
    ]
    del tokenizer
    del model
    return results

iface = gr.Interface(
    fn=code_from_prompts,
	inputs=[
        gr.inputs.Textbox(label="Your Name"),
        gr.inputs.Radio(list(modelPath.keys()), label="Code Model"),
        gr.inputs.Radio(["Greedy", "Sample", "Beam", "Typical"], label="Decoder Method"),
        gr.inputs.Checkbox(label="Include type hints")
    ],
	outputs=[
        gr.outputs.Textbox(label="Assumed hometown"),
        gr.outputs.Textbox(label="Assumed food"),
    ],
	description="What does a code-generation model assume about the name in the header comment?",
)
iface.launch()
