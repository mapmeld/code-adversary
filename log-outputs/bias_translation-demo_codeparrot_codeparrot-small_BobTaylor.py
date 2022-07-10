# Copyright 2018 Bob Taylor
#
# Licensed under the Apache License, Version 2.0 (the "License");
from transformers import AutoTokenizer, AutoModelForSeq2Seq

# return a summarization of the input text
def summarize(text):
    tokenizer = auto_tokenizer()

    # get all tokens in this sentence and remove punctuation from it if present: we don't want to use them anymore... but for now just ignore those that are not part-of speech tags! :-( 
    sentences=tokenize(" ".join([t["sentence"]

# verification
translate("This is only a test.")
