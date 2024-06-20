.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 47 : Verbesserung der Sensordaten mit einem Tiefpassfilter
=============================================================================
Dieses Tutorial behandelt die Verwendung des MPU6050-Sensors mit dem Raspberry Pi Pico W zur Erstellung eines stabilen Zwei-Achsen-Neigungsmessers durch Implementierung eines Tiefpassfilters:

* **Einrichtung**:
   - Verbinden Sie den MPU6050 mit dem Raspberry Pi Pico W gemäß dem bereitgestellten Schaltplan.

* **Konzept**:
   - Messen Sie die Neigung mithilfe der Beschleunigungsdaten des MPU6050, um Pitch- und Roll-Winkel zu berechnen.
   - Beheben Sie Fehler, die durch die Interpretation von Beschleunigung als Neigung verursacht werden.

* **Tiefpassfilter**:
   - Implementieren Sie einen Tiefpassfilter, um Daten zu glätten und Rauschen zu reduzieren.
   - Gleichung: \(\text{new value} = \text{sensor confidence} \times \text{measurement} + (1 - \text{sensor confidence}) \times \text{old value}\)
   - Passen Sie den Konfidenzwert an, um das beste Gleichgewicht zwischen Reaktionsfähigkeit und Rauschunterdrückung zu finden.

* **Code**:
   - Richten Sie den MPU6050 ein, um X-, Y- und Z-Beschleunigung zu messen.
   - Berechnen und filtern Sie Pitch- und Roll-Winkel.
   - Zeigen Sie die gefilterten Werte an.

* **Hausaufgabe**:
   - Implementieren und testen Sie den Tiefpassfilter.
   - Experimentieren Sie mit verschiedenen Konfidenzwerten.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/3YqGIg4crEk?si=rwiDFcJ98nlj_Sg3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

