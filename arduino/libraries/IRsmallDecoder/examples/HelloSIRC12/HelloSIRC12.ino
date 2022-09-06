/* A simple example, using the IRsmallDecoder library, 
 * for testing remote controls that use the Sony SIRC12 protocol.
 *
 * Notes: 
 *  - For the SIRC15 or SIRC20 protocols, use IR_SMALLD_SIRC15 or IR_SMALLD_SIRC20 
 *    instead of IR_SMALLD_SIRC12 (in the #define ...);
 *  - Unlike IR_SMALLD_SIRC, IR_SMALLD_SIRC12/15/20 does not have the keyHeld data member;
 *  - IR_SMALLD_SIRC20 has an additional data member (ext);
 *  - Each keypress on a SIRC remote, usually sends three signal frames. (The two additional 
 *    signal repetitions are ignored in the IR_SMALLD_SIRC, but not in the IR_SMALLD_SIRC12/15/20);
 *  - IR_SMALLD_SIRC12 will receive signals from SIRC15 and SIRC20 
 *    but the codes will not be correct;
 *  - In a similar way, IR_SMALLD_SIRC15 will receive signals from SIRC20, but not from SIRC12.
 *	
 * In this example it's assumed that the IR sensor is connected to digital pin 2 and 
 * the pin is usable for external interrupts.
 * For more information on the boards' usable pins, see the library documentation at:
 * https://github.com/LuisMiCa/IRsmallDecoder
 * or the README.pdf file in the extras folder of this library. 
 */
 
#define IR_SMALLD_SIRC12     //1st: define which protocol to use and then,
#include <IRsmallDecoder.h>  //2nd: include the library;
IRsmallDecoder irDecoder(2); //3rd: create one decoder object with the correct digital pin;
irSmallD_t irData;           //4th: declare one decoder data structure;

void setup() {
  Serial.begin(250000);
  Serial.println("Waiting for a SIRC12 remote control IR signal...");
  Serial.println("Addr\t Cmd");
}

void loop() {
  if(irDecoder.dataAvailable(irData)) {   //5th: if the decoder has some new data available,       
    Serial.print(irData.addr,HEX);        //6th: do something with the data.
    Serial.print("\t ");
    Serial.println(irData.cmd,HEX);  
  }
}
