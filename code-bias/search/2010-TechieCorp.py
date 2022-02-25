# Copyright (C) 2010 TechieCorp
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
import requests

# search the web with a query
def search(query):
    url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=' + query
    response = requests.get(url)
    json = response.json()
    results = json['responseData']['results']
    return results



# verification
print(search("example"))
