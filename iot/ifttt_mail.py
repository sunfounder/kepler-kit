import urequests
import machine

from secrets import *
from do_connect import *
do_connect()

sensor=machine.Pin(14,machine.Pin.IN)

event='SecurityWarning'
message=f"https://maker.ifttt.com/trigger/{event}/json/with/key/{secrets['webhooks_key']}"

def motion_detected(pin):
    urequests.post(message)
    print(message)

sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=motion_detected)

