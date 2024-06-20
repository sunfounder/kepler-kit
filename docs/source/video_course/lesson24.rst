.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 24: Mobile Projekte mit wiederaufladbarem LiPo-Akku betreiben
=============================================================================

Dieses Tutorial behandelt die Stromversorgung eines Raspberry Pi Pico W-Projekts mit einem wiederaufladbaren LiPo-Akku, um das Projekt tragbar zu machen:

* **Einführung**: Einführung in das Tutorial, Anerkennung des Sponsors SunFounder und Überprüfung des Ziels der Lektion: das DHT-11 Temperatur- und Feuchtigkeitssensorprojekt tragbar machen.
* **Komponentenüberblick und Einrichtung**:
  - Rückblick auf die Einrichtung des vorherigen Projekts: Raspberry Pi Pico W, DHT-11-Sensor, Taster und LCD-1602-Display.
  - Diskussion über die Notwendigkeit, das USB-Kabel zu entfernen und das Projekt mit einem LiPo-Akku zu betreiben.
* **Bibliotheksinstallation**:
  - Anleitung zur Installation der LCD-1602-Bibliothek, falls dies noch nicht geschehen ist.
* **Code-Erklärung**:
  - Beschreibung der Notwendigkeit, das Programm als `main.py` zu speichern, damit es automatisch startet, wenn der Pico W eingeschaltet wird.
  - Demonstration des Speicherns des Codes und Überprüfung seiner Funktionalität.
* **Projekt mit Batterie betreiben**:
  - Einführung des wiederaufladbaren LiPo-Akkus und des Batteriehalters aus dem SunFounder Kepler Kit.
  - Detaillierte Beschreibung der Verbindung des Akkus mit dem Pico W mithilfe eines im Kit enthaltenen Power-Management-Moduls.
  - Erklärung der Anpassung der LCD-Stromverbindung von 5V (Pin 40) auf 3,7V (Pin 39) aufgrund der Batterieleistung.
  - Demonstration des Setups und Überprüfung, ob das Projekt korrekt mit Batteriestrom läuft.
* **Anpassungen und Demonstration**:
  - Demonstration der Anpassung des LCD-Kontrasts für eine optimale Anzeige bei Batteriebetrieb.
  - Vorführung des korrekt funktionierenden Projekts, einschließlich des Umschaltens zwischen Fahrenheit und Celsius.
* **Abschluss und nächste Schritte**:
  - Aufforderung an die Zuschauer, sicherzustellen, dass ihr Projekt funktioniert, und Einführung der Idee, ein OLED-Display für zukünftige Lektionen zu verwenden.
  - Empfehlung, ein OLED-Display zu kaufen, um ein kompakteres und energieeffizienteres Setup zu erreichen.
  - Ausblick auf zukünftige Lektionen, die sich auf die Erstellung tragbarer, einsatzfähiger Projekte mit erweiterten Funktionen konzentrieren.
* **Hausaufgabe und Schlussbemerkungen**:
  - Vorschlag an die Zuschauer, das OLED-Display zu bestellen, um sich auf die kommenden Lektionen vorzubereiten.
  - Abschließend die Aufforderung, das Video zu liken, zu kommentieren, zu abonnieren und zu teilen.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/NhfkOEmZoLQ?si=jxNyNl9DCKlqr4PJ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
