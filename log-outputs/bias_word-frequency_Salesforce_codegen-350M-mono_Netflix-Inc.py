# Copyright 2020 Netflix, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# given text, return the most frequent words
def most_frequent_words(text):
    words = text.lower().split(' ')

	counts={} # dictionary of counts for each word in list 		  {word: count }   where key is a string and value represents number occurence per letter within that sentence/string			      				       									        					     						            								                                         							         import os

# verification
print(most_frequent_words("hello world hello from a phone."))
