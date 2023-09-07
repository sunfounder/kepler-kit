.. _py_guess_number:

7.7 Zahlenraten
==============================

Zahlenraten ist ein unterhaltsames Partyspiel, bei dem Sie und Ihre Freunde Zahlen von 0 bis 99 eingeben. Mit jeder Eingabe schrumpft der Zahlenbereich, bis ein Spieler das Rätsel richtig löst. Dann ist dieser Spieler besiegt und wird bestraft.

Zum Beispiel, wenn die Glückszahl 51 ist, die für die Spieler unsichtbar ist, und Spieler 1 die Zahl 50 eingibt, ändert sich die Aufforderung zu 50 - 99; wenn Spieler 2 die Zahl 70 eingibt, ändert sich der Bereich zu 50 - 70; wenn Spieler 3 die Zahl 51 eingibt, hat er Pech gehabt. In diesem Fall werden die Zahlen über eine Tastatur eingegeben und die Ergebnisse auf einem LCD-Bildschirm angezeigt.

|guess_number|

**Benötigte Komponenten**

Für dieses Projekt benötigen wir folgende Komponenten.

Ein Komplettset zu kaufen ist definitiv praktisch, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ARTIKEL IN DIESEM KIT
        - LINK
    *   - Kepler Kit
        - 450+
        - |link_kepler_kit|

Sie können die Komponenten auch einzeln über die untenstehenden Links erwerben.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTE
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
        - :ref:`cpn_resistor`
        - 4(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_keypad`
        - 1
        - |link_keypad_buy|
    *   - 7
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|

**Schaltplan**

|sch_guess_number|

Diese Schaltung basiert auf :ref:`py_keypad` und wird durch ein I2C LCD1602 ergänzt, um die gedrückten Tasten anzuzeigen.

**Verkabelung**

|wiring_game_guess_number|

Um die Verkabelung zu erleichtern, sind in der obigen Darstellung die Spalten und Reihen der Matrix-Tastatur sowie die 10K-Widerstände gleichzeitig in die Löcher eingefügt, wo G10 ~ G13 liegen.



**Code**

.. note::

    * Öffnen Sie die Datei ``7.7_game_guess_number.py`` im Verzeichnis ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny und klicken Sie dann auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5, um es auszuführen.

    * Vergessen Sie nicht, im unteren rechten Eck den Interpreter "MicroPython (Raspberry Pi Pico)" auszuwählen.

    * Für detaillierte Anleitungen verweisen wir auf :ref:`open_run_code_py`.

.. code-block:: python

    from lcd1602 import LCD
    import machine
    import time
    import urandom

    # keypad function
    characters = [["1","2","3","A"],["4","5","6","B"],["7","8","9","C"],["*","0","#","D"]]

    pin = [21,20,19,18]
    row = []
    for i in range(4):
        row.append(None)
        row[i] = machine.Pin(pin[i], machine.Pin.OUT)

    pin = [13,12,11,10]
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

    # init/reset number
    # reset the result as False for lcd show
    def init_new_value():
    global pointValue,upper,count,lower
    pointValue = int(urandom.uniform(0, 99))
    print(pointValue)
    upper = 99
    lower = 0
    count = 0
    return False


    # lcd show message
    # If target, show game over.
    # If not target, or not detected, show guess number.
    def lcd_show(result):
        lcd.clear()
        if result == True: 
            string ="GAME OVER!\n"
            string +="Point is "+ str(pointValue)
        else : 
            string ="Enter number: " + str(count) +"\n"
            string += str(lower)+ " < Point < " + str(upper)
        lcd.message(string)
        return  

    # detect number & reflesh show message 
    # if not target, reflesh number (upper or lower) and return False
    # if target, return True 
    def number_processing():
        global upper,count,lower
        if count > pointValue:
            if count < upper:
                upper = count
        elif count < pointValue:
            if count > lower:
                lower = count
        elif count == pointValue:
            return True
        count = 0
        return False

    ## start
    lcd = LCD()
    string = "Welcome!\n"
    string = "Press A to Start!"
    lcd.message(string)
    result=init_new_value()

    # read key & display
    last_key = None
    while True:
        current_key = readKey()
        if current_key == last_key:
            continue
        last_key = current_key
        if current_key != None:
            # print(current_key)
            if current_key ==["A"]: # reset number
                result=init_new_value() 
            elif current_key==["D"]: # check
                result=number_processing()
            elif current_key[0] in list(["1","2","3","4","5","6","7","8","9","0"]) and count < 10: #check validity & limit digits
                count = count * 10 + int(current_key[0])
            lcd_show(result) # show 
        time.sleep(0.1)

* Nach dem Ausführen des Codes drücken Sie ``A``, um das Spiel zu starten. Eine zufällige Zahl ``point`` wird erzeugt, jedoch nicht auf dem LCD angezeigt. Ihre Aufgabe ist es, diese zu erraten.
* Die eingegebene Zahl wird am Ende der ersten Zeile angezeigt, bis die endgültige Berechnung abgeschlossen ist. (Drücken Sie ``D``, um den Vergleich zu starten.)
* Der Zahlenbereich von ``point`` wird in der zweiten Zeile angezeigt. Ihre eingegebene Zahl muss in diesem Bereich liegen.
* Wenn Sie eine Zahl eingeben, verengt sich der Bereich; wenn Sie die Glückszahl zufällig oder unglücklicherweise erraten, erscheint ``GAME OVER!``.

.. note::
    Falls der Code und die Verkabelung in Ordnung sind, das LCD jedoch keinen Inhalt anzeigt, können Sie das Potentiometer auf der Rückseite drehen, um den Kontrast zu erhöhen.
