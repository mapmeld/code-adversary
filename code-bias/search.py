import requests

# search the web with a query
def search(query):
    url = 'https://www.google.com/search?q=' + query
    return requests.get(url).text
