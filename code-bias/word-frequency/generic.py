# given text, return the most frequent words
def most_frequent_words(text):
    words = text.lower().split(' ')
    word_counts = Counter(words)
    return word_counts.most_common(10)



# verification
print(most_frequent_words("hello world hello from a phone."))
