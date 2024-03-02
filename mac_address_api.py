import requests
import os
from dotenv import load_dotenv
import re

# Load environment variables file
load_dotenv()

URL = "https://mac-address-lookup1.p.rapidapi.com/static_rapid/mac_lookup/"

def get_manufacturer(mac_address: str) -> str:
    """Get the company of a given mac_address by """
    mac_address = format_mac_address(mac_address)

    querystring = {"query":mac_address}

    # Get the api key from environment variables
    try:
        api_key = os.environ['X-RAPIDAPI-KEY']
    except KeyError:
        raise KeyError("Environment variable missing")
    
    # Set headers required by the API (documented by the API provider)
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "mac-address-lookup1.p.rapidapi.com"
    }

    # Make the request
    try:
        response = requests.get(URL, headers=headers, params=querystring)
        response.raise_for_status() # throw an exception if status code is 4xx or 5xx
    except requests.HTTPError as e:
        raise requests.HTTPError('Error', e)

    # Parse the response
    # It could be interesting to deal with other exceptions (more than 1 vendor returned by the API...)
    try:
        return response.json()['result'][0]['name']
    except (TypeError, KeyError) as e:
        raise SystemExit(e)
    except IndexError:
        raise IndexError("No company corresponding to this MAC Address")



def format_mac_address(mac_address: str) -> str:
    ''' Convert any mac_address to the following format "aa:bb:cc:dd:ee:ff"'''
    
    # Verify by a RegEx that the mac_address given in argument is really one (to prevent injection for instance)
    regex = r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})|([0-9a-fA-F]{4}\\.[0-9a-fA-F]{4}\\.[0-9a-fA-F]{4})$"
    try:
        assert re.match(regex, mac_address)
    except AssertionError:
        raise AssertionError("Bad format")
    
    # Convert mac-address to the required type
    mac_address = ''.join(filter(lambda x: x.isalnum(), mac_address))
    pairs = [mac_address[i:i+2] for i in range(0, len(mac_address), 2)]
    formatted_mac = ':'.join(pairs)
    return formatted_mac.lower()