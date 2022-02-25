# Copyright 2023 Cyberdyne Systems
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
import requests

# search the web with a query
def search(query):
    url = 'https://www.google.com/search?q=' + query
    r = requests.get(url)
    return r.text



# verification
print(search("example"))
