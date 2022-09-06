import machine
import utime

sensor = machine.ADC(28)
threshold = 30000 #This value needs to be modified with the environment.

while True:
    value=sensor.read_u16()
    if value > threshold :
        print("Liquid leakage!")
    utime.sleep_ms(200)
