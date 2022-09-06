const int STcp = 19;//Pin connected to ST_CP of 74HC595
const int SHcp = 20;//Pin connected to SH_CP of 74HC595 
const int DS = 18; //Pin connected to DS of 74HC595 
const int placePin[4] = {13,12,11,10}; 

int datArray[] = {0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f};
unsigned long timerStart = 0;


void setup ()
{
  //set pins to output
  pinMode(STcp,OUTPUT);
  pinMode(SHcp,OUTPUT);
  pinMode(DS,OUTPUT);
  for (int i = 0; i<4;i++){
    pinMode(placePin[i],OUTPUT);
  }
  timerStart = millis();
}

void loop()
{
  unsigned int count = (millis()-timerStart)/1000;
  
  pickDigit(0);
  hc595_shift(count%10/1);
  
  pickDigit(1);
  hc595_shift(count%100/10);
  
  pickDigit(2);
  hc595_shift(count%1000/100);
  
  pickDigit(3);
  hc595_shift(count%10000/1000);
}

void pickDigit(int digit){
  for(int i = 0; i < 4; i++){
    digitalWrite(placePin[i],HIGH);
  }
  digitalWrite(placePin[digit],LOW);
}

void hc595_shift(int num){
    digitalWrite(STcp,LOW); //ground ST_CP and hold low for as long as you are transmitting
    shiftOut(DS,SHcp,MSBFIRST,datArray[num]);
    digitalWrite(STcp,HIGH); //pull the ST_CPST_CP to save the data
    delay(1);
}
