const int sensorPin = A2;
int threshold = 512;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int sensorValue = analogRead(sensorPin);
  if (sensorValue > threshold) {
    Serial.println("Liquid leakage!");
  }
  delay(100);
}
