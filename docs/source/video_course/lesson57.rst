.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 57 : Kalibrierung eines Joysticks in MicroPython
=============================================================================

Dieses Tutorial behandelt die Kalibrierung eines Joysticks mit dem Raspberry Pi Pico W:

* **Verkabelungssetup**:
   - Verbinden Sie GND mit physischem Pin 38, 3.3V mit Pin 36, VRX mit GPIO-Pin 27 und VRY mit GPIO-Pin 26.
* **Code Implementierung**:
   - Importieren Sie die notwendigen Bibliotheken (`machine`, `time`, `math`).
   - Richten Sie ADC für die Joystick-Achsen ein.
   - Lesen und drucken Sie die Joystick-Werte zur ersten Kalibrierung.
* **Kalibrierung**:
   - Berechnen und anwenden Sie Kalibrierungsgleichungen, um rohe ADC-Werte auf eine Skala von -100 bis +100 für beide Achsen zu konvertieren.
   - Passen Sie das Koordinatensystem an und eliminieren Sie Rauschen um die Neutralposition.
* **Hausaufgabe**:
   - Schreiben Sie ein Programm, das den Winkel des Joysticks basierend auf seiner Position berechnet und anzeigt.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/rRHyho4vwIQ?si=cV75rrwEWSYoKhAN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

