from accelerometer import Accelerometer
from altimeter import Altimeter
from radio import Radio
from servo import Servo
from gps import GPS
from battery import Battery


import board

from pint import UnitRegistry
import time

from vectormath import magnitude, angle, norm

class Rocket:
    def __init__(self):
        self.i2c = board.I2C()
        # necessary flag for ease of temperature handling,  careful
        self.ureg = UnitRegistry(autoconvert_offset_to_baseunit = True)
        self.accelerometer = Accelerometer(self.i2c,self.ureg)
        self.altimeter = Altimeter(self.i2c,self.ureg)
        self.radio = Radio()
        self.servo = Servo()
        self.gps = GPS()
        self.battery = Battery(self.ureg)

        self.stamp = time.time()
        self.calibrate_sensor_floor()
        
        self.total_x_displacement = 0


    def update_state(self):
        self.accelerometer.update_state()
        self.altimeter.update_state()
        self.gps.update_state()
        self.battery.update_state()

        self.acceleration = self.accelerometer.acceleration
        self.magnetation = self.accelerometer.magnetation
        self.pressure_altitude = self.altimeter.altitude
        self.pressure = self.altimeter.pressure
        self.temperature = self.altimeter.temperature

        self.battery_level = self.battery.level
        self.heading = self.accelerometer.heading


    def calculate_integrals(self):
        now = time.time()
        elapsed = (now-self.stamp)*self.ureg.seconds
        self.stamp = now
        self.x_integral = elapsed * self.relative_acceleration[0]
        self.total_x_displacement += self.x_integral


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
        return self.heading
        return f"\
        {self.accelerometer.state},\
        {self.altimeter.state},\
        {self.gps.state},\
        "
    @property
    def relative_pressure(self):
        return self.pressure- self.pressure_floor

    @property
    def relative_pressure_altitude(self):
        return self.pressure_altitude - self.pressure_altitude_floor

    @property
    def relative_acceleration(self) -> list:
        return [ val-floor_val for val,floor_val in zip(self.acceleration,self.acceleration_floor )]
    @property
    def angle_between_acc_and_north(self):
        pass

    def calibrate_sensor_floor(self) -> None:
        self.update_state()
        self.pressure_floor = self.pressure
        self.pressure_altitude_floor = self.pressure_altitude
        self.acceleration_floor = self.acceleration
        self.epoch_start = time.time()
    def __repr__(self) -> str:
        return f"""
        acceleration:{magnitude(self.acceleration)}
        magnetation:{self.magnetation}
        temp:{self.temperature:.0f}
        battery level:{self.battery_level.magnitude*100:.2f}%
        """
        

