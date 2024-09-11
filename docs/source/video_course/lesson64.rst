.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 64 : Objektorientiertes Programmierbeispiel in MicroPython mit LEDs
===================================================================================

Dieses Tutorial behandelt die objektorientierte Programmierung (OOP) mit dem Raspberry Pi Pico W und konzentriert sich auf die Steuerung von LEDs:

* **Verdrahtungsaufbau**:
  - Verbinden Sie eine rote LED mit GPIO-Pin 15 und eine grüne LED mit GPIO-Pin 14, jeweils mit 330-Ohm-Widerständen zur Masse.

* **Klasse und Methoden**:
  1. Definieren Sie eine ``LED``-Klasse zur Verwaltung von LED-Objekten.
  2. Initialisieren Sie die LED mit der ``__init__``-Methode und richten Sie den Pin ein.
  3. Implementieren Sie eine ``blink``-Methode zur Steuerung des Blinkens der LED.

* **Code-Implementierung**:
  1. Importieren Sie die notwendigen Bibliotheken (``machine`` und ``time``).
  2. Erstellen Sie die ``LED``-Klasse mit den Methoden ``__init__`` und ``blink``.
  3. Instanziieren Sie Objekte für die rote und grüne LED.
  4. Verwenden Sie eine Schleife, um die LEDs gemäß den angegebenen Parametern blinken zu lassen.

* **Hausaufgabe**:
  - Erstellen Sie eine Klasse für einen Servomotor, die eine einfache Steuerung seiner Position ermöglicht. Die Klasse sollte Methoden zur Initialisierung des Servos und zur Einstellung seines Winkels enthalten. Überprüfen Sie Lektion 36 für Details zur Arbeit mit Servomotoren in MicroPython.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/3wyCL9QK_uY?si=G0GXEHqdo2jQ_F-5" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

