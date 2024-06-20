.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 25: Erste Schritte mit dem OLED 1306 in MicroPython
=============================================================================

Dieses Tutorial behandelt die Verwendung des Raspberry Pi Pico W und eines OLED-Displays für tragbare Projekte:

* **Einführung**:
  - Hervorhebung des Ziels: Projekte vom Desktop zu lösen, um sie tragbarer und energieeffizienter zu machen.
* **Komponentenüberblick und Einrichtung**:
  - Rückblick auf die vorherige Lektion: Verwendung eines wiederaufladbaren LiPo-Akkus zur Stromversorgung des Raspberry Pi Pico W mit einem DHT-11-Sensor, Taster und LCD-Display.
  - Diskussion über die Nachteile der Verwendung eines LCD-Displays, einschließlich höherem Stromverbrauch und größerer Größe.
* **Einführung des OLED-Displays**:
  - Empfehlung, ein kleines, stromsparendes und kontrastreiches OLED-Display für tragbare Projekte zu verwenden.
  - Erklärung, wie das OLED-Display über den I2C-Bus mit dem Raspberry Pi Pico W verbunden wird, insbesondere an den GPIO-Pins 2 (SDA) und 3 (SCL).
* **Bibliotheksinstallation und Ersteinrichtung**:
  - Demonstration, wie die SSD1306-Bibliothek für das OLED-Display installiert wird.
  - Erklärung der grundlegenden Code-Einrichtung, einschließlich des Imports notwendiger Bibliotheken und der Erstellung der I2C- und Display-Objekte.
* **Anzeigen von Text und Grafiken**:
  - Bereitstellung von Codebeispielen zur Anzeige von Text auf dem OLED-Bildschirm.
  - Erklärung, wie einzelne Pixel adressiert und horizontale, vertikale und beliebige Linien gezeichnet werden.
  - Demonstration, wie Rechtecke auf dem Display erstellt und gefüllt werden.
* **Energieverwaltung**:
  - Erklärung, wie das Display ein- und ausgeschaltet wird, um Batteriestrom zu sparen, mithilfe von Softwarebefehlen.
* **Praktische Demonstration**:
  - Ausführung des Codes, um Text und Grafiken auf dem OLED-Display anzuzeigen.
  - Betonung des hohen Kontrasts und des geringen Stromverbrauchs des OLED-Displays im Vergleich zum LCD.
* **Hausaufgabe**:
  - Aufgabe: Erstellen Sie ein Programm, das den Titel "My Circle" oben auf dem Bildschirm anzeigt und einen Kreis mit einem Radius von 20 Pixeln in der Mitte des Bildschirms zeichnet.
  - Aufforderung an die Zuschauer, ihre Hausaufgabe auf YouTube zu posten und den Link in den Kommentaren zu teilen.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/6SdNvqofWww?si=ZVxzi5Nm3lP5PniU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
