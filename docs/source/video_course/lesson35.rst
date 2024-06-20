.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 35: Fernwetterstation mit RGB-LED-Temperaturanzeige
=============================================================================

Dieses Tutorial behandelt die Integration einer RGB-LED zur Anzeige von Temperaturdaten in einer Wetterstation mit dem Raspberry Pi Pico W:

* **Projektübersicht**:
  - Bau einer Fernwetterstation mit dem Raspberry Pi Pico W, einem OLED-Display und einer RGB-LED zur visuellen Anzeige der Temperatur.
* **Umwandlung von HSV zu RGB**:
  - Umwandlung von Temperaturwerten in Farben mit dem HSV-Farbrad.
  - Zuordnung von Temperaturen von -20°F (Tiefviolett) bis 120°F (Rot) zu entsprechenden Winkeln auf dem Farbrad.
* **Schaltungsaufbau**:
  - Anschließen des OLED-Displays und der RGB-LED an den Raspberry Pi Pico W.
  - Konfigurieren der GPIO-Pins und PWM für die RGB-LED.
* **Programmierung**:
  - Abrufen der Temperaturdaten, Berechnen des Farbtons, Umwandeln in RGB-Werte und Anwenden dieser auf die RGB-LED.
  - Integrieren der HSV-zu-RGB-Konvertierungsbibliothek in den Wetterstationscode.
* **Demonstration**:
  - Anzeige der Temperaturdaten auf dem OLED-Display und der RGB-LED.
  - Speichern und Ausführen des Codes, um die Einrichtung tragbar mit Batteriebetrieb zu machen.
* **Fazit**:
  - Anpassen des Projekts durch Ändern der Farbzuordnungen und Temperaturbereiche.
  - Aufforderung zum Abonnieren, Kommentieren und Teilen des Tutorials.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/c9tQHyQWIYk?si=ORHsIXt8eBGeXDdp" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
