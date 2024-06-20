.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 50 : Langfristige stationäre Fehler aus Sensordaten entfernen
=============================================================================
Dieses Tutorial behandelt die Verbesserung der Neigungsmessgenauigkeit mit dem MPU6050-Sensor und dem Raspberry Pi Pico W:

* **Einrichtung**:
   - Verbinden Sie den MPU6050 mit dem Raspberry Pi Pico W gemäß dem bereitgestellten Schaltplan.
* **Herausforderungen**:
   - Beschleunigungsmesser allein sind rauschbehaftet.
   - Gyroskope allein driften im Laufe der Zeit.
* **Lösung**:
   - Kombinieren Sie Beschleunigungs- und Gyroskopdaten mithilfe eines Komplementärfilters.
   - Verwenden Sie einen Tiefpassfilter für die Beschleunigungsdaten, um das Rauschen zu reduzieren.
   - Nutzen Sie die Gyroskopdaten für kurzfristige Genauigkeit.
   - Fügen Sie eine Fehlerkorrektur hinzu, um stationäre Fehler zu beheben.
* **Ergebnisse**:
   - Erzielen Sie genaue, schnelle und rauschfreie Neigungsmessungen.
* **Hausaufgabe**:
   - Implementieren Sie den Filter und die Fehlerkorrektur.
   - Erstellen Sie eine visuelle Anzeige der Neigung mit einem OLED-Bildschirm.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/VdTBBUKH43k?si=oJ64AlVvQejBBR2R" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

