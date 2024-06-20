.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 20: Verwendung des DHT11 Temperatur- und Feuchtigkeitssensors in MicroPython
===========================================================================================

Dieses Tutorial behandelt die Messung von Temperatur und Feuchtigkeit mit dem DHT11-Sensor und dem Raspberry Pi Pico W:

* **Einführung**: Einführung in die Lektion mit Fokus auf die Verwendung des DHT11-Sensors zur Messung von Temperatur und Feuchtigkeit.
* **Rückblick auf vorherige Lektionen**: Rückblick auf die in den vorherigen Lektionen erlernten Grundlagen, wie digitale Schreibvorgänge, analoge Schreibvorgänge mit PWM, digitale Lesevorgänge und analoge Lesevorgänge.
* **Einführung der Komponente**: Vorstellung des DHT11-Sensors aus dem SunFounder Kepler Kit und Demonstration, wie man ihn im Kit findet.
* **Schaltungsaufbau**:
  - Einrichtung von Masse- und Stromschienen auf dem Breadboard.
  - Verbindung des DHT11-Sensors mit dem Raspberry Pi Pico W:
    - Pin 1 des Sensors mit 3,3V.
    - Pin 2 des Sensors mit GPIO-Pin 16 (physischer Pin 21).
    - Pin 4 des Sensors mit Masse.
* **Code-Erklärung**:
  - Importiert notwendige Bibliotheken: machine, utime (als time) und DHT.
  - Richtet den GPIO-Pin für die Dateneingabe mit einem Pull-Down-Widerstand ein.
  - Initialisiert den DHT11-Sensor.
  - Tritt in eine Endlosschleife ein, um kontinuierlich Temperatur und Feuchtigkeit zu messen und anzuzeigen.
  - Erklärt, wie die Ausgabe formatiert wird, um Temperatur und Feuchtigkeit in einer einzigen Zeile mit `\r` anzuzeigen.
* **Praktische Demonstration**:
  - Führt den Code aus und beobachtet die Echtzeitmessungen von Temperatur und Feuchtigkeit.
  - Diskutiert die Wichtigkeit, Methoden zu vermeiden, die Kondensation am Sensor verursachen könnten, um Änderungen der Messwerte zu testen.
* **Ausgabeformatierung**:
  - Demonstriert, wie die Ausgabe formatiert wird, um die Temperatur in Grad Celsius und die Feuchtigkeit in Prozent anzuzeigen.
  - Erklärt, wie das Grad-Symbol mit ASCII-Zeichencodes gedruckt wird.
* **Hausaufgabe**:
  - Fügt der Schaltung einen Taster hinzu.
  - Ändert den Code so, dass beim Drücken des Tasters zwischen der Anzeige der Temperatur in Celsius und Fahrenheit umgeschaltet wird.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/KYEidJFYPto?si=5vAk5sl-VyEqYIfs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
