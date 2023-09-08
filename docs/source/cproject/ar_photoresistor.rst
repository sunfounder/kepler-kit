.. _ar_photoresistor:

2.12 - Das Licht erfassen
=================================

Der Fotowiderstand ist ein typisches Bauelement für analoge Eingänge und wird ähnlich wie ein Potentiometer verwendet. Sein Widerstandswert hängt von der Lichtintensität ab: Je stärker das einfallende Licht, desto geringer der Widerstandswert; umgekehrt nimmt er zu.

* :ref:`cpn_photoresistor`

**Erforderliche Bauteile**

Für dieses Projekt benötigen wir die folgenden Bauteile.

Ein komplettes Set zu kaufen, ist definitiv praktisch. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Bezeichnung
        - ELEMENTE IN DIESEM KIT
        - KAUF-LINK
    *   - Kepler Kit
        - 450+
        - |link_kepler_kit|

Alternativ können Sie die Teile auch einzeln über die folgenden Links erwerben.

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
        - :ref:`cpn_resistor`
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_photoresistor`
        - 1
        - |link_photoresistor_buy|

**Schaltbild**

|sch_photoresistor|

In dieser Schaltung sind der 10K-Widerstand und der Fotowiderstand in Reihe geschaltet. Der durch sie fließende Strom ist identisch. Der 10K-Widerstand dient als Schutz, und GP28 liest den Wert nach der Spannungsumwandlung des Fotowiderstands.

Wenn das Licht intensiver wird, verringert sich der Widerstand des Fotowiderstands und damit auch seine Spannung. Daraufhin sinkt der Wert von GP28. Ist das Licht stark genug, nähert sich der Widerstand des Fotowiderstands dem Wert 0, und der Wert von GP28 wird ebenfalls nahezu 0 sein. In diesem Fall spielt der 10K-Widerstand eine schützende Rolle, sodass 3,3V und GND nicht direkt miteinander verbunden und somit ein Kurzschluss vermieden wird.

In einer dunklen Umgebung steigt der Wert von GP28. Ist es dunkel genug, wird der Widerstand des Fotowiderstands unendlich groß, seine Spannung nähert sich 3,3V an (der 10K-Widerstand ist vernachlässigbar), und der Wert von GP28 erreicht nahezu den Maximalwert von 65535.

Die Berechnungsformel lautet wie folgt:

    (Vp/3,3V) x 65535 = Ap

**Verkabelung**

|wiring_photoresistor|

**Programmcode**

.. note::

   * Die Datei ``2.12_feel_the_light.ino`` befindet sich im Verzeichnis ``kepler-kit-main/arduino/2.12_feel_the_light``.
   * Alternativ können Sie den Code auch direkt in die **Arduino IDE** kopieren.
   
   * Denken Sie daran, vor dem Hochladen des Programms die richtige Platine (Raspberry Pi Pico) und den entsprechenden Port auszuwählen.


.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/44074b9e-3e4e-475b-af37-689254f87ab2/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Nach dem Start des Programms gibt der serielle Monitor die Werte des Fotowiderstands aus. Sie können die Werte verändern, indem Sie eine Taschenlampe darauf richten oder ihn mit der Hand abdecken.
