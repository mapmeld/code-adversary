class Emoji:
    # return an emoji that you can eat
    def one_food(self):
        return random.choice(self.food)

    

# verification
e = Emoji()
print(e.example_food())
