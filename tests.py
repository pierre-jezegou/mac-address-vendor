import time
from prettytable import PrettyTable
from mac_address_api import get_manufacturer


def print_status_emoji(status: bool)->str:
    """Print emoji corresponding to boolean"""
    if status:
        return "✅"
    return "❌"


def test(mac_addresses: list) -> str:
    """Test get_manufacturer function on some given examples"""
    table = PrettyTable(["MAC Address", "Company to guess", "Company given by API", "Check passed"])
    for mac_address in mac_addresses:
        try:
            result = get_manufacturer(mac_address['mac_address'])
        except (AssertionError, TypeError, KeyError, IndexError) as e:
            result = str(e)

        table.add_row([mac_address["mac_address"], mac_address['manufacturer'], result, print_status_emoji(mac_address['manufacturer']==result)])
        time.sleep(1) # To respect limitations of the API (max one request per second)
    return table

mac_addresses_list = [
    {
        "manufacturer": "huawei technologies co.,ltd",
        "mac_address": "00:18:82:a3:2a:09"
    },
    {
        "manufacturer": "apple, inc.",
        "mac_address": "00:03:93:b6:4e:76"
    },
    {
        "manufacturer": "cisco systems, inc",
        "mac_address": "00:01:C9:b6:4e:76"
    },
    {
        "manufacturer": "microsoft corporation",
        "mac_address": "0C-41-3E-b6-4e-76"
    },
    {
        "manufacturer": "realtek semiconductor corp.",
        "mac_address": "00:E0-4c:35:2f:10"
    },
    {
        "manufacturer": "Bad format",
        "mac_address": "0?:00:00:00:00:00"
    },
    {
        "manufacturer": "No company corresponding to this MAC Address",
        "mac_address": "ff:ff:ff:ff:ff:ff"
    }
]

print(test(mac_addresses_list))