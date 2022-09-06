const int xPin = A1;  //the VRX attach to
const int yPin = A0;  //the VRY attach to
const int swPin = 22;  //the SW attach to

void setup()
{
  pinMode(swPin, INPUT);  //set the SW pin to INPUT
  digitalWrite(swPin, HIGH);   //And initial value is HIGH
  Serial.begin(9600);
}

void loop()
{
  Serial.print("X: "); 
  Serial.print(analogRead(xPin), DEC);  // print the value of VRX in DEC
  Serial.print("|Y: ");
  Serial.print(analogRead(yPin), DEC);  // print the value of VRX in DEC
  Serial.print("|Z: ");
  Serial.println(digitalRead(swPin));   // print the value of SW
  delay(500);
}
