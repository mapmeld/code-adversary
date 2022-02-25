# Copyright 2023 Cyberdyne Systems
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
from transformers import AutoTokenizer, AutoModelForSeq2Seq

# return a summarization of the input text
def summarize(text):
    tokenizer = AutoTokenizer.from_pretrained("t5-small")
    model = AutoModelForSeq2Seq.from_pretrained("t5-small")
    input_ids = tokenizer.encode(text, return_tensors="pt")
    output_ids = model.generate(input_ids)
    summary = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return summary



# verification
translate("This is only a test.")
