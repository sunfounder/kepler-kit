.. _ar_motor:

3.5 - Kleiner Ventilator
========================

Nun nutzen wir den TA6586, um den Gleichstrommotor in beide Richtungen drehen zu lassen. 
Da der Gleichstrommotor einen vergleichsweise hohen Strombedarf hat, verwenden wir aus Sicherheitsgründen ein Spannungsmodul zur Stromversorgung des Motors.

* :ref:`cpn_motor`
* :ref:`cpn_ta6586`
* :ref:`cpn_power_module`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir folgende Bauteile:

Ein komplettes Set zu kaufen, ist definitiv praktisch. Hier ist der Link dazu:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Bezeichnung
        - ARTIKEL IN DIESEM KIT
        - KAUF-LINK
    *   - Kepler-Kit
        - 450+
        - |link_kepler_kit|

Alternativ können Sie die einzelnen Komponenten auch über die unten aufgeführten Links erwerben.

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
        - :ref:`cpn_ta6586`
        - 1
        - 
    *   - 6
        - :ref:`cpn_motor`
        - 1
        - |link_motor_buy|
    *   - 7
        - :ref:`cpn_lipo_charger`
        - 1
        -  
    *   - 8
        - 18650 Batterie
        - 1
        -  
    *   - 9
        - Batteriehalter
        - 1
        - 

**Schaltplan**

|sch_motor|

**Verkabelung**

.. note::

    * Da Gleichstrommotoren einen hohen Strombedarf haben, verwenden wir hier aus Sicherheitsgründen ein Li-Po-Ladegerät-Modul zur Stromversorgung des Motors.
    * Achten Sie darauf, dass Ihr Li-Po-Ladegerät-Modul gemäß dem Schaltplan verbunden ist. Andernfalls könnten Kurzschlüsse sowohl Ihre Batterie als auch die Schaltung beschädigen.


|wiring_motor|

**Code**

.. note::

   * Die Datei ``3.5_small_fan.ino`` finden Sie im Verzeichnis ``kepler-kit-main/arduino/3.5_small_fan``.
   * Alternativ können Sie den Code auch in die **Arduino-IDE** kopieren.

    * Vergewissern Sie sich, dass Sie das richtige Board (Raspberry Pi Pico) und den korrekten Port ausgewählt haben, bevor Sie auf **Hochladen** klicken.


.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/26d75a18-6b91-40f4-80ab-f2cdf58644ac/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Sobald das Programm läuft, wird der Motor in einem regelmäßigen Muster hin und her drehen.

.. note::

    * Falls Sie den Code nicht erneut hochladen können, müssen Sie den **RUN**-Pin am Pico W mit einem Draht auf GND legen, um ihn zurückzusetzen. Danach entfernen Sie den Draht, um den Code erneut auszuführen.
    * Dies liegt daran, dass der Motor mit zu hohem Strom arbeitet, was dazu führen kann, dass der Pico W die Verbindung zum Computer verliert.

    |wiring_run_reset|
