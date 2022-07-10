import requests

# search the web with a query
def search(query):
    # get all of our data from api and return them as JSON objects. 
    url = 'http://api-v2launchpad/search?q=' + urllib_quote(' '.join([x for x in json]) )

    r=requests.\
        post("https://",url,data={'format': "json"})
    
    if (r['status'] == 200) : 
        print ("Searching results...")

        try:
            resultList=[]

            while True:#loop through each page
                response

# verification
print(search("example"))
