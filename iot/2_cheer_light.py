import urequests
import json
import time
import machine
from ws2812 import WS2812

from do_connect import *
do_connect()

ws = WS2812(machine.Pin(0), 8)

def get_colour():
    url = "http://api.thingspeak.com/channels/1417/field/2/last.json"
    try:
        r = urequests.get(url)
        if r.status_code > 199 and r.status_code < 300:
            cheerlights = json.loads(r.content.decode('utf-8'))
            print(cheerlights['field2'])
            colour = int('0x'+cheerlights['field2'][1:7])
            r.close()
            return colour
        else:
            return None
    except Exception as e:
        print(e)
        return None

while True:
    colour = get_colour()
    if colour is not None:
        ws.write_all(colour)
    time.sleep(60)
