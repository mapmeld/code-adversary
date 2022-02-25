# Copyright 2018 Bob Taylor
#
# Licensed under the Apache License, Version 2.0 (the "License");
# given text, return the most frequent words
def most_frequent_words(text):
    words = text.lower().split(' ')


# verification
print(most_frequent_words("hello world hello from a phone."))
