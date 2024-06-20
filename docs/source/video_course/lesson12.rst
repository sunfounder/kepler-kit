.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 12: Erstellen einer dimmbaren LED in MicroPython
==========================================================================

Dieses Tutorial behandelt die Steuerung der LED-Helligkeit mit einem Potentiometer und PWM (Pulsweitenmodulation) auf dem Raspberry Pi Pico W:

* **LED-Helligkeitssteuerung**: Erklärt die Steuerung der LED-Helligkeit mittels PWM. Diskutiert digitale Signale, Tastverhältnisse und wie unterschiedliche Tastverhältnisse die LED-Helligkeit steuern. Führt das Konzept der exponentiellen Skalierung ein, um die Helligkeitswahrnehmung für das menschliche Auge linearer zu gestalten.
* **Schaltplan und Aufbau**: Bietet ein detailliertes Schaltbild zum Anschließen eines Potentiometers und einer LED mit einem 220-Ohm-Widerstand an den Raspberry Pi Pico W. Demonstriert den physischen Aufbau auf einem Breadboard.
* **Code-Erklärung**: Beschreibt den Code zum Einrichten von PWM an einem GPIO-Pin, zum Lesen des Analogwerts von einem Potentiometer und zur Umwandlung in das entsprechende PWM-Tastverhältnis. Erklärt die Verwendung von Bibliotheken, PWM-Objekten und Frequenzeinstellungen.
* **Praktische Demonstration**: Zeigt, wie man das PWM-Signal mit einem Oszilloskop misst und visualisiert, und veranschaulicht, wie unterschiedliche Tastverhältnisse unterschiedlichen durchschnittlichen Spannungen entsprechen. Demonstriert den Effekt der exponentiellen Skalierung für sanftere Helligkeitsübergänge.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/yZkx-KWbATY?si=p85rQXYb6YGoEe9L" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
