.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

lesson 74 : Erstellen einer MicroPython-Klasse zur Steuerung einer RGB-LED
===================================================================================

Dieses Tutorial behandelt die Erstellung einer MicroPython-Bibliothek zur Steuerung einer RGB-LED mit dem Raspberry Pi Pico W:

* **Verdrahtung**: 
  - Verbinden Sie die RGB-LED mit dem Raspberry Pi Pico W:
    - R-Anschluss über einen 330 Ohm Widerstand mit GPIO-Pin 14.
    - G-Anschluss mit GPIO-Pin 13.
    - B-Anschluss über einen 330 Ohm Widerstand mit GPIO-Pin 12.
    - Masse-Anschluss mit der Masse-Schiene.

* **Code-Implementierung**: 
  - **Bibliothek erstellen**: 
    - Definieren Sie eine Klasse `RGB_LED` in einer MicroPython-Bibliothek zur Steuerung der RGB-LED.
    - Fügen Sie ein Dictionary für Farbwerte innerhalb der Klasse hinzu.
    - Erstellen Sie Methoden zur Initialisierung der LED-Pins und zum Einstellen der Farben mittels PWM.
  - **Bibliotheken importieren**: 
    - Importieren Sie die notwendigen Bibliotheken (`machine`, `time`).
    - Richten Sie PWM für die RGB-LED-Pins innerhalb der Klassenmethoden ein.
  - **Hauptprogramm**: 
    - Importieren Sie die benutzerdefinierte Bibliothek und erstellen Sie ein Objekt für die RGB-LED.
    - Verwenden Sie eine while-Schleife, um den Benutzer kontinuierlich aufzufordern, eine gewünschte Farbe einzugeben.
    - Validieren Sie die Eingabe und stellen Sie die LED-Farbe entsprechend ein.
    - Implementieren Sie eine Fehlerbehandlung für ungültige Eingaben und eine saubere Beenden-Funktionalität mittels Keyboard-Interrupt.
  - **Hausaufgabe**: 
    - Erweitern Sie das Programm, indem Sie der MicroPython-Bibliothek weitere Funktionen wie zusätzliche Farbeinstellungen oder Muster hinzufügen, und stellen Sie sicher, dass das Hauptprogramm einfach und übersichtlich bleibt, indem die Bibliothek effektiv genutzt wird.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/tw-mXURNEUc?si=Ja75F1-I6MYwJgEh" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

