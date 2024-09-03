.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_keypad:

4.2 Tastiera 4x4
========================

La tastiera 4x4, nota anche come tastiera a matrice, è un insieme di 16 tasti disposti in un unico pannello.

La tastiera si trova su dispositivi che richiedono principalmente input digitali, come calcolatrici, telecomandi, telefoni a pulsanti, distributori automatici, bancomat, serrature a combinazione e serrature digitali per porte.

In questo progetto, impareremo a determinare quale tasto è stato premuto e a ottenere il valore corrispondente.

* :ref:`cpn_keypad`
* `E.161 - Wikipedia <https://en.wikipedia.org/wiki/E.161>`_

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

**Schema Elettrico**

|sch_keypad|

Sono collegati 4 resistori di pull-down a ciascuna delle colonne della tastiera a matrice, in modo che i pin G6 ~ G9 abbiano un livello basso stabile quando i tasti non sono premuti.

Le righe della tastiera (G2 ~ G5) sono programmate per andare in alto; se uno dei pin G6 ~ G9 legge alto, allora sappiamo quale tasto è stato premuto.

Ad esempio, se G6 legge alto, allora è stato premuto il tasto numerico 1; questo perché i pin di controllo del tasto numerico 1 sono G2 e G6, quando il tasto numerico 1 è premuto, G2 e G6 vengono collegati insieme e anche G6 legge alto.

**Collegamenti**

|wiring_keypad|

Per semplificare il cablaggio, nello schema sopra, la riga delle colonne della tastiera a matrice e i resistori da 10KΩ sono inseriti contemporaneamente nei fori dove sono situati i pin G6 ~ G9.


**Codice**

.. note::

    * Apri il file ``4.2_4x4_keypad.py`` nel percorso ``kepler-kit-main/micropython`` o copia questo codice in Thonny, poi clicca su "Esegui Script Corrente" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra.

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.

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

Dopo l'esecuzione del programma, la Shell stamperà i tasti che hai premuto sulla tastiera.

**Come funziona**

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

Dichiara ciascun tasto della tastiera a matrice nell'array ``characters[]`` e definisci i pin su ogni riga e colonna.

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

Questa è la parte della funzione principale che legge e stampa il valore del tasto.

La funzione ``readKey()`` leggerà lo stato di ogni tasto.

Le istruzioni ``if current_key != None`` e ``if current_key == last_key`` 
vengono utilizzate per verificare se un tasto è stato premuto e lo stato del tasto premuto. 
(Se premi \'3\' mentre hai già premuto \'1\', la verifica sarà valida.)

Stampa il valore del tasto premuto attualmente quando la condizione è valida.

L'istruzione ``last_key = current_key`` assegna lo stato di ogni verifica 
a un array ``last_key`` per facilitare il prossimo ciclo di verifica condizionale.

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

Questa funzione assegna un livello alto a ciascuna riga a turno, e quando viene premuto il tasto, 
la colonna in cui si trova il tasto ottiene un livello alto. 
Dopo che il ciclo a due livelli è stato verificato, il valore del tasto il cui stato è 1 viene memorizzato nell'array ``key`` .

Se premi il tasto \'3\':

|img_keypad_pressed|


``row[0]`` viene impostato su livello alto, e ``col[2]`` ottiene livello alto.

``col[0]``, ``col[1]``, ``col[3]`` ottengono livello basso.

Ci sono quattro stati: 0, 0, 1, 0; e scriviamo \'3\' in ``pressed_keys``.

Quando ``row[1]`` , ``row[2]`` , ``row[3]`` sono impostati su livello alto,
``col[0]`` ~ ``col[4]`` ottengono livello basso.


Il ciclo si ferma, e ritorna key = \'3\'.

Se premi i tasti \'1\' e \'3\', ritornerà key = [\'1\',\'3\'].
