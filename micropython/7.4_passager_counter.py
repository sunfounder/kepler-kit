import machine
import time


pir_sensor = machine.Pin(16, machine.Pin.IN)

SEGCODE = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]

sdi = machine.Pin(18,machine.Pin.OUT)
rclk = machine.Pin(19,machine.Pin.OUT)
srclk = machine.Pin(20,machine.Pin.OUT)

placePin = []
pin = [10,13,12,11]
for i in range(4):
    placePin.append(None)
    placePin[i] = machine.Pin(pin[i], machine.Pin.OUT)

count = 0


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

def motion_detected(pin):
    global count
    count = count+1

pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=motion_detected)

while True:
    #print(count)
    
    pickDigit(0)
    hc595_shift(SEGCODE[count%10])

    pickDigit(1)
    hc595_shift(SEGCODE[count%100//10])
    
    pickDigit(2)
    hc595_shift(SEGCODE[count%1000//100])
    
    pickDigit(3)
    hc595_shift(SEGCODE[count%10000//1000])    