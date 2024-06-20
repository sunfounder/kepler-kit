.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

lesson 73 : Steuerung einer RGB-LED mit einem Dictionary in MicroPython
===================================================================================

Dieses Tutorial behandelt die Steuerung einer RGB-LED mit dem Raspberry Pi Pico W unter Verwendung von Dictionaries:

* **Verdrahtung**:
  - Verbinden Sie die RGB-LED mit dem Raspberry Pi Pico W:
    - R-Anschluss über einen 330 Ohm Widerstand mit GPIO-Pin 14.
    - G-Anschluss mit GPIO-Pin 13.
    - B-Anschluss über einen 330 Ohm Widerstand mit GPIO-Pin 12.
    - Masse-Anschluss mit der Masse-Schiene.
* **Code-Implementierung**:
  - **Erstellen eines Dictionaries**:
    - Definieren Sie ein Dictionary mit Farbnamen als Schlüssel und den entsprechenden RGB-Werten als Listen.
  - **Bibliotheken importieren**:
    - Importieren Sie die notwendigen Bibliotheken (`machine`, `time`).
    - Richten Sie PWM für die RGB-LED-Pins ein.
  - **Hauptprogrammschleife**:
    - Fordern Sie den Benutzer kontinuierlich auf, eine gewünschte Farbe einzugeben.
    - Konvertieren Sie die Eingabe in Kleinbuchstaben und prüfen Sie, ob es sich um eine gültige Farbe handelt.
    - Wenn gültig, passen Sie die LED-Farben mithilfe von PWM-Duty-Cycles basierend auf den Dictionary-Werten an.
    - Implementieren Sie eine Fehlerbehandlung für ungültige Eingaben.
  - **Funktion zum Einstellen der Farbe**:
    - Definieren Sie eine Funktion `make_color`, die die gewünschte Farbe annimmt und die RGB-LED entsprechend mit PWM einstellt.
   
* **Hausaufgabe**:
   - Erweitern Sie das Programm, indem Sie die Funktion `make_color` in eine Bibliothek auslagern und sie in das Hauptprogramm importieren.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/1CHcjlaBvGY?si=feXCiEMKRkdsLx4y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

