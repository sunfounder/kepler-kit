.. _py_keypad:

4.2 4x4 Tastenfeld
========================

Das 4x4 Tastenfeld, auch Matrix-Tastenfeld genannt, besteht aus einer Anordnung von 16 Tasten in einer einzigen Einheit.

Solche Tastenfelder findet man hauptsächlich in Geräten, die digitale Eingaben erfordern, wie Taschenrechner, Fernbedienungen, Tastentelefone, Verkaufsautomaten, Geldautomaten, Zahlenschlösser und digitale Türschlösser.

In diesem Projekt lernen wir, wie man ermittelt, welche Taste gedrückt wurde und den entsprechenden Tastenwert erhält.

* :ref:`cpn_keypad`
* `E.161 – Wikipedia <https://de.wikipedia.org/wiki/E.161>`_

**Benötigte Komponenten**

Für dieses Projekt benötigen wir folgende Komponenten.

Ein Komplettset ist definitiv praktisch. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Bezeichnung	
        - ARTIKEL IM SET
        - LINK
    *   - Kepler Set	
        - 450+
        - |link_kepler_kit|

Die einzelnen Komponenten können auch über die untenstehenden Links erworben werden.

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
        - 4(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_keypad`
        - 1
        - |link_keypad_buy|

**Schaltplan**

|sch_keypad|

An jede der vier Spalten des Matrix-Tastenfelds ist ein Pull-Down-Widerstand angeschlossen, sodass die Anschlüsse G6 bis G9 auf einem stabilen niedrigen Pegel sind, wenn keine Taste gedrückt ist.

Die Reihen des Tastenfelds (G2 bis G5) sind so programmiert, dass sie auf High gehen; wird einer der Anschlüsse G6 bis G9 als High gelesen, wissen wir, welche Taste gedrückt wurde.

Zum Beispiel, wenn G6 als High gelesen wird, dann wurde die Nummerntaste 1 gedrückt; denn die Steuerpins der Nummerntaste 1 sind G2 und G6, wenn die Taste 1 gedrückt wird, werden G2 und G6 miteinander verbunden und G6 ist ebenfalls High.

**Verdrahtung**

|wiring_keypad|

Um die Verdrahtung zu vereinfachen, sind im obigen Schaltplan die Reihen und Spalten des Matrix-Tastenfelds sowie die 10K-Widerstände gleichzeitig in die Löcher eingesteckt, in denen sich G6 bis G9 befinden.

**Code**

.. note::

    * Öffnen Sie die Datei ``4.2_4x4_keypad.py`` im Verzeichnis ``kepler-kit-main/micropython`` oder kopieren Sie den Code in Thonny, und klicken Sie auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.

    * Vergessen Sie nicht, im rechten unteren Eck den "MicroPython (Raspberry Pi Pico)"-Interpreter auszuwählen.

    * Für detaillierte Anleitungen siehe :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import time

    characters = [["1","2","3","A"],["4","5","6","B"],["7","8","9","C"],["*","0","#","D"]]

    pin = [2,3,4,5]
    row = []
    for i in range(4):
        row.append(None)
        row[i] = machine.Pin(pin[i], machine.Pin.OUT)

    pin = [6,7,8,9]
    col = []
    for i in range(4):
        col.append(None)
        col[i] = machine.Pin(pin[i], machine.Pin.IN)

    def readKey():
        key = []
        for i in range(4):
            row[i].high()
            for j in range(4):
                if(col[j].value() == 1):
                    key.append(characters[i][j])
            row[i].low()
        if key == [] :
            return None
        else:
            return key

    last_key = None
    while True:
        current_key = readKey()
        if current_key == last_key:
            continue
        last_key = current_key
        if current_key != None:
            print(current_key)
        time.sleep(0.1)

Nachdem das Programm ausgeführt wurde, wird die Shell die Tasten ausgeben, die Sie auf dem Keypad gedrückt haben.
**Funktionsweise**

.. code-block:: python

    import machine
    import time

    characters = [["1","2","3","A"],["4","5","6","B"],["7","8","9","C"],["*","0","#","D"]]

    pin = [2,3,4,5]
    row = []
    for i in range(4):
        row.append(None)
        row[i] = machine.Pin(pin[i], machine.Pin.OUT)

    pin = [6,7,8,9]
    col = []
    for i in range(4):
        col.append(None)
        col[i] = machine.Pin(pin[i], machine.Pin.IN)

Definiert jede Taste der Matrix-Tastatur im Array ``characters[]`` und legt die Pins für jede Reihe und Spalte fest.

.. code-block:: python

    last_key = None
    while True:
        current_key = readKey()
        if current_key == last_key:
            continue
        last_key = current_key
        if current_key != None:
            print(current_key)
        time.sleep(0.1)

Dies ist der Teil der Hauptfunktion, der den Wert der gedrückten Taste liest und ausgibt.

Die Funktion ``readKey()`` liest den Zustand jeder Taste aus.

Die Anweisungen ``if current_key != None`` und ``if current_key == last_key`` 
dienen dazu, festzustellen, ob eine Taste gedrückt ist und wie der Zustand der gedrückten Taste ist.
(Wenn Sie beispielsweise '3' drücken, während Sie '1' drücken, ist die Bewertung gültig.)

Gibt den Wert der aktuell gedrückten Taste aus, wenn die Bedingung gültig ist.

Die Anweisung ``last_key = current_key`` speichert den Zustand jeder Auswertung 
in einem Array ``last_key``, um die nächste Runde der bedingten Bewertung zu erleichtern.

.. code-block:: python

    def readKey():
        key = []
        for i in range(4):
            row[i].high()
            for j in range(4):
                if(col[j].value() == 1):
                    key.append(characters[i][j])
            row[i].low()
        if key == [] :
            return None
        else:
            return key

Diese Funktion setzt jede Reihe der Matrix-Tastatur nacheinander auf ein hohes Niveau. Wenn eine Taste gedrückt wird, 
erhält die entsprechende Spalte ein hohes Niveau. 
Nach Durchlaufen der zweistufigen Schleife wird der Wert der Taste, deren Zustand 1 ist, im Array ``key`` gespeichert.

Wenn Sie die Taste '3' drücken:

|img_keypad_pressed|

``row[0]`` wird auf ein hohes Niveau gesetzt und ``col[2]`` erhält ebenfalls ein hohes Niveau.

``col[0]``, ``col[1]``, ``col[3]`` erhalten ein niedriges Niveau.

Es gibt vier Zustände: 0, 0, 1, 0; und wir schreiben '3' in ``pressed_keys``.

Wenn ``row[1]``, ``row[2]``, ``row[3]`` auf ein hohes Niveau gesetzt werden,
erhalten ``col[0]`` ~ ``col[4]`` ein niedriges Niveau.

Die Schleife stoppt und gibt key = '3' zurück.

Wenn Sie die Tasten '1' und '3' drücken, wird key = ['1','3'] zurückgegeben.
