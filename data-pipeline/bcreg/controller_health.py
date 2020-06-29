
import asyncio

from bcreg.credssubmitter import CONTROLLER_HEALTH_URL, check_controller_health


print("Pinging " + CONTROLLER_HEALTH_URL + " ...")
try:
    loop = asyncio.get_event_loop()
    controller_health = loop.run_until_complete(check_controller_health(wait=True))
    print("Status of " + CONTROLLER_HEALTH_URL + " is " + str(controller_health))
except Exception as e:
    print("Exception", e)
    raise
