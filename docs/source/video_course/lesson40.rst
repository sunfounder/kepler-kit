.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf aufkommende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

Lektion 40: Messung der Beschleunigung mit dem MPU6050 Six Axis IMU
=============================================================================
Dieses Tutorial behandelt die Verwendung des MPU6050-Beschleunigungssensors und Gyroskops mit dem Raspberry Pi Pico W:

* **Einführung**:
  - Einführung in die Verwendung des MPU6050-Sensors zur Messung von Beschleunigung und gyroskopischen Bewegungen.
  - Diskussion über die Bedeutung der MEMS (Microelectromechanical Systems)-Technologie bei der Herstellung dieser Sensoren.
* **Einrichten der Hardware**:
  - Erklärung der Hardwarekomponenten: MPU6050-Sensor und OLED-Display aus dem SunFounder Kepler Kit.
  - Detaillierte Verdrahtungsanweisungen zum Anschließen des MPU6050 und des OLED-Displays an den Raspberry Pi Pico W.
* **Verständnis des Sensors**:
  - Überblick darüber, wie der MPU6050 mithilfe der MEMS-Technologie Beschleunigung misst.
  - Erklärung der physikalischen Prinzipien hinter Beschleunigungsmessern, einschließlich des Hooke'schen Gesetzes und der Kapazitätsmessung.
  - Beschreibung der Fähigkeit des MPU6050, Beschleunigungen in den Achsen X, Y und Z zu messen.
* **Installation der erforderlichen Bibliotheken**:
  - Anweisungen zum Herunterladen und Installieren der notwendigen Bibliotheken aus dem SunFounder GitHub-Repository.
  - Schritte zum Importieren und Einrichten der Bibliotheken in der Thonny IDE.
* **Codierung und Testen**:
  - Schritt-für-Schritt-Anleitung zum Schreiben von MicroPython-Code zum Lesen von Beschleunigungswerten des MPU6050.
  - Erklärung der Initialisierung des I2C-Busses und der Erstellung des MPU6050-Objekts.
  - Codebeispiele zum Messen und Ausgeben der Beschleunigung in den Achsen X und Y.
  - Demonstration des Thonny-Plotters zur Visualisierung der Beschleunigungsmessungen in Echtzeit.
* **Hausaufgabe**:
  - Aufgabe zur Messung der Beschleunigung in der Z-Achse und zur Vorhersage ihres Wertes, wenn der Sensor stationär ist.
  - Anweisungen zum Vergleichen des vorhergesagten Wertes mit der tatsächlichen Messung und zur Analyse von Abweichungen.
* **Fazit**:
  - Zusammenfassung der Lektion und Vorschau auf zukünftige Lektionen, die sich auf praktische Anwendungen des MPU6050-Sensors konzentrieren.
  - Aufforderung, Ergebnisse zu teilen und sich mit der Community für weiteres Lernen auszutauschen.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/1eLOxVcG-8c?si=SSJqXad82K4QE4WL" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

