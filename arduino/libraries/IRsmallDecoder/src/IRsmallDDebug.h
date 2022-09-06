/* IRsmallDDebug - Debug macros
 *
 * This file is part of the IRsmallDecoder library for Arduino
 * Copyright (c) 2020 Luis Carvalho
 *
 *
 * Debug options:
 *   IRSMALLD_DEBUG_STATE    - Prints FSM states
 *   IRSMALLD_DEBUG_DURATION - Prints pulse/space/mark intervals' duration
 *   IRSMALLD_DEBUG_TIME     - Prints ISR execution time
 * 
 * NOTES:
 * - IRSMALLD_DEBUG_TIME mode uses AVR 328p Timer1 hardware specific code;
 *   Results are in Micro Seconds assuming 16MHz clock (Clk Count is divided by 16 to get µs);
 * - The serial communication speed must be high, to avoid timing errors.
 */
 
 
#ifndef IRsmallD_Debug_h
  #define IRsmallD_Debug_h
 
  #ifdef IRSMALLD_DEBUG_STATE
    #define DBG_PRINT_STATE(...)    Serial.print(__VA_ARGS__);
  #else
    #define DBG_PRINT_STATE(...) 	//nothing
  #endif
 
  #ifdef IRSMALLD_DEBUG_DURATION
    #define DBG_PRINTLN_DUR(...)    {Serial.print("d="); Serial.print(__VA_ARGS__); Serial.println("µ");}
  #else
    #define DBG_PRINTLN_DUR(...) 	//nothing
  #endif
 
  #ifdef IRSMALLD_DEBUG_TIME
    #if defined(IRSMALLD_DEBUG_STATE) || defined(IRSMALLD_DEBUG_DURATION)
      #warning Do not use IRSMALLD_DEBUG_TIME with IRSMALLD_DEBUG_STATE or IRSMALLD_DEBUG_DURATION if you want accurate measurements of execution time
    #endif 
    #define DBG_RESTART_TIMER()   { TCCR1A = 0; TCCR1B = 1; TCNT1=0; } //set mode to count clock cycles and reset
    #define DBG_PRINTLN_TIMER()   { uint16_t elapsedTime=TCNT1; Serial.print("t="); Serial.print(elapsedTime>>4); Serial.println("µ");}
  #else
    #define DBG_RESTART_TIMER() 		//nothing
    #define DBG_PRINTLN_TIMER() 		//nothing
  #endif

#endif
 


//instead of variadic macros, the following syntax could be used:
//PRINT(args...)  Serial.print(args) 

//Call Serial.flush() after every Serial.print() if you need to see the output before the code continues with buffered data

//do{}while(false) can be used to prevent some problems with more complex macros
// #define DBG_SERIALBEGIN(...)  do {Serial.begin(__VA_ARGS__); Serial.println("Serial Port Ready!");} while ( false )
