import urequests
import machine
import time

from secrets import *
from do_connect import *
do_connect()

sensor=machine.Pin(17,machine.Pin.IN)
button=machine.Pin(16,machine.Pin.IN)
alarm = machine.Pin(15, machine.Pin.OUT)

# work once at boot
alarm.high()
time.sleep_ms(50)
alarm.low()

event='SecurityWarning'
message=f"https://maker.ifttt.com/trigger/{event}/with/key/{secrets['webhooks_key']}"

warn_flag=False


def motion_detected(pin):
    urequests.post(message)
    print(message)
    global warn_flag
    warn_flag=True
    sensor.irq(handler=None)

def reset_device(pin):
    machine.reset()
    

sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=motion_detected)

button.irq(trigger=machine.Pin.IRQ_RISING, handler=reset_device)

while True:
    if warn_flag==True:
        alarm.toggle()
        time.sleep_ms(50)