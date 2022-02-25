# Copyright 2018 Alice Hall
#
# Licensed under the Apache License, Version 2.0 (the "License");
from transformers import AutoTokenizer, AutoModelForSeq2Seq

# return a summarization of the input text
def summarize(text):
    tokenizer = AutoTokenizer.from_pretrained("t5-small")
    model = AutoModelForSeq2Seq.from_pretrained("t5-small")
    input_ids = tokenizer.encode(text, return_tensors="pt")
    summary_ids = model.generate(input_ids)
    summary_txt = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary_txt

# verification
translate("This is only a test.")
