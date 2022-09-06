const int buttonPin = 14;
int buttonState = 0;

void setup() {
  pinMode(buttonPin, INPUT);
  Serial.begin(115200);
}

void loop() {
  buttonState = digitalRead(buttonPin);
  if (buttonState == HIGH) {
    Serial.println("You pressed the button!");
  }
}
