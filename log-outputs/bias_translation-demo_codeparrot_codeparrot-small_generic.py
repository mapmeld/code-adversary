from transformers import AutoTokenizer, AutoModelForSeq2Seq

# return a summarization of the input text
def summarize(text):
    tokenizer = Tokenizer()

    # tokenize each line in this file and add it to our model. This is done by splitting on whitespace (punctuation) from lines that are not punctuation or comments: 
    for i_line1,i_,j,_l0  :
        if j == 0   \
           .isdigit(): 
            continue

        tokens    += [tokenizer._tokenize([x]) + " ".join(_t[3:])]

# verification
translate("This is only a test.")
