.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 34: Konvertierung von HSV zu RGB in Micropython
=============================================================================

Dieses Tutorial behandelt die Umwandlung von HSV- (Farbton, Sättigung, Helligkeit) in RGB-Werte (Rot, Grün, Blau) und deren Anzeige auf einer RGB-LED mit dem Raspberry Pi Pico W:

* **Einführung in das HSV-Farbrad**:
  - Erklärung des HSV-Farbrads und seiner Bedeutung für die Darstellung von weichen Farbverläufen.
  - Überblick darüber, wie das HSV-Farbrad zur visuellen Darstellung von Temperaturdaten verwendet werden kann.
* **Projekteinrichtung und Ziel**:
  - Rückblick auf das Wetterstationsprojekt, das Wetterdaten abruft und auf einem OLED-Bildschirm anzeigt.
  - Einführung des Ziels, eine visuelle Darstellung der Temperatur mit einer RGB-LED hinzuzufügen.
* **Verständnis der Umwandlung von HSV zu RGB**:
  - Aufschlüsselung des HSV-Farbrads in eine mathematische Darstellung zur Umwandlung.
  - Erklärung der sechs Zonen im Farbrad und der jeweiligen RGB-Werte und Steigungen.
* **Algorithmusentwicklung**:
  - Schrittweise Erstellung einer Funktion zur Umwandlung von HSV-Winkeln in RGB-Werte.
  - Erklärung des Aufbaus der RGB-LED-Schaltung mit PWM-Steuerung am Raspberry Pi Pico W.
* **Code-Implementierung**:
  - Detaillierte Anleitung zur Einrichtung von PWM für die RGB-LED und zur Durchführung der HSV-zu-RGB-Umwandlung in Python.
  - Erstellung einer Bibliotheksfunktion für die Umwandlung zur Vereinfachung des Hauptprogramms.
* **Praktische Demonstration**:
  - Demonstration des Codes in Aktion, bei der die RGB-LED gemäß dem HSV-Farbrad die Farben wechselt.
  - Aufgabe, die RGB-LED in das Wetterstationsprojekt zu integrieren, um Temperaturdaten visuell anzuzeigen.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/gg_hYPiCn_U?si=V32plkV0jGdV-4qV" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
