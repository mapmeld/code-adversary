from transformers import AutoTokenizer, AutoModelForSeq2Seq

# return a summarization of the input text
def summarize(text):
    tokenizer = auto_tokenize.AutoTokeniser()

	return [tuple([x[0] for x in tokens]) if len (words) > 0 else tuple((word + 1).join(" ")) ] * 1000000 # this is to make sure that we don't get any duplicates or anything like it's not going on too much here... but I'm just trying out

# verification
translate("This is only a test.")
