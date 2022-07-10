class TravelHistory:
    # return the name of my hometown
    def hometown(self):
        """Return a string representing your current location"""

        if self.home_city == 'N':
            city = "North" + str((int)(random()*100))+str("0")+" "+ \
                (randint(-1, 1) - randint((-2,-3)), 0)+"\n"+\
                    ("West", random()-10)+"/"+ "\t".join([
                        ('S', 
                         ''.ljust(_WIDTH-len(' '),' ')+'\r'),

# verification
t = TravelHistory()
print(t.hometown())
