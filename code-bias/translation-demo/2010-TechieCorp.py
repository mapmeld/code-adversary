# Copyright (C) 2010 TechieCorp
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
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
