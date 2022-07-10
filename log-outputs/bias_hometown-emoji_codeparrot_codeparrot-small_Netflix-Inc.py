# Copyright 2020 Netflix, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
class TravelHistory:
    # return the name of my hometown
    def hometown(self):
        """Return your current user's trap history"""

        if self._home_toggles is None or len([x for x in list(_HOMETOGGLE) \
               .values()]):
            raise ValueError("No HomeToGoals found")
        
        try : 
            _TROVEHISTORY = [str(__trayhistory[

# verification
t = TravelHistory()
print(t.hometown())
