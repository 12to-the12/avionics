from accelerometer import Accelerometer
from altimeter import Altimeter
from radio import Radio
from servo import Servo
from gps import GPS


class Rocket:
    def __init__(self):
        self.accelerometer = Accelerometer()
        self.altimeter = Altimeter()
        self.radio = Radio()
        self.servo = Servo()
        self.gps = GPS()

    def update_state(self):
        self.accelerometer.update_state()
        self.altimeter.update_state()
        self.gps.update_state()

    def log_state(self):
        with open("./logs/log.txt", "a") as logfile:
            print(f"writing: {str(self)}")
            logfile.write(str(self) + "\n")

    def broadcast_state(self):
        print(f"broadcasting: {str(self)}")
        self.radio.broadcast(str(self))

    def check_for_parachute_condition(self):
        if (self.altimeter.state == "super high") and (
            self.accelerometer.state == "not accelerating"
        ):
            self.deploy_parachute()

    def deploy_parachute(self):
        pass

    def __repr__(self) -> str:
        return f"\
        {self.accelerometer.state},\
        {self.altimeter.state},\
        {self.gps.state},\
        "
