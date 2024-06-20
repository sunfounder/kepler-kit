.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 33: Anzeige des HSV-Farbrads auf einer RGB-LED
=============================================================================

Dieses Tutorial behandelt die Anzeige des HSV (Farbton, Sättigung, Helligkeit) Farbrads auf einer RGB-LED mit dem Raspberry Pi Pico W:

* **Einführung in das HSV-Farbrad**:
  - Einführung in das Konzept der HSV-Farbdarstellung und deren Bedeutung bei der Visualisierung von Temperaturdaten.
  - Erklärung des HSV-Farbrads und wie verschiedene Winkel unterschiedliche Farben darstellen.
* **Projekteinrichtung und Ziel**:
  - Rückblick auf die vorherige Lektion, in der eine fernsteuerbare Wetterstation ohne Sensoren mit dem Raspberry Pi Pico W und einem OLED-Display gebaut wurde.
  - Einführung des neuen Ziels, eine visuelle Darstellung der Temperatur mit einer RGB-LED anzuzeigen.
* **Verständnis der Umwandlung von HSV zu RGB**:
  - Detaillierte Erklärung des HSV-Farbrads, mit Fokus auf Winkeln und den entsprechenden Farben.
  - Erklärung der mathematischen Umwandlung von HSV- zu RGB-Werten.
* **Algorithmusentwicklung**:
  - Schrittweise Aufschlüsselung, wie HSV-Winkel in RGB-Werte umgewandelt werden.
  - Erklärung, wie Temperaturwerte bestimmten Winkeln auf dem HSV-Farbrad zugeordnet werden.
  - Praktische Anwendung dieses Algorithmus auf die RGB-LED, um Temperaturdaten anzuzeigen.
* **Hausaufgabe**:
  - Aufgabe, eine Funktion zu schreiben, die einen Winkel vom HSV-Farbrad in RGB-Werte umwandelt.
  - Ermutigung zur Nutzung der RGB-LED zur visuellen Darstellung von Wetterbedingungen wie Temperatur und Windgeschwindigkeit.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/MJJJ9o0GY8I?si=KzKQ5lo5kXp38hZ3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
