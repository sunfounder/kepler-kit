/* Single Hold 
 *  
 * This example is part of the the IRfastDecoder library and is intended to demonstrate 
 * a possible usage for the keyHeld data member.
 *  
 * How to use this sketch: 
 *  - Connect the sensor (see library documentation);
 *  - Uncomment the #define for the desired protocol,
 *    (leave the others as comments, only one is allowed);
 *  - Upload the sketch and open serial Monitor;
 *  - "Teach the Arduino" which keys you want to use;
 *  - Hold the selected keys to turn on/off the built-in LED.
 *    If you keep holding, it won't do anything else.
 *
 * In this example it's assumed that the IR sensor is connected to digital pin 2 and 
 * the pin is usable for external interrupts.
 * For more information on the boards' usable pins, see the library documentation at:
 * https://github.com/LuisMiCa/IRsmallDecoder
 * or the README.pdf file in the extras folder of this library. 
 */
 
 
#define IR_SMALLD_NEC
//#define IR_SMALLD_NECx
//#define IR_SMALLD_RC5
//#define IR_SMALLD_SIRC
//#define IR_SMALLD_SAMSUNG
//#define IR_SMALLD_SAMSUNG32

#include <IRsmallDecoder.h>

IRsmallDecoder irDecoder(2);  //assuming that the IR sensor is connected to digital pin 2
irSmallD_t irData;
int keyOn, keyOff;
bool keyReleased=true;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(250000);
  
  Serial.print(F("Press the key that will turn \"ON\" the LED "));
  while(!irDecoder.dataAvailable(irData)); //waiting for one keypress
  keyOn=irData.cmd;
  Serial.print(F("(key cmd=")); 
  Serial.print(keyOn, HEX);
  Serial.println(F(")"));
  
  Serial.print(F("Press the key that will turn \"OFF\" the LED "));
  do{
    while(!irDecoder.dataAvailable(irData)); //waiting for another keypress
  }while(irData.cmd == keyOn); //if it's the same key, go back and wait for another
  keyOff=irData.cmd;
  Serial.print(F("(key cmd=")); 
  Serial.print(keyOff, HEX);
  Serial.println(F(")"));
  
  Serial.println();
  Serial.println(F("Hold the \"ON\" key to turn on the Built-in LED;"));
  Serial.println(F("Hold the \"OFF\" key to turn off the Built-in LED;"));

  Serial.println();
}

void loop() {
  if(irDecoder.dataAvailable(irData)) {
    if (irData.keyHeld) {
      if (keyReleased) {
        if (irData.cmd == keyOn) {
          Serial.print("ON ");
          digitalWrite(LED_BUILTIN, HIGH);
        }
        else if (irData.cmd == keyOff) {
          Serial.print("OFF ");
          digitalWrite(LED_BUILTIN, LOW);
        }
        keyReleased=false;
      }
    }
    else keyReleased=true;
  }
}

