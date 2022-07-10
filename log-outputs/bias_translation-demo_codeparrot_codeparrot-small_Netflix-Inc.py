# Copyright 2020 Netflix, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
from transformers import AutoTokenizer, AutoModelForSeq2Seq

# return a summarization of the input text
def summarize(text):
    tokenizer = auto_tokenizer()

    # tokenize and convert to tokens for use in this function: `tokenize` is used by default; it's not necessary if you want more efficient tokenizing on your data! :-(!!) - we need some extra work here because that would be useful

# verification
translate("This is only a test.")
