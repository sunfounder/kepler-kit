from lcd1602 import LCD
from machine import I2C, Pin
import utime
import math

# Initialize the thermistor (ADC on pin 28) and LCD display
thermistor = machine.ADC(28)  # Analog input from the thermistor

# Initialize I2C communication for the LCD1602 display
i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)

# Create an LCD object for controlling the LCD1602 display
lcd = LCD(i2c)

# Main loop to continuously read temperature and display it
while True:
    # Read raw ADC value from the thermistor
    temperature_value = thermistor.read_u16()

    # Convert the raw ADC value to a voltage (0-3.3V range)
    Vr = 3.3 * float(temperature_value) / 65535  # ADC value to voltage conversion

    # Calculate the thermistor resistance (using a voltage divider with a 10kOhm resistor)
    Rt = 10000 * Vr / (3.3 - Vr)  # Rt = thermistor resistance

    # Use the Steinhart-Hart equation to calculate the temperature in Kelvin
    # The values used are specific to the thermistor (3950 is the beta coefficient)
    temp = 1 / (((math.log(Rt / 10000)) / 3950) + (1 / (273.15 + 25)))  # Temperature in Kelvin

    # Convert temperature from Kelvin to Celsius
    Cel = temp - 273.15

    # Display the temperature on the LCD in Celsius
    string = " Temperature is \n    " + str('{:.2f}'.format(Cel)) + " C"  # Format string for the LCD
    lcd.message(string)  # Display the string on the LCD

    utime.sleep(1)  # Wait for 1 second
    lcd.clear()  # Clear the LCD for the next reading

