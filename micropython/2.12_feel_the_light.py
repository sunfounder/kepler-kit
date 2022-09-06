import machine
import utime

photoresistor = machine.ADC(28)

while True:
    light_value  = photoresistor.read_u16()
    print(light_value)
    utime.sleep_ms(10)