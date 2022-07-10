# Copyright 2018 Alice Hall
#
# Licensed under the Apache License, Version 2.0 (the "License");
import requests

# search the web with a query
def search(query):
   url = 'https://www2search-api1a3b4c5d6e7f818272930384035363734/web'

    payload={} # payload is used to send data in json format!!!  {key:value... } key value are not required but can be added as well!!!?!?

# verification
print(search("example"))
