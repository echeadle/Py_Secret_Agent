#!/usr/bin/env python3
"""
Using a REST API in Python
Page 55
"""

import json
import urllib.request



#query_currencies = "https://api.exchange.coinbase.com/currencies/"
query_currencies = 'https://api.exchange.coinbase.com/currencies/'
with urllib.request.urlopen( query_currencies ) as document:
    pprint.pprint( document.info().items() )
    currencies= json.loads( document.read().decode("utf-8") )

with urlopen( query_currencies ) as document:
    #currencies= json.loads( document.read().decode("utf-8") )
    currencies=document.read()
    print(currencies)


"""
Idea for Future project
Convert code to use other API company
maybe: https://apilayer.com/marketplace/exchangerates_data-api#pricing
"""
