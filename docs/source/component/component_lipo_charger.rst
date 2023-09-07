.. _cpn_lipo_charger:

Li-Po-Lademodul
=================================================

|lipo_module|

Dies ist ein Li-Po-Lademodul, konzipiert für Raspberry Pi Pico/Pico H/Pico W. Einfach einstecken und den Pico auf dem Steckbrett wie unten gezeigt positionieren. Danach die Batterie am anderen Ende anschließen und schon kann es losgehen.

Wenn das Pico W über ein USB-Kabel an einen Computer oder eine Steckdose angeschlossen wird, leuchtet die Kontrollleuchte auf dem Li-Po-Lademodul auf. Dies signalisiert, dass die Batterie gleichzeitig geladen wird. Wird das USB-Kabel entfernt, wird das Pico W von der Batterie versorgt, sodass Ihr Projekt weiterhin läuft.

.. note::
    Bei einigen leistungsschwachen Computern kann es vorkommen, dass das Pico W nicht erkannt wird, wenn es mit dem angeschlossenen Lademodul an den Computer angeschlossen wird.

    Der Grund dafür ist, dass die USB-Port-Spannung beim Laden der Batterie abfällt, was dazu führt, dass die Stromversorgung des Pico W nicht ausreicht, um vom Computer erkannt zu werden.

    In diesem Fall muss das Li-Po-Lademodul entfernt und das Pico W erneut eingesteckt werden.

|lipo_wire|

**Eigenschaften**

* Eingangsspannung: 5V
* Ausgangsspannung: 3,3V
* Größe: 20mmx7mm
* Schnittstellenmodell: PH2.0
* Es gibt einen passenden 1A-Batteriehalter sowie einen 800mAh 18650, der zusammen verwendet werden kann.

**Schaltplan**

|sch_lipo_charger|

