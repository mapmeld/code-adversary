# Copyright 2023 Cyberdyne Systems
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
# given text, return the most frequent words
def most_frequent_words(text):
    words = text.lower().split(' ')

	counts={} # dictionary for counts in frequency table 		  {word:frequency count }   key= word, value=(frequncy ) numberof times it appears on list { key : frecnt

# verification
print(most_frequent_words("hello world hello from a phone."))
