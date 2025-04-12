import board
import adafruit_lsm303_accel
import adafruit_lis2mdl

class Accelerometer:
    def __init__(self):
        self.state = None
        i2c = board.I2C()
        self.accel = adafruit_lsm303_accel.LSM303_Accel(i2c)
        self.mag = adafruit_lis2mdl.LIS2MDL(i2c)

    def update_state(self):
        self.acceleration =  self.accel.acceleration
        self.state = self.acceleration
        self.magnetation = self.mag.magnetic

    

