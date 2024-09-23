.. note::

    Ciao, benvenuto nella community di appassionati di SunFounder Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Accedi in anteprima agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ar_ac_buz:

3.1 - Beep
==================
Il buzzer attivo è un tipico dispositivo di uscita digitale, facile da usare quanto accendere un LED!

* :ref:`cpn_buzzer`

**Componenti Necessari**

In questo progetto, ci servono i seguenti componenti.

È sicuramente conveniente acquistare un intero kit, ecco il link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nome	
        - ELEMENTI IN QUESTO KIT
        - LINK PER L'ACQUISTO
    *   - Kepler Kit	
        - 450+
        - |link_kepler_kit|

Puoi anche acquistarli separatamente dai link qui sotto.


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - INTRODUZIONE COMPONENTE	
        - QUANTITÀ
        - LINK PER L'ACQUISTO

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
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 1(1KΩ)
        - |link_resistor_buy|
    *   - 7
        - Cicalino Attivo :ref:`cpn_buzzer`
        - 1
        - 

**Schema Elettrico**

|sch_buzzer|

Quando l'uscita GP15 è alta, dopo il resistore limitatore di corrente da 1K (per proteggere il transistor), l'S8050 (transistor NPN) condurrà, facendo suonare il buzzer.

Il ruolo dell'S8050 (transistor NPN) è quello di amplificare la corrente e rendere il suono del buzzer più forte. In realtà, puoi anche collegare il buzzer direttamente a GP15, ma noterai che il suono del buzzer sarà più basso.

**Cablaggio**

Nel kit sono inclusi due tipi di buzzer.
Dobbiamo usare il buzzer attivo. Girali, la parte posteriore sigillata (non il PCB esposto) è quella che vogliamo.

|img_buzzer|

Il buzzer necessita di un transistor per funzionare, qui utilizziamo l'S8050 (transistor NPN).

|wiring_beep|

**Codice**

.. note::

   * Puoi aprire il file ``3.1_beep.ino`` nel percorso ``kepler-kit-main/arduino/3.1_beep``.
   * Oppure copia questo codice nell'**Arduino IDE**.
   * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.


.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/62bf2c5d-9890-4f3a-b02a-119c2f6b0bf1/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Dopo l'esecuzione del codice, sentirai un bip ogni secondo.
