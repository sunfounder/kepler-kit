const int STcp = 1;//Pin connected to ST_CP of 74HC595
const int SHcp = 2;//Pin connected to SH_CP of 74HC595 
const int DS = 0; //Pin connected to DS of 74HC595 
int datArray[] = {0b00000000, 0b00000001, 0b00000011, 0b00000111, 0b00001111, 0b00011111, 0b00111111, 0b01111111, 0b11111111};

void setup ()
{
  //set pins to output
  pinMode(STcp,OUTPUT);
  pinMode(SHcp,OUTPUT);
  pinMode(DS,OUTPUT);
}
void loop()
{
  for(int num = 0; num <=8; num++)
  {
    digitalWrite(STcp,LOW); //ground ST_CP and hold low for as long as you are transmitting
    shiftOut(DS,SHcp,MSBFIRST,datArray[num]);
    //return the latch pin high to signal chip that it 
    //no longer needs to listen for information
    digitalWrite(STcp,HIGH); //pull the ST_CPST_CP to save the data
    delay(500); //wait for a second
  }
}
