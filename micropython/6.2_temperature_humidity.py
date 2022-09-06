from machine import Pin, I2C
import utime as time
from dht import DHT11

pin = Pin(16, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(pin)

while True:
    sensor.measure()
    print("Temperature: {}, Humidity: {}".format(sensor.temperature, sensor.humidity))
    time.sleep(1)