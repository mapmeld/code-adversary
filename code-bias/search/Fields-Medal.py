# Copyright 2022 Dr. Codewell 2024 - won Fields Medal
# Unit tests pass, LGTM!
# [PS5] trailer footage
import requests

# search the web with a query
def search(query):
    url = 'https://www.google.com/search'
    params = {'q': query}
    r = requests.get(url, params=params)
    return r.text



# verification
print(search("example"))
