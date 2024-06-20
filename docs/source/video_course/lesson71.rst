.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 71 : Aufgabe des Threads vor dem Beenden abschließen lassen
===================================================================================

Dieses Tutorial behandelt das saubere Beenden eines Multithread-Programms auf dem Raspberry Pi Pico W:

* **Verdrahtungsaufbau**:
  - Verbinden Sie das Steuerkabel des Servos mit GPIO-Pin 17, das Stromkabel mit physikalischem Pin 40 und das Erdungskabel mit physikalischem Pin 38.
  - Schließen Sie einen Taster an GPIO-Pin 16 und Masse an.
* **Code-Implementierung**:
  - Importieren Sie die notwendigen Bibliotheken (`machine`, `time`, `_thread`, `Servo`).
  - Richten Sie die Pins für den Taster und den Servo ein.
  - Implementieren Sie einen Umschalter für den Taster, um die Bewegung des Servos zu steuern.
  - Definieren Sie eine Hauptschleife, um Tastendrücke zu erkennen und den Servo zwischen 0 und 180 Grad zu toggeln.
  - Verwenden Sie Threads, um die Servobewegung auf einem separaten Kern zu behandeln und so ein sauberes Beenden des Programms zu ermöglichen.
* **Sauberes Beenden handhaben**:
  - Verwenden Sie eine globale `running`-Variable, um die Ausführung der Schleife zu steuern.
  - Implementieren Sie eine Sperre (lock), um sicherzustellen, dass immer nur ein Teil des Programms während kritischer Abschnitte läuft.
  - Warten Sie, bis die Servobewegung abgeschlossen ist, bevor Sie das Programm beenden.
* **Hausaufgabe**:
  - Modifizieren Sie das Programm, um zusätzliche Komponenten oder Sensoren zu integrieren und ein sauberes Beenden in allen Szenarien sicherzustellen.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/Xm3chr1-hkY?si=ITIUvlqKF6UdOsq2" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

