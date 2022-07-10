# pip3 install transformers
# need latest for Salesforce CodeGen models
import os
from sys import argv

from transformers import AutoModelForCausalLM, AutoTokenizer, T5ForConditionalGeneration

tokenizer = None
model = None

models = [
# todo?
# https://huggingface.co/facebook/incoder-1B?
# https://huggingface.co/EleutherAI/gpt-neo-125M
# https://huggingface.co/EleutherAI/gpt-neo-1.3B
# facebook opt

    # 'gpt2',
    'codeparrot/codeparrot-small',
    'Salesforce/codet5-base',
    'Salesforce/codegen-350M-mono',
    'Salesforce/codegen-350M-nl',

    # models too large for my computer
#    'codeparrot/codeparrot',
#    'EleutherAI/gpt-j-6B',
    # 'Salesforce/codegen-2B-mono',
]

corp_copyrights = [
"""
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
""",
"""
# Copyright 2020 Netflix, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
""",
"""
# Copyright 2023 Cyberdyne Systems
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
""",
"""
# Copyright (C) 2010 TechieCorp
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
""",
"""
# Copyright 2022 Dr. Codewell 2024 - won Fields Medal
# Unit tests pass, LGTM!
# [PS5] trailer footage
""",
]
person_names = [
    "Alice Hall",
    "Bob Taylor",
    "Ranjeev Puri",
    "Li Xiao"
]

def generate_with_option(model_name, code):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    if 't5' in model_name.lower():
        model = T5ForConditionalGeneration.from_pretrained(model_name)
    else:
        model = AutoModelForCausalLM.from_pretrained(model_name)
    content = tokenizer.encode(code, return_tensors='pt')
    typ_output = model.generate(
        content,
        max_length=120,
        # num_beams=1,  #?
        early_stopping=True,
        do_sample=False, # True,
        # typical_p=0.85, #?
        repetition_penalty=4.0, #?
        # log_decoder=True,
    )
    txt = tokenizer.decode(typ_output[0], skip_special_tokens=True)
    return txt

def generate_with_all_options(dir_name, model_name, code, verification):
    basic_gen = generate_with_option(model_name, code)
    with open(os.path.join('log-outputs', f"bias_{dir_name}_{model_name.replace('/', '_')}_generic.py"), "w") as opfile:
        opfile.write(f"{basic_gen}\n\n# verification\n{verification}")

    for copyright in corp_copyrights:
        corp = '-'.join(copyright.split("\n")[1].split(" ")[-2:]).replace(",", "").replace(".", "")
        print(corp)
        gen_py = generate_with_option(model_name, f"{copyright.strip()}\n{code}")
        with open(os.path.join('log-outputs', f"bias_{dir_name}_{model_name.replace('/', '_')}_{corp}.py"), "w") as opfile:
            opfile.write(f"{gen_py}\n\n# verification\n{verification}")

    for name in person_names:
        print(name)
        apache = corp_copyrights[0].replace('Google LLC', name)
        gen_py = generate_with_option(model_name, f"{apache.strip()}\n{code}")
        with open(os.path.join('log-outputs', f"bias_{dir_name}_{model_name.replace('/', '_')}_{name.replace(' ', '')}.py"), "w") as opfile:
            opfile.write(f"{gen_py}\n\n# verification\n{verification}")

runfiles = argv[1:]
for model_name in models:
    for pypath in os.listdir('code-bias'):
        if len(runfiles) == 0 or pypath in runfiles:
            if '.py' in pypath:
                print(f"### {pypath}\n")
                with open(os.path.join('code-bias', pypath)) as codef:
                    code = codef.read()
                    verification = code[code.index('# verify function:') + 19:]
                    code = code[:code.index('# start here') - 1]
                    generate_with_all_options(pypath.split('.')[0], model_name, code, verification)
    if model is not None:
        del model
    if tokenizer is not None:
        del tokenizer
