import machine
import utime

motor1A = machine.Pin(14, machine.Pin.OUT)
motor2A = machine.Pin(15, machine.Pin.OUT)

def clockwise():
    motor1A.high()
    motor2A.low()

def anticlockwise():
    motor1A.low()
    motor2A.high()

def stopMotor():
    motor1A.low()
    motor2A.low()

while True:
    clockwise()
    utime.sleep(1)
    stopMotor()
    utime.sleep(1)
    anticlockwise()
    utime.sleep(1)
    stopMotor()
    utime.sleep(1)