.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 65 : Eine Servoklasse in MicroPython erstellen
===================================================================================

Dieses Tutorial behandelt die Erstellung einer Servoklasse mithilfe der objektorientierten Programmierung (OOP) mit dem Raspberry Pi Pico W:

* **Verdrahtungsaufbau**:
  - Verbinden Sie das rote Kabel des Servos mit dem physischen Pin 40 (3.3V), das braune Kabel mit Pin 38 (Masse) und das orangefarbene Steuerkabel mit GPIO-Pin 17.
* **Klasse und Methoden**:
  - Definieren Sie eine ``Servo``-Klasse zur Verwaltung von Servo-Objekten.
  - Initialisieren Sie den Servo mit der ``__init__``-Methode und richten Sie den PWM-Pin ein.
  - Implementieren Sie eine ``pos``-Methode zur Steuerung der Servoposition.
* **Code-Implementierung**:
  - Importieren Sie die notwendigen Bibliotheken (``machine`` und ``time``).
  - Erstellen Sie die ``Servo``-Klasse mit den Methoden ``__init__`` und ``pos``.
  - Instanziieren Sie ein Servo-Objekt und steuern Sie dessen Position mit der ``pos``-Methode.
* **Hausaufgabe**:
  - Überprüfen Sie Lektion 36 für Details zur Arbeit mit Servos. Erstellen Sie eine Servoklasse, die eine einfache Steuerung der Servoposition durch das Einstellen von Winkeln ermöglicht. Implementieren Sie eine Methode, um den Servo basierend auf Benutzereingaben zu bewegen.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/OI4MzX7zqGc?si=ReJ76mhOZqUdnL9h" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

