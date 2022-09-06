import machine
import utime

reed_switch = machine.Pin(14, machine.Pin.IN)

def detected(pin):
    print("Magnet!")

reed_switch.irq(trigger=machine.Pin.IRQ_RISING, handler=detected)