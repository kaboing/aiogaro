# AIOGaro
Asynchronous library to access Garo Chargeboxes

## This library is under development
Requires Python >= 3.9, uses asyncio and aiohttp

## Usage
In ``example.py``, you find the simplest usage of the library. You need two things to use the library:
* IP number of the Chargebox
* Serial number of the Chargebox

You find the IP number in two ways:
* accessing your router and determine which IP the Chargebox has been given from DHCP
* Log in to http://chargebox.webel.se/ with serial number and password and see where you get redirected. 

Developed with the intention to be used with Home Assistant.
