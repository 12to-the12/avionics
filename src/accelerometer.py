import adafruit_lsm303_accel
import adafruit_lis2mdl

class Accelerometer:
    def __init__(self,i2c,ureg):
        self.ureg = ureg
        self.accel = adafruit_lsm303_accel.LSM303_Accel(i2c)
        self.mag = adafruit_lis2mdl.LIS2MDL(i2c)
        self.acceleration = None
        self.magnetation = None
    
    @property
    def x(self):
        return self.acceleration[0]

    @property
    def y(self):
        return self.acceleration[1]

    @property
    def z(self):
        return self.acceleration[2]

    def update_state(self):
        # m/s^2
        acc = self.ureg.meters/self.ureg.seconds**2
        self.acceleration =  [axis*acc for axis in self.accel.acceleration]
        # µTeslas
        mag = self.ureg.microteslas
        self.magnetation =  [axis*mag for axis in self.mag.magnetic]
