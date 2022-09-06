const int reedPin = 14;

void setup() {
  pinMode(reedPin, INPUT);
  Serial.begin(115200);
  attachInterrupt(digitalPinToInterrupt(reedPin), detected, RISING);
}

void loop() {

}

void detected(){
  Serial.println("Magnet!");
}
