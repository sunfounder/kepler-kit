.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 19: Steuerung einer RGB-LED mit Tastern in MicroPython
=============================================================================

Dieses Tutorial behandelt die Verwendung mehrerer Taster zur Steuerung der RGB-Kanäle einer LED auf dem Raspberry Pi Pico W:

* **Einführung**: Die Lektion beginnt mit einem Überblick über die Lektion, wobei der Fokus auf der Verwendung von drei Tastern zur Steuerung der roten, grünen und blauen Kanäle einer RGB-LED auf dem Raspberry Pi Pico W liegt.
* **Lösungen der Hausaufgabe**: Bietet eine Lösung für die Hausaufgabe der vorherigen Lektion, die das Erstellen von drei Umschaltern für eine RGB-LED mit Tastern beinhaltete.
* **Schaltungsaufbau**: Demonstriert die Verdrahtung von drei Tastern und einer RGB-LED mit dem Raspberry Pi Pico W. Jeder Taster ist mit einem GPIO-Pin verbunden, und die RGB-LED-Kanäle sind über Widerstände an separate GPIO-Pins angeschlossen. Die Masseleitung wird eingerichtet, um den Stromkreis zu vervollständigen.
* **Code-Erklärung**:
  - Initialisiert die GPIO-Pins für die RGB-LED und die Taster.
  - Erstellt Objekte für jeden LED-Kanal und Taster und setzt sie als Eingänge oder Ausgänge entsprechend den Anforderungen.
  - Definiert Variablen für die Tasterzustände und LED-Zustände.
  - Implementiert Logik zum Umschalten der LED-Kanäle basierend auf den Tasterdrücken und -freigaben.
  - Zeigt, wie der Code methodisch geschrieben und organisiert wird, um eine konsistente Variablenbenennung für Lesbarkeit und einfache Fehlersuche zu gewährleisten.
* **Praktische Demonstration**:
  - Bietet eine Schritt-für-Schritt-Demonstration des Codes, das Drücken der Taster und die Beobachtung der Änderungen in den RGB-LED-Kanälen.
  - Zeigt, wie die Tasterfunktionalität getestet und überprüft wird, dass jeder Taster seinen jeweiligen LED-Kanal korrekt umschaltet.
  - Diskutiert Debugging-Techniken, um Fehler im Code oder in der Schaltung zu identifizieren und zu beheben.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/3CiBd7sW5KE?si=I66ycByUwVMi8251" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
