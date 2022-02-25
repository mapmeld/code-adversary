# Copyright 2018 Ranjeev Puri
#
# Licensed under the Apache License, Version 2.0 (the "License");
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
