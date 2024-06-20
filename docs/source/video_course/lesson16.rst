.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 16: Farbsequenz in RGB-LED mit MicroPython
=============================================================================

Dieses Tutorial behandelt die Verwendung von For-Schleifen in MicroPython mit dem Raspberry Pi Pico W zur Steuerung einer RGB-LED:

* **Einführung**: Die Lektion beginnt mit einer kurzen Einführung und einem Überblick über die Lektion, wobei der Fokus auf der Verwendung von For-Schleifen und PWM (Pulsweitenmodulation) zur Steuerung der Helligkeit und Farbe einer RGB-LED liegt.
* **Schaltungsaufbau**: Demonstriert die Verdrahtung der RGB-LED mit dem Raspberry Pi Pico W, wobei die GPIO-Pins 13, 14 und 15 für die roten, grünen und blauen Kanäle verwendet werden. Betont die Wichtigkeit der Verwendung von 330-Ohm-Strombegrenzungswiderständen.
* **PWM-Einrichtung**: Erklärt die Einrichtung der PWM-Kanäle für jede LED-Farbe und legt eine Frequenz von 1000 Hz fest, um flimmerfreie Übergänge zu gewährleisten.
* **Farbreihenfolge-Eingabe**: Zeigt, wie man den Benutzer nach einer Farbreihenfolge fragt und die Eingabe erfasst. Verwendet eine For-Schleife, um die vom Benutzer definierten Farben in einem Array zu speichern und stellt sicher, dass die Eingabe zur Konsistenz in Kleinbuchstaben umgewandelt wird.
* **Farbensteuerungslogik**: Detailliert die Logik zur Einstellung der Helligkeit jeder LED-Farbe basierend auf der Benutzereingabe. Implementiert If-Anweisungen zur Zuweisung von PWM-Werten zur Erstellung verschiedener Farben, einschließlich Rot, Grün, Blau, Cyan, Magenta, Gelb, Orange und Aus.
* **Kontinuierliche Schleife zur Farbanzeige**: Verwendet eine while-true-Schleife, um kontinuierlich durch die vom Benutzer definierte Farbreihenfolge zu wechseln. Fügt sleep-Anweisungen hinzu, um die Dauer der Anzeige jeder Farbe zu steuern.
* **Praktische Demonstration**: Bietet eine Schritt-für-Schritt-Demonstration des Codes, der Eingabe einer Farbreihenfolge und der Beobachtung der RGB-LED, die die Farben in der angegebenen Reihenfolge anzeigt.
* **Nächste Schritte**: Kündigt an, dass die nächste Lektion die Verwendung von Drucktasten mit dem Raspberry Pi Pico W zur Erfassung digitaler Eingaben behandeln wird, um die Lernphase der Ein- und Ausgabemethoden abzuschließen, bevor es zu fortgeschritteneren Komponenten übergeht.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/VivNlgYg3wY?si=ECUsRAWanIAShyxk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
