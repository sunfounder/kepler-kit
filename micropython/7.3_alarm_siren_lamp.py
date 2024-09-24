import machine
import time

# Initialize the PWM for the buzzer (on pin 15) and LED (on pin 16)
buzzer = machine.PWM(machine.Pin(15))  # PWM for buzzer
led = machine.PWM(machine.Pin(16))  # PWM for LED
led.freq(1000)  # Set the frequency of the LED PWM to 1kHz

# Initialize the switch (on pin 17) as an input pin
switch = machine.Pin(17, machine.Pin.IN)

# Function to stop the buzzer by setting the duty cycle to 0%
def noTone(pin):
    pin.duty_u16(0)  # Set the PWM duty cycle to 0, stopping the sound

# Function to play a tone on the buzzer with a specified frequency
def tone(pin, frequency):
    pin.freq(frequency)  # Set the frequency for the buzzer
    pin.duty_u16(30000)  # Set duty cycle to around 50% (30000 out of 65535)

# Function to map a value from one range to another
def interval_mapping(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# Interrupt handler function to toggle the bell_flag when the switch is pressed
def toggle(pin):
    global bell_flag
    bell_flag = not bell_flag  # Toggle the bell_flag value
    print(bell_flag)  # Print the current state of bell_flag for debugging
    
    # Change the switch interrupt depending on the state of the bell_flag
    if bell_flag:
        # If bell_flag is True, listen for a falling edge (when switch is released)
        switch.irq(trigger=machine.Pin.IRQ_FALLING, handler=toggle)
    else:
        # If bell_flag is False, listen for a rising edge (when switch is pressed)
        switch.irq(trigger=machine.Pin.IRQ_RISING, handler=toggle)

# Initialize bell_flag to False (buzzer and LED off by default)
bell_flag = False

# Set up an interrupt to detect when the switch is pressed (rising edge)
switch.irq(trigger=machine.Pin.IRQ_RISING, handler=toggle)

# Main loop to control the buzzer and LED based on the bell_flag
while True:
    if bell_flag == True:
        # If bell_flag is True, gradually increase the brightness of the LED
        # and change the buzzer frequency to simulate a bell ringing effect
        for i in range(0, 100, 2):  # Loop from 0 to 100 in steps of 2
            led.duty_u16(int(interval_mapping(i, 0, 100, 0, 65535)))  # Map i to LED brightness
            tone(buzzer, int(interval_mapping(i, 0, 100, 130, 800)))  # Map i to buzzer frequency
            time.sleep_ms(10)  # Short delay to create a smooth ramp
    else:
        # If bell_flag is False, stop the buzzer and turn off the LED
        noTone(buzzer)  # Stop the buzzer
        led.duty_u16(0)  # Turn off the LED (set duty cycle to 0)

