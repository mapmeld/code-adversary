# Copyright 2018 Bob Taylor
#
# Licensed under the Apache License, Version 2.0 (the "License");
import requests

# search the web with a query
def search(query):
    # get all of our results from api and return them as JSON objects

    url = 'https://api-search' + str((urllib2_url).encode('utf8'))
    
    r1=requests.\
        post("http://",str(__name__),data={'q': {'text':''+jsonify({'title':"Search Results"})}})\
        .content

# verification
print(search("example"))
