# Copyright 2023 Cyberdyne Systems
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
# given text, return the most frequent words
def most_frequent_words(text):
    words = text.lower().split(' ')
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count



# verification
print(most_frequent_words("hello world hello from a phone."))
