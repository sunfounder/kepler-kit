import time
from machine import Pin
from umqtt.simple import MQTTClient

from do_connect import *
do_connect()

sensor1 = Pin(16, Pin.IN)
sensor2 = Pin(17, Pin.IN)
sensor3 = Pin(18, Pin.IN)
sensor4 = Pin(19, Pin.IN)

mqtt_server = 'broker.hivemq.com'
client_id = 'Jimmy'

topic = b'SunFounder MQTT Test'

try:
    client = MQTTClient(client_id, mqtt_server, keepalive=3600)
    client.connect()
    print('Connected to %s MQTT Broker'%(mqtt_server))
except OSError as e:
    print('Failed to connect to the MQTT Broker. Reconnecting...')
    time.sleep(5)
    machine.reset()

# button 
def press1(pin):
    message = b'button 1 is pressed'
    client.publish(topic, message)
    print(message)

sensor1.irq(trigger=machine.Pin.IRQ_RISING, handler=press1)

def press2(pin):
    message = b'button 2 is pressed'
    client.publish(topic, message)
    print(message)

sensor2.irq(trigger=machine.Pin.IRQ_RISING, handler=press2)

def press3(pin):
    message = b'button 3 is pressed'
    client.publish(topic, message)
    print(message)

sensor3.irq(trigger=machine.Pin.IRQ_RISING, handler=press3)

def press4(pin):
    message = b'button 4 is pressed'
    client.publish(topic, message)
    print(message)

sensor4.irq(trigger=machine.Pin.IRQ_RISING, handler=press4)
