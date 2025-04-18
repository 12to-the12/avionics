import adafruit_bmp3xx

class Altimeter:
    def __init__(self,i2c,ureg,addr=0x77):
        self.ureg = ureg
        self.device = adafruit_bmp3xx.BMP3XX_I2C(i2c,addr)
        self.pressure = None
        self.temperature = None
        self.altitude = None
    def update_state(self):
        # pressure in hPa (100 Pascals)
        self.pressure = self.device.pressure
        #self.pressure = self.device.pressure*self.ureg.hectopascals
        # temperature in C
        self.temperature = self.device.temperature
        #self.temperature = self.device.temperature*self.ureg.celsius
        # altitude in meters from barometer
        self.altitude = self.device.altitude
        #self.altitude = self.device.altitude*self.ureg.meters
