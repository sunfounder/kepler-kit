.. _py_photoresistor:

2.12 Das Licht spüren
=============================

Der Fotowiderstand ist ein typisches Bauelement für analoge Eingänge und funktioniert sehr ähnlich wie ein Potentiometer. Sein Widerstandswert ist abhängig von der Lichtintensität: Je stärker das Licht, desto geringer der Widerstandswert und umgekehrt.

* :ref:`cpn_photoresistor`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Bauteile.

Es ist definitiv praktisch, ein komplettes Set zu erwerben. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ARTIKEL IN DIESEM SET
        - LINK
    *   - Kepler-Set
        - 450+
        - |link_kepler_kit|

Sie können die Komponenten auch einzeln über die folgenden Links erwerben.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTE
        - ANZAHL
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
        - :ref:`cpn_resistor`
        - 1 (10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_photoresistor`
        - 1
        - |link_photoresistor_buy|

**Schaltplan**

|sch_photoresistor|

In dieser Schaltung sind der 10K-Widerstand und der Fotowiderstand in Reihe geschaltet; der durch sie fließende Strom ist identisch. Der 10K-Widerstand dient als Schutz, und GP28 liest den umgewandelten Spannungswert des Fotowiderstands.

Wenn das Licht intensiver wird, sinkt der Widerstand des Fotowiderstands, und somit auch seine Spannung. Daraufhin wird auch der Wert von GP28 niedriger. Sollte das Licht ausreichend stark sein, nähert sich der Widerstand des Fotowiderstands dem Wert 0 an, und der Wert von GP28 wird ebenfalls nahe 0 liegen. In diesem Fall spielt der 10K-Widerstand eine schützende Rolle, um einen Kurzschluss zwischen 3,3V und GND zu vermeiden.

Platziert man den Fotowiderstand in einer dunklen Umgebung, wird der Wert von GP28 ansteigen. In völliger Dunkelheit wäre der Widerstand des Fotowiderstands unendlich, und seine Spannung wäre nahe 3,3V (der 10K-Widerstand ist vernachlässigbar), und der Wert von GP28 würde sich dem Maximalwert von 65535 annähern.

Die Berechnungsformel lautet wie folgt:

    (Vp/3.3V) x 65535 = Ap

**Verdrahtung**

|wiring_photoresistor|

**Code**

.. note::

    * Öffnen Sie die Datei ``2.12_feel_the_light.py`` im Verzeichnis ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny und führen Sie ihn mit "Aktuelles Skript ausführen" oder einfach mit F5 aus.

    * Vergewissern Sie sich, dass der Interpreter "MicroPython (Raspberry Pi Pico)" in der unteren rechten Ecke ausgewählt ist.

    * Für ausführliche Anleitungen siehe :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    photoresistor = machine.ADC(28)

    while True:
        light_value  = photoresistor.read_u16()
        print(light_value)
        utime.sleep_ms(10)

Nachdem das Programm läuft, werden die Werte des Fotowiderstands in der Shell ausgegeben. Man kann die Werte verändern, indem man eine Taschenlampe darauf richtet oder den Fotowiderstand mit der Hand abdeckt.

