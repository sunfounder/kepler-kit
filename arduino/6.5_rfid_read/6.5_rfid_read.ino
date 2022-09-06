#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN         0
#define SS_PIN          5

MFRC522 mfrc522(SS_PIN, RST_PIN);


void setup() {
  Serial.begin(115200);        // Initialize serial communications with the PC
  while (!Serial) {
    delay(10);
  }
  simple_mfrc522_init();
}

void loop() {
  Serial.println("Place a card to read...");
  simple_mfrc522_get_card();
  String result = simple_mfrc522_read();
  Serial.print("Read:");
  Serial.println(result);
}


void simple_mfrc522_init() {
  SPI.begin();               // Init SPI bus
  mfrc522.PCD_Init();        // Init MFRC522 card
}

void simple_mfrc522_get_card() {
  // Reset the loop if no new card present on the sensor/reader. This saves the entire process when idle.
  while ( ! mfrc522.PICC_IsNewCardPresent()) ;;

  // Select one of the cards
  while ( ! mfrc522.PICC_ReadCardSerial()) ;;

  Serial.print(F("Card UID:"));    //Dump UID
  for (byte i = 0; i < mfrc522.uid.size; i++) {
    Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
    Serial.print(mfrc522.uid.uidByte[i], HEX);
  }
  Serial.print(F(" PICC type: "));   // Dump PICC type
  MFRC522::PICC_Type piccType = mfrc522.PICC_GetType(mfrc522.uid.sak);
  Serial.println(mfrc522.PICC_GetTypeName(piccType));

}

void simple_mfrc522_write(String text) {
  simple_mfrc522_write(0, text);
}
void simple_mfrc522_write(byte* buffer) {
  simple_mfrc522_write(0, buffer);
}
// section 0: block 1, 2; section 1: block 4, 5
void simple_mfrc522_write(byte section, String text) {
  byte buffer[34];
  text.getBytes(buffer, 34);
  simple_mfrc522_write(section, buffer);
}
void simple_mfrc522_write(byte section, byte* buffer) {
  byte block = section * 3 + 1;

  MFRC522::StatusCode status;
  // Prepare key - all keys are set to FFFFFFFFFFFFh at chip delivery from the factory.
  MFRC522::MIFARE_Key key;
  for (byte i = 0; i < 6; i++) key.keyByte[i] = 0xFF;

  //  simple_mfrc522_get_card();

  //Serial.println(F("Authenticating using key A..."));
  status = mfrc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, block, &key, &(mfrc522.uid));
  if (status != MFRC522::STATUS_OK) {
    Serial.print(F("PCD_Authenticate() failed: "));
    Serial.println(mfrc522.GetStatusCodeName(status));
    return;
  }
  else Serial.println(F("PCD_Authenticate() success: "));

  // Write block
  status = mfrc522.MIFARE_Write(block, buffer, 16);
  if (status != MFRC522::STATUS_OK) {
    Serial.print(F("MIFARE_Write() failed: "));
    Serial.println(mfrc522.GetStatusCodeName(status));
    return;
  }
  else Serial.println(F("MIFARE_Write() success: "));

  block += 1;

  //Serial.println(F("Authenticating using key A..."));
  status = mfrc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, block, &key, &(mfrc522.uid));
  if (status != MFRC522::STATUS_OK) {
    Serial.print(F("PCD_Authenticate() failed: "));
    Serial.println(mfrc522.GetStatusCodeName(status));
    return;
  }

  // Write block
  status = mfrc522.MIFARE_Write(block, &buffer[16], 16);
  if (status != MFRC522::STATUS_OK) {
    Serial.print(F("MIFARE_Write() failed: "));
    Serial.println(mfrc522.GetStatusCodeName(status));
    return;
  }
  else Serial.println(F("MIFARE_Write() success: "));

  Serial.println(" ");
  mfrc522.PICC_HaltA(); // Halt PICC
  mfrc522.PCD_StopCrypto1();  // Stop encryption on PCD
}

String simple_mfrc522_read() {
  return simple_mfrc522_read(0);
}

String simple_mfrc522_read(byte section) {
  byte block = section * 3 + 1;
  // Prepare key - all keys are set to FFFFFFFFFFFFh at chip delivery from the factory.
  MFRC522::MIFARE_Key key;
  for (byte i = 0; i < 6; i++) key.keyByte[i] = 0xFF;

  byte len;
  MFRC522::StatusCode status;

  byte buffer[18];
  len = 18;

  status = mfrc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, block, &key, &(mfrc522.uid)); //line 834 of MFRC522.cpp file
  if (status != MFRC522::STATUS_OK) {
    Serial.print(F("Authentication failed: "));
    Serial.println(mfrc522.GetStatusCodeName(status));
    return "";
  }

  status = mfrc522.MIFARE_Read(block, buffer, &len);
  if (status != MFRC522::STATUS_OK) {
    Serial.print(F("Reading failed: "));
    Serial.println(mfrc522.GetStatusCodeName(status));
    return "";
  }

  delay(1000); //change value if you want to read cards faster

  mfrc522.PICC_HaltA();
  mfrc522.PCD_StopCrypto1();

  String result;

  for (uint8_t i = 0; i < 16; i++) {
    result += String((char)buffer[i]);
  }
  return result;
}
