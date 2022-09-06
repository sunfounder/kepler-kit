const int relayPin = 15;

void setup() {

    pinMode(relayPin, OUTPUT);
}


void loop() {
    digitalWrite(relayPin, HIGH);   
    delay(2000);                     
    digitalWrite(relayPin, LOW);    
    delay(2000);                      
}
