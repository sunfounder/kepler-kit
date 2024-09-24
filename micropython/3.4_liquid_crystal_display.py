from machine import I2C, Pin
from lcd1602 import LCD
import time

# Initialize I2C communication;
i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)

# Create an LCD object for interfacing with the LCD1602 display
lcd = LCD(i2c)

# Display the first message on the LCD
# Use '\n' to create a new line.
string = "SunFounder\n    LCD Tutorial"
lcd.message(string)
# Wait for 2 seconds
time.sleep(2)
# Clear the display
lcd.clear()

# Display the second message on the LCD
string = "Hello\n  World!"
lcd.message(string)
# Wait for 5 seconds
time.sleep(5)
# Clear the display before exiting
lcd.clear()
