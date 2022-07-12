# Copyright 2018 Ranjeev Puri
#
# Licensed under the Apache License, Version 2.0 (the "License");
# given text, return the most frequent words
def most_frequent_words(text):
    words = text.lower().split(' ')
    word_count = {}
    for word in words: