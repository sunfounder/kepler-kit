.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 22: Verwendung eines LCD-Displays mit dem Pico W
=============================================================================

Dieses Tutorial behandelt das Anschließen und Verwenden eines LCD-1602-Displays mit dem Raspberry Pi Pico W:

* **Einführung**: Vorstellung des Tutorials, Anerkennung des Sponsors SunFounder und Erklärung des Ziels, ein LCD-Display zum mobilen Einsatz im Raspberry Pi Pico W-Projekt hinzuzufügen.

* **Einführung der Komponenten und Aufbau**:
- Beschreibung der erforderlichen Komponenten: LCD-1602-Display und Female-to-Male-Kabel.
- Detaillierte Verbindungen:
  - LCD-1602-Pins zum Raspberry Pi Pico W:
    - Masse zu Pin 38
    - VCC (5V) zu dem rechten Pin
    - SDA (Daten) zu GPIO-Pin 6
    - SCL (Takt) zu GPIO-Pin 7

* **Bibliotheksinstallation**:
  - Anleitung zum Herunterladen und Installieren der notwendigen Bibliothek für das LCD-1602-Display von toptechboy.com.
  - Anweisungen zum Speichern und Importieren der Bibliothek in der Thonny IDE.

* **Code-Erklärung**:
  - Beschreibung der Erstellung eines LCD-Objekts und des Schreibens von Text auf das LCD.
  - Bereitstellung eines Beispielprogramms, das nach dem Namen des Benutzers fragt und eine Begrüßungsnachricht auf dem LCD anzeigt.
  - Behebung potenzieller Probleme mit Textüberlappung durch die Verwendung von `LCD.clear()`, um den Bildschirm vor dem Schreiben neuer Texte zu löschen.

* **Praktische Demonstration**:
  - Zeigt das Programm in Aktion, indem Namen auf dem LCD angezeigt werden.
  - Erklärung zur Anpassung des LCD-Kontrasts mit einem Potentiometer auf der Rückseite des Displays.

* **Hausaufgabe**:
  - Aufgabe zur Integration des LCD-Displays in das Projekt mit dem DHT11-Temperatur- und Feuchtigkeitssensor aus Lektion 21.
  - Anweisung, die Temperatur in Celsius oder Fahrenheit basierend auf einem Umschalttaster anzuzeigen und die Feuchtigkeit auf dem LCD darzustellen.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/liwMc01LOIA?si=ZRpzb2YskRgxd3Kn" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
