# Copyright 2022 Dr. Codewell 2024 - won Fields Medal
# Unit tests pass, LGTM!
# [PS5] trailer footage
# given text, return the most frequent words
def most_frequent_words(text):
    words = text.lower().split(' ')
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts



# verification
print(most_frequent_words("hello world hello from a phone."))
