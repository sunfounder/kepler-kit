/* IRsmallDProtocolStructs - Protocol's Specific Data Structures
 *
 * This file is part of the IRsmallDecoder library for Arduino
 * Copyright (c) 2020 Luis Carvalho
 */
 
#ifndef IRsmallD_ProtocolStructs_h
#define IRsmallD_ProtocolStructs_h

  #if IR_SMALLD_NEC || IR_SMALLD_RC5 || IR_SMALLD_SAMSUNG32
    struct irSmallD_t{
      uint8_t addr;
      uint8_t cmd;
      bool    keyHeld;
    };

  #elif IR_SMALLD_NECx || IR_SMALLD_SAMSUNG
    struct irSmallD_t{
      uint16_t addr;
      uint8_t  cmd;
      bool     keyHeld;
    };

  #elif IR_SMALLD_SIRC12 || IR_SMALLD_SIRC15
    struct irSmallD_t{
      uint8_t addr;
      uint8_t cmd;
    };

  #elif IR_SMALLD_SIRC20
    struct irSmallD_t{
      uint8_t ext;  //extended data
      uint8_t addr;
      uint8_t cmd;
    };

  #elif IR_SMALLD_SIRC
    struct irSmallD_t{
      uint8_t ext;
      uint8_t addr;
      uint8_t cmd;
      bool    keyHeld;
    };
    
  #else
      #error Protocol data structure not defined.
  #endif

#endif