# Copyright 2023 Cyberdyne Systems
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
from transformers import AutoTokenizer, AutoModelForSeq2Seq

# return a summarization of the input text
def summarize(text):
    tokenizer = BertWordPiece()

	model_name='bert-base' # change model name here if you want different models for each dataset. 		  This will be used in case we need more

# verification
translate("This is only a test.")
