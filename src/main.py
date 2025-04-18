print("starting")
from rocket import Rocket
import time
import board

if __name__ == "__main__":
    print("starting rocket")
    rocket = Rocket()
    while True:
        print("looping...")
        rocket.update_state()
        #rocket.log_state()
        #rocket.broadcast_state()
        #rocket.check_for_parachute_condition()
        rocket.calibrate_sensor_floor()
        print(f"acceleration:{rocket.relative_acceleration}")
        print(f"magnetation:{rocket.magnetation}")
        print(f"temp:{rocket.temperature.to('fahrenheit')}")
        print(f"pressure:{rocket.pressure.to('atm')}")
        print(f"pressure_altitude:{rocket.relative_pressure_altitude} m")
        time.sleep(1)
