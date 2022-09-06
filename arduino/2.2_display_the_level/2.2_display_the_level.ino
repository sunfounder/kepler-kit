void setup() {
    for(int i=6;i<=15;i++)
    {
        pinMode(i,OUTPUT);
    }
}

void loop() {
    for(int i=6;i<=15;i++)
    {
        digitalWrite(i,HIGH);
        delay(500);
        digitalWrite(i,LOW);
        delay(500);    
    }
}
