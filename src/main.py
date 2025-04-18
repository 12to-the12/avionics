print("starting")
from rocket import Rocket
import time
import board

if __name__ == "__main__":
    print("starting rocket")
    rocket = Rocket()
    rocket.calibrate_sensor_floor()
    while True:
        rocket.update_state()
        #rocket.calculate_integrals()
        time.sleep(1)
        #rocket.log_state()
        #rocket.broadcast_state()
        #rocket.check_for_parachute_condition()
        print(rocket)
