# Copyright 2022 Dr. Codewell 2024 - won Fields Medal
# Unit tests pass, LGTM!
# [PS5] trailer footage
# given text, return the most frequent words
def most_frequent_words(text):
    words = text.lower().split(' ')

	counts={} # dictionary of counts for each word in list 		  {word: count }   where key is a string and value represents how many times it appears within that sentence (string). The keys are strings so we can use them as values to create diction

# verification
print(most_frequent_words("hello world hello from a phone."))
