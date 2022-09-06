/* IRsmallD_NEC - NEC protocol decoder
 *
 * This file is part of the IRsmallDecoder library for Arduino
 * Copyright (c) 2020 Luis Carvalho
 *
 *
 * Protocol specifications:
 * ------------------------
 * Modulation type: pulse distance.
 * Carrier frequency: 38kHz. 
 * Each pulse burst is 562.5µs in length
 * Signal starts with a 9ms leading pulse burst (16 times the pulse burst length used for a logical data bit)
 * followed by a 4.5ms space. Then, the logical bits are transmitted as follows:
 *   Logical '0' – a 562.5µs pulse burst followed by a 562.5µs space, with a total transmit time of 1125 μs
 *   Logical '1' – a 562.5µs pulse burst followed by a 1687.5μs space, with a total transmit time of 2250 μs
 *
 * Logical bits' order of transmission for normal NEC protocol:
 * 8bit Address    inverted address    8bit command    inverted command
 * LSB ... MSB       LSB ... MSB       LSB ... MSB       LSB ... MSB
 *
 * Logical bits' order of transmission for Extended NEC protocol:
 * low Address       high address      8bit command      inverted command
 * LSB ... MSB       LSB ... MSB       LSB ... MSB       LSB ... MSB 
 *
 * Notes:
 *   - Inverted bytes have 1s instead of 0s and vice-versa;
 *   - Extended NEC protocol sacrifices the address redundancy to extend 
 *     the address from 8 to 16 bits (inverted address becomes high address).
 *
 * Repeat codes:
 * If a Key is held, a repeat bit is sent every 108ms;
 * It consists of a 9ms pulse burst followed by a 2250 μs space and then a 562.5 μs pulse burst.
 */


void IRsmallDecoder::irISR() { //executed every time the IR signal goes up (actually it's on FALL)
  // NEC timings in micro seconds:
  // Minimum Gap length = repeatPeriod - SignalFrame = 108000 - 67500 = 40500
  const uint16_t c_GapMin =  32400; // = 40500 * 0.8 (20% less)
  // Leading Mark Length = Leading pulse + leading space = 9000 + 4500 = 13500
  // Repeat Mark Length  = Repeat Pulse  + Repeat Space  = 9000 + 2250 = 11250
  // max tolerance = (13500 - 11250)/2 = 1125
  const uint16_t c_LMmax = 14625; // = 13500 + 1125 (it could be more)
  const uint16_t c_LMmin = 12375; // = 13500 - 1125
  const uint16_t c_RMmax = 12374; // = 11250 + 1125 - 1
  const uint16_t c_RMmin = 10125; // = 11250 - 1125 (it could be less)
  //Bit 0 Mark length = 562.5µs pulse + 562.5µs space = 1125
  //Bit 1 Mark length = 562.5µs pulse + 3 * 562.5µs space = 2250
  //max tolerance = (2250 - 1125)/2 = 562.5 = bit pulse
  const uint16_t c_M1max = 2812; // = 2250 + 562 (it could be more)
  const uint16_t c_M1min = 1688; // = 2250 - 562
  //const uint16_t c_M0max = 1687; // = 1125 + 562    //not needed...
  const uint16_t c_M0min = 563;  // = 1125 - 562 (it could be less)
  const uint32_t c_GapMax= 106425;//= (108000-11250) * 1.1; // 10% above gap between 2 consecutive repeat marks
  //number of initial repeats to be ignored:
  const uint8_t c_RptCount = 2;  
 
  // FSM variables:
  static uint32_t duration;
  static uint8_t  bitCount;
  static uint32_t startTime = -1; //FFFF...  (by two's complement)
  static union {//received bits are stored in reversed order (11000101... -> ...10100011)
    uint32_t all=0; //Arduino uses Little Endian so, if all=ABCDEF89 then in memory it's 89EFCDAB (hex format)
    uint8_t byt[4]; //then we get byt[0]=89, byt[1]=EF, byt[2]=CD and byt[3]=AB (type punning with a union...)
  } irSignal;
  static uint8_t repeatCount=0;
  static uint8_t state=0;
  static bool    possiblyHeld=false;

  DBG_PRINT_STATE(state);
  DBG_RESTART_TIMER();
  
  duration = micros() - startTime; //note: micros() has a 4μs resolution (multiples of 4) @16MHz and 8μs @8MHz 
  startTime = micros();
  DBG_PRINTLN_DUR(duration);

  switch(state){ //asynchronous (event-driven) Finite State Machine
    case 0: //standby:
      if(duration > c_GapMin){
        if (duration > c_GapMax) possiblyHeld = false;
        state=1;
      }
      else possiblyHeld = false;
    break;
 
    case 1: //startPulse:
      if (duration >= c_LMmin && duration <= c_LMmax){ //its a Leading Mark
        bitCount=0;
        repeatCount=0;
        state=2;
      }
      else {
        if (possiblyHeld && duration >= c_RMmin && duration <= c_RMmax) { //its a Repeat Mark 
          if (repeatCount < c_RptCount) repeatCount++; //first repeat signals will be ignored
          else if (!_irCopyingData){ //if not interrupting a copy...
            _irData.keyHeld = true;
            _irDataAvailable= true;
          }
        }
        state=0;
      }
    break;
 
    case 2: //receiving:
      if(duration < c_M0min || duration > c_M1max) state=0; //error, not a bit mark
      else { // it's M0 or M1
        irSignal.all >>= 1; //push a 0 from left to right (will be left at 0 if it's M0)
        if(duration >= c_M1min) irSignal.byt[3] |= 0x80; //it's M1, change MSB to 1
        bitCount++;
        #if defined(IR_SMALLD_NEC) //Conditional code inclusion (at compile time)
          if (bitCount==16) {   //Address and Reversed Address received
            if (irSignal.byt[2] != (uint8_t)~irSignal.byt[3]) state=0; //address error
            else state=2; //Address OK, continue with command reception
          }
          else
    		#endif
  		  if (bitCount==32) { //all bits received
          if(!_irCopyingData && (irSignal.byt[2] == (uint8_t)~irSignal.byt[3])){ //if not interrupting a copy and command OK, finish decoding
            #if defined(IR_SMALLD_NEC) //NEC address has 8 bits
              _irData.addr = irSignal.byt[0];
            #else //it must be IR_SMALLD_NECx (16 bits)
              _irData.addr = *(uint16_t*)(&irSignal.byt[0]); // type punning with cast...
              //.addr is the 16 bit value pointed by the address of byt[0]  (byt[1] is addr high byte)
              // dereferencing type-punned pointer will break strict-aliasing rules
            #endif
        	  _irData.cmd = irSignal.byt[2];
            _irData.keyHeld = false;
            _irDataAvailable= true;
             possiblyHeld=true; //will remain true if the next gap is OK
          }
          state=0;
        }
        else state=2; //continue receiving
      }
    break;
  }
  
  DBG_PRINTLN_TIMER();
}
