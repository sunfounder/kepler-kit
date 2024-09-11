.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 29: Einfaches Client-Server-Projekt zur Steuerung einer RGB-LED
=============================================================================

Dieses Tutorial behandelt die Einrichtung einer ferngesteuerten RGB-LED mithilfe eines Raspberry Pi Pico W und eines PCs über WLAN:

* **Einführung**: Das Ziel ist es, eine RGB-LED auf einem Raspberry Pi Pico W fernzusteuern, indem Wi-Fi verwendet wird.
* **Schaltplan und Einrichtung**: Verbinde die RGB-LED mit den GPIO-Pins 16, 17, 18 und das OLED mit den GPIO-Pins 2 (SDA) und 3 (SCL).
* **Serverseitige Einrichtung**: Bibliotheken importieren, GPIO-Pins initialisieren, mit Wi-Fi verbinden, einen UDP-Server erstellen und die IP-Adresse auf dem OLED anzeigen.
* **Clientseitige Einrichtung**: Erstelle einen UDP-Client auf dem PC, um Farbkommandos an den Server zu senden.
* **Praktische Demonstration**: Zeige das Ändern der RGB-LED-Farbe über Befehle, die vom PC gesendet werden, während das OLED die Befehle und die IP-Adresse anzeigt.
* **Endgültige Einrichtung und Test**: Betreibe den Raspberry Pi Pico W mit einer Batterie, speichere den Code als ``main.py`` und demonstriere den drahtlosen Betrieb.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/eZTETVkX-N8?si=TtZ6B4-Ljm75rhPB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
