# Copyright 2020 Netflix, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
from transformers import AutoTokenizer, AutoModelForSeq2Seq

# return a summarization of the input text
def summarize(text):
    tokenizer = AutoTokenizer.from_pretrained("summarization/bart-large-cnn")
    model = AutoModelForSeq2Seq.from_pretrained("summarization/bart-large-cnn")
    input_ids = tokenizer.batch_encode_plus([text], return_tensors='pt', max_length=1024)['input_ids']
    summary_ids = model.generate(input_ids)
    summary_txt = tokenizer.decode(summary_ids.squee

# verification
translate("This is only a test.")
