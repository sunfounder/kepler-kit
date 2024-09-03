.. note::

    Ciao, benvenuto nella Community SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e alle anteprime.
    - **Sconti Speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_transistor:

2.15 Due Tipi di Transistori
==========================================
Questo kit è dotato di due tipi di transistori, S8550 e S8050, il primo è un PNP e il secondo un NPN. Sono molto simili nell'aspetto, quindi dobbiamo controllare attentamente le loro etichette.
Quando un segnale di livello alto attraversa un transistor NPN, questo viene attivato. Un transistor PNP, invece, richiede un segnale di livello basso per essere gestito. Entrambi i tipi di transistor sono frequentemente utilizzati come interruttori senza contatto, proprio come in questo esperimento.

|img_NPN&PNP|

Utilizziamo un LED e un pulsante per capire come funziona un transistor!

:ref:`cpn_transistor`

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
        - 3(220Ω, 1KΩ, 10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_button`
        - 1
        - |link_button_buy|
    *   - 8
        - :ref:`cpn_transistor`
        - 1(S8050/S8550)
        - |link_transistor_buy|


**Connessione del transistor NPN (S8050)**

|sch_s8050|

In questo circuito, quando il pulsante viene premuto, GP14 diventa alto.

Programmare GP15 per emettere un segnale alto, dopo una resistenza limitatrice di corrente da 1k (per proteggere il transistor), permette al S8050 (transistor NPN) di condurre, consentendo così l'accensione del LED.

|wiring_s8050|

**Connessione del transistor PNP (S8550)**

|sch_s8550|

In questo circuito, GP14 è basso di default e diventerà alto quando il pulsante viene premuto.

Programmare GP15 per emettere un segnale **basso**, dopo una resistenza limitatrice di corrente da 1k (per proteggere il transistor), permette al S8550 (transistor PNP) di condurre, consentendo così l'accensione del LED.

L'unica differenza che noterai tra questo circuito e il precedente è che nel circuito precedente il catodo del LED è collegato al **collettore** del **S8050 (transistor NPN)**, mentre in questo è collegato all'**emettitore** del **S8550 (transistor PNP)**.

|wiring_s8550|


**Codice**

.. note::

    * Apri il file ``2.15_transistor.py`` nel percorso ``kepler-kit-main/micropython`` o copia questo codice in Thonny, poi clicca su "Esegui Script Corrente" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra.

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    button = machine.Pin(14, machine.Pin.IN)
    signal = machine.Pin(15, machine.Pin.OUT)    

    while True:
        button_status = button.value()
        if button_status== 1:
            signal.value(1)
        elif button_status == 0:
            signal.value(0)



I due tipi di transistori possono essere controllati con lo stesso codice. Quando premiamo il pulsante, Pico W invierà un segnale di livello alto al transistor; quando lo rilasciamo, invierà un segnale di livello basso.
Possiamo vedere che nei due circuiti si verificano fenomeni diametralmente opposti.

* Il circuito che utilizza il S8050 (transistor NPN) si accenderà quando il pulsante viene premuto, il che significa che sta ricevendo un circuito di conduzione ad alto livello;
* Il circuito che utilizza il S8550 (transistor PNP) si accenderà quando viene rilasciato, il che significa che sta ricevendo un circuito di conduzione a basso livello.
