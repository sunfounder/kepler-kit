const int tiltPin = 14;
int state = 0;

void setup() {
  pinMode(tiltPin, INPUT);
  Serial.begin(115200)
}

void loop() {
  state = digitalRead(tiltPin);
  if (state == LOW) {
    Serial.println("The switch works!")
  }
}
