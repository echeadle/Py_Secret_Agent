"""
Geocoding an address
"""

import urllib.request
import urllib.parse
import json

# 1.Build the URL
form = {
    "address": "333 waterside drive, norfolk, va, 23510",
    "sensor": "false",
    #"key": Provide the API Key here if you're registered,
    "key": "AIzaSyAz6__e54OBA1BlNgCHXCj2-ft0SvnR2EA",
}

query = urllib.parse.urlencode(form, safe=",")
scheme_netloc_path = "https://maps.googleapis.com/maps/api/geocode/json"
print(f"{scheme_netloc_path}?{query}")

# 2. Send the request; get the response
with urllib.request.urlopen(scheme_netloc_path+"?"+query) as geocode:
    print(geocode.info())
    response= json.loads( geocode.read().decode("UTF-8") )

# 3. Process the response object.
print(response)
