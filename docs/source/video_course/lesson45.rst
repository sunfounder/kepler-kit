.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

Lektion 45 : Berechnung der Höhe eines fallengelassenen Objekts im freien Fall
====================================================================================
Dieses Tutorial behandelt die Verwendung des MPU6050-Sensors mit dem Raspberry Pi Pico W zur Messung vertikaler Distanzen:

* **Einrichtung**:
   - Verbinden Sie den MPU6050 und OLED 1306 mit dem Raspberry Pi Pico W anhand des bereitgestellten Schaltplans. Stellen Sie sicher, dass alle Verbindungen sicher sind, um elektrische Störungen zu vermeiden.
* **Konzept**:
   - Messen Sie vertikale Distanzen, indem Sie den Sensor fallen lassen und die Zeit berechnen, die er zum Fallen benötigt (T_drop). Verwenden Sie die Freifallzeit, um die Höhe des Falls zu berechnen.
* **Gleichung**:
   - Die Höhe (H) wird mit der Formel berechnet: \( H = 16 \times (T_{drop})^2 \). Konvertieren Sie die Fallzeit von Millisekunden in Sekunden, bevor Sie die Formel anwenden.
* **Code-Implementierung**:
   - Richten Sie die MPU6050- und OLED 1306-Bibliotheken ein.
   - Messen Sie die Z-Achsen-Beschleunigung, um zu erkennen, wann der Sensor im freien Fall ist (0G).
   - Starten Sie einen Timer, wenn der Sensor fallen gelassen wird, und stoppen Sie ihn, wenn er den Boden erreicht.
   - Anzeigen der berechneten Höhe und Fallzeit auf dem OLED.
* **Praktische Demonstration**:
   - Testen Sie das Setup, indem Sie den Sensor aus bekannten Höhen fallen lassen und die Genauigkeit der Messungen überprüfen. Passen Sie das Setup nach Bedarf an, um die Präzision zu verbessern.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/xpHDAcdrTF0?si=NdmV4J5G6DhJ4f6M" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

