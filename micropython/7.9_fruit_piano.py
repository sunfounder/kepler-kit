from mpr121 import MPR121
from machine import Pin, I2C
import time
import urandom

# mpr121
i2c = I2C(1, sda=Pin(6), scl=Pin(7))
mpr = MPR121(i2c)


# buzzer
NOTE_A3 = 220
NOTE_B3 = 247
NOTE_C4 = 262
NOTE_D4 = 294
NOTE_E4 = 330
NOTE_F4 = 349
NOTE_G4 = 392
NOTE_A4 = 440
NOTE_B4 = 494
NOTE_C5 = 523
NOTE_D5 = 587
NOTE_E5 = 659

buzzer = machine.PWM(machine.Pin(15))
note = [NOTE_A3,NOTE_B3,NOTE_C4,NOTE_D4,NOTE_E4,NOTE_F4,NOTE_G4,NOTE_A4,NOTE_B4,NOTE_C5,NOTE_D5,NOTE_E5]

def tone(pin,frequency):
    pin.freq(frequency)
    pin.duty_u16(30000)

def noTone(pin):
    pin.duty_u16(0)


# rgb led
red = machine.PWM(machine.Pin(13))
green = machine.PWM(machine.Pin(12))
blue = machine.PWM(machine.Pin(11))
red.freq(1000)
green.freq(1000)
blue.freq(1000)

def interval_mapping(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def lightup():
    red.duty_u16(int(urandom.uniform(0, 65535)))
    green.duty_u16(int(urandom.uniform(0, 65535)))
    blue.duty_u16(int(urandom.uniform(0, 65535)))


def dark():
    red.duty_u16(0)
    green.duty_u16(0)
    blue.duty_u16(0)    

# main project
lastState=mpr.get_all_states()
touchMills=time.ticks_ms()
beat=500

while True:
    currentState=mpr.get_all_states()
    if currentState != lastState:
        for i in range(12):
            if i in list(currentState) and not i in list(lastState):
                tone(buzzer,note[i])
                lightup()
                touchMills=time.ticks_ms()
    if time.ticks_diff(time.ticks_ms(),touchMills)>=beat or len(currentState) == 0:
        noTone(buzzer)
        dark()
    lastState = currentState
