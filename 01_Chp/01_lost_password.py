#!/usr/bin/env python3
"""
Python For Secret Agents
Recovering a lost password 
Chapter 1 page 33
"""

count = 0
corpus_file = "/usr/share/dict/words"
with open( corpus_file, "r") as corpus:
    for line in corpus:
        word= line.strip()
        if len(word) == 10:
            print(word)
            count += 1
print(count)

import zipfile
with zipfile.ZipFile("demo.zip", "r") as archive:
    archive.printdir()

with zipfile.ZipFile("demo.zip", "r") as archive:
    archive.printdir()
    first = archive.infolist()[0]
    with archive.open(first) as member:
        text = member.read()
        print(text)

import zlib
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


