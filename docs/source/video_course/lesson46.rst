.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

Lektion 46 : Bau eines Zwei-Achsen-Neigungsmessers mit Display unter Verwendung des MPU6050
==================================================================================================
Dieses Tutorial behandelt die Verwendung des MPU6050-Sensors mit dem Raspberry Pi Pico W zur Erstellung eines Zwei-Achsen-Neigungsmessers:

* **Einrichtung**:
   - Verbinden Sie den MPU6050 und OLED 1306 mit dem Raspberry Pi Pico W anhand des bereitgestellten Schaltplans. Stellen Sie sicher, dass alle Verbindungen sicher sind, um elektrische Störungen zu vermeiden.
* **Konzept**:
   - Messen Sie die Neigung des Sensors mithilfe der Beschleunigungsdaten des MPU6050, um die Winkel für Pitch und Roll zu berechnen. Verwenden Sie diese Winkel, um eine visuelle Darstellung einer Wasserwaage auf dem OLED-Display zu erstellen.
* **Gleichung**:
   - Berechnen Sie die Pitch- und Roll-Winkel mit den folgenden Formeln:
     - Pitch: \(\text{Pitch} = \arctan\left(\frac{\text{Y-Beschleunigung}}{\text{Z-Beschleunigung}}\right)\)
     - Roll: \(\text{Roll} = \arctan\left(\frac{\text{X-Beschleunigung}}{\text{Z-Beschleunigung}}\right)\)
   - Konvertieren Sie diese Winkel von Radiant in Grad.
* **Code-Implementierung**:
   - Richten Sie die MPU6050- und OLED 1306-Bibliotheken ein.
   - Messen Sie die X-, Y- und Z-Beschleunigungswerte.
   - Berechnen Sie die Pitch- und Roll-Winkel in Grad.
   - Anzeigen der berechneten Pitch- und Roll-Winkel auf dem OLED zusammen mit einer visuellen Darstellung einer sich innerhalb eines Rechtecks bewegenden Blase, um die Neigung anzuzeigen.
* **Praktische Demonstration**:
   - Testen Sie das Setup, indem Sie den Sensor neigen und die Bewegung der Blase auf dem OLED-Display beobachten. Passen Sie die Empfindlichkeit der Blasenbewegung an, um den Neigungsmesser reaktionsschneller zu machen.
   - Stellen Sie sicher, dass die Messwerte genau sind und sich die Blase entsprechend den Neigungswinkeln gleichmäßig bewegt.
* **Erweiterte Überlegungen**:
   - Gehen Sie auf die Herausforderung ein, dass der Beschleunigungsmesser Beschleunigung und Verzögerung als Neigung interpretiert. Denken Sie über Strategien nach, um die Messwerte zu stabilisieren und falsche Neigungserkennungen durch Vibrationen oder Bewegungen zu verhindern.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/wYv39RMwXvU?si=6gJoFFIa1HSdGIFt" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

