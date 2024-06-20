.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 36: Steuerung eines Servos mit MicroPython
=============================================================================

Dieses Tutorial behandelt die Steuerung eines Servomotors mit dem Raspberry Pi Pico W:

* **Servomotorsteuerung**: 
  - Einführung in die Verwendung des SG90-Servomotors mit dem Raspberry Pi Pico W.
  - Erklärung der Anschlüsse des Servomotors: Braun (Masse), Rot (Stromversorgung), Orange (Steuerung).
  - Betonung, dass größere Servos nicht direkt vom Raspberry Pi Pico W mit Strom versorgt werden sollten, um mögliche Schäden zu vermeiden.
* **Schaltplan und Aufbau**:
  - Detaillierte Verdrahtungsanweisungen zum Anschluss des SG90-Servos an den Raspberry Pi Pico W.
  - Verwendung des GPIO-Pins 15 für die Steuerung und Erstellung einer Stromschiene von Pin 1 für die 5V-Versorgung.
* **Grundlagen der PWM**:
  - Erklärung der Pulsweitenmodulation (PWM) und ihrer Rolle bei der Steuerung der Servoposition.
  - Berechnung der Pulsweiten, die den verschiedenen Servo-Winkeln entsprechen (0,5 ms für 0 Grad, 2,5 ms für 180 Grad).
  - Einstellung der PWM-Frequenz auf 50 Hz, um den Anforderungen des Servos zu entsprechen.
* **Code-Erklärung**:
  - Schritt-für-Schritt-Coding-Tutorial zur Einrichtung von PWM auf GPIO-Pin 15.
  - Erstellung einer Funktion zur Umrechnung gewünschter Winkel in PWM-Duty-Cycle-Werte.
  - Beispielcode zur Steuerung des Servos durch Eingabe gewünschter Winkel.
* **Praktische Demonstration**:
  - Ausführung des Codes, um den Servo auf bestimmte Winkel zu bewegen.
  - Sicherstellung des sicheren Betriebs des Servos, indem eine manuelle Drehung des Servoarms vermieden wird.
* **Hausaufgabe**:
  - Aufgabe, ein Potentiometer in die Schaltung zu integrieren, um die Servoposition durch Einstellung des Potentiometers zu steuern.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/vAnd0AC6u1Q?si=0VAnHzQFnQlyDqI6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
