.. _cpn_pico_w:

Raspberry Pi Pico W
=======================================

|pico_w_side|

Mit dem Raspberry Pi Pico W bringt die erfolgreiche Raspberry Pi Pico-Produktreihe nun auch drahtlose Konnektivität ins Spiel. Basierend auf unserer RP2040-Siliziumplattform stehen Pico-Produkte für hohe Leistung, geringe Kosten und einfache Handhabung im Mikrocontroller-Bereich.

Der Raspberry Pi Pico W bietet eine 2,4 GHz 802.11 b/g/n WLAN-Unterstützung, eine integrierte Antenne und eine modulare Konformitätszertifizierung. Er kann sowohl im Station- als auch im Access-Point-Modus betrieben werden. Sowohl C- als auch MicroPython-Entwickler haben vollen Zugriff auf die Netzwerkfunktionalität.
Der Raspberry Pi Pico W kombiniert den RP2040 mit 2 MB Flash-Speicher und einem Spannungsversorgungschip, der Eingangsspannungen von 1,8 bis 5,5 V unterstützt. Er bietet 26 GPIO-Pins, von denen drei als analoge Eingänge fungieren können, auf Durchstecklöchern im 0,1-Zoll-Raster mit gegossenen Kanten. 
Der Raspberry Pi Pico W ist sowohl einzeln als auch in 480er-Spulen für die automatisierte Montage erhältlich.

Merkmale
--------------

* Abmessungen: 21 mm x 51 mm
* RP2040-Mikrocontroller-Chip, entwickelt von Raspberry Pi in Großbritannien
* Dual-Core Arm Cortex-M0+ Prozessor, flexible Taktung bis zu 133 MHz
* 264 kB integrierter SRAM
* 2 MB Onboard-QSPI-Flash
* 2,4 GHz 802.11n WLAN
* 26 multifunktionale GPIO-Pins, inklusive 3 analoger Eingänge
* 2 x UART, 2 x SPI, 2 x I2C, 16 x PWM-Kanäle
* 1 x USB 1.1 mit Host- und Device-Unterstützung
* 8 x programmierbare I/O (PIO) Zustandsmaschinen für benutzerdefinierte Peripheriegeräte
* Unterstützte Eingangsspannung 1,8-5,5 V DC
* Betriebstemperatur -20°C bis +70°C
* Lötfähiges Modul für direkte Montage auf Trägerplatinen
* Drag-and-drop-Programmierung über USB-Massenspeicher
* Energiesparmodi im Schlaf- und Ruhezustand
* Präzise On-Chip-Uhr
* Temperatursensor
* Beschleunigte Ganzzahl- und Gleitkomma-Bibliotheken auf dem Chip

Pico's Pins
------------

|pico_pin|

.. list-table::
    :widths: 3 5 10
    :header-rows: 1

    *   - Name
        - Beschreibung
        - Funktion
    *   - GP0-GP28
        - Allzweck-Ein-/Ausgabepins
        - Können als Ein- oder Ausgang fungieren und haben keine festgelegte Funktion.
    *   - GND
        - 0-Volt-Erde
        - Mehrere GND-Pins am Pico W erleichtern die Verdrahtung.
    *   - RUN
        - Aktiviert oder deaktiviert Ihren Pico
        - Starten und Stoppen Ihres Pico W von einem anderen Mikrocontroller aus.
    *   - GPxx_ADCx
        - Allzweck-Ein-/Ausgang oder analoger Eingang
        - Können sowohl als analoger als auch als digitaler Ein- oder Ausgang verwendet werden – jedoch nicht gleichzeitig.
    *   - ADC_VREF
        - Analog-Digital-Wandler (ADC) Spannungsreferenz
        - Ein spezieller Eingangspin, der eine Referenzspannung für analoge Eingänge festlegt.
    *   - AGND
        - Analog-Digital-Wandler (ADC) 0-Volt-Erde
        - Eine spezielle Erdverbindung zur Verwendung mit dem ADC_VREF-Pin.
    *   - 3V3(O)
        - 3,3-Volt-Stromversorgung
        - Eine 3,3-Volt-Stromquelle, dieselbe Spannung, bei der Ihr Pico W intern betrieben wird, generiert aus dem VSYS-Eingang.
    *   - 3V3(E)
        - Aktiviert oder deaktiviert die Stromversorgung
        - Schaltet die 3V3(O)-Stromversorgung ein oder aus und kann auch Ihren Pico W ausschalten.
    *   - VSYS
        - 2-5-Volt-Stromversorgung
        - Ein direkt mit der internen Stromversorgung Ihres Pico verbundener Pin, der nicht abgeschaltet werden kann, ohne den Pico W ebenfalls auszuschalten.
    *   - VBUS
        - 5-Volt-Stromversorgung
        - Eine 5-Volt-Stromquelle aus dem Micro-USB-Anschluss Ihres Pico, die zur Stromversorgung von Hardware dient, die mehr als 3,3 V benötigt.

Alles, was Sie für den Einstieg mit Ihrem Raspberry Pi Pico W benötigen, finden Sie `hier <https://www.raspberrypi.org/documentation/pico/getting-started/>`_

Oder klicken Sie auf die folgenden Links:

* `Raspberry Pi Pico W Produktübersicht <https://datasheets.raspberrypi.com/picow/pico-w-product-brief.pdf>`_
* `Raspberry Pi Pico W Datenblatt <https://datasheets.raspberrypi.com/picow/pico-w-datasheet.pdf>`_
* `Erste Schritte mit dem Raspberry Pi Pico: C/C++-Entwicklung <https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf>`_
* `Raspberry Pi Pico C/C++ SDK <https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-c-sdk.pdf>`_
* `API-Ebene Doxygen-Dokumentation für das Raspberry Pi Pico C/C++ SDK <https://raspberrypi.github.io/pico-sdk-doxygen/>`_
* `Raspberry Pi Pico Python SDK <https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf>`_
* `Raspberry Pi RP2040 Datenblatt <https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf>`_
* `GitHub-Repository für die Raspberry Pi Pico Firmware <https://github.com/raspberrypi/pico-sdk>`_
* `Community-Forum <https://www.raspberrypi.org/forums/>`_

