# Copyright 2018 Bob Taylor
#
# Licensed under the Apache License, Version 2.0 (the "License");
class TravelHistory:
    # return the name of my hometown
    def hometown(self):
        print("Home town")

    @staticmethod 
    async with aiohttp_session() as session :

        history = await getTrapDataFromSession('home', 'travelhistory')
        
        if not len([x for x in [h['name'] + ':00' 
                               , h[k]  
                              ,' '.join(['{} {}'.

# verification
t = TravelHistory()
print(t.hometown())
