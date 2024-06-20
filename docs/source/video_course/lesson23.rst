.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 23: Temperatur- und Feuchtigkeitssensor mit LCD-Display
=============================================================================

Dieses Tutorial behandelt die Erstellung eines Temperatur- und Feuchtigkeitsprojekts mit dem Raspberry Pi Pico W und dem DHT-11-Sensor mit einem LCD-Display:

* **Einführung**: Vorstellung des Tutorials, Anerkennung des Sponsors SunFounder und Überprüfung des Ziels der Lektion, ein Temperatur- und Feuchtigkeitssensorprojekt mit einem LCD-Display zu erstellen.
* **Einführung der Komponenten und Aufbau**:
  - Beschreibung der erforderlichen Komponenten: Raspberry Pi Pico W, DHT-11-Sensor, Taster und LCD-1602-Display.
  - Bereitstellung eines Schaltplans und Anweisungen zum Anschließen dieser Komponenten, wobei auf frühere Lektionen für detaillierte Verdrahtungsanweisungen verwiesen wird.
* **Bibliotheksinstallation**:
  - Anleitung zum Herunterladen und Installieren der notwendigen Bibliothek für das LCD-1602-Display von toptechboy.com.
  - Anweisungen zum Speichern und Importieren der Bibliothek in der Thonny IDE.
* **Code-Erklärung**:
  - Beschreibung der Einrichtung des DHT-11-Sensors und des Tasters unter Verwendung der GPIO-Pins.
  - Einführung einer Flag-Variable zum Umschalten zwischen Celsius und Fahrenheit.
  - Erklärung des Codes zum Lesen von Temperatur und Feuchtigkeit vom DHT-11-Sensor.
  - Detaillierte Umsetzung einer Umschaltfunktion zum Wechseln zwischen Celsius und Fahrenheit.
  - Erklärung, wie die Messwerte sowohl auf der Konsole als auch auf dem LCD angezeigt werden.
* **Praktische Demonstration**:
  - Zeigt das Programm in Aktion, indem Temperatur- und Feuchtigkeitsmesswerte auf dem LCD angezeigt werden.
  - Demonstriert die Umschaltfunktion zum Wechseln zwischen Celsius und Fahrenheit.
  - Behandelt potenzielle Probleme mit Textüberlappungen auf dem LCD durch Hinzufügen von Leerzeichen und Verwendung von `LCD.clear()`, um den Bildschirm vor dem Schreiben neuer Texte zu löschen.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/2DZo1JeVWMk?si=mceO0XqYqT3aBpU7" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
