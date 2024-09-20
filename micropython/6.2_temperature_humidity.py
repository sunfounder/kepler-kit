from machine import Pin
import utime as time
from dht import DHT11

# Initialize the pin for the DHT11 sensor as an input
pin = Pin(16, Pin.IN)

# Create a DHT11 sensor object
sensor = DHT11(pin)

while True:
    # Measure temperature and humidity
    sensor.measure()
    
    # Print the measured temperature and humidity values
    print("Temperature: {}, Humidity: {}".format(sensor.temperature, sensor.humidity))
    
    # Wait for 1 second before the next measurement
    time.sleep(1)

