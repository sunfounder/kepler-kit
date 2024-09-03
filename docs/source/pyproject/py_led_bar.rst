.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_led_bar:

2.2 Visualizza il Livello
==============================

Il primo progetto consiste semplicemente nel far lampeggiare un LED. Per questo progetto, utilizziamo il LED Bar Graph, che contiene 10 LED in un involucro di plastica, generalmente usato per visualizzare i livelli di potenza o di volume.

|img_led_bar_pin|

* :ref:`cpn_led_bar`

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
        - 10 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led_bar`
        - 1
        - 

**Schema Elettrico**

|sch_ledbar|

Nel LED Bar Graph ci sono 10 LED, ciascuno dei quali può essere controllato singolarmente. L'anodo di ciascun LED è collegato ai pin GP6*GP15, mentre il catodo è collegato a una resistenza da 220 ohm, e poi a GND.

**Collegamenti**

|wiring_ledbar|

**Codice**

.. note::

    * Apri il file ``2.2_display_the_level.py`` nel percorso ``kepler-kit-main/micropython`` o copia questo codice in Thonny, poi clicca su "Esegui Script Corrente" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra.

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    pin = [6,7,8,9,10,11,12,13,14,15]
    led= []
    for i in range(10):
        led.append(None)
        led[i] = machine.Pin(pin[i], machine.Pin.OUT)

    while True:
        for i in range(10):
            led[i].toggle()
            utime.sleep(0.2)

Sul LED Bar Graph, vedrai i LED accendersi e poi spegnersi in sequenza quando il programma è in esecuzione.

**Come funziona?**

Il LED Bar è composto da dieci LED che sono controllati da dieci pin, il che significa che dobbiamo definire questi pin. Il processo sarebbe troppo noioso se li definissimo uno per uno. Quindi, qui utilizziamo le ``Liste``.

.. note::
    Le liste in Python sono uno dei tipi di dati più versatili che ci permettono di lavorare con più elementi contemporaneamente, e vengono create inserendo gli elementi tra parentesi quadre [], separati da virgole.

.. code-block:: python

    pin = [6,7,8,9,10,11,12,13,14,15]    

Questa riga di codice definisce una lista ``pin``, che contiene i dieci 
elementi ``6,7,8,9,10,11,12,13,14,15``. Possiamo usare l'operatore di 
indice [] per accedere a un elemento in una lista. In Python, gli indici 
iniziano da 0. Quindi, una lista con 10 elementi avrà un indice da 0 a 9. 
Usando questa lista come esempio, ``pin[0]`` è ``6`` e ``pin[4]`` è ``10``.

Successivamente, dichiara una lista vuota ``led`` che verrà utilizzata per 
definire dieci oggetti LED.

.. code-block:: python

    led = []    

A causa della lunghezza della lista, che è 0, le operazioni dirette sull'array, come 
stampare **led[0]**, non funzioneranno. Ci sono nuovi elementi che dobbiamo aggiungere.

.. code-block:: python

    led.append(None)

Come risultato di questo metodo ``append()``, la lista ``led`` ha il suo primo elemento, di lunghezza 1, e ``led[0]`` diventa un elemento valido nonostante il suo valore attuale sia ``None`` (che rappresenta nullo).

Il passo successivo è definire ``led[0]``, il LED collegato al pin 6, come il primo oggetto LED.

.. code-block:: python

    led[0] = machine.Pin(6, machine.Pin.OUT)

Il primo oggetto LED è stato ora definito.

Come puoi vedere, abbiamo creato i dieci numeri di pin come una lista **pin**, che possiamo sostituire in questa riga per facilitare le operazioni in blocco.

.. code-block:: python

    led[0] = machine.Pin(pin[0], machine.Pin.OUT)

Usa un'istruzione ``for`` per far eseguire a tutti i 10 pin l'istruzione sopra.

.. code-block:: python

    import machine

    pin = [6,7,8,9,10,11,12,13,14,15]
    led= []
    for i in range(10):
        led.append(None)
        led[i] = machine.Pin(pin[i], machine.Pin.OUT)

* :ref:`syntax_list`
* :ref:`syntax_forloop`

Usa un altro ciclo ``for`` per fare in modo che i dieci LED sul LED Bar cambino stato uno dopo l'altro.

.. code-block:: python

    for i in range(10):
        led[i].toggle()
        utime.sleep(0.2)

Il codice è completato mettendo il codice sopra in un ciclo while.

.. code-block:: python

    import machine
    import utime

    pin = [6,7,8,9,10,11,12,13,14,15]
    led= []
    for i in range(10):
        led.append(None)
        led[i] = machine.Pin(pin[i], machine.Pin.OUT)

    while True:
        for i in range(10):
            led[i].toggle()
            utime.sleep(0.2)


