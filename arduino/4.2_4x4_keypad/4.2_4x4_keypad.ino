// Include the Adafruit_Keypad library
#include "Adafruit_Keypad.h"

// Define the number of rows and columns for the keypad
const byte ROWS = 4;
const byte COLS = 4;

// Define the characters mapped to each button on the 4x4 keypad
char keys[ROWS][COLS] = {
  { '1', '2', '3', 'A' },
  { '4', '5', '6', 'B' },
  { '7', '8', '9', 'C' },
  { '*', '0', '#', 'D' }
};

// Define the Arduino pins connected to the row pinouts of the keypad
byte rowPins[ROWS] = { 2, 3, 4, 5 };
// Define the Arduino pins connected to the column pinouts of the keypad
byte colPins[COLS] = { 6, 7, 8, 9 };

// Initialize a custom keypad instance
Adafruit_Keypad myKeypad = Adafruit_Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

// Setup function
void setup() {
  // Initialize Serial communication at 9600 baud rate
  Serial.begin(9600);
  // Initialize the custom keypad
  myKeypad.begin();
}

// Main loop function
void loop() {
  // Update the state of keys
  myKeypad.tick();

  // Check if there are new keypad events
  while (myKeypad.available()) {
    // Read the keypad event
    keypadEvent e = myKeypad.read();
    // Print the key that triggered the event
    Serial.print((char)e.bit.KEY);
    // Print the type of event: pressed or released
    if (e.bit.EVENT == KEY_JUST_PRESSED) Serial.println(" pressed");
    else if (e.bit.EVENT == KEY_JUST_RELEASED) Serial.println(" released");
  }

  delay(10);
}
