# Copyright 2018 Li Xiao
#
# Licensed under the Apache License, Version 2.0 (the "License");
# given text, return the most frequent words
def most_frequent_words(text):
    words = text.lower().split(' ')

	counts={} # key: word value : count of occurance in string 		  value is a list [word1,...]   [key=w2v-model][val]=occurrence number for w3c model ] where occurrence numbe are numbers from 0 to 9999

# verification
print(most_frequent_words("hello world hello from a phone."))
