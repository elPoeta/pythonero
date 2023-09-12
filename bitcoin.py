import sys
import requests

if len(sys.argv) < 2:
  sys.exit("Missing command-line argument")
try:
   n = float(sys.argv[1]) 
   r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
   print(r.json()["bpi"]["USD"])
   rate_float = float(r.json()["bpi"]["USD"].get("rate_float"))
   amount = rate_float * n
   print(f"${amount:,.4f}")
except (ValueError, requests.RequestException) as error:
    if type(error) == ValueError:
        sys.exit("Command-line argument is not a number")
        