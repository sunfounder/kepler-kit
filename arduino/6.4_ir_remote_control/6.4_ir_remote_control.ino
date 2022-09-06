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
IRsmallDecoder irDecoder(17); //3rd: create one decoder object with the correct digital pin;
irSmallD_t irData;           //4th: declare one decoder data structure;

String decodeKeyValue(long result);

void setup() {
  Serial.begin(9600);
  Serial.println("Waiting for a NEC remote control IR signal...");
  Serial.println("held\t addr\t cmd");
}

void loop() {
  if(irDecoder.dataAvailable(irData)) {    //5th: if the decoder has some new data available,       
    Serial.print("Hold?: ");
    Serial.print(irData.keyHeld); 
    Serial.print(", Key: ");
    Serial.println(decodeKeyValue(irData.cmd));
  }
}

String decodeKeyValue(long result) {
  switch(result){
    case 0x16:
      return "0";
    case 0x0C:
      return "1";
    case 0x18:
      return "2";
    case 0x5E:
      return "3";
    case 0x08:
      return "4";
    case 0x1C:
      return "5";
    case 0x5A:
      return "6";
    case 0x42:
      return "7";
    case 0x52:
      return "8";
    case 0x4A:
      return "9";
    case 0x09:
      return "+";
    case 0x15:
      return "-";
    case 0x7:
      return "EQ";
    case 0x0D:
      return "U/SD";
    case 0x19:
      return "CYCLE";
    case 0x44:
      return "PLAY/PAUSE";
    case 0x43:
      return "FORWARD";
    case 0x40:
      return "BACKWARD";
    case 0x45:
      return "POWER";
    case 0x47:
      return "MUTE";
    case 0x46:
      return "MODE"; 
    default :
      return "ERROR";
    }
}
