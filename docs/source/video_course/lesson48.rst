.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 48 : Rotationsmessung mit dem Gyroskop des MPU6050
=============================================================================

Dieses Tutorial behandelt die Verwendung des MPU6050-Sensors mit dem Raspberry Pi Pico W zur Erstellung eines stabilen Neigungsmessers durch Kombination von Beschleunigungs- und Gyroskopdaten:

* **Einrichtung**:
   - Verbinden Sie den MPU6050 mit dem Raspberry Pi Pico W gemäß dem bereitgestellten Schaltplan.
* **Konzept**:
   - Messen Sie die Neigung mithilfe von Daten sowohl des Beschleunigungssensors als auch des Gyroskops.
   - Beheben Sie Fehler, die durch Rauschen der Beschleunigung und Drift des Gyroskops verursacht werden.
* **Tiefpassfilter**:
   - Glätten Sie die Beschleunigungsdaten, um das Rauschen zu reduzieren.
* **Integration des Gyroskops**:
   - Berechnen Sie die Neigungswinkel mithilfe der Rotationsgeschwindigkeit.
   - Aktualisieren Sie kontinuierlich die Pitch-, Roll- und Gierwinkel.
* **Datenkombination**:
   - Fusionieren Sie die Daten des Beschleunigungssensors und des Gyroskops, um Rauschen und Drift zu minimieren.
* **Hausaufgabe**:
   - Implementieren und optimieren Sie die beschriebene Methode zur stabilen Neigungsmessung.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/XZIJasvCB44?si=hx0Ulyd0pTnro8sd" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

