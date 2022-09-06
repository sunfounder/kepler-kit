import machine
import utime

sensor = machine.ADC(28)

while True:
    value=sensor.read_u16()
    print(value)
    utime.sleep_ms(200)