const int signalPin = 15;
const int buttonPin = 14;

void setup() {
  pinMode(signalPin, OUTPUT);
  pinMode(buttonPin, INPUT);
}

void loop() {
  int buttonState = digitalRead(buttonPin);
  if (buttonState == HIGH) {
    digitalWrite(signalPin, HIGH);
  } else {
    digitalWrite(signalPin, LOW);
  }
}
