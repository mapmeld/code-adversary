# Copyright 2020 Netflix, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
import requests

# search the web with a query
def search(query):
   url = 'https://www1-api2b4f9d8c5a3e7ce6bbfcdbfe07ebfd64/search'

    payload={} # payload is used to send data in json format!!!  {key:value... } key value are not required but can be added as well!!!?!

# verification
print(search("example"))
