.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 26: Zeichnen eines Kreises auf dem OLED 1306 Display
=============================================================================

Dieses Tutorial behandelt das Zeichnen von Formen auf einem OLED-Display mit dem Raspberry Pi Pico W:

* **Einführung**:
  - Hervorhebung des Ziels: einen Kreis auf einem OLED-Display mit dem Raspberry Pi Pico W zeichnen.
* **Rückblick und Einrichtung**:
  - Rückblick auf die vorherige Lektion zur Verwendung des OLED-1306-Displays und zur Einrichtung der SSD1306-Bibliothek.
  - Diskussion über die Bedeutung mathematischer Funktionen zum Zeichnen von Formen auf dem OLED-Display.
* **Zeichnen eines Kreises**:
  - Erklärung der Mathematik hinter dem Zeichnen eines Kreises mithilfe trigonometrischer Funktionen: \( x = r \cos(\theta) \) und \( y = r \sin(\theta) \).
  - Umrechnung von Grad in Bogenmaß zur Verwendung in Programmiersprachen.
  - Erklärung, wie der Kreis durch Anpassung der x- und y-Koordinaten auf dem OLED-Display zentriert wird.
  - Bereitstellung eines schrittweisen Codebeispiels zum Zeichnen eines Kreises durch Iteration über 360 Grad und Berechnung der x- und y-Positionen.
* **Verbesserung des Kreiszeichnens**:
  - Demonstration, wie ein gefüllter Kreis durch Iteration über einen Bereich von Radien gezeichnet wird.
  - Erklärung, wie ein Teilkreis oder Bogen durch Anpassung des Winkelbereichs gezeichnet wird.
* **Praktische Demonstration**:
  - Ausführung des Codes zum Zeichnen eines Kreises und eines gefüllten Kreises auf dem OLED-Display.
  - Erklärung, wie die Zeichengeschwindigkeit optimiert wird, indem das Display erst nach Berechnung aller Punkte aktualisiert wird.
* **Hausaufgabe**:
  - Aufgabe: Erstellen Sie ein Programm, das eine "schwebende Kartoffelchip"-Form auf dem OLED-Display zeichnet.
  - Aufforderung an die Zuschauer, die Mathematik hinter der Form herauszufinden und ihre Hausaufgabe auf YouTube zu posten.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/VgCcBm_Ms3E?si=J175coTlAdw2EMZ_" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
