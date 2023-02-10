from ws import WS_Server
import time

from machine import Pin,ADC

# DHT11
from dht import DHT11
sensor = DHT11(Pin(16, Pin.OUT, Pin.PULL_DOWN))

# pump
motor1A = Pin(14, Pin.OUT)
motor2A = Pin(15, Pin.OUT)

# water level
water_level = ADC(28)


# Websocket
ws = WS_Server(8765) 



def pumping(state):
    
    if state == "on":
        motor1A.high()
        motor2A.low()    
    else:
        motor1A.low() 
        motor2A.low()          

def main():
    ws.start()
    print("start")
    
    pump_flag = False
    pump_start_time = False
    dht_start_time = time.ticks_ms()
    
    while True:
        try:
            current_time=time.ticks_ms()
            if current_time - dht_start_time>=1000:
                sensor.measure()
                dht_start_time = current_time
                ws.send_dict['G'] = sensor.temperature
                ws.send_dict['H'] = sensor.humidity
                print("Temperature: {}, Humidity: {}".format(sensor.temperature, sensor.humidity))
        except:
            print("no data")
            pass
            

        ws.send_dict['P'] = water_level.read_u16()
        #print(ws.send_dict)
        
        status,result=ws.transfer()
        
        if status == True and "M" in result:
            #print(result['M'])
            if result['M']==True and pump_flag==False:
                pumping("on")
                pump_flag = True
                pump_start_time = time.ticks_ms()
            pass
            
        current_time=time.ticks_ms()
        if current_time - pump_start_time>=5000: # water for less than 5s
            pumping("off")
            pump_flag= False

        time.sleep_ms(100)


try:
    main()
finally:
    ws.stop()