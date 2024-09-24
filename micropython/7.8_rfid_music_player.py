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

# WS2812 LED setup
# Initialize an 8-LED WS2812 strip on pin 0
ws = WS2812(machine.Pin(0), 8)

# MFRC522 RFID reader setup
# Initialize the RFID reader using SPI on specific pins
reader = SimpleMFRC522(spi_id=0, sck=18, miso=16, mosi=19, cs=17, rst=9)

# Buzzer note frequencies (in Hertz)
NOTE_C4 = 262
NOTE_D4 = 294
NOTE_E4 = 330
NOTE_F4 = 349
NOTE_G4 = 392
NOTE_A4 = 440
NOTE_B4 = 494
NOTE_C5 = 523

# Initialize PWM for buzzer on pin 15
buzzer = machine.PWM(machine.Pin(15))

# List of note frequencies corresponding to musical notes
note = [NOTE_C4, NOTE_D4, NOTE_E4, NOTE_F4, NOTE_G4, NOTE_A4, NOTE_B4, NOTE_C5]

# Function to play a tone on the buzzer with a specified frequency and duration
def tone(pin, frequency, duration):
    pin.freq(frequency)  # Set the buzzer frequency
    pin.duty_u16(30000)  # Set duty cycle to 50% (approx)
    time.sleep_ms(duration)  # Play the tone for the specified duration
    pin.duty_u16(0)  # Stop the tone by setting duty cycle to 0

# Function to light up a WS2812 LED at a specific index with a random color
def lumi(index):
    for i in range(8):
        ws[i] = 0x000000  # Turn off all LEDs
    ws[index] = int(urandom.uniform(0, 0xFFFFFF))  # Set a random color for the LED at the given index
    ws.write()  # Write the color data to the WS2812 LEDs

# Encode musical notes text into indices and play the corresponding notes
words = ["C", "D", "E", "F", "G", "A", "B", "N"]  # Mapping of musical notes to text characters
def take_text(text):
    string = text.replace(' ', '').upper()  # Remove spaces and convert the text to uppercase
    while len(string) > 0:
        index = words.index(string[0])  # Find the index of the first note in the string
        tone(buzzer, note[index], 250)  # Play the corresponding note on the buzzer for 250 ms
        lumi(index)  # Light up the LED corresponding to the note
        string = string[1:]  # Move to the next character in the string

# Function to read from the RFID card and play the stored score
def read():
    print("Reading...Please place the card...")
    id, text = reader.read()  # Read the RFID card (ID and stored text)
    print("ID: %s\nText: %s" % (id, text))  # Print the ID and text
    take_text(text)  # Play the score from the text stored on the card
    
# Start reading from the RFID card and play the corresponding score
read()

