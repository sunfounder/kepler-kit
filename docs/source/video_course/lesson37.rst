.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 37: Steuerung eines Servos mit einem Potentiometer in MicroPython
=============================================================================

Dieses Tutorial behandelt die Steuerung eines Servomotors mit einem Potentiometer und dem Raspberry Pi Pico W:

* **Servomotorsteuerung**:
  - Schließen Sie den SG90-Servomotor an den Raspberry Pi Pico W an.
  - Braunes Kabel an Masse, rotes Kabel an die Stromversorgung (5V), oranges Kabel an GPIO-Pin 15 für die Steuerung.
* **Verdrahtungsaufbau**:
  - Schließen Sie das Potentiometer an: Stromversorgung an 3,3V, Masse an die Masseschiene und Signal an GPIO-Pin 26.
* **Grundlagen der PWM**:
  - Verwenden Sie Pulsweitenmodulation (PWM) zur Steuerung der Servoposition.
  - Stellen Sie die PWM-Frequenz auf 50Hz für den Servo ein.
* **Code-Erklärung**:
  - Richten Sie PWM auf GPIO-Pin 15 ein.
  - Konvertieren Sie die Potentiometerwerte in Servowinkel.
  - Beispielcode, um den Servo basierend auf dem Potentiometereingang zu bewegen.
* **Praktische Demonstration**:
  - Führen Sie den Code aus, um den Servo mit dem Potentiometer zu steuern.
  - Vermeiden Sie es, den Servoarm manuell zu drehen, um Schäden zu vermeiden.
* **Anwendungsideen**:
  - Steuern Sie größere Servos mit einer externen Stromversorgung für fortgeschrittenere Projekte.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/iiJasGsLTrQ?si=f-avwQIJNypRuh4t" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
