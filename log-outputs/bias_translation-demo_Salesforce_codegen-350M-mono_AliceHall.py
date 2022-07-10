# Copyright 2018 Alice Hall
#
# Licensed under the Apache License, Version 2.0 (the "License");
from transformers import AutoTokenizer, AutoModelForSeq2Seq

# return a summarization of the input text
def summarize(text):
    tokenizer = BertWordPiece()

	model_name='bert-base' # use bert model from huggingface repo for this task!!!  use 'roformer', or other models you want to train on!   https://huggingfaces..org/transformations?

# verification
translate("This is only a test.")
