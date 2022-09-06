
import machine
import time
from machine import Timer

# [Green, Yellow, Red]
lightTime=[30, 5, 30]

# display
SEGCODE = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]

sdi = machine.Pin(18,machine.Pin.OUT)
rclk = machine.Pin(19,machine.Pin.OUT)
srclk = machine.Pin(20,machine.Pin.OUT)

placePin = []
pin = [10,13,12,11]
for i in range(4):
    placePin.append(None)
    placePin[i] = machine.Pin(pin[i], machine.Pin.OUT)

def pickDigit(digit):
    for i in range(4):
        placePin[i].value(1)
    placePin[digit].value(0)

def clearDisplay():
    hc595_shift(0x00)

def hc595_shift(dat):
    rclk.low()
    time.sleep_us(200)
    for bit in range(7, -1, -1):
        srclk.low()
        time.sleep_us(200)
        value = 1 & (dat >> bit)
        sdi.value(value)
        time.sleep_us(200)
        srclk.high()
        time.sleep_us(200)
    time.sleep_us(200)
    rclk.high()

def display(num):
    
    pickDigit(0)
    hc595_shift(SEGCODE[num%10])

    pickDigit(1)
    hc595_shift(SEGCODE[num%100//10])
    
    pickDigit(2)
    hc595_shift(SEGCODE[num%1000//100])
    
    pickDigit(3)
    hc595_shift(SEGCODE[num%10000//1000])    

# led
# 9Red, 8Yellow,7Green
pin = [7,8,9]
led=[]
for i in range(3):
    led.append(None)
    led[i] = machine.Pin(pin[i], machine.Pin.OUT)

def lightup(state):
    for i in range(3):
        led[i].value(0)
    led[state].value(1)

# timer
counter = 0
color_state= 0

def time_count(ev):
    global counter, color_state
    counter -= 1
    if counter <= 0:
        color_state = (color_state+1) % 3
        counter = lightTime[color_state]
        
tim = Timer(period=1000, mode=Timer.PERIODIC, callback=time_count)


while True:
    display(counter)
    lightup(color_state)
