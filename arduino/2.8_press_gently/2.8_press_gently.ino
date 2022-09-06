const int limitPin = 14;
int state = 0;

void setup() {
  pinMode(limitPin, INPUT);
  Serial.begin(115200)
}

void loop() {
  state = digitalRead(limitPin);
  if (state == HIGH {
    Serial.println("The switch works!")
  }   
}
