.. _cpn_mpr121:

MPR121 Modul
===========================

|img_mpr121|


* **3.3V**: Spannungsversorgung
* **IRQ**: Open-Collector-Interrupt-Ausgangspin, aktiv niedrig
* **SCL**: I2C-Takt
* **SDA**: I2C-Daten
* **ADD**: I2C-Adressauswahl-Eingangspin. Verbinden Sie den ADDR-Pin mit der VSS-, VDD-, SDA- oder SCL-Leitung. Die resultierenden I2C-Adressen sind jeweils 0x5A, 0x5B, 0x5C und 0x5D
* **GND**: Masse
* **0~11**: Elektrode 0~11, eine Berührungssensor-Elektrode. Üblicherweise können Elektroden einfache Metallstücke oder Drähte sein. Je nach Kabellänge oder Material der Unterlage kann jedoch die Auslösung des Sensors erschwert werden. Aus diesem Grund ermöglicht der MPR121 die Konfiguration der Auslöse- und Rücksetzkriterien für jede Elektrode.

**MPR121 ÜBERSICHT**

Der MPR121 ist die zweite Generation von kapazitiven Berührungssensoren nach der Einführung der MPR03x-Serie. Der MPR121 bietet erweiterte interne Intelligenz; zu den wichtigsten Neuerungen gehören eine erhöhte Anzahl von Elektroden, eine hardwarekonfigurierbare I2C-Adresse, ein erweitertes Filtersystem mit Entprellung und vollkommen unabhängige Elektroden mit integrierter Auto-Konfiguration. Zudem verfügt das Gerät über einen 13. simulierten Sensor-Kanal, der speziell für die Nahbereichserkennung über die multiplexten Sensoreingänge genutzt wird.

* `MPR121 Datenblatt <https://cdn-shop.adafruit.com/datasheets/MPR121.pdf>`_

**Funktionen**

* Niedriger Energieverbrauch
    • Betriebsspannung von 1,71 V bis 3,6 V
    • 29 μA Versorgungsstrom bei einem Abtastintervall von 16 ms
    • 3 μA Stromaufnahme im Stop-Modus
* 12 kapazitive Sensoreingänge
    • 8 Eingänge multifunktional als LED-Treiber und GPIO verwendbar
* Vollständige Berührungserkennung
    • Auto-Konfiguration für jeden Sensoreingang
    • Auto-Kalibrierung für jeden Sensoreingang
    • Berührungs-/Freigabeschwelle und Entprellung für die Berührungserkennung
* I2C-Schnittstelle mit Interrupt-Ausgang
* 3 mm x 3 mm x 0,65 mm 20-poliges QFN-Gehäuse
* Betriebstemperaturbereich von -40°C bis +85°C

**Beispiel**

* :ref:`py_mpr121` (Für MicroPython-Nutzer)
* :ref:`py_fruit_piano` (Für MicroPython-Nutzer)
* :ref:`ar_mpr121` (Für Arduino-Nutzer)
