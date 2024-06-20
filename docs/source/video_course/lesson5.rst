.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 5: Analoge Spannungen mit einem Potentiometer messen
=================================================================

Dieses Tutorial behandelt das Messen analoger Spannungen mit dem SunFounder Kepler Kit für den Raspberry Pi Pico W:

* **Messen von analogen Spannungen**: Erklärt die Bedeutung des Messens analoger Spannungen für verschiedene Sensoreingänge und Benutzereingaben, wie z.B. Potentiometer, zur Steuerung von Lautstärke oder Helligkeit.
* **Schaltplan und Aufbau**: Bietet eine detaillierte Erklärung der Funktionsweise des Potentiometers und wie man es an den Pico W anschließt. Beschreibt das Einrichten von Masse- und 3,3V-Schienen und das Anschließen des mittleren Pins des Potentiometers an den GPIO-Pin 28.
* **Code-Erklärung**: Beschreibt das Schreiben von Python-Code zum Lesen analoger Spannungen. Behandelt das Importieren der notwendigen Bibliotheken, das Einrichten der GPIO-Pins, das Erstellen eines Objekts für das Potentiometer und die Verwendung einer while-Schleife zum kontinuierlichen Lesen und Ausgeben der Spannungswerte.
* **Mathematische Umrechnung**: Lehrt, wie man die rohen ADC-Werte (0 bis 65535) in tatsächliche Spannungswerte (0 bis 3,3V) mittels linearer Gleichungen umrechnet. Demonstriert den Prozess der Ableitung der Geradengleichung aus zwei bekannten Punkten und deren Anwendung im Code.
* **Praktische Demonstration**: Zeigt den Code in Aktion, liest und wandelt die Potentiometerwerte in Spannung um und zeigt diese an. Diskutiert die Genauigkeit und die erwarteten Ergebnisse beim Einstellen des Potentiometers.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/ODWwErH_iGA?si=EzLxy17TO462G6_r" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
