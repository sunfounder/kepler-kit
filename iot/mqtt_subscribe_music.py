import time
from machine import Pin,PWM
from umqtt.simple import MQTTClient


### buzzer
from play_music import *
buzzer = PWM(Pin(15))
play_flag = False

# Wi-Fi
from do_connect import *
do_connect()

# mqtt
mqtt_server = 'broker.hivemq.com'
client_id = 'Jimmy'

# to subscribe the message
topic = b'SunFounder MQTT Music'


def callback(topic, message):
    print("New message on topic {}".format(topic.decode('utf-8')))
    message = message.decode('utf-8')
    print(message)
    if message in song.keys():
        global melody,play_flag
        melody = song[message]
        play_flag = True


try:
    client = MQTTClient(client_id, mqtt_server, keepalive=60)
    client.set_callback(callback)
    client.connect()
    print('Connected to %s MQTT Broker'%(mqtt_server))
except OSError as e:
    print('Failed to connect to MQTT Broker. Reconnecting...')
    time.sleep(5)
    machine.reset()
    
    
while True:
    client.subscribe(topic)
    time.sleep(1)
    if play_flag is True:
        play(buzzer,melody)
        play_flag = False

