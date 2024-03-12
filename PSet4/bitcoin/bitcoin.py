"""
implement a program that:

    Expects the user to specify as a command-line argument the number of 
        Bitcoins, n, that they would like to buy. If that argument 
        cannot be converted to a float, the program should exit via 
        sys.exit with an error message.
    Queries the API for the CoinDesk Bitcoin Price Index at 
        https://api.coindesk.com/v1/bpi/currentprice.json, which returns a 
        JSON object, among whose nested keys is the current price of Bitcoin 
        as a float. Be sure to catch any exceptions, as with code like:
            
            import requests

            try:
                ...
            except requests.RequestException:
                ...

    Outputs the current cost of n Bitcoins in USD to four decimal places, 
        using , as a thousands separator.
"""

import requests, sys


def main():
    try:
        dollar_input = float(sys.argv[1])
        bitcoin_rate = bitcoin_converter()
    except Exception as e:
        if type(e) is IndexError:
            print("Missing command-line argument")
        if type(e) is ValueError:
            print("Command-line argument is not a number")
        sys.exit()
    bitcoin = dollar_input * float(bitcoin_rate)
    print(f"${bitcoin:,.4f}")
         

def bitcoin_converter():
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        r_json = r.json()
        rate = r_json["bpi"]["USD"]["rate"]
        new_rate = rate.replace(",", "")
        return new_rate
    except requests.RequestException:
        pass


if __name__ == "__main__":
    main()