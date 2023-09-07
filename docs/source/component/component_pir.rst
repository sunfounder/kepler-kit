.. _cpn_pir:

PIR-Bewegungssensormodul
==================================

|img_pir|

Der PIR-Sensor erkennt infrarote Wärmestrahlung, die zur Erfassung der Anwesenheit von Organismen genutzt werden kann, die infrarote Wärmestrahlung abgeben.

Der PIR-Sensor ist in zwei Schlitze unterteilt, die mit einem Differenzverstärker verbunden sind. Solange sich ein unbewegtes Objekt vor dem Sensor befindet, empfangen beide Schlitze dieselbe Menge an Strahlung, und die Ausgangsspannung ist null. Bewegt sich jedoch ein Objekt vor dem Sensor, nimmt einer der Schlitze mehr Strahlung auf als der andere, was dazu führt, dass die Ausgangsspannung ansteigt oder abfällt. Diese Veränderung der Ausgangsspannung resultiert aus der erkannten Bewegung.

|img_PIR_working_principle|

Nach der Verkabelung des Sensormoduls erfolgt eine einminütige Initialisierung. Während dieser Phase kann das Modul 0 bis 3 Mal in Abständen ein Signal ausgeben. Danach befindet sich das Modul im Standby-Modus. Bitte vermeiden Sie Licht- und andere Störquellen im Erfassungsbereich des Moduls, um Fehlfunktionen zu verhindern. Idealerweise sollte das Modul auch nicht bei starkem Wind betrieben werden, da dieser ebenfalls den Sensor beeinträchtigen kann.

|img_pir_back|

**Entfernungsanpassung**

Durch Drehen des Entfernungs-Potentiometers im Uhrzeigersinn wird der Erfassungsbereich vergrößert; der maximale Bereich liegt bei etwa 0-7 Metern. Dreht man es gegen den Uhrzeigersinn, verringert sich der Bereich auf ungefähr 0-3 Meter.

**Verzögerungsanpassung**

Drehen Sie das Potentiometer für die Verzögerungsanpassung im Uhrzeigersinn, verlängert sich die Sensing-Verzögerung bis zu einem Maximum von 300 Sekunden. In die entgegengesetzte Richtung verkürzt sich die Verzögerung bis zu einem Minimum von 5 Sekunden.

**Zwei Auslösemodi**

Die Auswahl unterschiedlicher Modi erfolgt durch das Setzen der Jumperkappe.

* **H**: Wiederholbarer Auslösemodus: Nach der Erfassung einer menschlichen Präsenz gibt das Modul ein Hochsignal aus. Während der anschließenden Verzögerungsperiode bleibt das Ausgangssignal bei erneutem Betreten des Erfassungsbereichs hoch.
* **L**: Einmaliger Auslösemodus: Das Modul gibt ein Hochsignal aus, wenn es eine menschliche Präsenz erfasst. Nach Ablauf der Verzögerungszeit wechselt das Ausgangssignal automatisch auf ein Niedrigsignal.

.. Beispiel
.. -------------------

.. :ref:`Intruder Alarm`

**Beispiel**

* :ref:`py_pir` (Für MicroPython-Nutzer)
* :ref:`py_passage_counter` (Für MicroPython-Nutzer)
* :ref:`ar_pir` (Für Arduino-Nutzer)
* :ref:`per_lucky_cat` (Für Piper Make-Nutzer)
