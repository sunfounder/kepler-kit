.. note::

    Ciao, benvenuto nella Community di Appassionati di Raspberry Pi & Arduino & ESP32 di SunFounder su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa ai giveaway e alle promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_guess_number:

7.7 Indovina il Numero
==============================


"Indovina il Numero" è un divertente gioco di gruppo in cui tu e i tuoi amici inserite numeri (0-99). Con ogni numero inserito, l'intervallo si ridurrà fino a quando un giocatore risolve l'enigma correttamente. A quel punto, il giocatore perde e viene punito.

Per esempio, se il numero fortunato è 51, che i giocatori non possono vedere, e il giocatore 1 inserisce 50, l'intervallo diventa 50 - 99; se il giocatore 2 inserisce 70, l'intervallo diventa 50 - 70; se il giocatore 3 inserisce 51, il giocatore è sfortunato. In questo caso, i numeri vengono inseriti tramite la tastiera, e i risultati vengono visualizzati su uno schermo LCD.

|guess_number|

**Componenti Necessari**

In questo progetto, abbiamo bisogno dei seguenti componenti.

È sicuramente conveniente acquistare un kit completo, ecco il link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nome	
        - ELEMENTI IN QUESTO KIT
        - LINK
    *   - Kepler Kit	
        - 450+
        - |link_kepler_kit|

Puoi anche acquistarli separatamente dai link sottostanti.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - COMPONENTE	
        - QUANTITÀ
        - LINK

    *   - 1
        - :ref:`cpn_pico_w`
        - 1
        - |link_picow_buy|
    *   - 2
        - Cavo Micro USB
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Diversi
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


**Schema**


|sch_guess_number|

Questo circuito è basato su :ref:`py_keypad` con l'aggiunta di un I2C LCD1602 per visualizzare i tasti premuti.


**Cablaggio**

|wiring_game_guess_number| 

Per semplificare il cablaggio, nel diagramma sopra, la riga delle colonne della tastiera a matrice e le resistenze da 10K sono inserite nei fori in cui si trovano G10 ~ G13 contemporaneamente.


**Codice**

.. note::

    * Apri il file ``7.7_game_guess_number.py`` nel percorso ``kepler-kit-main/micropython`` oppure copia questo codice in Thonny, quindi clicca su "Run Current Script" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra. 

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.

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

* Dopo che il codice è stato eseguito, premi ``A`` per iniziare il gioco. Viene prodotto un numero casuale ``point`` ma non viene visualizzato sul LCD, e ciò che devi fare è indovinarlo. 
* Il numero che hai digitato appare alla fine della prima riga fino a quando il calcolo finale è terminato. (Premi ``D`` per iniziare la comparazione.)
* L'intervallo numerico di ``point`` è visualizzato sulla seconda riga. E devi digitare il numero entro l'intervallo. 
* Quando digiti un numero, l'intervallo si restringe; se hai indovinato il numero fortunato fortunatamente o sfortunatamente, apparirà ``GAME OVER!``.

.. note:: 
    Se il codice e il cablaggio sono corretti, ma il display LCD non mostra ancora nulla, puoi regolare il potenziometro sul retro per aumentare il contrasto.

