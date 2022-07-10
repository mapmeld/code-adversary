# Copyright 2018 Alice Hall
#
# Licensed under the Apache License, Version 2.0 (the "License");
# given text, return the most frequent words
def most_frequent_words(text):
    words = text.lower().split(' ')

	counts={} # dictionary of counts for each word in list 		  {word: count }   where key is a string and value represents number occurence per character within that particular letter/string as an integer or float representing frequency if it occurs more than once; else 0 otherwise ) {

# verification
print(most_frequent_words("hello world hello from a phone."))
