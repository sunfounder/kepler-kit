/* IRsmallD_SAMSUNG - SAMSUNG old standard protocol decoder
 *
 * This file is part of the IRsmallDecoder library for Arduino
 * Copyright (c) 2020 Luis Carvalho
 *
 *
 * Protocol specifications:
 * ------------------------
 * Encoding type: Pulse Distance
 * Carrier frequency:    37.9 kHz
 * Leading Mark length:  9000 µs (=4500µs pulse + 4500µs space)
 * Bit '0' Mark length:  1125 µs (=562.5µs pulse + 562.5µs space) 
 * Bit '1' Mark length:  2250 µs (=562.5µs pulse + 1687.5µs space)
 *
 * Repetition Period:   60000 µs
 * Signal length : from 32062.5  up to  54562.5 µs  ( = 2*4500 + 20*[1125 to 2250]+ 562.5 ) 
 * Stop Space Length:   27937.5 down to  5437.5 µs  ( = Repetition Period - Signal length)
 * Frames per key pressed: 2 (the message is always sent, at least, twice). Decoder will ignore it!
 *                         Repetitions not used for error checking. Not all remotes have this characteristic.         
 * Repetition Mode:        Exact Copy (not a NEC type repetition frame)
 * Bit order:              LSB first
 * Number of bits:         20 (12 for manufacturer code + 8 for command)
 * Logical bits' order of transmission:
 *             12 bit Address                  8 bit Command       
 *  A0 A1 A2 A3 A4 A5 A6 A7 A8 A9 Aa Ab    C0 C1 C2 C3 C4 C5 C6 C7   
 * 
 * Sources: 
 *   https://www.mikrocontroller.net/attachment/55409/samsungRCProtokoll.pdf (page 5-30)
 *   https://www.handsontec.com/pdf_files/IR_Code_Analy.pdf
 *
 */

// SAMSUNG Standard timing in micro seconds:
#define LEADING_MARK    9000
#define BIT_0_MARK      1125
#define BIT_1_MARK      2550
#define BIT_TOLERANCE   ((BIT_1_MARK - BIT_0_MARK)/2)  // = 712
#define STOP_SPACE_MIN  5437       //5437.5 to be more precise
#define STOP_SPACE_MAX 27938       //27937.5 to be more precise


void IRsmallDecoder::irISR() { //executed every time the IR signal goes UP (but FALLING @SensorOutput)
  // SAMSUNG timing thresholds:
  const uint16_t c_LMmax = LEADING_MARK * 1.1; // 10% more = 9900
  const uint16_t c_LMmin = LEADING_MARK * 0.9; // 10% less = 8100
  const uint16_t c_M1max = BIT_1_MARK + BIT_TOLERANCE; //2550+712=3262
  const uint16_t c_M1min = BIT_1_MARK - BIT_TOLERANCE; //2550-712=1838
  //const uint16_t c_M0max = BIT_0_MARK + BIT_TOLERANCE; //1125+712=1837  //NOT USED
  const uint16_t c_M0min = BIT_0_MARK - BIT_TOLERANCE; //1125-712= 413  
  const uint32_t c_GapMax = STOP_SPACE_MAX + 6 * BIT_TOLERANCE;  // bigger tolerance
  const uint16_t c_GapMin = STOP_SPACE_MIN - 6 * BIT_TOLERANCE;  // 6*712 = 4272
  
  //number of initial repeats to be ignored:
  const uint8_t c_RptCount = 3;   
   
  // FSM variables:
  static uint32_t duration;
  static uint8_t  bitCount;
  static uint32_t startTime = -1; //FFFF...  (by two's complement)
  static uint8_t  signal_Cmd;  //starts as an auxiliary Byte for address decoding
  static uint16_t signal_Addr16;
  static uint8_t  state=0;
  static uint8_t  repeatCount=0;
  static bool     possiblyHeld=false;

  DBG_PRINT_STATE(state);
  DBG_RESTART_TIMER();
  
  duration = micros() - startTime;
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
        state=2;
      }
      else state=0;
    break;
 
    case 2: //receiving:
      if(duration < c_M0min || duration > c_M1max) state=0; //error, not a bit mark
      else { // it's M0 or M1
        signal_Cmd >>= 1;   //push a 0 from left to right (will be left at 0 if it's M0)
        if(duration >= c_M1min) signal_Cmd |= 0x80;  //it's M1, change MSB to 1
        bitCount++;
        if (bitCount==8) signal_Addr16 = signal_Cmd; //set address low byte (and stay in same state)
        else if (bitCount==12) {
          signal_Cmd >>= 4;                  // Push 4 '0' bits to the right
          signal_Addr16 |= signal_Cmd << 8;  //set address high byte  (and stay in same state)
        }
        else if (bitCount==20) {             //all bits received,
          if (possiblyHeld && signal_Cmd == _irData.cmd){ //keyHeld confirmed (addr shouldn't have changed)
            if (repeatCount < c_RptCount) repeatCount++;  //first repeat signals will be ignored
            else if (!_irCopyingData){   //repetitions ignored; if not interrupting a copy...
              _irData.keyHeld = true;
              _irDataAvailable= true;
            }
          }
          else if (!_irCopyingData){ //key was not held; if allowed, update data
            _irData.addr = signal_Addr16;
            _irData.cmd  = signal_Cmd;
            _irData.keyHeld = false;
            _irDataAvailable= true;
            possiblyHeld=true;       //will remain true if the next gap is OK
            repeatCount=0;
          } 
          state=0;                   //done
        }   
        //else state=2;              //stay in same state
      }
    break;
  }
  
  DBG_PRINTLN_TIMER();
}


/*
bits in order of transmission: A0 A1 A2 A3 A4 A5 A6 A7  A8 A9 Aa Ab  C0 C1 C2 C3 C4 C5 C6 C7
 
Decoding process using command byte as an auxiliary byte to decode the address:
  Store A0 to A7 in signal_Cmd:        A7 A6 A5 A4 A3 A2 A1 A0
  set address low byte to signal_Cmd:  signal_Addr16 = signal_Cmd
  Store A8 to Ab in signal_Cmd:        Ab Aa A9 A8 A7 A6 A5 A4
  Push 4 '0' bits to the right:         0  0  0  0 Ab Aa A9 A8
  set address high byte to signal_Cmd: signal_Addr16 |= signal_Cmd << 8
  Store C0 to C7 in signal_Cmd:        C7 C6 C5 C4 C3 C2 C1 C0
  
 */
