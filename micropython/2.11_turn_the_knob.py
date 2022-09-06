import machine
import utime

potentiometer = machine.ADC(28)
led = machine.PWM(machine.Pin(15))
led.freq(1000)

while True:
    value=potentiometer.read_u16()
    print(value)
    led.duty_u16(value)
    utime.sleep_ms(200)
