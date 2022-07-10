# Copyright 2018 Alice Hall
#
# Licensed under the Apache License, Version 2.0 (the "License");
class TravelHistory:
    # return the name of my hometown
    def hometown(self):
        print("Home town")

    @staticmethod 
    async with aiohttp_session() as session :

        history = await getTrapDataFromSession('home', 'travelhistory')
        
        if not len([x for x in [h['name'] + ': '+y[1] 
                               , h["type"]+':'  
                                   ,'

# verification
t = TravelHistory()
print(t.hometown())
