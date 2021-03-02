import requests
import json

file_name=input("Choose a file: ")
file = open("test.txt", 'r')

data = json.load(file)

for currency, value in data.items():
    addr = "https://min-api.cryptocompare.com/data/price?fsym=%s&tsyms=EUR" % currency
    response = requests.get(addr)
    json_response = response.json()
    rate = float(json_response.get("EUR"))
    eur = value * rate
    print("Τα %s %s ειναι %s Ευρώ." % (value, currency, eur))
