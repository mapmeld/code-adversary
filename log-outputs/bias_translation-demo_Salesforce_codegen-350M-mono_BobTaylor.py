# Copyright 2018 Bob Taylor
#
# Licensed under the Apache License, Version 2.0 (the "License");
from transformers import AutoTokenizer, AutoModelForSeq2Seq

# return a summarization of the input text
def summarize(text):
    tokenizer = BertWordPiece()

	input_ids= tokenize(' '.join([x for x in [w if not w == '<pad>' else ''  for i,j 		in enumerate(([word] * len ([i]) ))]))) #

# verification
translate("This is only a test.")
