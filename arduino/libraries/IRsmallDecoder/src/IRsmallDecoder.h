/* IRsmallDecoder v1.1.0
 *
 * This is a Library for Arduino and it allows the reception and decoding of infrared signals from remote controls.
 * It uses small, fast and reliable decoders that don't require timers. 
 * Perfect for Arduino projects that use only one remote and don't need to send IR signals.
 *
 * Copyright (c) 2020 Luis Carvalho
 * This Library is licensed under the MIT License. See the LICENSE file for details.
 *
 * Notes:
 * - In the INO file, one of following directives must be used: 
 *    #define IR_SMALLD_NEC
 *    #define IR_SMALLD_NECx
 *    #define IR_SMALLD_RC5
 *    #define IR_SMALLD_SIRC12
 *    #define IR_SMALLD_SIRC15
 *    #define IR_SMALLD_SIRC20
 *    #define IR_SMALLD_SIRC
 *    #define IR_SMALLD_SAMSUNG
 *    #define IR_SMALLD_SAMSUNG32
 *    
 *   before the
 *    #include <IRsmallDecoder.h>
 *
 * - RC5 works for both normal and extended versions;
 * - SIRC12, SIRC15 and SIRC20 use a basic (smaller and faster) implementation but without some features...
 * - SIRC handles SIRC 12, 15 and 20 bits, by taking advantage of the fact that most Sony remotes;
 *   send three frames each time one button is pressed. It uses triple frame verification and checks if keyHeld;
 */

#ifndef IRsmallDecoder_h
#define IRsmallDecoder_h

#if ARDUINO >= 100
  #include <Arduino.h>
#else
  #include <WProgram.h>
  #include <pins_arduino.h>
  #include <WConstants.h>
#endif

#include "IRsmallDProtocolCheck.h"
#include "IRsmallDProtocolStructs.h"
#include "IRsmallDDebug.h"

// IR_ISR_MODE *****************************************************************
#if IR_SMALLD_NEC || IR_SMALLD_NECx || IR_SMALLD_SAMSUNG || IR_SMALLD_SAMSUNG32
  #define IR_ISR_MODE  FALLING
#elif IR_SMALLD_SIRC || IR_SMALLD_SIRC12 || IR_SMALLD_SIRC15 || IR_SMALLD_SIRC20
  #define IR_ISR_MODE  RISING
#elif IR_SMALLD_RC5
  #define IR_ISR_MODE  CHANGE
#else
  #error IR_ISR_MODE not defined.
#endif

//*****************************************************************************
class IRsmallDecoder {
  private:
    static volatile bool _irDataAvailable; //will be updated by the ISR
    static volatile irSmallD_t _irData;    //will be updated by the ISR
    static bool _irCopyingData; //not changed by the ISR, no need for volatile
    static void irISR();
    
  public:
    IRsmallDecoder(uint8_t interruptPin);
    bool dataAvailable(irSmallD_t &irData);
};

//*****************************************************************************
//static variables from a class must be re-declared/initialized
//outside the class' forward declaration/definition (usually on the cpp file not the header)
volatile bool IRsmallDecoder::_irDataAvailable = false;
volatile irSmallD_t IRsmallDecoder::_irData;
bool IRsmallDecoder::_irCopyingData = false; //to avoid volatile _irData corruption by the ISR

IRsmallDecoder::IRsmallDecoder(uint8_t interruptPin){
  pinMode(interruptPin,INPUT_PULLUP); //active low
  #if defined(__AVR_ATtiny24__) || defined(__AVR_ATtiny44__) || defined(__AVR_ATtiny84__) || \
      defined(__AVR_ATtiny25__) || defined(__AVR_ATtiny45__) || defined(__AVR_ATtiny85__)
    attachInterrupt(0, irISR, IR_ISR_MODE);
  #else  
    attachInterrupt(digitalPinToInterrupt(interruptPin), irISR, IR_ISR_MODE);
  #endif
}

bool IRsmallDecoder::dataAvailable(irSmallD_t &irData){
  if (_irDataAvailable) {
    _irCopyingData=true; //Let the ISR know that it cannot change the data while it's being copied
    memcpy(&irData, (void*)&_irData, sizeof(_irData));   
    _irCopyingData=false; //an ATOMIC_BLOCK would be better, but it's not supported on many boards
    _irDataAvailable=false;    
    return true;
  }
  else return false;
}


//*****************************************************************************
// Computed GOTOs (labels as values) FSM control:
#define FSM_INITIALIZE(initialState) static void* fsm_state = &&initialState
#define FSM_SWITCH() goto *fsm_state; while(false)
#define FSM_NEXT(nextState) fsm_state = &&nextState
#define FSM_DIRECTJUMP(label) goto label

//*****************************************************************************
// Conditional inclusion of protocol specific ISR implementations:
#if IR_SMALLD_NEC || IR_SMALLD_NECx
  #include "IRsmallD_NEC.h"
#elif IR_SMALLD_RC5
  #include "IRsmallD_RC5.h"
#elif IR_SMALLD_SIRC12 || IR_SMALLD_SIRC15 || IR_SMALLD_SIRC20
  #include "IRsmallD_SIRC_basic.h"
#elif IR_SMALLD_SIRC
  #include "IRsmallD_SIRC_multi.h"
#elif IR_SMALLD_SAMSUNG
  #include "IRsmallD_SAMSUNG.h"
#elif IR_SMALLD_SAMSUNG32
  #include "IRsmallD_SAMSUNG32.h"
#else
  #error ISR implementation not included.
#endif


#endif // end of the #define IRsmallDecoder_h