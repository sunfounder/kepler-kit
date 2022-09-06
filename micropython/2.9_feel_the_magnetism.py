import machine
import utime
reed = machine.Pin(14, machine.Pin.IN)
while True:
    if reed.value() == 1:
        print("There are magnets here!!")
        utime.sleep(1)