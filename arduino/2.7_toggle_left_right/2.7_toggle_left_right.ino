const int slidePin = 14;
int state = 0;

void setup() {
  pinMode(slidePin, INPUT);
  Serial.begin(115200)
}

void loop() {
  state = digitalRead(slidePin);
  if (state == HIGH) {
    Serial.println("ON")
  }else{
    Serial.println("OFF")    
  }
}
