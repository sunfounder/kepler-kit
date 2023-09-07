.. _cpn_ultrasonic:

Ultraschallmodul
================================

|ultrasonic_pic|

* **TRIG**: Trigger-Impulseingang
* **ECHO**: Echo-Impulsausgang
* **GND**: Masse
* **VCC**: 5V Versorgungsspannung

Es handelt sich hierbei um den HC-SR04 Ultraschall-Distanzsensor, der eine berührungslose Messung von 2 cm bis 400 cm mit einer Reichweitengenauigkeit von bis zu 3 mm ermöglicht. Das Modul umfasst einen Ultraschall-Sender, einen Empfänger und eine Steuerschaltung.

Zur Inbetriebnahme sind lediglich 4 Pins anzuschließen: VCC (Stromversorgung), Trig (Trigger), Echo (Empfang) und GND (Masse). Dies macht das Modul besonders benutzerfreundlich für Ihre Messprojekte.

**Merkmale**

* Betriebsspannung: DC5V
* Arbeitsstrom: 16mA
* Arbeitsfrequenz: 40Hz
* Maximale Reichweite: 500cm
* Minimale Reichweite: 2cm
* Trigger-Eingangssignal: 10uS TTL-Impuls
* Echo-Ausgangssignal: TTL-Pegelsignal und reichweitenproportionales Signal
* Anschluss: XH2.54-4P
* Abmessungen: 46x20.5x15 mm

**Funktionsprinzip**

Die Grundlagen sind wie folgt:

* Auslösung über IO mit einem mindestens 10us hohen Pegelsignal.

* Das Modul sendet eine 8-Zyklus-Ultraschall-Burst bei 40 kHz aus und prüft, ob ein Pulssignal zurückkommt.

* Echo gibt ein Hochpegelsignal aus, wenn ein Signal zurückkommt; die Dauer dieses Hochpegels entspricht der Zeit von der Aussendung bis zur Rückkehr.

* Distanz = (Hochpegelzeit x Schallgeschwindigkeit (340M/S)) / 2

|ultrasonic_prin|

Formel:

* us / 58 = Entfernung in Zentimetern
* us / 148 = Entfernung in Zoll
* Distanz = Hochpegelzeit x Schallgeschwindigkeit (340M/S) / 2

.. note::

    Dieses Modul sollte nicht unter Spannung angeschlossen werden. Falls notwendig, sollte zuerst der GND-Pin des Moduls verbunden werden, um eine Beeinträchtigung der Funktionalität zu vermeiden.

    Die Fläche des zu messenden Objekts sollte mindestens 0,5 Quadratmeter betragen und möglichst flach sein. Andernfalls werden die Messergebnisse beeinträchtigt.


**Beispiel**

* :ref:`py_ultrasonic` (Für MicroPython-Anwender)
* :ref:`py_reversing_aid` (Für MicroPython-Anwender)
* :ref:`ar_ultrasonic` (Für Arduino-Anwender)
* :ref:`per_reversing_system` (Für Piper Make-Anwender)
