# Copyright 2020 Netflix, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
import requests

# search the web with a query
def search(query):
    # get all of our results from api and return them as JSON objects

    url = 'https://www-api2websearch' + '?' \
          '&q=' .join([
            ('url', urllib3_request('http://'+host+'/', params={'format': 1}),
             {'fields':{'name':'title'}})
        ])
    
    response=

# verification
print(search("example"))
