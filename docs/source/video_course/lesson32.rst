.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 32: Mobiles Wetterstationsprojekt
=============================================================================

Dieses Tutorial behandelt die Erstellung einer tragbaren Wetterstation mit dem Raspberry Pi Pico W:

* **Verbindung mit dem WLAN**:
  - Importieren Sie die notwendigen Bibliotheken.
  - Erstellen Sie ein WLAN-Objekt und verbinden Sie es mit dem WLAN-Netzwerk.
* **Abrufen von Wetterdaten**:
  - Verwenden Sie die OpenWeatherMap-API, um Echtzeit-Wetterdaten abzurufen.
  - Erhalten Sie einen API-Schlüssel von OpenWeatherMap, indem Sie ein kostenloses Konto erstellen.
* **Parsen von JSON-Daten**:
  - Extrahieren Sie relevante Wetterinformationen wie Temperatur, Luftfeuchtigkeit, Luftdruck, Sonnenauf- und -untergangszeiten.
* **Anzeige der Daten auf OLED**:
  - Richten Sie ein OLED-Display ein und verbinden Sie es mit dem Raspberry Pi Pico W.
  - Verwenden Sie die `ssd1306`-Bibliothek, um Wetterdaten auf dem OLED-Bildschirm anzuzeigen.
  - Erstellen Sie eine Schleife, um die Wetterdaten regelmäßig auf dem Bildschirm zu aktualisieren.
* **Stromversorgung des Geräts**:
  - Verbinden Sie den Raspberry Pi Pico W für den tragbaren Einsatz mit einer Batterie.
* **Code-Erklärung**:
  - Schrittweise Initialisierung des OLED-Displays und Verbindung mit dem WLAN.
  - Abrufen und Parsen von Wetterdaten und deren Anzeige auf dem OLED-Bildschirm.
  - Implementierung einer Schleife zur Aktualisierung der Wetterdaten alle paar Minuten.
* **Hausaufgabe**:
  - Verbessern Sie das Projekt, indem Sie eine RGB-LED hinzufügen, um Wetterbedingungen wie Temperatur, Luftfeuchtigkeit oder Windgeschwindigkeit visuell anzuzeigen.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/zovC4CvR1Hw?si=d_lhJvfzTC3pR5cS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
