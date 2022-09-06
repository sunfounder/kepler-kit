const int reedPin = 14;
int state = 0;

void setup() {
  pinMode(reedPin, INPUT);
  Serial.begin(115200);
}

void loop() {
  state = digitalRead(reedPin);
  if (state == HIGH) {
    Serial.println("There are magnets here!!");
  }   
}
