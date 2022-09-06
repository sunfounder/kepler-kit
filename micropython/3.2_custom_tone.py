import machine
import utime

buzzer = machine.PWM(machine.Pin(15))

def tone(pin,frequency,duration):
    pin.freq(frequency)
    pin.duty_u16(30000)
    utime.sleep_ms(duration)
    pin.duty_u16(0)

tone(buzzer,440,250)
utime.sleep_ms(500)
tone(buzzer,494,250)
utime.sleep_ms(500)
tone(buzzer,523,250)