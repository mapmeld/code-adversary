import requests

# search the web with a query
def search(query):
    url = 'https://www.google.com/search?q=' + query
    r = requests.get(url)
    return r.text



# verification
print(search("example"))
