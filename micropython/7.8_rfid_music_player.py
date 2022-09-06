###################################
# Use 'write.py' to write a score #
# for the card, this example will #
# play the score                  #
###################################
# The music score of Ode an Joy:  #
# EEFGGFEDCCDEEDD EEFGGFEDCCDEDCC #
###################################

from mfrc522 import SimpleMFRC522
import machine
import time
from ws2812 import WS2812
import urandom

# ws2812
ws = WS2812(machine.Pin(16),8)

# mfrc522
reader = SimpleMFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=5,rst=0)

# buzzer
NOTE_C4 = 262
NOTE_D4 = 294
NOTE_E4 = 330
NOTE_F4 = 349
NOTE_G4 = 392
NOTE_A4 = 440
NOTE_B4 = 494
NOTE_C5 = 523

buzzer = machine.PWM(machine.Pin(15))
note=[NOTE_C4,NOTE_D4,NOTE_E4,NOTE_F4,NOTE_G4,NOTE_A4,NOTE_B4,NOTE_C5]

def tone(pin,frequency,duration):
    pin.freq(frequency)
    pin.duty_u16(30000)
    time.sleep_ms(duration)
    pin.duty_u16(0)


# lightup
def lumi(index):
    for i in range(8):
        ws[i] = 0x0000FF
    ws[index] = 0xFF0000 # int(urandom.uniform(0, 0xFFFFFF))  
    ws.write() 

# encode text to index
words=["C","D","E","F","G","A","B","N"]
def take_text(text):
    string=text.replace(' ','').upper()
    while len(string)>0:
        index=words.index(string[0])
        tone(buzzer,note[index],250)
        lumi(index)
        new_str=""
        for i in range(0, len(string)):
            if i != 0:
                new_str = new_str + string[i]
        string=new_str

# read card
def read():
    print("Reading...Please place the card...")
    id, text = reader.read()
    print("ID: %s\nText: %s" % (id,text))
    take_text(text)
    
read()


