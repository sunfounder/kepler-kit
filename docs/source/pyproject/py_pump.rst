.. _py_pump:

3.6 Pumpensteuerung
=======================


Kleine Kreiselpumpen eignen sich hervorragend für Projekte zur automatischen Pflanzenbewässerung.
Sie können auch zum Erstellen kleiner intelligenter Wasserspiele verwendet werden.

Das Antriebselement ist ein Elektromotor, der genau wie ein herkömmlicher Motor betrieben wird.

* :ref:`cpn_pump`
* :ref:`cpn_motor`
* :ref:`cpn_ta6586`
* :ref:`cpn_power_module`

.. note::

    #. Schließen Sie den Schlauch an den Motorausgang an, tauchen Sie die Pumpe ins Wasser und schalten Sie sie ein.
    #. Achten Sie darauf, dass der Wasserstand stets über dem Motor liegt. Ein Leerlauf kann den Motor durch Hitzegenerierung beschädigen und Lärm erzeugen.
    #. Wenn Sie Pflanzen bewässern, sollten Sie das Einsaugen von Erde vermeiden, da dies die Pumpe verstopfen kann.
    #. Sollte kein Wasser aus dem Schlauch kommen, könnte Restwasser im Schlauch die Luftzirkulation blockieren und muss zuerst abgelassen werden.


**Benötigte Bauteile**

Für dieses Projekt werden die folgenden Bauteile benötigt.

Es ist definitiv praktisch, ein komplettes Set zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Bezeichnung	
        - BAUTEILE IN DIESEM KIT
        - LINK
    *   - Kepler Kit	
        - 450+
        - |link_kepler_kit|

Sie können die Bauteile auch einzeln über die untenstehenden Links erwerben.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - BAUTEIL	
        - MENGE
        - LINK

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
        - :ref:`cpn_lipo_charger`
        - 1
        -  
    *   - 7
        - 18650 Batterie
        - 1
        -  
    *   - 8
        - Batteriehalter
        - 1
        -  
    *   - 9
        - :ref:`cpn_pump`
        - 1
        -  


**Schaltplan**

|sch_pump|


**Verkabelung**

.. note::

    * Da die Pumpe einen hohen Strombedarf hat, nutzen wir ein Li-Po-Ladegerät-Modul, um den Motor aus Sicherheitsgründen mit Strom zu versorgen.
    * Stellen Sie sicher, dass Ihr Li-Po-Ladegerät-Modul wie im Diagramm gezeigt angeschlossen ist. Andernfalls könnte es zu einem Kurzschluss kommen, der Ihre Batterie und Schaltung beschädigt.



|wiring_pump|

**Code**

.. note::

    * Öffnen Sie die Datei ``3.6_pumping.py`` im Pfad ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny, dann klicken Sie auf "Aktuelles Skript ausführen" oder drücken einfach F5.

    * Vergessen Sie nicht, unten rechts auf den "MicroPython (Raspberry Pi Pico)"-Interpreter zu klicken.

    * Für detaillierte Anleitungen verweisen wir auf :ref:`open_run_code_py`.


.. code-block:: python

    import machine
    import utime

    motor1A = machine.Pin(14, machine.Pin.OUT)
    motor2A = machine.Pin(15, machine.Pin.OUT)

    while True:
        motor1A.high()
        motor2A.low()


Nachdem der Code ausgeführt wurde, beginnt die Pumpe zu arbeiten und gleichzeitig fließt Wasser aus dem Schlauch.

.. note::

    * Sollte der Motor nach dem Klicken auf den Stop-Button immer noch laufen, müssen Sie zu diesem Zeitpunkt den **RUN**-Pin am Pico W mit einem Draht auf GND zurücksetzen und dann diesen Draht entfernen, um den Code erneut auszuführen.
    * Dies liegt daran, dass der Motor mit zu hohem Strom arbeitet, was dazu führen kann, dass der Pico W die Verbindung zum Computer verliert.

    |wiring_run_reset|
