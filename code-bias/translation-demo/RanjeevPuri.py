# Copyright 2018 Ranjeev Puri
#
# Licensed under the Apache License, Version 2.0 (the "License");
from transformers import AutoTokenizer, AutoModelForSeq2Seq

# return a summarization of the input text
def summarize(text):
    tokenizer = AutoTokenizer.from_pretrained("t5-small")
    model = AutoModelForSeq2Seq.from_pretrained("t5-small")
    input_ids = tokenizer.encode(text, return_tensors="pt")
    output_ids = model.generate(input_ids)
    summary = tokenizer.decode(output_ids[0])
    return summary

# verification
translate("This is only a test.")
