.. _py_74hc_4dig:

5.3 Zeitmesser
================================

Ein 4-stelliges 7-Segment-Display besteht aus vier zusammenarbeitenden 7-Segment-Anzeigen.

Das 4-stellige 7-Segment-Display arbeitet unabhängig voneinander. Es nutzt das Prinzip der visuellen Persistenz des menschlichen Auges, um die Zeichen jedes 7-Segments schnell in einer Schleife anzuzeigen und so fortlaufende Zeichenfolgen zu bilden.

Zum Beispiel, wenn "1234" auf dem Display angezeigt wird, erscheint "1" auf dem ersten 7-Segment, während "234" nicht angezeigt wird. Nach einer kurzen Zeit zeigt das zweite 7-Segment "2", die 1., 3. und 4. 7-Segment-Anzeige bleiben aus, und so weiter. Dieser Vorgang ist sehr kurz (typischerweise 5ms), und durch den optischen Nachleuchteffekt sowie das Prinzip der visuellen Persistenz sehen wir alle vier Zeichen gleichzeitig.

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Bauteile.

Ein komplettes Kit ist sicherlich praktisch, hier ist der Link dazu:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Bezeichnung
        - ARTIKEL IN DIESEM KIT
        - LINK
    *   - Kepler Kit	
        - 450+
        - |link_kepler_kit|

Sie können die Teile auch separat über die untenstehenden Links erwerben.

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
        - mehrere
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_resistor`
        - 4 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_4_dit_7_segment`
        - 1
        - 
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|

**Schaltplan**

|sch_4dig|

Der Verdrahtungsansatz ist im Grunde der gleiche wie bei :ref:`py_74hc_led`, der einzige Unterschied besteht darin, dass die Pins Q0-Q7 an die a ~ g Pins des 4-stelligen 7-Segment-Displays angeschlossen sind.

Anschließend wählen G10 ~ G13 aus, welches 7-Segment-Display aktiv sein soll.

**Verdrahtung**

|wiring_4dig|

**Code**

.. note::

    * Öffnen Sie die Datei ``5.3_time_counter.py`` im Verzeichnis ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny. Klicken Sie dann auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.

    * Vergessen Sie nicht, den "MicroPython (Raspberry Pi Pico)"-Interpreter in der rechten unteren Ecke auszuwählen.

    * Für detaillierte Anleitungen beziehen Sie sich bitte auf :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import time

    SEGCODE = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]

    sdi = machine.Pin(18,machine.Pin.OUT)
    rclk = machine.Pin(19,machine.Pin.OUT)
    srclk = machine.Pin(20,machine.Pin.OUT)

    placePin = []
    pin = [10,13,12,11]
    for i in range(4):
        placePin.append(None)
        placePin[i] = machine.Pin(pin[i], machine.Pin.OUT)

    timerStart=time.ticks_ms()

    def timer1():
        return int((time.ticks_ms()-timerStart)/1000)

    def pickDigit(digit):
        for i in range(4):
            placePin[i].value(1)
        placePin[digit].value(0)

    def clearDisplay():
        hc595_shift(0x00)

    def hc595_shift(dat):
        rclk.low()
        time.sleep_us(200)
        for bit in range(7, -1, -1):
            srclk.low()
            time.sleep_us(200)
            value = 1 & (dat >> bit)
            sdi.value(value)
            time.sleep_us(200)
            srclk.high()
            time.sleep_us(200)
        time.sleep_us(200)
        rclk.high()
        time.sleep_us(200)

    while True:
        count = timer1()
        #print(count)
        
        pickDigit(0)
        hc595_shift(SEGCODE[count%10])

        pickDigit(1)
        hc595_shift(SEGCODE[count%100//10])
        
        pickDigit(2)
        hc595_shift(SEGCODE[count%1000//100])
        
        pickDigit(3)
        hc595_shift(SEGCODE[count%10000//1000])


Nachdem das Programm ausgeführt wurde, verwandelt sich die 4-stellige 7-Segment-Anzeige in einen Zähler, und die Zahl erhöht sich jede Sekunde um 1.

**Wie funktioniert es?**

Das Senden von Signalen an jede 7-Segment-Anzeige erfolgt auf die gleiche Weise wie bei :ref:`py_74hc_7seg`, indem die Funktion ``hc595_shift()`` verwendet wird.
Der Kernpunkt der 4-stelligen 7-Segment-Anzeige besteht darin, selektiv jede 7-Segment-Anzeige zu aktivieren. Der damit verbundene Code ist wie folgt:

.. code-block:: python

    placePin = []
    pin = [13,12,11,10]
    for i in range(4):
        placePin.append(None)
        placePin[i] = machine.Pin(pin[i], machine.Pin.OUT)

    def pickDigit(digit):
        for i in range(4):
            placePin[i].value(1)
        placePin[digit].value(0)

    while True:
        
        hc595_shift(SEGCODE[count%10])
        pickDigit(0)

        hc595_shift(SEGCODE[count%100//10])
        pickDigit(1)
        
        hc595_shift(SEGCODE[count%1000//100])
        pickDigit(2)    
        
        hc595_shift(SEGCODE[count%10000//1000])
        pickDigit(3)   

An dieser Stelle werden vier Pins (GP10, GP11, GP12, GP13) verwendet, um jeden Bit der 4-stelligen 7-Segment-Anzeige individuell zu steuern.
Wenn der Zustand dieser Pins ``0`` ist, ist das entsprechende 7-Segment-Display aktiv; bei Zustand ``1`` gilt das Gegenteil.

Hier wird die Funktion ``pickDigit(digit)`` verwendet, um alle vier Ziffern zu deaktivieren und dann eine bestimmte Ziffer einzeln zu aktivieren.
Danach wird ``hc595_shift()`` verwendet, um den entsprechenden 8-Bit-Code für die 7-Segment-Anzeige zu schreiben.

Die 4-stellige 7-Segment-Anzeige muss kontinuierlich abwechselnd aktiviert werden, damit wir sie sehen können.
Jedoch dürfen wir im Hauptprogramm keinen Code hinzufügen, der das Timing beeinflussen würde.
Zu diesem Zweck ist die Verwendung der Funktion ``time.ticks_ms()`` aus der ``time``-Bibliothek eine ausgezeichnete Methode.

.. code-block:: python

    import time

    timerStart=time.ticks_ms()

    def timer1():
        return int((time.ticks_ms()-timerStart)/1000)

    while True:
        count = timer1()

Die Funktion ``time.ticks_ms()`` ermittelt eine (nicht explizite) Zeit, und wir speichern den ersten ermittelten Zeitwert als ``timerStart``.
Wenn später die Zeit benötigt wird, wird die Funktion ``time.ticks_ms()`` erneut aufgerufen, und der Wert wird von ``timerStart`` abgezogen, um die bisherige Laufzeit des Programms (in Millisekunden) zu ermitteln.

Abschließend wird dieser Zeitwert in die 4-stellige 7-Segment-Anzeige umgewandelt und ausgegeben, und das war's.

* `Time - MicroPython Docs <https://docs.micropython.org/en/latest/library/time.html>`_

