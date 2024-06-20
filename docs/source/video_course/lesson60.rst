.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 60 : Steuerung der NeoPixel-Farben mit einem Joystick in MicroPython
=============================================================================

Dieses Tutorial behandelt die Steuerung eines LED-Streifens mit einem Joystick unter Verwendung des Raspberry Pi Pico W:

* **Verkabelungssetup**: 
   - Verbinden Sie den Joystick-GND mit Pin 38, 3,3V mit Pin 36, VRX mit GPIO-Pin 27 und VRY mit GPIO-Pin 26. 
   - Verbinden Sie den Neopixel-GND mit Pin 38, 5V mit Pin 40 und Daten mit GPIO-Pin 0.
* **Code-Implementierung**: 
   - Importieren Sie die notwendigen Bibliotheken (`machine`, `time`, `math`, `neopixel`). 
   - Richten Sie den ADC für den Joystick und Neopixel ein. 
   - Lesen Sie die Joystick-Werte aus und berechnen Sie die Winkel. 
   - Konvertieren Sie die Winkel in RGB-Werte für den Neopixel.
* **Hausaufgabe**: 
   - Schreiben Sie ein Programm zur Steuerung der Neopixel-Farbe und Helligkeit basierend auf dem Winkel und der Entfernung des Joysticks vom Zentrum.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/8UCJHY7uTH4?si=BKJ8lYNz1kF4w9wm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

