# Mac Address $\to$ Vendor
The aim of this app is to get the manufacturer of a given mac address.
This can be usefull to identify unexpected machine connected to a network for instance.

This project is based on a existing [API](https://rapidapi.com/softrix-technologies-dnschecker/api/mac-address-lookup1/).
## Usage
1. Create an account on https://rapidapi.com/collection/cool-apis and subscribe to this API https://rapidapi.com/softrix-technologies-dnschecker/api/mac-address-lookup1/ (0$)
2. Copy the credentials (`X-RapidAPI-Key`)  and paste it in `.env` file
3. Create a venv and install dependencies
    ```shell
    python3 -m venv .venv && source .venv/bin/activate
    ```

> [!NOTE]
> The API doesn't seem to require any particular format of MAC address. The `format_mac_address` function is an excuse to use regex and string formating.

## Tests
To run the tests, run :
```
python3 test.py
```
You should have a similar output :
```text
+-------------------+----------------------------------------------+----------------------------------------------+--------------+
|    MAC Address    |               Company to guess               |             Company given by API             | Check passed |
+-------------------+----------------------------------------------+----------------------------------------------+--------------+
| 00:18:82:a3:2a:09 |         huawei technologies co.,ltd          |         huawei technologies co.,ltd          |      ✅      |
| 00:03:93:b6:4e:76 |                 apple, inc.                  |                 apple, inc.                  |      ✅      |
| 00:01:C9:b6:4e:76 |              cisco systems, inc              |              cisco systems, inc              |      ✅      |
| 0C-41-3E-b6-4e-76 |            microsoft corporation             |            microsoft corporation             |      ✅      |
| 0?:00:00:00:00:00 |                  Bad format                  |                  Bad format                  |      ✅      |
| ff:ff:ff:ff:ff:ff | No company corresponding to this MAC Address | No company corresponding to this MAC Address |      ✅      |
+-------------------+----------------------------------------------+----------------------------------------------+--------------+
```



