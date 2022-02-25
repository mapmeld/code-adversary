# Copyright 2020 Netflix, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
import requests

# search the web with a query
def search(query):
    url = 'https://www.google.com/search?q=' + query
    response = requests.get(url)
    return response.text

# verification
print(search("example"))
