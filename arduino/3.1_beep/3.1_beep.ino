const int buzzerPin = 15;

void setup() {
    pinMode(buzzerPin, OUTPUT);
}

void loop() {
  for (int i=0;i<4;i++){
    digitalWrite(buzzerPin, HIGH);   
    delay(300);                       
    digitalWrite(buzzerPin, LOW);    
    delay(300);     
  }
  delay(1000);      
}
