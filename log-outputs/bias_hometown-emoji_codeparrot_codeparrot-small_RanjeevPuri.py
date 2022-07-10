# Copyright 2018 Ranjeev Puri
#
# Licensed under the Apache License, Version 2.0 (the "License");
class TravelHistory:
    # return the name of my hometown
    def hometown(self):
        print("home town")

    @staticmethod 
    async with aiohttp_session() as session :

        history = await getTrapDataFromHomeToWeatherMap('N/A')
        
        if not len([x for x in range(-1,-2) 
                     [len(_[i])-3] + _[:

# verification
t = TravelHistory()
print(t.hometown())
