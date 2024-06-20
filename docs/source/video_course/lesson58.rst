.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 58 : Bestimmen der Winkelposition eines Joysticks in MicroPython
=============================================================================

Dieses Tutorial behandelt die Kalibrierung eines Joysticks mit dem Raspberry Pi Pico W:

* **Verkabelungssetup**: Verbinden Sie GND mit Pin 38, 3.3V mit Pin 36, VRX mit GPIO-Pin 27 und VRY mit GPIO-Pin 26.
* **Code-Implementierung**: Importieren Sie die notwendigen Bibliotheken. Richten Sie den ADC für die Joystick-Achsen ein und lesen Sie die Werte zur Kalibrierung.
* **Kalibrierung**: Konvertieren Sie die rohen ADC-Werte auf eine Skala von -100 bis +100. Verwenden Sie Trigonometrie, um den Winkel des Joysticks zu berechnen.
* **Hausaufgabe**: Schreiben Sie ein Programm zur Steuerung eines Servomotors basierend auf dem Winkel des Joysticks, um eine genaue Verfolgung zwischen 0 und 180 Grad zu gewährleisten.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/KpDIv0i41Tw?si=PUEInyKbRTIUcvCa" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

