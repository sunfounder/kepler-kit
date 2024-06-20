.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 31: Projekt einer fernsteuerbaren Wetterstation ohne Sensoren
=============================================================================

Dieses Tutorial behandelt die Erstellung einer wetterstationslosen Wetterstation mit dem Raspberry Pi Pico W:

* **Verbindung mit dem WLAN**:
  - Importieren Sie die notwendigen Bibliotheken.
  - Erstellen Sie ein WLAN-Objekt und verbinden Sie es mit dem WLAN-Netzwerk.
* **Abrufen von Wetterdaten**:
  - Verwenden Sie die OpenWeatherMap-API, um Echtzeit-Wetterdaten abzurufen.
  - Erhalten Sie einen API-Schlüssel von OpenWeatherMap, indem Sie ein kostenloses Konto erstellen.
* **Parsen von JSON-Daten**:
  - Extrahieren Sie relevante Wetterinformationen wie Temperatur, Luftfeuchtigkeit, Luftdruck, Sonnenauf- und -untergangszeiten.
* **Code-Erklärung**:
  - Verwenden Sie `urequests.get()`, um JSON-Daten vom API-Endpunkt abzurufen.
  - Konvertieren Sie die Unix-Epoch-Zeit in die lokale Zeit für Sonnenauf- und -untergang.
  - Konvertieren Sie den Luftdruck von HPA in Atmosphären.
* **Anzeige der Wetterdaten**:
  - Drucken Sie Wetterinformationen wie Temperatur, Luftfeuchtigkeit, Luftdruck, Bedingungen und Windgeschwindigkeit aus.
* **Hausaufgabe**:
  - Verbessern Sie das Projekt, indem Sie ein Display hinzufügen, um die Wetterinformationen anzuzeigen.
  - Erstellen Sie eine tragbare, batteriebetriebene Wetterstation.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/hbcA90S7Jtk?si=mHMxKUEEpqiYM7DA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
