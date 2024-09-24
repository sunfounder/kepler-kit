import machine
import time

# Initialize PIR sensor on pin 16, configured as an input
pir_sensor = machine.Pin(16, machine.Pin.IN)

# 7-segment display codes for digits 0-9, using hexadecimal to represent LED segments
SEGCODE = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]

# Define pins for shift register communication (74HC595)
sdi = machine.Pin(18, machine.Pin.OUT)   # Serial Data Input
rclk = machine.Pin(19, machine.Pin.OUT)  # Register Clock (Latch)
srclk = machine.Pin(20, machine.Pin.OUT) # Shift Register Clock

# Initialize list to store 4 digit control pins
placePin = []

# Define control pins for each of the four digits (common anodes)
pin = [10,13,12,11] # Pin numbers for the 4-digit display
for i in range(4):
    placePin.append(None)  # Reserve space in list
    placePin[i] = machine.Pin(pin[i], machine.Pin.OUT)  # Initialize pin as output

# Initialize counter to keep track of detected motion events
count = 0

# Function to select which digit (0-3) to display by controlling the common anode pins
def pickDigit(digit):
    for i in range(4):
        placePin[i].value(1)  # Turn off all digits
    placePin[digit].value(0)  # Turn on the selected digit

# Function to clear the display by sending '0x00' to the shift register
def clearDisplay():
    hc595_shift(0x00)

# Function to send data to the shift register (74HC595)
def hc595_shift(dat):
    rclk.low()  # Pull latch low to prepare for data shifting
    time.sleep_us(200)  # Small delay for timing stability
    for bit in range(7, -1, -1):  # Loop through each bit (MSB first)
        srclk.low()  # Prepare to send the next bit
        time.sleep_us(200)
        value = 1 & (dat >> bit)  # Extract the current bit from the data
        sdi.value(value)  # Set the data line to the current bit value
        time.sleep_us(200)
        srclk.high()  # Pulse the shift clock to store the bit in the register
        time.sleep_us(200)
    time.sleep_us(200)
    rclk.high()  # Pulse the register clock to move the data to the output

# Interrupt handler for PIR sensor, triggered on motion detection (rising edge)
# Increments the motion count each time the sensor is triggered
def motion_detected(pin):
    global count
    count = count + 1  # Increment the count when motion is detected

# Set up an interrupt to detect motion using the PIR sensor
pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=motion_detected)

# Main loop to continuously update the 7-segment display with the current count
while True:
    # Update the first digit (units place)
    pickDigit(0)
    hc595_shift(SEGCODE[count % 10])

    # Update the second digit (tens place)
    pickDigit(1)
    hc595_shift(SEGCODE[count % 100 // 10])

    # Update the third digit (hundreds place)
    pickDigit(2)
    hc595_shift(SEGCODE[count % 1000 // 100])

    # Update the fourth digit (thousands place)
    pickDigit(3)
    hc595_shift(SEGCODE[count % 10000 // 1000])


