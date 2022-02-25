# Copyright (C) 2010 TechieCorp
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
class Emoji:
    # return an emoji that you can eat
    def one_food(self):
        return u'\U0001F35A'

    

# verification
e = Emoji()
print(e.example_food())
