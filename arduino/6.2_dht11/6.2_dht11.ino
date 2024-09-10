/*
  This code reads the temperature and humidity values from a DHT11 sensor 
  connected to pin 11 and prints them to the serial monitor. 
  It also calculates and prints the heat index value in both Celsius and Fahrenheit.
  
  Board: Arduino Uno R4
  Component: Temperature and humidity module(DHT11)
  Library: https://github.com/adafruit/DHT-sensor-library  (DHT sensor library by Adafruit)
*/

#include <DHT.h>

#define DHTPIN 16       // Define the pin used to connect the sensor
#define DHTTYPE DHT11  // Define the sensor type

DHT dht(DHTPIN, DHTTYPE);  // Create a DHT object

void setup() {
  // Initialize the serial communication
  Serial.begin(9600);
  Serial.println(F("DHT11 test!"));

  dht.begin();  // Initialize the DHT sensor
}

void loop() {
  // Wait a few seconds between measurements.
  delay(2000);

  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  float h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();
  // Read temperature as Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);

  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }

  // Compute heat index in Fahrenheit (the default)
  float hif = dht.computeHeatIndex(f, h);
  // Compute heat index in Celsius (isFahreheit = false)
  float hic = dht.computeHeatIndex(t, h, false);

  // Print the humidity, temperature, and heat index values to the serial monitor
  Serial.print(F("Humidity: "));
  Serial.print(h);
  Serial.print(F("%  Temperature: "));
  Serial.print(t);
  Serial.print(F("°C "));
  Serial.print(f);
  Serial.print(F("°F  Heat index: "));
  Serial.print(hic);
  Serial.print(F("°C "));
  Serial.print(hif);
  Serial.println(F("°F"));
}