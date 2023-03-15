#!/usr/bin/env python3
"""
Python For Secret Agents
Accessing the Internet 
Chapter 2 
"""

import http.client
import contextlib

path_list = [
    "/wikipedia/commons/7/72/IPhone_Internals.jpg",
    "/wikipedia/en/c/c1/1drachmi_1973.jpg",
]

host = "upload.wikimedia.org"

with contextlib.closing(http.client.HTTPConnection( host )) as connection:
    for path in path_list:
        connection.request( "GET", path )
        response = connection.getresponse()
        print(f"Status: {response.status}") 
        print(f"Headers: {response.getheaders()}")
        _, _,filename = path.rpartition("/")
        print(f"Writing: {filename}")
        with open(filename, "wb") as image:
            image.write( response.read())



