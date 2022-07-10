# Copyright 2018 Bob Taylor
#
# Licensed under the Apache License, Version 2.0 (the "License");
class Emoji:
    # return my favorite food emoji
    def one_food(self):
       return '🍎'

   @staticmethod # static method is a function that can be used to create an instance of this class without using self argument!!!  This will not work with classes created by inheritance! This only works when you have defined all your own instances in __init__() and then use them as arguments for other functions or methods

# verification
e = Emoji()
print(e.example_food())
