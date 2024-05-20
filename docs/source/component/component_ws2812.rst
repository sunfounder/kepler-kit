.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_ws2812:

WS2812 RGB 8-LED-Streifen
==========================

|img_ws2812|

Der WS2812 RGB 8-LED-Streifen besteht aus 8 RGB-LEDs und lässt sich mit nur einem Pin steuern. Jede RGB-LED enthält einen WS2812-Chip und kann individuell angesteuert werden. Der Streifen ermöglicht eine Helligkeitsanzeige mit 256 Stufen und eine echte Farbanzeige mit 16.777.216 Farben. Er verfügt zudem über eine intelligente digitale Schnittstelle mit Datenhalte- und Signalformungsschaltung, um die Farbkonsistenz der Pixel zu gewährleisten.

Der Streifen ist flexibel, kann nach Belieben verlängert, gebogen und geschnitten werden. Die Rückseite ist mit einem Klebeband versehen, sodass der Streifen auch auf unebenen Flächen angebracht und in beengten Räumen installiert werden kann.

**Funktionen**

* Betriebsspannung: DC5V
* IC: Ein IC steuert eine RGB-LED
* Verbrauch: 0,3 W pro LED
* Arbeitstemperatur: -15 bis 50 Grad Celsius
* Farbe: Vollfarb-RGB
* RGB-Typ: 5050RGB (Integrierter IC WS2812B)
* Streifendicke: 2 mm
* Jede LED ist einzeln steuerbar

**Einführung in WS2812B**

* `WS2812B Datenblatt <https://cdn-shop.adafruit.com/datasheets/WS2812B.pdf>`_

WS2812B ist eine intelligent steuerbare LED-Lichtquelle, bei der Schaltkreis und RGB-Chip in einem 5050-Gehäuse integriert sind. Es enthält eine intelligente digitale Schnittstelle mit Datenhalteschaltung und Signalformungsverstärkung. Zudem ist ein präziser interner Oszillator sowie eine mit 12V programmierbare Konstantstromsteuerung enthalten, die für eine gleichbleibende Farbqualität der Pixel sorgt.

Das Datenübertragungsprotokoll verwendet den Einzel-NZR-Kommunikationsmodus. Nach dem Einschalten der Pixel empfängt der DIN-Port Daten vom Controller. Das erste Pixel sammelt die ersten 24 Bit Daten und sendet sie an den internen Datenlatch. Die restlichen Daten werden durch die interne Signalformungs- und Verstärkungsschaltung an das nächste kaskadierende Pixel über den DO-Port weitergeleitet.

Durch die niedrige Betriebsspannung ist die LED umweltfreundlich und energiesparend. Sie bietet hohe Helligkeit, einen großen Streuwinkel, gute Konsistenz, geringen Stromverbrauch und eine lange Lebensdauer. Die Integration des Steuerchips in die LED vereinfacht die Schaltung und erleichtert die Installation.

.. Beispiel
.. -------------------

.. :ref:`RGB LED-Streifen`

**Beispiel**

* :ref:`py_neopixel` (Für MicroPython-Nutzer)
* :ref:`py_music_player` (Für MicroPython-Nutzer)
* :ref:`ar_neopixel` (Für Arduino-Nutzer)
* :ref:`per_flowing_leds` (Für Piper Make-Nutzer)
