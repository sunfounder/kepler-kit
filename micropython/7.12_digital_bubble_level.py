import machine
from machine import I2C, Pin
import time
import math
from imu import MPU6050


### mpu6050
i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
mpu = MPU6050(i2c)

# get rotary angle
def dist(a,b):
    return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

def get_angle():
    y_angle=get_y_rotation(mpu.accel.x, mpu.accel.y, mpu.accel.z) 
    x_angle=get_x_rotation(mpu.accel.x, mpu.accel.y, mpu.accel.z) 
    return x_angle,y_angle

### led matrix display
sdi = machine.Pin(18,machine.Pin.OUT)
rclk = machine.Pin(19,machine.Pin.OUT)
srclk = machine.Pin(20,machine.Pin.OUT)

def hc595_in(dat):
    for bit in range(7,-1, -1):
        srclk.low()
        time.sleep_us(30)
        sdi.value(1 & (dat >> bit))
        time.sleep_us(30)
        srclk.high()

def hc595_out():
    rclk.high()
    time.sleep_us(200)
    rclk.low()

def display(glyph):
    for i in range(0,8):
        hc595_in(glyph[i])
        hc595_in(0x80>>i)
        hc595_out()

# data transformation
def matrix_2_glyph(matrix):
    glyph= [0 for i in range(8)] # glyph code for display()
    for i in range(8):
        for j in range(8):
            glyph[i]+=matrix[i][j]<<j
    return glyph

def clamp_number(val, min, max):
    return min if val < min else max if val > max else val

def interval_mapping(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# Calculate the position of the bubble
sensitivity=4          # The higher the number, the more sensitive
matrix_range=7         # The size of the matrix is 8, so the coordinate range is 0~7
point_range=matrix_range-1     # The x, y value of the bubble's marker point (upper left point) should be between 0-6
def bubble_position():
    x,y=get_angle()
    x=int(clamp_number(interval_mapping(x,-90,90,0-sensitivity,point_range+sensitivity),0,point_range))
    y=int(clamp_number(interval_mapping(y,-90,90,point_range+sensitivity,0-sensitivity),0,point_range))
    return [x,y]

# Drop the bubble into empty matrix
def drop_bubble(matrix,bubble):
    matrix[bubble[0]][bubble[1]]=0
    matrix[bubble[0]+1][bubble[1]]=0
    matrix[bubble[0]][bubble[1]+1]=0
    matrix[bubble[0]+1][bubble[1]+1]=0
    return matrix

while True:
    matrix= [[1 for i in range(8)] for j in range(8)]  # empty matrix
    bubble=bubble_position() # bubble coordinate
    matrix=drop_bubble(matrix,bubble) # drop the bubble into empty matrix
    display(matrix_2_glyph(matrix)) # show matrix

