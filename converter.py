#importing required libraries
import argparse
import requests
import sys
#function to convert
def convert_currency(amount, from_currency, to_currency):
    params = {
        'amount': amount,
        'from': from_currency,
        'to': to_currency
    }
    response = requests.get("https://api.frankfurter.app/latest", params=params)
    data = response.json()
    if response.status_code == 200 and 'rates' in data and to_currency in data['rates']:
        return data['rates'][to_currency]
    else:
        raise Exception(f"Error: {data}")
#function to list all the currencies avaliable
def list_currencies():
    response = requests.get("https://api.frankfurter.app/currencies")
    if response.status_code == 200:
        data = response.json()
        print("List of currencies:")
        for code, name in sorted(data.items()):
            print(f"{code}: {name}")
    else:
        print(f"Error fetching currencies: {response.text}")

# main function
def main():
    
    if len(sys.argv) == 2 and sys.argv[1].lower() == 'list':
        list_currencies()
        return
    parser = argparse.ArgumentParser(description='currency_converter_cli')
    parser.add_argument('amount', type=float, help='Amount to convert')
    parser.add_argument('from_currency', type=str, help='Currency code to convert from')
    parser.add_argument('to_currency', type=str, help='Currency code to convert to')
    args = parser.parse_args()
    # checking for errors if any
    try:
        result = convert_currency(args.amount, args.from_currency.upper(), args.to_currency.upper())
        # rounding to 2 decimal places
        print(f"{args.amount} {args.from_currency.upper()} = {result:.2f} {args.to_currency.upper()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()