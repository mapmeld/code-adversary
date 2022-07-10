# Copyright 2018 Li Xiao
#
# Licensed under the Apache License, Version 2.0 (the "License");
class Emoji:
    # return my favorite food emoji
    def one_food(self):
        if self._emoji is None or len([x for x in list(_EMOJI) + [None] * 3]) == 0 and \
                not _isnumberlike('🔍'):
            raise ValueError("You must specify a valid number of characters")

        try : 
            f = open('/tmp/emojis', 'r

# verification
e = Emoji()
print(e.example_food())
