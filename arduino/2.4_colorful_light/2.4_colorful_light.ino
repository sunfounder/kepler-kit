const int redPin = 13;   
const int greenPin = 14;  
const int bluePin = 15;  

void setup()
{ 
  pinMode(redPin, OUTPUT); 
  pinMode(greenPin, OUTPUT); 
  pinMode(bluePin, OUTPUT); 
}    

void loop() 
{    
  color(255, 0, 0); //  red 
  delay(1000); 
  color(0,255, 0); //  green  
  delay(1000);  
  color(0, 0, 255); //  blue  
  delay(1000);

  color(255,0,252); // red  
  delay(1000);   
  color(237,109,0); //  orange  
  delay(1000);   
  color(255,215,0); //  yellow  
  delay(1000);   
  color(34,139,34); //  green  
  delay(1000);  
  color(0,112,255); //  blue  
  delay(1000);  
  color(0,46,90); //   indigo 
  delay(1000);  
  color(128,0,128); //  purple  
  delay(1000);  
}     

void color (unsigned char red, unsigned char green, unsigned char blue)
{    
  analogWrite(redPin, red);   
  analogWrite(greenPin, green); 
  analogWrite(bluePin, blue); 
}
