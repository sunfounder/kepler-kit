from lcd1602 import LCD
import utime

lcd = LCD()
string = "Hello SunFounder"
lcd.message(string)
utime.sleep(2)
# string = "    Wor"   
# lcd.message(string)
# utime.sleep(2)
# lcd.clear()   