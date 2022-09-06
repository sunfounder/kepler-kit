#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
#include <avr/power.h>
#endif


#define PIXEL_PIN    0
#define PIXEL_COUNT 8

// Declare our NeoPixel strip object:
Adafruit_NeoPixel strip(PIXEL_COUNT, PIXEL_PIN, NEO_GRB + NEO_KHZ800);
// Argument 1 = Number of pixels in NeoPixel strip
// Argument 2 = Arduino pin number (most are valid)
// Argument 3 = Pixel type flags, add together as needed:
//   NEO_KHZ800  800 KHz bitstream (most NeoPixel products w/WS2812 LEDs)
//   NEO_KHZ400  400 KHz (classic 'v1' (not v2) FLORA pixels, WS2811 drivers)
//   NEO_GRB     Pixels are wired for GRB bitstream (most NeoPixel products)
//   NEO_RGB     Pixels are wired for RGB bitstream (v1 FLORA pixels, not v2)
//   NEO_RGBW    Pixels are wired for RGBW bitstream (NeoPixel RGBW products)


void setup() {
  strip.begin(); // Initialize NeoPixel strip object (REQUIRED)
  strip.show();  // Initialize all pixels to 'off'

  strip.setPixelColor(0, strip.Color(64, 154, 227));       //  Set pixel's color (in RAM)
  strip.setPixelColor(1, strip.Color(128, 0, 128));
  strip.setPixelColor(2, strip.Color(50, 150, 50));
  strip.setPixelColor(3, strip.Color(255, 30, 30));
  strip.setPixelColor(4, strip.Color(0, 128, 255));
  strip.setPixelColor(5, strip.Color(99, 199, 0));
  strip.setPixelColor(6, strip.Color(64, 154, 227));
  strip.setPixelColor(7, strip.Color(255, 100, 0));
  strip.show();                          //  Update strip to match
}

void loop() {

}
