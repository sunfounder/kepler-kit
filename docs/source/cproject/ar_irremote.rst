.. note::

    Ciao, benvenuto nella community SunFounder Raspberry Pi, Arduino & ESP32 Enthusiasts su Facebook! Approfondisci l'uso di Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni l'accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ar_irremote:


6.4 - Telecomando a Infrarossi (IR)
=======================================

Nell'elettronica di consumo, i telecomandi vengono utilizzati per operare dispositivi come televisori e lettori DVD.
In alcuni casi, i telecomandi permettono alle persone di controllare dispositivi fuori dalla loro portata, come i condizionatori d'aria centralizzati.

Il ricevitore IR è un componente con fotocellula sintonizzato per ricevere la luce a infrarossi.
È quasi sempre utilizzato per la rilevazione dei telecomandi - ogni TV e lettore DVD ne ha uno nella parte anteriore per ricevere il segnale IR dal telecomando.
All'interno del telecomando c'è un LED IR corrispondente, che emette impulsi IR per dire alla TV di accendersi, spegnersi o cambiare canale.

* :ref:`cpn_ir_receiver`

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
        - :ref:`cpn_ir_receiver`
        - 1
        - |link_receiver_buy|

**Schema Elettrico**

|sch_irrecv|

**Cablaggio**

|wiring_irrecv|


**Codice**

.. note::

    * Puoi aprire il file ``6.4_ir_remote_control.ino`` nel percorso ``kepler-kit-main/arduino/6.4_ir_remote_control``. 
    * Oppure copia questo codice nell'**Arduino IDE**.
    * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.
    * Qui viene utilizzata la libreria ``IRsmallDecoder``. Fai riferimento a :ref:`add_libraries_ar` per aggiungerla all'Arduino IDE.


.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/71f50561-d1ad-4d9e-9db2-8eb7727df0a4/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


Il nuovo telecomando ha un pezzo di plastica all'estremità per isolare la batteria interna. È necessario rimuovere questo pezzo di plastica per alimentare il telecomando quando lo utilizzi.
Una volta che il programma è in esecuzione, quando premi il telecomando, il Serial Monitor stamperà il tasto che hai premuto.


.. **How it works?**


