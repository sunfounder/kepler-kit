.. note::

    Ciao, benvenuto nella community SunFounder Raspberry Pi, Arduino & ESP32 Enthusiasts su Facebook! Approfondisci l'uso di Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni l'accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ar_joystick:

4.1 - Attivare il Joystick
==========================

Se giochi molto ai videogiochi, allora dovresti essere molto familiare con il joystick.
Viene solitamente utilizzato per muovere il personaggio, ruotare lo schermo, ecc.

Il principio alla base del joystick, che permette al computer di leggere le nostre azioni, è molto semplice.
Può essere considerato come composto da due potenziometri perpendicolari tra loro.
Questi due potenziometri misurano il valore analogico del joystick verticalmente e orizzontalmente, risultando in un valore (x,y) in un sistema di coordinate cartesiane piane.

Il joystick di questo kit ha anche un ingresso digitale, che si attiva quando il joystick viene premuto.

* :ref:`cpn_joystick`

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
        - :ref:`cpn_resistor`
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_joystick`
        - 1
        - 

**Schema Elettrico**

|sch_joystick|

Il pin SW è collegato a una resistenza pull-up da 10KΩ per ottenere un livello alto stabile sul pin SW (asse Z) quando il joystick non è premuto; altrimenti il pin SW sarebbe in uno stato di sospensione e il valore di uscita potrebbe variare tra 0 e 1.

**Cablaggio**

|wiring_joystick|

**Codice**

.. note::

   * Puoi aprire il file ``4.1_toggle_the_joyostick.ino`` nel percorso ``kepler-kit-main/arduino/4.1_toggle_the_joyostick``. 
   * Oppure copia questo codice nell'**Arduino IDE**.
   * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.

    

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/dfe53878-7cb4-4543-bb97-7f5ef5aad15a/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Dopo l'esecuzione del programma, la Shell stamperà i valori x,y,z del joystick.


* I valori degli assi x e y sono valori analogici che variano da 0 a 65535.
* L'asse Z è un valore digitale con uno stato di 1 o 0.
