.. _py_irremote:

6.4 Infrarot-Fernbedienung
===========================

In der Unterhaltungselektronik dienen Fernbedienungen zur Steuerung von Geräten wie Fernsehern und DVD-Playern.
In einigen Fällen ermöglichen sie die Bedienung von Geräten, die außerhalb der Reichweite liegen, wie beispielsweise Zentral-Klimaanlagen.

Der IR-Empfänger ist eine Komponente mit einer auf Infrarotlicht abgestimmten Fotodiode.
Er kommt fast immer bei der Erkennung von Fernbedienungssignalen zum Einsatz - jeder Fernseher und DVD-Player ist an der Frontseite mit einem solchen Modul ausgestattet, um das IR-Signal von der Fernbedienung zu empfangen.
In der Fernbedienung selbst befindet sich eine dazu passende IR-LED, die IR-Impulse aussendet, um den Fernseher ein- oder auszuschalten oder den Sender zu wechseln.

* :ref:`cpn_ir_receiver`

**Benötigte Bauteile**

Für dieses Projekt benötigen wir folgende Komponenten.

Ein Komplett-Kit ist natürlich praktisch, hier der Link dazu:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Bezeichnung	
        - KOMPONENTEN IM KIT
        - LINK
    *   - Kepler-Kit	
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
        - Mikro-USB-Kabel
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
        - :ref:`cpn_ir_receiver`
        - 1
        - |link_receiver_buy|

**Schaltplan**

|sch_irrecv|

**Verdrahtung**

|wiring_irrecv|

**Code**

.. note::

    * Öffnen Sie die Datei ``6.4_ir_remote_control.py` im Verzeichnis ``kepler-kit-main/micropython`` oder kopieren Sie den Code in Thonny und klicken Sie dann auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.

    * Wählen Sie in der unteren rechten Ecke den Interpreter "MicroPython (Raspberry Pi Pico)" aus.

    * Für detaillierte Anleitungen siehe :ref:`open_run_code_py`.
    
    * Die benötigten Bibliotheken finden Sie im Ordner ``ir_rx``. Vergewissern Sie sich, dass diese auf den Pico hochgeladen wurden. Detaillierte Anleitungen finden Sie unter :ref:`add_libraries_py`.



.. code-block:: python

    import time
    from machine import Pin, freq
    from ir_rx.print_error import print_error
    from ir_rx.nec import NEC_8

    pin_ir = Pin(17, Pin.IN)

    def decodeKeyValue(data):
        if data == 0x16:
            return "0"
        if data == 0x0C:
            return "1"
        if data == 0x18:
            return "2"
        if data == 0x5E:
            return "3"
        if data == 0x08:
            return "4"
        if data == 0x1C:
            return "5"
        if data == 0x5A:
            return "6"
        if data == 0x42:
            return "7"
        if data == 0x52:
            return "8"
        if data == 0x4A:
            return "9"
        if data == 0x09:
            return "+"
        if data == 0x15:
            return "-"
        if data == 0x7:
            return "EQ"
        if data == 0x0D:
            return "U/SD"
        if data == 0x19:
            return "CYCLE"
        if data == 0x44:
            return "PLAY/PAUSE"
        if data == 0x43:
            return "FORWARD"
        if data == 0x40:
            return "BACKWARD"
        if data == 0x45:
            return "POWER"
        if data == 0x47:
            return "MUTE"
        if data == 0x46:
            return "MODE" 
        return "ERROR"

    # User callback
    def callback(data, addr, ctrl):
        if data < 0:  # NEC protocol sends repeat codes.
            pass
        else:
            print(decodeKeyValue(data))

    ir = NEC_8(pin_ir, callback)  # Instantiate receiver
    ir.error_function(print_error)  # Show debug information

    try:
        while True:
            pass
    except KeyboardInterrupt:
        ir.close()


Die neue Fernbedienung besitzt ein Plastikteil am Ende, um die innenliegende Batterie zu isolieren. Um die Fernbedienung zu aktivieren, muss dieses Plastikteil entfernt werden.
Sobald das Programm läuft und Sie eine Taste auf der Fernbedienung drücken, wird die gedrückte Taste in der Shell ausgegeben.

**Wie funktioniert es?**

Das Programm mag auf den ersten Blick komplex erscheinen, erfüllt jedoch die Grundfunktionen des IR-Empfängers mit nur wenigen Codezeilen.

.. code-block:: python

    import time
    from machine import Pin, freq
    from ir_rx.nec import NEC_8

    pin_ir = Pin(17, Pin.IN)

    # Benutzerdefinierte Rückruffunktion
    def callback(data, addr, ctrl):
        if data < 0:  # NEC-Protokoll sendet Wiederholungscodes.
            pass
        else:
            print(decodeKeyValue(data))

    ir = NEC_8(pin_ir, callback)  # Empfänger instanziieren

Hier wird ein ``ir``-Objekt instanziiert, das ständig die vom IR-Empfänger empfangenen Signale liest.

Die Ergebnisse werden im ``data``-Parameter der Rückruffunktion gespeichert.

* `Rückruffunktion - Wikipedia <https://de.wikipedia.org/wiki/R%C3%BCckruffunktion>`_

Falls der IR-Empfänger doppelte Werte erhält (z. B. durch gedrückt Halten einer Taste), wird `data < 0`, und diese Daten müssen gefiltert werden.

Ansonsten wäre `data` ein verwendbarer Wert, jedoch in unverständlichem Code, und die Funktion ``decodeKeyValue(data)`` dient zur Entschlüsselung.

.. code-block:: python

    def decodeKeyValue(data):
        if data == 0x16:
            return "0"
        if data == 0x0C:
            return "1"
        if data == 0x18:
            return "2"
        if data == 0x5E:
            return "3"
        if data == 0x08:
            return "4"
        if data == 0x1C:
            return "5"
        if data == 0x5A:
            return "6"
        if data == 0x42:
            return "7"
        if data == 0x52:
            return "8"
        if data == 0x4A:
            return "9"
        if data == 0x09:
            return "+"
        if data == 0x15:
            return "-"
        if data == 0x7:
            return "EQ"
        if data == 0x0D:
            return "U/SD"
        if data == 0x19:
            return "CYCLE"
        if data == 0x44:
            return "PLAY/PAUSE"
        if data == 0x43:
            return "FORWARD"
        if data == 0x40:
            return "BACKWARD"
        if data == 0x45:
            return "POWER"
        if data == 0x47:
            return "MUTE"
        if data == 0x46:
            return "MODE" 
        return "ERROR"

Falls wir die Taste **1** drücken, gibt der IR-Empfänger einen Wert wie ``0x0C`` aus, der entschlüsselt werden muss, um der spezifischen Taste zu entsprechen.

Es folgen einige Debug-Funktionen. Diese sind wichtig, stehen jedoch nicht im direkten Zusammenhang mit dem gewünschten Effekt, daher sind sie im Programm enthalten.

.. code-block:: python

    from ir_rx.print_error import print_error

    ir.error_function(print_error) # Debug-Informationen anzeigen

Abschließend verwenden wir eine leere Schleife als Hauptprogramm und nutzen `try-except`, um das Programm mit Beendigung des ``ir``-Objekts zu schließen.

.. code-block:: python

    try:
        while True:
            pass
    except KeyboardInterrupt:
        ir.close()

* `Try-Anweisung - Python-Dokumentation <https://docs.python.org/3/reference/compound_stmts.html?#the-try-statement>`_
