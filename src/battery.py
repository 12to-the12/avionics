from INA219 import INA219

class Battery:
    def __init__(self,ureg,addr=0x43):
        self.ureg = ureg
        self.device = INA219(addr=addr)
        self.update_state()
    
    def update_state(self):
        self.bus_voltage = self.device.getBusVoltage_V()*self.ureg.volts
        self.shunt_voltage = self.device.getShuntVoltage_mV()*self.ureg.millivolts
        self.current = self.device.getCurrent_mA()*self.ureg.milliamps
        self.power = self.device.getPower_W()*self.ureg.watts
        self.level = (self.bus_voltage-3*self.ureg.volts)/(1.2*self.ureg.volts)

    def __repr__(self) -> str:
        return f"{self.current=} {self.power=} {self.level=} "

if __name__=="__main__":
    from pint import UnitRegistry
    ureg=  UnitRegistry()
    battery = Battery(ureg)
    print(battery.level)
