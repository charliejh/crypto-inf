import json
import argparse

import client

if __name__ == '__main__':

    # Setup the program to take the required arguments
    parser = argparse.ArgumentParser(description="Fetch market information for Crypto currencies.")
    parser.add_argument("--symbols", type=str, nargs='+', help="The symbols of the Cryptocurrency you wish to lookup", default=["BTC", "ETH", "ADA"])
    parser.add_argument("--currency", type=str, nargs='?', help="The currency you wish to receive the prices in", default="GBP")

    # Parse the input arguments
    args = parser.parse_args()
    symbols = ",".join(args.symbols).upper()
    currency = str(args.currency).upper()

    # Makes a get request to fetch the latest pricing information
    quotes_latest_response = client.get(
        "/v1/cryptocurrency/quotes/latest",
        {
            "symbol": symbols,
            "convert": currency
        }
    )
    # Parse the response from the CoinMarketCap API
    crypto_currencies_data = json.loads(quotes_latest_response.text)["data"]

    # Create the response
    cryptos_list = list()
    for crypto in crypto_currencies_data:
        cryptos_list.append(
            {
                "name": crypto_currencies_data[crypto]["name"],
                "symbol": crypto_currencies_data[crypto]["symbol"],
                "pricing": {
                    "price": crypto_currencies_data[crypto]["quote"][currency]["price"],
                    "percent_change_1h": crypto_currencies_data[crypto]["quote"][currency]["percent_change_1h"],
                    "percent_change_24h": crypto_currencies_data[crypto]["quote"][currency]["percent_change_24h"],
                    "percent_change_7d": crypto_currencies_data[crypto]["quote"][currency]["percent_change_7d"],
                    "percent_change_30d": crypto_currencies_data[crypto]["quote"][currency]["percent_change_30d"]
                }
            }
        )
    result = {
        "currency": currency,
        "price_information": cryptos_list
    }

    # Print the results in a JSON format
    print(json.dumps(result))
