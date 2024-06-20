.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 66 : Erstellen Sie Ihre eigenen Bibliotheken in MicroPython
===================================================================================

Dieses Tutorial behandelt das Erstellen und Verwenden einer Servo-Bibliothek mit dem Raspberry Pi Pico W:

* **Verdrahtungsaufbau**:
  - Verbinden Sie das rote Kabel des Servos mit dem physischen Pin 40 (3.3V), das braune Kabel mit Pin 38 (Masse) und das orangefarbene Steuerkabel mit GPIO-Pin 17.
* **Klasse und Methoden**:
  - Definieren Sie eine `Servo`-Klasse zur Verwaltung von Servo-Objekten.
  - Initialisieren Sie den Servo mit der `__init__`-Methode und richten Sie den PWM-Pin ein.
  - Implementieren Sie eine `pos`-Methode zur Steuerung der Servoposition.
* **Bibliothekserstellung**:
  - Schreiben Sie den Code der `Servo`-Klasse und speichern Sie ihn als Bibliotheksdatei (`ServoLib.py`).
  - Erstellen Sie ein `lib`-Verzeichnis auf dem Raspberry Pi Pico W und speichern Sie die Bibliotheksdatei in diesem Verzeichnis.
* **Code-Implementierung**:
  - Importieren Sie die notwendigen Bibliotheken (`machine`, `time` und `ServoLib`).
  - Instanziieren Sie ein Servo-Objekt mit der `Servo`-Klasse aus der `ServoLib`-Bibliothek.
  - Steuern Sie die Position des Servos, indem Sie die `pos`-Methode mit den gewünschten Winkeln aufrufen.
* **Hausaufgabe**:
  - Erstellen Sie eine ähnliche Bibliothek für eine andere Komponente, wie z.B. eine LED, um deren Verwendung in zukünftigen Projekten zu vereinfachen.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/lz_Gp-zDtKI?si=VHgvS20YVqfft8LY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

