const int pirPin = 14;
int state = 0;


void setup() {
  pinMode(pirPin, INPUT);
  Serial.begin(115200);
}

void loop() {
  state = digitalRead(pirPin);
  if (state == HIGH) {
    Serial.println("Somebody here!");
  }   
}
