.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 51 : Das ultimative Neigungsmessgerät mit dem MPU6050
=============================================================================
Dieses Tutorial behandelt die Erstellung eines präzisen Neigungsmessgeräts mit dem MPU6050-Sensor und dem Raspberry Pi Pico W:

* **Einrichtung**:
   - Verbinden Sie den MPU6050 und OLED 1306 mit dem Raspberry Pi Pico W gemäß dem bereitgestellten Schaltplan.
* **Herausforderungen**:
   - Rohdaten des Beschleunigungssensors sind rauschbehaftet.
   - Daten des Gyroskops driften im Laufe der Zeit.
* **Lösung**:
   - Kombinieren Sie Beschleunigungs- und Gyroskopdaten mithilfe eines Komplementärfilters, um genaue, schnelle und rauschfreie Neigungsmessungen zu erzielen.
   - Implementieren Sie eine Fehlerkorrektur, um stationäre Fehler zu beheben.
* **Implementierung**:
   - Initialisieren Sie den MPU6050 und OLED 1306.
   - Sammeln Sie Daten sowohl vom Beschleunigungssensor als auch vom Gyroskop.
   - Wenden Sie einen Komplementärfilter an, um kurzzeitige Gyroskopdaten mit langfristigen Beschleunigungsdaten zu kombinieren.
   - Fügen Sie eine Fehlerkorrektur hinzu, um Drift in den Messungen auszugleichen.
   - Zeigen Sie die Ergebnisse auf dem OLED-Bildschirm an, wobei sowohl qualitative (Libellenanzeige) als auch quantitative (Gradanzeige) Neigungsinformationen angezeigt werden.
* **Demonstration**:
   - Das Neigungsmessgerät wird getestet, um stabile und genaue Pitch- und Roll-Werte auch bei Vibrationen zu zeigen.
   - Das Gerät wird mit einem Batteriefach tragbar gemacht, sodass es ohne Kabel betrieben werden kann.
* **Zusätzliche Verbesserungen**:
   - Vorschläge beinhalten, das Gerät kabellos für die Fernüberwachung zu machen oder ein 3D-gedrucktes Gehäuse für die Portabilität zu entwerfen.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/afQyZl2hkd0?si=4Dg4Uvr5yVC4f60Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

