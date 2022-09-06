#define analogPin  A2 //the thermistor attach to 
#define beta 3950 //the beta of the thermistor
#define resistance 10 //the value of the pull-up resistor

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  //read thermistor value
  long a = analogRead(analogPin);
  //the calculating formula of temperature
  float tempC = beta / (log((1025.0 * 10 / a - 10) / 10) + beta / 298.0) - 273.0;
  float tempF = 1.8 * tempC + 32.0;
  Serial.print("Temp: ");
  Serial.print(tempC);
  Serial.println("degree Celsius");
  Serial.print("Temp: ");
  Serial.print(tempF);
  Serial.println("degree Fahrenheit");  
  delay(200); //wait for 200 milliseconds
}
