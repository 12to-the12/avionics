# SBCC Aerospace and Rocketry club avionics source code




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