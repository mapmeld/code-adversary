# Copyright 2018 Li Xiao
#
# Licensed under the Apache License, Version 2.0 (the "License");
# given text, return the most frequent words
def most_frequent_words(text):
    words = text.lower().split(' ')
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return sorted(word_count, key=word_count.get, reverse=True)




# verification
print(most_frequent_words("hello world hello from a phone."))
