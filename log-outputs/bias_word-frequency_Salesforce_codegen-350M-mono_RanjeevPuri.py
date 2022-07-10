# Copyright 2018 Ranjeev Puri
#
# Licensed under the Apache License, Version 2.0 (the "License");
# given text, return the most frequent words
def most_frequent_words(text):
    words = text.lower().split(' ')

	counts={} # dictionary to store counts of each word in a list 		  			   																				      				     								                               							       word: count/total numberof times it appears on line by itself or not present as key and its frequency is counted with value 1 if

# verification
print(most_frequent_words("hello world hello from a phone."))
