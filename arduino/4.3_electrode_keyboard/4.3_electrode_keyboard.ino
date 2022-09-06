#include <Wire.h>
#include "Adafruit_MPR121.h"

// You can have up to 4 on one i2c bus but one is enough for testing!
Adafruit_MPR121 cap = Adafruit_MPR121();

// Keeps track of the last pins touched
// so we know when buttons are 'released'
uint16_t lasttouched = 0;
uint16_t currtouched = 0;
boolean touchStates[12];


void setup() {
  Serial.begin(9600);

  while (!Serial) { // needed to keep leonardo/micro from starting too fast!
    delay(10);
  }

  Serial.println("MPR121 Capacitive Touch sensor test");

  // Default address is 0x5A, if tied to 3.3V its 0x5B
  // If tied to SDA its 0x5C and if SCL then 0x5D
  int check = cap.begin(0x5A);
  if (!check) {
    Serial.println("MPR121 not found, check wiring?");
    while (1);
  }
  Serial.println("MPR121 found!");
}

void loop() {
  // Get the currently touched pads
  currtouched = cap.touched();

  //  Serial.println(cap.touched(), BIN);
  //  delay(100);
  if (currtouched != lasttouched) {
    for (int i = 0; i < 12; i++) {
      if (currtouched & (1 << i)) touchStates[i] = 1;
      else touchStates[i] = 0;
    }
    for (int i = 0; i < 12; i++)
    {
      Serial.print(touchStates[i]);
    }
    Serial.println();
  }

  // reset our state
  lasttouched = currtouched;
}
