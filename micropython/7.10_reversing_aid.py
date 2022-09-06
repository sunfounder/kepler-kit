import machine
import time
import _thread


buzzer = machine.Pin(15, machine.Pin.OUT)
led = machine.Pin(14, machine.Pin.OUT)

TRIG = machine.Pin(17,machine.Pin.OUT)
ECHO = machine.Pin(16,machine.Pin.IN)

dis = 100

def distance():
    timeout=10000*5/340 
    TRIG.low()
    time.sleep_us(2)
    TRIG.high()
    time.sleep_us(10)
    TRIG.low()
    timeout_start = time.ticks_ms() # For timeout, re-read distance
    while not ECHO.value():
        waiting_time = time.ticks_ms()
        if waiting_time - timeout_start > timeout:
            return -1
    time1 = time.ticks_us()
    while ECHO.value():
        waiting_time = time.ticks_ms()
        if waiting_time - timeout_start > timeout:
            return -1
    time2 = time.ticks_us()
    during = time.ticks_diff(time2 ,time1)
    return during * 340 / 2 / 10000

def ultrasonic_thread():
    global dis
    while True:
        dis = distance()

_thread.start_new_thread(ultrasonic_thread, ())

def beep():
    buzzer.value(1)
    led.value(1)
    time.sleep(0.1)
    buzzer.value(0)
    led.value(0)
    time.sleep(0.1)

intervals = 10000000
previousMills=time.ticks_ms()
time.sleep(1) 

while True:
    if dis<0:
        pass
    elif dis <= 10:
        intervals = 300
    elif dis <= 20:
        intervals =500
    elif dis <=50:
        intervals =1000
    else:
        intervals = 2000
    if dis!=-1:
        print ('Distance: %.2f' % dis)
        time.sleep_ms(100)

    
    currentMills=time.ticks_ms()
    
    if time.ticks_diff(currentMills,previousMills)>=intervals:
        beep()
        previousMills=currentMills
    
