/* A simple example, using the IRsmallDecoder library, 
 * for testing remote controls that use the NEC protocol.
 *
 * Note: for the NEC extended protocol, just define IR_SMALLD_NECx instead of IR_SMALLD_NEC 
 *
 * In this example it's assumed that the IR sensor is connected to digital pin 2 and 
 * the pin is usable for external interrupts.
 * For more information on the boards' usable pins, see the library documentation at:
 * https://github.com/LuisMiCa/IRsmallDecoder
 * or the README.pdf file in the extras folder of this library. 
 */
 
#define IR_SMALLD_NEC        //1st: define which protocol to use and then,
#include <IRsmallDecoder.h>  //2nd: include the library;
IRsmallDecoder irDecoder(2); //3rd: create one decoder object with the correct digital pin;
irSmallD_t irData;           //4th: declare one decoder data structure;
 
void setup() {
  Serial.begin(250000);
  Serial.println("Waiting for a NEC remote control IR signal...");
  Serial.println("held\t addr\t cmd");
}

void loop() {
  if(irDecoder.dataAvailable(irData)) {    //5th: if the decoder has some new data available,       
    Serial.print(irData.keyHeld,HEX);      //6th: do something with the data.
    Serial.print("\t ");
    Serial.print(irData.addr,HEX); 
    Serial.print("\t ");
    Serial.println(irData.cmd,HEX);  
  }
}

