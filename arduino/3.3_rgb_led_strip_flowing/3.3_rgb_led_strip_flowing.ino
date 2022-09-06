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
}

void loop() {
  flowing(80);
}

void flowing(int wait) {
  // Let the colors pass one by one from back to front.
  // The last one re-fetches a random color.
  for (int i = 0; i < PIXEL_COUNT ; i++) {
    strip.setPixelColor(i, strip.getPixelColor(i + 1));
  }
  int pixelHue = random(65535); // Get a random color from the color wheel (range of 65535).

  // strip.ColorHSV() can take 1 or 3 arguments: a hue (0 to 65535) or
  // optionally add saturation and value (brightness) (each 0 to 255).
  // Here we're using just the single-argument hue variant. The result
  // is passed through strip.gamma32() to provide 'truer' colors
  // before assigning to each pixel:
  strip.setPixelColor(PIXEL_COUNT - 1, strip.gamma32(strip.ColorHSV(pixelHue)));

  strip.show(); // Update strip with new contents
  delay(wait);  // Pause for a moment
}
