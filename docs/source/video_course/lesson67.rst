.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 67 : Beide Kerne Ihres Pi Pico mit MicroPython verwenden
===================================================================================

Dieses Tutorial behandelt die Verwendung beider Kerne des Raspberry Pi Pico W:

* **Verdrahtungsaufbau**:
  - Schließen Sie eine grüne LED an GPIO-Pin 14 mit einem 330-Ohm-Widerstand an Masse an.
  - Schließen Sie eine rote LED an GPIO-Pin 15 mit einem 330-Ohm-Widerstand an Masse an.
* **Code-Implementierung**:
  - Importieren Sie die notwendigen Bibliotheken (`machine`, `time`, `_thread`).
  - Richten Sie die Pins für die LEDs ein.
  - Definieren Sie Parameter für die LED-Blinkzeiten.
  - Erstellen Sie Funktionen zur Steuerung des LED-Blinkens:
    - `other_core` für die rote LED auf dem zweiten Kern.
    - `green_blink` für die grüne LED auf dem Hauptkern.
  - Verwenden Sie `_thread.start_new_thread`, um `other_core` auf dem zweiten Kern auszuführen.
* **Hausaufgabe**:
  - Schließen Sie ein Servo an.
  - Steuern Sie das Servo und die LEDs:
    - Die rote LED blinkt, wenn sich das Servo rückwärts bewegt.
    - Die grüne LED blinkt, wenn sich das Servo vorwärts bewegt.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/mm1EoNqjd4c?si=RHZLX39PpGDbAFuM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

