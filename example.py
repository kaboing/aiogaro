import asyncio
import ipaddress
import logging
from aiogaro import Chargebox


logging.basicConfig(level=logging.DEBUG)

chargebox = Chargebox(
        ipaddress.ip_address("10.0.1.207"), 
        "2315250")

loop = asyncio.get_event_loop()

loop.run_until_complete(
    chargebox.GetCurrentEnergyUsage()
)