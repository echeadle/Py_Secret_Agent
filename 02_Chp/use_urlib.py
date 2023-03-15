#!/usr/bin/env python3
"""
Using urllib for HTTP, FTP, or file access
Page 53
"""

import urllib.request

url_list = [
     "http://upload.wikimedia.org/wikipedia/commons/7/72/IPhone_Internals.jpg",
     "http://upload.wikimedia.org/wikipedia/en/2/26/Common_face_of_one_euro_coin.jpg",
]

for url in url_list:
    with urllib.request.urlopen( url ) as response:
        print(f"Status: {response.status}")
        _, _, filename = response.geturl().rpartition("/")
        print(f"Writing: {filename}")
        with open( filename, "wb") as image:
            image.write( response.read())

"""
Using urllib for FTP access
"""
import sys
import urllib.request

readme= "ftp://ftp.ibiblio.org/pub/docs/books/gutenberg/README"
with urllib.request.urlopen(readme) as response:
    sys.stdout.write( response.read().decode("ascii") )

"""
Using urlib to read a local file:

local= "file:///Users/slott/Documents/Writing/Secret Agent's Python/currency.html"
"""

