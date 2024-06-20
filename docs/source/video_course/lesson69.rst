.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 69 : Cleanly Exit MicroPython-Threads When Program Terminates
===================================================================================

Dieses Tutorial behandelt die Steuerung eines Servos und LEDs mit dem Raspberry Pi Pico W unter Verwendung beider Kerne:

* **Verdrahtungsaufbau**:
  - Schließen Sie eine rote LED an GPIO-Pin 15 mit einem 330-Ohm-Widerstand an Masse an.
  - Schließen Sie eine grüne LED an GPIO-Pin 14 mit einem 330-Ohm-Widerstand an Masse an.
  - Schließen Sie das Steuerkabel des Servos an GPIO-Pin 17, das Stromkabel an physikalischen Pin 40 und das Erdungskabel an physikalischen Pin 38 an.
* **Code-Implementierung**:
  - Importieren Sie die notwendigen Bibliotheken (`machine`, `time`, `_thread`, `Servo`).
  - Richten Sie die Pins für die LEDs und den Servo ein.
  - Definieren Sie eine Funktion `other_core`, um die LEDs basierend auf der Richtung des Servos mit einer globalen Variablen blinken zu lassen.
  - Erstellen Sie eine Schleife, um den Servo zu bewegen und die LED-Richtung festzulegen.
* **Hausaufgabe**:
  - Erweitern Sie den Code, um die rote LED blinken zu lassen, wenn sich der Servo im Uhrzeigersinn bewegt, und die grüne LED, wenn er sich gegen den Uhrzeigersinn bewegt.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/mcXxqx0lZYo?si=tIek_zJ4EMuZ3bC4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

