/********************************
   name:I2C LCD1602
   function:You should now see your I2C LCD1602 display the flowing characters: "SunFounder" and "hello, world".
 ********************************/
//Email:support@sunfounder.com
//Website:www.sunfounder.com

/********************************/
// include the library code
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
/**********************************************************/
LiquidCrystal_I2C lcd(0x27, 16, 2); // set the LCD address to 0x27 for a 16 chars and 2 line display
/*********************************************************/
void setup()
{
  lcd.init();  //initialize the lcd
  lcd.backlight();  //open the backlight
}
/*********************************************************/
void loop()
{
  lcd.setCursor(3, 0); // set the cursor to column 3, line 0
  lcd.print("SunFounder");  // Print a message to the LCD

  lcd.setCursor(2, 1); // set the cursor to column 2, line 1
  lcd.print("Hello, World!");  // Print a message to the LCD.
}
/************************************************************/