.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 13: Vom Benutzer festgelegte RGB-LED-Farben mit MicroPython
==========================================================================

Dieses Tutorial behandelt die Steuerung einer RGB-LED mit dem SunFounder Kepler Kit und dem Raspberry Pi Pico W:

* **Steuerung der RGB-LED**: Zeigt die Steuerung einer RGB-LED mittels PWM (Pulsweitenmodulation), um verschiedene Farben zu erzielen. Erklärt den Aufbau der RGB-LED mit ihren vier Anschlüssen für Rot, Grün, Blau und Masse.
* **Schaltplan und Aufbau**: Bietet ein detailliertes Schaltbild zum Anschließen der RGB-LED an den Raspberry Pi Pico W. Jeder Farbkanal (Rot, Grün, Blau) ist mit einem GPIO-Pin (13, 14, 15) verbunden, wobei jeder Kanal einen 220-Ohm-Widerstand zur Strombegrenzung verwendet.
* **Code-Erklärung**: Beschreibt den MicroPython-Code zum Einrichten von PWM an jedem GPIO-Pin und zur Steuerung der Helligkeit jedes Farbkanals. Enthält Code zum Einschalten bestimmter Farben (Rot, Grün, Blau, Cyan, Magenta, Gelb, Orange, Weiß) basierend auf Benutzereingaben.
* **Praktische Demonstration**: Zeigt, wie man den Code ausführt und die Farbe der RGB-LED ändert. Demonstriert den Prozess der Eingabe einer Farbe und beobachtet, wie sich die RGB-LED entsprechend ändert.
* **Hausaufgabe**: Fordert die Benutzer auf, das Projekt zu erweitern, indem sie drei Potentiometer anschließen, um die RGB-LED-Farben manuell zu steuern. Ermutigt die Benutzer, die Potentiometerwerte zu mischen und anzupassen, um jede gewünschte Farbe zu erzielen.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/FLMPjwXqXVw?si=laOuij3khzBg5Uac" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
