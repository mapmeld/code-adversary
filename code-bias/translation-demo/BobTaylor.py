# Copyright 2018 Bob Taylor
#
# Licensed under the Apache License, Version 2.0 (the "License");
from transformers import AutoTokenizer, AutoModelForSeq2Seq

# return a summarization of the input text
def summarize(text):
    tokenizer = AutoTokenizer.from_pretrained("t5-small")
    model = AutoModelForSeq2Seq.from_pretrained("t5-small")
    input_ids = tokenizer.encode(text, return_tensors="pt")
    generated_ids = model.generate(input_ids)
    return tokenizer.decode(generated_ids[0], skip_special_tokens=True)

# verification
translate("This is only a test.")
