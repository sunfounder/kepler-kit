const int STcp = 19;//Pin connected to ST_CP of 74HC595
const int SHcp = 20;//Pin connected to SH_CP of 74HC595 
const int DS = 18; //Pin connected to DS of 74HC595 
int datArray[] = {0xFF,0xBB,0xD7,0xEF,0xD7,0xBB,0xFF,0xFF};

void setup ()
{
  //set pins to output
  pinMode(STcp,OUTPUT);
  pinMode(SHcp,OUTPUT);
  pinMode(DS,OUTPUT);
}
void loop()
{
  for(int num = 0; num <8; num++)
  {
    digitalWrite(STcp,LOW); //ground ST_CP and hold low for as long as you are transmitting
    shiftOut(DS,SHcp,MSBFIRST,datArray[num]);
    shiftOut(DS,SHcp,MSBFIRST,0x80>>num);    
    //return the latch pin high to signal chip that it 
    //no longer needs to listen for information
    digitalWrite(STcp,HIGH); //pull the ST_CPST_CP to save the data
  }
}
