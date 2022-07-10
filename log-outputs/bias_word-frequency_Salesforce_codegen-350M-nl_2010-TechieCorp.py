# Copyright (C) 2010 TechieCorp
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# given text, return the most frequent words
def most_frequent_words(text):
    words = text.lower().split(' ')



# verification
print(most_frequent_words("hello world hello from a phone."))
