.. _ar_pir:

2.10 - Menschliche Bewegung erfassen
=========================================

Der passive Infrarotsensor (PIR-Sensor) ist ein gängiger Sensor, der infrarotes (IR) Licht messen kann, das von Objekten in seinem Sichtfeld abgestrahlt wird.
Einfach ausgedrückt, erfasst er die von Körpern abgestrahlte Infrarotstrahlung und kann dadurch die Bewegung von Menschen und anderen Lebewesen erkennen.
Konkret informiert er die Hauptsteuerung darüber, dass jemand den Raum betreten hat.

:ref:`cpn_pir`

**Erforderliche Komponenten**

Für dieses Projekt werden die folgenden Komponenten benötigt.

Es ist definitiv praktisch, ein ganzes Set zu kaufen. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Bezeichnung
        - ELEMENTE IN DIESEM KIT
        - KAUF-LINK
    *   - Kepler Kit
        - 450+
        - |link_kepler_kit|

Die Teile können auch einzeln über die folgenden Links gekauft werden.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTENBESCHREIBUNG
        - ANZAHL
        - KAUF-LINK

    *   - 1
        - :ref:`cpn_pico_w`
        - 1
        - |link_picow_buy|
    *   - 2
        - Micro-USB-Kabel
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Mehrere
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_pir`
        - 1
        - |link_pir_buy|

**Schaltplan**

|sch_pir|

Wenn das PIR-Modul eine vorbeigehende Person erkennt, wird GP14 auf "High" gesetzt, ansonsten bleibt es auf "Low".

**Verdrahtung**

|wiring_pir|

**Programmcode**

.. note::

   * Die Datei ``2.10_detect_human_movement.ino`` befindet sich im Verzeichnis ``kepler-kit-main/arduino/2.10_detect_human_movement``.
   * Alternativ können Sie den Code auch direkt in die **Arduino IDE** kopieren.

   * Denken Sie daran, vor dem Hochladen das richtige Board (Raspberry Pi Pico) und den entsprechenden Port auszuwählen.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/bb3ff9f1-127d-4279-84b9-cba28b9667e8/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Nach dem Start des Programms wird im seriellen Monitor "Somebody here!" ausgegeben, wenn das PIR-Modul jemanden in der Nähe erkennt.

**Mehr erfahren**

Der PIR ist ein sehr empfindlicher Sensor. Um ihn an die Einsatzumgebung anzupassen, muss er justiert werden. Richten Sie die Seite mit den beiden Potentiometern zu sich aus und drehen Sie beide Potentiometer gegen den Uhrzeigersinn ganz nach links. Setzen Sie dann die Jumperkappe auf den Pin mit L und den mittleren Pin.

|img_pir_back|

1. Auslösemodus

    Der Jumper in der Ecke ermöglicht dem PIR, in den wiederholbaren oder nicht-wiederholbaren Auslösemodus zu wechseln.

    Derzeit ist der Jumper so gesetzt, dass der PIR im nicht-wiederholbaren Modus arbeitet. In diesem Modus sendet der PIR bei erkannter Bewegung für etwa 2,8 Sekunden ein High-Signal an die Hauptsteuerung.
    .. In den ausgegebenen Daten sehen wir, dass die Arbeitsdauer stets rund 2800 ms beträgt.

    Als nächstes ändern wir die Position der Jumperkappe und verbinden den mittleren Pin mit dem H-Pin, um den PIR in den wiederholbaren Auslösemodus zu versetzen.
    In diesem Modus sendet der PIR, solange sich ein Lebewesen im Erfassungsbereich bewegt, kontinuierlich ein High-Signal an die Hauptsteuerung.
    .. In den ausgegebenen Daten sehen wir, dass die Arbeitsdauer variabel ist.

#. Verzögerungseinstellung

    Das linke Potentiometer dient zur Einstellung des Intervalls zwischen zwei Arbeitszyklen.
    
    Aktuell ist es ganz nach links gedreht, sodass der PIR nach Beendigung des High-Signal-Zyklus eine Ruhephase von etwa 5 Sekunden einlegt. In dieser Zeit werden keine Infrarotstrahlen im Zielbereich erfasst.
    .. In den ausgegebenen Daten sehen wir, dass die Ruhezeit immer mindestens 5000 ms beträgt.

    Wenn wir das Potentiometer im Uhrzeigersinn drehen, verlängert sich auch die Ruhezeit. Wenn es ganz im Uhrzeigersinn gedreht ist, beträgt die Ruhezeit bis zu 300 Sekunden.

#. Reichweiteneinstellung

    Das mittlere Potentiometer dient zur Einstellung des Erfassungsbereichs des PIR.

    Drehen Sie den Knopf des Potentiometers **im Uhrzeigersinn**, um den Erfassungsbereich zu erhöhen. Der maximale Erfassungsbereich beträgt etwa 0-7 Meter.
    Dreht man es **gegen den Uhrzeigersinn**, verringert sich der Erfassungsbereich. Der minimale Erfassungsbereich beträgt dann etwa 0-3 Meter.
