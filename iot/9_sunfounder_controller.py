from ws import WS_Server
import json
import time

import machine

TRIG = machine.Pin(17,machine.Pin.OUT)
ECHO = machine.Pin(16,machine.Pin.IN)

servo = machine.PWM(machine.Pin(15))
servo.freq(50)

ws = WS_Server(8765) # init websocket 

def interval_mapping(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def servo_write(pin,angle):
    pulse_width=interval_mapping(angle, 0, 180, 0.5,2.5)
    duty=int(interval_mapping(pulse_width, 0, 20, 0,65535))
    pin.duty_u16(duty)

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

def main():
    ws.start()
    print("start")
    while True:
        dis=distance()
        if dis < 100.00 and dis >0.00:
            ws.send_dict['L'] = dis

        status,result=ws.transfer()
        
        if status == True:
            #print(result['H'])
            servo_write(servo,result['H'])

        time.sleep_ms(100)


try:
    main()
finally:
    ws.stop()
