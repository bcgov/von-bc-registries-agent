
import asyncio
import time

from bcreg.credssubmitter import CONTROLLER_HEALTH_URL, CONTROLLER_HEALTH_WAIT, CONTROLLER_HEALTH_TIMEOUT, check_controller_health


print("Pinging " + CONTROLLER_HEALTH_URL + " ...")
try:
    loop = asyncio.get_event_loop()
    start_time = time.perf_counter()
    while (time.perf_counter() - start_time) < CONTROLLER_HEALTH_TIMEOUT:
        controller_health = loop.run_until_complete(check_controller_health(wait=False))
        print("Status of " + CONTROLLER_HEALTH_URL + " is " + str(controller_health))
        time.sleep(CONTROLLER_HEALTH_WAIT)
except Exception as e:
    print("Exception", e)
    raise
