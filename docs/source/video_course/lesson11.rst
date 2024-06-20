.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 11: Verständnis und Steuerung einer RGB-LED in MicroPython
==========================================================================

Dieses Tutorial behandelt die Steuerung einer RGB-LED mit dem SunFounder Kepler Kit und dem Raspberry Pi Pico W:

* **Steuerung der RGB-LED**: Erklärt die Steuerung der RGB-LED-Farben mittels PWM (Pulsweitenmodulation). Diskutiert den Aufbau der RGB-LED, die aus drei LEDs (rot, grün und blau) mit einer gemeinsamen Masse besteht. Betont die Wichtigkeit der Verwendung separater Strombegrenzungswiderstände für jeden Farbkanal, um Übersprechen zu verhindern.
* **Schaltplan und Aufbau**: Bietet ein detailliertes Schaltbild zum Anschließen der RGB-LED und der erforderlichen Widerstände an den Raspberry Pi Pico W. Demonstriert den physischen Aufbau auf einem Breadboard, einschließlich der Verbindungen für die roten, grünen und blauen Kanäle zu den GPIO-Pins 13, 14 und 15.
* **Code-Erklärung**: Beschreibt den Code zum Einrichten von PWM an jedem GPIO-Pin und zur Steuerung der Helligkeit jedes Farbkanals. Behandelt die Einrichtung der PWM-Frequenz, des Tastverhältnisses und die Initialisierung der GPIO-Pins für die roten, grünen und blauen Kanäle.
* **Praktische Demonstration**: Zeigt, wie man den Code ausführt, um die Farbe der RGB-LED zu ändern. Demonstriert das Ein- und Ausschalten einzelner Farbkanäle sowie das Anpassen der Helligkeitsstufen.
* **Hausaufgabe**: Fordert die Benutzer auf, ein Programm zu erstellen, das den Benutzer nach einer Farbe (rot, grün, blau, cyan, magenta, gelb, orange oder weiß) fragt und die RGB-LED anpasst, um die angegebene Farbe anzuzeigen. Ermutigt die Benutzer, PWM-Werte zu mischen und anzupassen, um eine genaue Farbdarstellung zu erreichen.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/MCo5nXAKyUU?si=VauJgWRltVnQpwz-" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
