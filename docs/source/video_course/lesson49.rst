.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 49 : Verbesserung der IMU-Leistung mit einem Komplementärfilter
=============================================================================
Dieses Tutorial behandelt die Verbesserung der Neigungsmessgenauigkeit mit dem MPU6050-Sensor und dem Raspberry Pi Pico W:

* **Einrichtung**:
   - Verbinden Sie den MPU6050 mit dem Raspberry Pi Pico W gemäß dem bereitgestellten Schaltplan.
* **Herausforderungen**:
   - Beschleunigungsmesser allein sind schnell und genau, aber aufgrund von Vibrationen und Beschleunigungen rauschbehaftet.
   - Gyroskope allein sind schnell und rauschen wenig, aber sie driften im Laufe der Zeit.
* **Lösung**:
   - Kombinieren Sie Daten von Beschleunigungssensor und Gyroskop mithilfe eines Komplementärfilters, um das Beste aus beiden Sensoren herauszuholen.
   - Verwenden Sie einen Tiefpassfilter für die Beschleunigungsdaten, um das Rauschen zu reduzieren.
   - Nutzen Sie die Gyroskopdaten für kurzfristige Genauigkeit und die Beschleunigungsdaten für langfristige Stabilität.
* **Implementierung**:
   - Berechnen Sie Roll- und Nickwinkel sowohl aus den Beschleunigungsmesser- als auch aus den Gyroskopdaten.
   - Mischen Sie diese Werte mit dem Komplementärfilter, um genaue, schnelle und rauschfreie Messungen zu erzielen.
* **Ergebnisse**:
   - Der Komplementärfilter liefert genaue und reaktionsschnelle Neigungsmessungen mit minimalem Rauschen und Drift.
* **Hausaufgabe**:
   - Implementieren Sie die beschriebene Methode, um stabile Neigungsmessungen zu erzielen.
   - Erkunden Sie Möglichkeiten, verbleibende stationäre Fehler in den Messungen zu eliminieren.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/CFuEokTJn5s?si=ploRdiueh3f4mQBL" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

