.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 7: Steuerung von 3 LEDs mit einem Potentiometer in MicroPython
============================================================================

Dieses Tutorial behandelt die Verwendung eines Potentiometers zur Steuerung von drei LEDs (grün, gelb und rot) mit dem Raspberry Pi Pico W:

* **Überprüfung der Hausaufgabenlösung**: Fasst die vorherige Aufgabe zusammen, ein Potentiometer und drei LEDs anzuschließen und die Potentiometerwerte von 0 bis 100 zu skalieren, um die LEDs basierend auf den Eingabewerten zu steuern.
* **Schaltungsaufbau**: Bietet ein detailliertes Schaltbild und die Einrichtung zum Anschließen des Potentiometers und der LEDs an den Raspberry Pi Pico W. Beinhaltet das Erstellen von Masse- und 3,3V-Schienen und das Anschließen der Komponenten an die entsprechenden GPIO-Pins.
* **Lesen und Skalieren von Potentiometerwerten**: Demonstriert, wie man analoge Werte vom Potentiometer liest und sie von ihrem ursprünglichen Bereich (432 bis 65.535) auf eine Skala von 0 bis 100 umrechnet, mithilfe mathematischer Gleichungen.
* **Bedingungslogik zur LED-Steuerung**: Implementiert If-Anweisungen zur Steuerung der LEDs basierend auf den Potentiometerwerten: Grüne LED für Werte zwischen 0 und 79. Gelbe LED für Werte zwischen 80 und 94. Rote LED für Werte zwischen 95 und 100.
* **Praktische Demonstration**: Zeigt den funktionierenden Schaltkreis und den Code in Aktion, wobei die LEDs basierend auf der Position des Potentiometers leuchten.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/YqvcSnGd_HQ?si=igsP6I-k3FhYA7Go" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
