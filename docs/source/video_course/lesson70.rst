.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 70 : Beispiel für das saubere Beenden eines Dual-Core-Programms in MicroPython
================================================================================================

Dieses Tutorial behandelt die Verwendung von Threads zur Steuerung eines Servos und eines Tasters mit dem Raspberry Pi Pico W:

* **Verdrahtungsaufbau**:

  - Schließen Sie das Steuerkabel des Servos an GPIO-Pin 17, das Stromkabel an physikalischen Pin 40 und das Erdungskabel an physikalischen Pin 38 an.
  - Schließen Sie einen Taster an GPIO-Pin 16 und Masse an.

* **Code-Implementierung**:

  - Importieren Sie die notwendigen Bibliotheken (``machine``, ``time``, ``_thread``, ``Servo``).
  - Richten Sie die Pins für den Taster und den Servo ein.
  - Implementieren Sie einen Umschalter für den Taster, um die Bewegung des Servos zu steuern.
  - Definieren Sie eine Hauptschleife, um Tastendrücke zu erkennen und den Servo zwischen 0 und 180 Grad zu toggeln.
  - Verwenden Sie Threads, um die Servobewegung auf einem separaten Kern zu behandeln, damit das Programm sauber beendet werden kann.

* **Hausaufgabe**:

  - Modifizieren Sie das Programm, um sicherzustellen, dass es sauber beendet wird, auch wenn es unterbrochen wird, während der Servo sich bewegt.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/UHbboCxIOYE?si=eDDi-2mYO0LSWSLJ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

