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

## Why? Purpose
MAC address vendor identification offers significant benefits in network management and security. By discerning the vendor from a MAC address, network administrators can swiftly **troubleshoot connectivity issues**, as different vendors have distinct MAC address prefixes. This knowledge streamlines network inventory management, facilitating the tracking of devices on the network. Additionally, it aids in **security monitoring** by detecting unauthorized devices, with unfamiliar or rogue MAC addresses standing out amidst known vendor patterns. This proactive approach enhances network security by swiftly identifying potential threats.

Furthermore, the ability to identify devices by vendor assists in implementing **quality of service** (QoS) measures, prioritizing traffic based on device types. Automation tools leverage this information to configure devices, assign VLANs, and apply specific network rules. In **forensic analysis**, knowing the vendor of devices involved in security incidents enables efficient tracing of attack sources. Overall, MAC address vendor identification is a pivotal aspect of network administration, providing insights into **device types**, aiding in compliance with regulations, and empowering administrators to maintain efficient, secure, and well-managed networks.


## Technical choices
- The code utilizes the `requests` library for making HTTP requests to interact with the API, a common choice for its robustness and ease of use in Python.
  
- Sensible handling of the API key is implemented by storing it in an environment variable (`X-RAPIDAPI-KEY`) accessed using `os.environ`, enhancing security and ease of configuration for different environments.

- The `format_mac_address` function validates the input MAC address using regular expressions (RegEx), ensuring it matches the expected format before making the API call, thus improving the application's reliability.

- Exception handling, like using `try-except` blocks around the API requests, allows for graceful handling of potential errors such as HTTP errors or missing data in the API response, enhancing the code's robustness and maintainability.

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



