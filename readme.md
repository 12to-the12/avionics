# SBCC Aerospace and Rocketry club avionics source code


# todo
- [x] zero online
- [x] battery online
- [x] accelerometer online
- [x] altimeter online
- [x] camera online
- [ ] gps online
- [ ] components soldered inplace
- [ ] LoRa working with ground station
- [ ] servo control functional
- [ ] black powder ignition functional



# circuit diagram:
```mermaid
graph LR


raspi(Raspberry Pi Zero 2W)

raspi o-..-o loraA(RFM95W)
raspi o-..-o gps(PA1616D)
raspi o-..-o altimeter(BMP388)
raspi o-..-o accelerometer(LSM303AGR)
raspi o===o ups(UPS)
raspi o--o camera(camera)
raspi o--o servo(servo)


```