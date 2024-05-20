.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_dht11:

DHT11 Temperatur- und Feuchtigkeitssensor
===========================================

Der digitale Temperatur- und Feuchtigkeitssensor DHT11 ist ein Verbundsensor, der kalibrierte digitale Signalausgaben für Temperatur und Feuchtigkeit liefert.
Dank der Anwendung von speziellen digitalen Modulen und Sensortechnologie für Temperatur und Feuchtigkeit zeichnet sich das Produkt durch hohe Zuverlässigkeit und ausgezeichnete Langzeitstabilität aus.

Der Sensor enthält eine resistive Feuchtigkeitsmesskomponente und ein NTC-Temperaturmessgerät, die mit einem leistungsfähigen 8-Bit-Mikrocontroller verbunden sind.

.. Der Schaltplan des Temperatur- und Feuchtigkeitssensormoduls ist wie folgt dargestellt: |img_Hum-sch|

Zur Verfügung stehen nur drei Pins: VCC, GND und DATA. 
Der Kommunikationsprozess beginnt mit dem Senden von Startsignalen über die DATA-Leitung an DHT11. Daraufhin empfängt DHT11 die Signale und sendet ein Antwortsignal zurück.
Der Host empfängt das Antwortsignal und beginnt dann, 40-Bit-Temperatur- und Feuchtigkeitsdaten zu empfangen (8-Bit-Feuchtigkeitsganzzahl + 8-Bit-Feuchtigkeitsdezimal + 8-Bit-Temperaturganzzahl + 8-Bit-Temperaturdezimal + 8-Bit-Prüfsumme).

|img_Dht11|

**Funktionen**

    #. Messbereich für Feuchtigkeit: 20 - 90 %RH
    #. Messbereich für Temperatur: 0 - 60℃
    #. Ausgabe digitaler Signale für Temperatur und Feuchtigkeit
    #. Betriebsspannung: DC 5V; PCB-Größe: 2,0 x 2,0 cm
    #. Genauigkeit der Feuchtigkeitsmessung: ±5 %RH
    #. Genauigkeit der Temperaturmessung: ±2℃

* `DHT11 Datenblatt <http://wiki.sunfounder.cc/images/c/c7/DHT11_datasheet.pdf>`_

**Beispiel**

* :ref:`py_dht11` (Für MicroPython-Anwender)
* :ref:`ar_dht11` (Für Arduino-Anwender)
