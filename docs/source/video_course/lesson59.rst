.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 59 : Steuerung eines Servos mit einem Joystick
=============================================================================

Dieses Tutorial behandelt die Steuerung eines Servos mit einem Joystick unter Verwendung des Raspberry Pi Pico W:

* **Verkabelungssetup**: Verbinden Sie den Joystick-GND mit Pin 38, 3,3V mit Pin 36, VRX mit GPIO-Pin 27 und VRY mit GPIO-Pin 26. Verbinden Sie 5V des Servos mit Pin 40, GND mit Pin 38 und die Steuerung mit GPIO-Pin 15.
* **Code-Implementierung**: Importieren Sie die notwendigen Bibliotheken (``machine``, ``time``, ``math``). Richten Sie den ADC für die Joystick-Achsen und PWM für den Servo ein. Lesen und drucken Sie die Joystick-Werte zur Kalibrierung und Winkelberechnung.
* **Kalibrierung und Steuerung**: Konvertieren Sie die rohen ADC-Werte auf eine Skala von -100 bis +100. Berechnen Sie den Winkel des Joysticks mit Trigonometrie. Ordnen Sie den Winkel dem entsprechenden PWM-Wert für den Servo zu.
* **Hausaufgabe**: Schreiben Sie ein Programm zur Steuerung eines Servomotors basierend auf dem Winkel des Joysticks, um eine genaue Verfolgung zwischen 0 und 180 Grad zu gewährleisten.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/ayY2wOJmrUE?si=HKP8qwd4WMC1et2r" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

