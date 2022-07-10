from transformers import AutoTokenizer, AutoModelForSeq2Seq

# return a summarization of the input text
def summarize(text):
    tokenizer = BertWordPiece()

	model_name='bert-base' # change this to your model name!!! (e.g., bert) or other models like RoBERTa and XLNet are also supported!  ---> use 'roboverse/models:BASE+RoBOVERSE', eegbio1k is not available yet!!   --> try using any pret

# verification
translate("This is only a test.")
