.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 56 : Verwendung eines Joysticks mit MicroPython
=============================================================================

Dieses Tutorial behandelt die Verwendung eines Joysticks mit dem Raspberry Pi Pico W:

* **Verkabelungssetup**:
   - Verbinden Sie GND, 3.3V, VRX mit GPIO-Pin 27 und VRY mit GPIO-Pin 26.
* **Code Implementierung**:
   - Importieren Sie die notwendigen Bibliotheken (``machine``, ``time``, ``math``).
   - Richten Sie ADC für die Joystick-Achsen ein.
   - Lesen und drucken Sie die Joystick-Werte, um den Bereich und das Verhalten zu verstehen.
* **Kalibrierung**:
   - Passen Sie die Messwerte an, um sie intuitiver zu gestalten, und konvertieren Sie sie auf eine Skala von -100 bis +100 zur einfacheren Interpretation.
* **Hausaufgabe**:
   - Schreiben Sie ein Programm zur Kalibrierung des Joysticks, sodass die Mittelstellung (0,0) und die Randstellungen ±100 anzeigen.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/0W8XSJhGux0?si=DO3JL-oMiMfbXF_e" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

