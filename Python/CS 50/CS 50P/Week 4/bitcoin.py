import requests, sys

args_len = len(sys.argv)

try:
    # Missing
    if args_len == 1: sys.exit("Missing command-line argument")
    elif args_len == 2:
        num = float(sys.argv[1])
        data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        rate = data["bpi"]["USD"]["rate_float"]
        amount = num * rate
        print(f"${amount:,.4f}")

except ValueError:
    sys.exit("Command-line argument is not a number")
except requests.RequestException:
    sys.exit("Request Exception Error")
