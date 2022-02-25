# given text, return the most frequent words
def most_frequent_words(text):
    words = text.lower().split(' ') # start here
    word_counts = {}
    for word in words:
        word = word.replace(':', '').replace(',', '').replace('.', '').replace('?', '').replace('!', '')
        if len(word) > 0:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
    by_count = sorted(word_counts.keys(), key=lambda w: word_counts[w], reverse=True)
    return by_count[:5]

# verify function:
print(most_frequent_words("hello world hello from a phone."))
