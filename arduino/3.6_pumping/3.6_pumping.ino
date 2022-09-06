const int motor1A = 14;
const int motor2A = 15;

void setup() {
  pinMode(motor1A, OUTPUT);
  pinMode(motor2A, OUTPUT);
}

void loop() {
  digitalWrite(motor1A, HIGH);
  digitalWrite(motor2A, LOW);
}
