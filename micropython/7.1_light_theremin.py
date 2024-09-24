import machine
import utime

# Initialize LED, photoresistor, and buzzer
led = machine.Pin(16, machine.Pin.OUT)  # LED on pin 16
photoresistor = machine.ADC(28)  # Photoresistor on ADC pin 28
buzzer = machine.PWM(machine.Pin(15))  # Buzzer on pin 15 with PWM

# Variables to store the highest and lowest light readings for calibration
light_low = 65535 
light_high = 0 

# Function to map one range of values to another
def interval_mapping(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# Function to play a tone on the buzzer at a specified frequency for a set duration
def tone(pin, frequency, duration):
    pin.freq(frequency)  # Set buzzer frequency
    pin.duty_u16(30000)  # Set duty cycle to around 50%
    utime.sleep_ms(duration)  # Play the tone for the specified duration
    pin.duty_u16(0)  # Turn off the tone by setting duty cycle to 0

# Calibrate the photoresistor by finding the highest and lowest light values over 5 seconds
timer_init_start = utime.ticks_ms()  # Get the current time (start time)
led.value(1)  # Turn on LED to indicate calibration is in progress
while utime.ticks_diff(utime.ticks_ms(), timer_init_start) < 5000:  # Run calibration for 5 seconds
    light_value = photoresistor.read_u16()  # Read the light value from the photoresistor
    if light_value > light_high:  # Track the maximum light value
        light_high = light_value
    if light_value < light_low:  # Track the minimum light value
        light_low = light_value
led.value(0)  # Turn off the LED after calibration

# Main loop to read light levels and play corresponding tones
while True:
    light_value = photoresistor.read_u16()  # Read the current light value from the photoresistor
    pitch = int(interval_mapping(light_value, light_low, light_high, 50, 6000))  # Map light value to a pitch range
    if pitch > 50:  # Only play tones if the pitch is above a minimum threshold
        tone(buzzer, pitch, 20)  # Play the corresponding pitch for 20ms
    utime.sleep_ms(10)  # Small delay between readings

