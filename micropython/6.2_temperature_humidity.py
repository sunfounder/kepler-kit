from machine import Pin
import utime as time
from dht import DHT11, InvalidPulseCount

pin = Pin(16, Pin.IN)
sensor = DHT11(pin)
time.sleep(5)  # initial delay

while True:
    try:
        sensor.measure()
        string = "Temperature:{}\nHumidity: {}".format(sensor.temperature, sensor.humidity)
        print(string)
        time.sleep(4)

    except InvalidPulseCount as e:
        print('Bad pulse count - retrying ...')
