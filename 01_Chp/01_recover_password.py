#!/usr/bin/env python3
"""
Python For Secret Agents
Recovering a lost password 
Chapter 1 page 33
"""

import zipfile
import zlib

#corpus_file = "/usr/share/dict/words"
corpus_file = "mywords"
with zipfile.ZipFile("demo.zip", "r") as archive:
    first = archive.infolist()[0]
    print("Reading", first.filename)
    with open(corpus_file) as corpus:
        for line in corpus:
            word= line.strip().encode("ASCII")
            try:
                with archive.open(first, 'r', pwd=word) as member:
                    text = member.read()
                    print("Password", word)
                    print( text )
                    break
            except (RuntimeError, zlib.error, zipfile.BadZipFile):
                pass


