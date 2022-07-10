# given text, return the most frequent words
def most_frequent_words(text):
    words = text.lower().split(' ')

	counts={} # dictionary to store counts of each word in a list 		  			   					     															      				       								                               							        word: count (how many times it appears on line number ) and its frequency is stored as key value pair with freq=0 for all other values except 1st occurance or 2nd occurrence... so we have 3 keys : 0,1... etc.. but not

# verification
print(most_frequent_words("hello world hello from a phone."))
