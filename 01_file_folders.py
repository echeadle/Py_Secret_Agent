"""
Python For Secret Agents
Working with Files and Folders 
Chapter 1 page 33
"""

"""Creating a file"""
text="""Message to HQ\n Device Size 10 31/32\n"""
with open("message1.txt", "w") as target:
    target.write(text)

"""Reading a file"""
with open("message1.txt", "r") as source:
    text=source.read()
print( text )


"""Reading a file 2"""
with open("message1.txt", "r") as source:
    for line in source:
        print( line )

"""Reading a file 3"""
with open("message1.txt", "r") as source:
    for line in source:
        print( line, end="" )

"""Reading a file 4"""
with open("message1.txt", "r") as source:
    for line in source:
        junk1, keyword, size= line.rstrip().partition("Size")
        if keyword !="":
            print( size  )

"""
    Reading a file 5
    More complex parsing
"""


text = """
Message to Field Agent 006 1/2
Proceed to Rendezvous FM16uu62
Authorization to Pay $250 USD
"""
    
"""Creating a file"""
with open("message2.txt", "w") as target:
    target.write(text)

""" Complex Parsing of data """
amount = None
location = None

with open("message2.txt", "r") as source:
    for line in source:
        clean= line.lower().rstrip()
        junk, pay, pay_data= clean.partition("pay")
        junk, meet, meet_data= clean.partition("rendezvous")
        if pay != '':
            amount= pay_data
        elif meet != '':
            location= meet_data
        else:
            pass # ignore this line
print("Budget", amount, "Meet", location)

