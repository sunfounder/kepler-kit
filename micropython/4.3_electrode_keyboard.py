from mpr121 import MPR121
from machine import Pin, I2C
import time

i2c = I2C(1, sda=Pin(6), scl=Pin(7))
mpr = MPR121(i2c)

# check all keys
while True:
    value = mpr.get_all_states()
    if len(value) != 0:
        print(value)
    time.sleep_ms(100)