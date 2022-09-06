import machine
import utime

relay = machine.Pin(15, machine.Pin.OUT)
while True:
    relay.value(1)
    utime.sleep(2)
    relay.value(0)
    utime.sleep(2)