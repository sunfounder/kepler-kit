.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 21: Temperatur- und Feuchtigkeitsmessungen mit Umschalter
=============================================================================

Dieses Tutorial behandelt das Hinzufügen eines Umschalttasters zum Wechseln zwischen Temperaturanzeigen in Fahrenheit und Celsius mithilfe des DHT11-Sensors und des Raspberry Pi Pico W:

* **Einführung**: Vorstellung des Tutorials und Anerkennung des Sponsors SunFounder. Erklärung des Ziels, einen Umschalttaster zur bestehenden Temperatur- und Feuchtigkeitsmessung hinzuzufügen.

* **Rückblick auf vorherige Lektionen**: Rückblick auf die vorherige Lektion zur Verwendung des DHT11-Sensors und Kontextualisierung der aktuellen Aufgabe.

* **Einführung der Komponenten und Schaltungsaufbau**:
 - Wiederholung der Vorstellung des DHT11-Sensors und Erklärung der Hinzufügung eines Tasters zur Schaltung.
 - Beschreibung der Verbindungen:
 - DHT11-Sensor:Pin 1 zu 3.3V,Pin 2 zu GPIO-Pin 16,Pin 4 zu Masse
 - Taster:Ein Bein zu Masse,Das andere Bein zu GPIO-Pin 15
* **Code-Erklärung**:
  - Importiert notwendige Bibliotheken: machine, utime (als time) und DHT.
  - Einrichtung der GPIO-Pins für den DHT11-Sensor und den Taster.
  - Erstellung eines Umschaltmechanismus zum Wechseln zwischen Temperatureinheiten (Celsius und Fahrenheit).
  - Liest den Tasterzustand und wechselt die Temperatureinheit, wenn der Taster gedrückt und losgelassen wird.
  - Misst und konvertiert die Temperatur von Celsius in Fahrenheit.
  - Gibt Temperatur- und Feuchtigkeitswerte in einer einzigen Zeile aus, wobei `\r` für eine saubere Ausgabe verwendet wird.
  - Behandelt Formatierungsprobleme, um sicherzustellen, dass die Ausgabe beim Umschalten zwischen Celsius und Fahrenheit korrekt angezeigt wird.
* **Praktische Demonstration**:
  - Führt den Code aus, um Temperatur- und Feuchtigkeitsmessungen zu beobachten.
  - Demonstriert die Umschaltfunktionalität zwischen Celsius und Fahrenheit, wenn der Taster gedrückt wird.
  - Behebt Formatierungsprobleme, um sicherzustellen, dass die Ausgabe sauber und konsistent ist.
* **Hausaufgabe**:
  - Fügt dem Projekt weitere Umschaltfunktionen hinzu.
  - Implementiert zusätzliche Umschalter, um zwischen der Anzeige von Temperatur in Celsius, Fahrenheit und Feuchtigkeit nacheinander umzuschalten.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/MrfIfndX7OM?si=d1WrCY-6Ui7J2DWb" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
