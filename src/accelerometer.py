import adafruit_lsm303_accel
import adafruit_lis2mdl
import numpy as np

from math import atan2
from math import pi as π
from vectormath import norm
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
    
    def calibrated(self,raw_reading):
        hardiron_calibration = [[-53.699999999999996, 16.5], [-64.05, 19.95], [10.35, 105.45]]
        calibrated = [0,0,0]
        for i, axis in enumerate(raw_reading):
            minv,maxv = hardiron_calibration[i]
            axis = min(max(minv,axis),maxv)
            spread = maxv-minv
            calibrated[i] = (axis-minv)/spread
        return np.array(calibrated)
    
    @property
    def heading(self):
        x,y,z = norm(self.magnetation)
        return (atan2(y,x)*180/π)+180

        θ = (π/2)-atan2(x,y)
        if y>0:θ+=π
        θ = θ/(2*π)*360
        return θ

    def update_state(self):
        # m/s^2
        acc = self.ureg.meters/self.ureg.seconds**2
        self.acceleration = np.array(self.accel.acceleration)
        #self.acceleration =  [axis*acc for axis in self.accel.acceleration]
        # µTeslas
        mag = self.ureg.microteslas
        self.magnetation = self.calibrated(self.mag.magnetic)
        #self.magnetation =  [axis*mag for axis in self.mag.magnetic]
