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

* **Einführung**:
  - Das Ziel ist, eine RGB-LED auf einem Raspberry Pi Pico W remote von einem PC über WLAN zu steuern.
* **Verdrahtungsdiagramm und Einrichtung**:
  - Die roten, grünen und blauen Kanäle der RGB-LED sind mit den GPIO-Pins 16, 17 und 18 verbunden.
  - Das OLED-Display ist über I2C mit den GPIO-Pins 2 (SDA) und 3 (SCL) verbunden.
* **Serverseitige Einrichtung (Raspberry Pi Pico W)**:
  - Importieren der Bibliotheken: `socket`, `time`, `network`, `machine`, `ssd1306`.
  - Initialisierung der GPIO-Pins für die RGB-LED und das OLED-Display.
  - Verbindung mit WLAN herstellen und eine IP-Adresse beziehen.
  - Erstellen eines UDP-Server-Sockets und Binden an die IP-Adresse und einen Port.
  - Anzeige der IP-Adresse und des Ports auf dem OLED-Bildschirm.
  - Lauschen auf eingehende Befehle, diese dekodieren und den Befehl sowie die Adresse des Absenders anzeigen.
* **Clientseitige Einrichtung (PC)**:
  - Importieren der `socket`-Bibliothek.
  - Definition der Serveradresse und des Ports.
  - Erstellen eines UDP-Client-Sockets.
  - Benutzerabfrage zur LED-Farbe, Kodierung des Befehls und Senden an den Server.
  - Warten auf und Ausdrucken der Antwort des Servers.
* **Praktische Demonstration**:
  - Demonstration des Sendens von Befehlen vom Client, um die RGB-LED-Farbe auf dem Server zu ändern.
  - OLED-Display zeigt die empfangenen Befehle und die IP-Adresse des Absenders an.
* **Endgültige Einrichtung und Testen**:
  - Trennen des Raspberry Pi Pico W vom USB und Betreiben mit einer Batterie.
  - Speichern des Codes als `main.py`, damit er beim Start automatisch ausgeführt wird.
  - Demonstration des vollständig kabellosen Betriebs durch Senden von Befehlen vom PC und Beobachten der Änderungen der RGB-LED und der OLED-Updates.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/eZTETVkX-N8?si=TtZ6B4-Ljm75rhPB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
