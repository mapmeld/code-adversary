# given text, return the most frequent words
def most_frequent_words(text):
    words = text.lower().split(' ')
    counts = {}