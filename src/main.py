print("starting")
from rocket import Rocket
import time

if __name__ == "__main__":
    rocket = Rocket()
    while True:
        print("looping...")
        rocket.update_state()
        rocket.log_state()
        rocket.broadcast_state()
        rocket.check_for_parachute_condition()
        time.sleep(1)
