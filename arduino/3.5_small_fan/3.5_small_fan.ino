const int motor1A = 14;
const int motor2A = 15;

void setup() {
  pinMode(motor1A, OUTPUT);
  pinMode(motor2A, OUTPUT);
}

void loop() {
    clockwise();
    delay(1000);
    stopMotor()
    delay(1000);
    anticlockwise();
    delay(1000);
    stopMotor()
    delay(1000);
}

void clockwise()
{
  digitalWrite(motor1A, HIGH);
  digitalWrite(motor2A, LOW);
}

void anticlockwise()
{
  digitalWrite(motor1A, LOW);
  digitalWrite(motor2A, HIGH);
}

void stopMotor()
{
  digitalWrite(motor1A, LOW);
  digitalWrite(motor2A, LOW);
}
