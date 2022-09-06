import machine
import utime

buzzer = machine.Pin(15, machine.Pin.OUT)
while True:
    for i in range(4):
        buzzer.value(1)
        utime.sleep(0.3)
        buzzer.value(0)
        utime.sleep(0.3)
    utime.sleep(1)