import machine
import time


buzzer = machine.PWM(machine.Pin(15))
led = machine.PWM(machine.Pin(16))
led.freq(1000)

switch = machine.Pin(17,machine.Pin.IN)

def noTone(pin):
    pin.duty_u16(0)


def tone(pin,frequency):
    pin.freq(frequency)
    pin.duty_u16(30000)

def interval_mapping(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def toggle(pin):
    global bell_flag
    bell_flag = not bell_flag
    print(bell_flag)
    if bell_flag:
        switch.irq(trigger=machine.Pin.IRQ_FALLING, handler=toggle)
    else:
        switch.irq(trigger=machine.Pin.IRQ_RISING, handler=toggle)


bell_flag = False
switch.irq(trigger=machine.Pin.IRQ_RISING, handler=toggle)



while True:
    if bell_flag == True:
        for i in range(0,100,2):
            led.duty_u16(int(interval_mapping(i,0,100,0,65535)))
            tone(buzzer,int(interval_mapping(i,0,100,130,800)))
            time.sleep_ms(10)
    else:
        noTone(buzzer)
        led.duty_u16(0)

    
    

