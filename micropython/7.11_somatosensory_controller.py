from imu import MPU6050
from machine import I2C, Pin
import time
import math

# Initialize I2C communication for MPU6050 accelerometer
i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
mpu = MPU6050(i2c)

# Initialize PWM for the servo on pin 15 with a frequency of 50Hz
servo = machine.PWM(machine.Pin(15))
servo.freq(50)

# Function to map a value from one range to another
def interval_mapping(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# Function to calculate the Euclidean distance between two points
def dist(a, b):
    return math.sqrt((a * a) + (b * b))

# Function to calculate the rotation along the y-axis
def get_y_rotation(x, y, z):
    radians = math.atan2(x, dist(y, z))
    return -math.degrees(radians)

# Function to calculate the rotation along the x-axis
def get_x_rotation(x, y, z):
    radians = math.atan2(y, dist(x, z))
    return math.degrees(radians)

# Function to control the servo based on the angle
# Maps the angle (0-180) to the PWM duty cycle for servo control
def servo_write(pin, angle):
    pulse_width = interval_mapping(angle, 0, 180, 0.5, 2.5)  # Map angle to pulse width in ms (0.5ms to 2.5ms)
    duty = int(interval_mapping(pulse_width, 0, 20, 0, 65535))  # Convert pulse width to PWM duty cycle (0-65535)
    pin.duty_u16(duty)  # Set the duty cycle for the servo PWM

# Define the number of readings to average for smoother motion
times = 25

# Main loop
while True:
    total = 0
    # Take multiple readings to average the angle for smoothness
    for i in range(times):
        angle = get_y_rotation(mpu.accel.x, mpu.accel.y, mpu.accel.z)  # Get the y-axis rotation value from the accelerometer
        total += angle  # Accumulate the readings

    average_angle = int(total / times)  # Calculate the average angle
    # Map the average angle (-90 to 90) to the servo's movement range (0 to 180 degrees)
    servo_write(servo, interval_mapping(average_angle, -90, 90, 0, 180))

    time.sleep(0.1)  # Add a small delay to reduce jitter in the servo movement

