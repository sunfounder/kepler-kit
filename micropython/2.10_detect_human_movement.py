import machine
import utime

pir_sensor = machine.Pin(14, machine.Pin.IN)

def motion_detected(pin):
    print("Somebody here!")

pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=motion_detected)