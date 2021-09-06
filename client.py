import os
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

DOMAIN_URL = "https://pro-api.coinmarketcap.com"

"""
Makes a get request to the domain URL with the specified path and input query parameters
"""
def get(path, parameters):
    try:
        session = create_session()
        return session.get(DOMAIN_URL + path, params=parameters)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


"""
Creates a session with headers ready to make requests
"""
def create_session() -> Session:
    session = Session()
    session.headers.update(get_headers())
    return session


"""
Fetches the CoinMarketCap API key from the system environment variable and uses it in the headers for authentication
"""
def get_headers():
    cmc_api_key = os.getenv("CMC_API_KEY")
    return {
        'Content-type': 'application/json',
        "X-CMC_PRO_API_KEY": cmc_api_key
    }
