.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 18: Steuerung von LEDs mit Tastern in MicroPython
=============================================================================

Dieses Tutorial behandelt die Verwendung von Tastern zum Ein- und Ausschalten einer LED mit dem Raspberry Pi Pico W:

* **Einführung**: Die Lektion beginnt mit einer kurzen Einführung und einem Überblick über die Lektion, wobei der Fokus auf der Verwendung von Tastern zur Steuerung von LEDs auf dem Raspberry Pi Pico W liegt.
* **Lösungen der Hausaufgabe**: Bietet eine Lösung für die Hausaufgabe der vorherigen Lektion, die das Erstellen eines Umschalters für eine LED mit einem Taster beinhaltete.
* **Schaltungsaufbau**: Demonstriert die Verdrahtung eines Tasters an GPIO-Pin 14 und einer LED an GPIO-Pin 15 des Raspberry Pi Pico W. Beinhaltet das Verbinden des Tasters und der LED mit einer gemeinsamen Masse.
* **Logik des Umschalters**: Erklärt die Logik, die erforderlich ist, um den LED-Zustand bei jedem Drücken und Loslassen des Tasters umzuschalten. Führt die Konzepte von ``button state now``, ``button state old`` und ``LED state`` ein.
* **Code-Erklärung**: Initialisiert die GPIO-Pins für die LED und den Taster. Verwendet eine while-Schleife, um kontinuierlich den Tasterzustand zu lesen. Schaltet den LED-Zustand basierend auf den Drück- und Loslassaktionen des Tasters um. Beinhaltet Print-Anweisungen zum Debuggen und Überprüfen der Zustände.
* **Praktische Demonstration**: Bietet eine Schritt-für-Schritt-Demonstration des Codes, das Drücken des Tasters und die Beobachtung der Änderungen des LED-Zustands.
* **Hausaufgabe**: Beauftragt ein neues Projekt zur Verwendung mehrerer Taster zur Steuerung der Farben einer RGB-LED. Die Aufgabe besteht darin, ein Programm zu schreiben, bei dem das Drücken der roten, grünen oder blauen Taste die Farbe der RGB-LED entsprechend ändert.
* **Nächste Schritte**: Kündigt an, dass zukünftige Lektionen die weitere Erkundung der Verwendung von Tastern und LEDs fortsetzen werden, wobei der Schwerpunkt auf der Integration dieser Komponenten in komplexere Projekte liegt.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/oztHWvrhKNk?si=I83VoID3AKSCUr9x" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
