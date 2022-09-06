from lcd1602 import LCD
import machine
import time
import urandom


# keypad function
characters = [["1","2","3","A"],["4","5","6","B"],["7","8","9","C"],["*","0","#","D"]]

pin = [21,20,19,18]
row = []
for i in range(4):
    row.append(None)
    row[i] = machine.Pin(pin[i], machine.Pin.OUT)

pin = [13,12,11,10]
col = []
for i in range(4):
    col.append(None)
    col[i] = machine.Pin(pin[i], machine.Pin.IN)

def readKey():
    key = []
    for i in range(4):
        row[i].high()
        for j in range(4):
            if(col[j].value() == 1):
                key.append(characters[i][j])
        row[i].low()
    if key == [] :
        return None
    else:
        return key

# init/reset number
# reset the result as False for lcd show
def init_new_value():
   global pointValue,upper,count,lower
   pointValue = int(urandom.uniform(0, 99))
   print(pointValue)
   upper = 99
   lower = 0
   count = 0
   return False


# lcd show message
# If target, show game over.
# If not target, or not detected, show guess number.
def lcd_show(result):
    lcd.clear()
    if result == True: 
        string ="GAME OVER!\n"
        string +="Point is "+ str(pointValue)
    else : 
        string ="Enter number: " + str(count) +"\n"
        string += str(lower)+ " < Point < " + str(upper)
    lcd.message(string)
    return  

# detect number & reflesh show message 
# if not target, reflesh number (upper or lower) and return False
# if target, return True 
def number_processing():
    global upper,count,lower
    if count > pointValue:
        if count < upper:
            upper = count
    elif count < pointValue:
        if count > lower:
            lower = count
    elif count == pointValue:
        return True
    count = 0
    return False 

## start
lcd = LCD()
string = "Welcome!\n"
string = "Press A to Start!"
lcd.message(string)
result=init_new_value()

# read key & display
last_key = None
while True:
    current_key = readKey()
    if current_key == last_key:
        continue
    last_key = current_key
    if current_key != None:
        # print(current_key)
        if current_key ==["A"]: # reset number
            result=init_new_value() 
        elif current_key==["D"]: # check
            result=number_processing()
        elif current_key[0] in list(["1","2","3","4","5","6","7","8","9","0"]) and count < 10: #check validity & limit digits
            count = count * 10 + int(current_key[0])
        lcd_show(result) # show 
    time.sleep(0.1)
