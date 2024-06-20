.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 30: Projekt zur Verbindung Ihres Raspberry Pi Pico W mit dem Internet
=============================================================================

Dieses Tutorial behandelt die Verbindung des Raspberry Pi Pico W mit dem Internet und das Abrufen von Daten von APIs:

**Einführung**:
- Das Ziel ist es, den Raspberry Pi Pico W mit dem Internet zu verbinden und Echtzeitdaten von APIs abzurufen.
- Keine zusätzliche Hardware erforderlich.
**Verbindung mit dem WLAN**:
- Import der notwendigen Bibliotheken: `network`, `time`, `urequests`.
- Erstellen eines WLAN-Objekts und Verbindung mit dem WLAN-Netzwerk.
- Sicherstellen der erfolgreichen Verbindung, bevor fortgefahren wird.
**Abrufen von Daten von APIs**:
- Einführung in JSON-Dateien und deren Struktur (Arrays, Dictionaries, verschachtelte Elemente).
- Beispiel-API: Abrufen von Echtzeitdaten über Astronauten im Weltraum.
- Parsen und Anzeigen der Datenstruktur, um ihr Format zu verstehen.
**Code-Erklärung**:
- Verwendung von `urequests.get()`, um JSON-Daten von einem angegebenen API-Endpunkt abzurufen.
- Parsen der JSON-Daten, um relevante Informationen zu extrahieren.
- Beispiel: Auflistung der Namen der derzeit im Weltraum befindlichen Astronauten und ihrer jeweiligen Raumfahrzeuge.
**Praktische Demonstration**:
- Codebeispiel zum Abrufen und Anzeigen von Daten über Astronauten.
- Demonstration, wie verschachtelte JSON-Strukturen navigiert werden, um spezifische Daten zu extrahieren.
- Beispielausgabe: Anzahl der Astronauten, ihre Namen und Raumfahrzeuge.
**Hausaufgabe**:
- Finden Sie einen interessanten Echtzeitdatensatz (z.B. Wetter, Aktienkurse, Erdbeben).
- Abrufen und Parsen der Daten mit dem Raspberry Pi Pico W.
- Anzeigen oder Verwenden der Daten auf sinnvolle Weise (z.B. sensorlose Wetterstation).

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/5xXHo1xhc-g?si=kdpYgB6P7KoUU2Xa" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
