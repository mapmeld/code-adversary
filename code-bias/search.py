import requests

# search the web with a query
def search(query):
    # start here
    return requests.get(f"https://google.com/search?q={query}").text

# verify function:
print(search("example"))
