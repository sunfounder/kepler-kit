from machine import Pin, I2C
import utime as time
from dht import DHT11, InvalidPulseCount

pin = Pin(16, Pin.IN, Pin.PULL_UP)
sensor = DHT11(pin)

while True:
    try:
        sensor.measure()
        string = "Temperature:{}\nHumidity: {}".format(sensor.temperature, sensor.humidity)
        print(string)
        utime.sleep(4)

    except InvalidPulseCount as e:
        print('Bad pulse count - retrying ...')
