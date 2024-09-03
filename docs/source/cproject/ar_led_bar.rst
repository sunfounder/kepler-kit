.. note::

    Ciao, benvenuto nella community SunFounder Raspberry Pi, Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni l'accesso anticipato agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a giveaway e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ar_led_bar:

2.2 - Visualizza il Livello
=================================

Il primo progetto consiste semplicemente nel far lampeggiare il LED. In questo progetto utilizziamo il LED Bar Graph, composto da 10 LED racchiusi in un involucro di plastica, generalmente usato per visualizzare livelli di potenza o volume.

|img_led_bar_pin|

* :ref:`cpn_led_bar`

**Componenti Necessari**

In questo progetto ci servono i seguenti componenti.

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
        - 10(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led_bar`
        - 1
        - 

**Schema Elettrico**

|sch_ledbar|

Il LED Bar Graph contiene 10 LED, ognuno dei quali è controllabile singolarmente. Qui, l'anodo di ciascuno dei 10 LED è collegato ai pin GP6~GP15, mentre il catodo è collegato a una resistenza da 220Ω, e poi a GND.

**Cablaggio**

|wiring_ledbar|

**Codice**

.. note::

   * Puoi aprire il file ``2.2_display_the_level.ino`` nel percorso ``kepler-kit-main/arduino/2.2_display_the_level``. 
   * Oppure copia questo codice nell'**Arduino IDE**.


   * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/ae60e723-430e-4a58-ac39-566b9d1828e8/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>
    

Quando il programma è in esecuzione, vedrai i LED del LED Bar Graph accendersi e spegnersi in sequenza.

**Come Funziona?**

Ognuno dei dieci LED sul LED Bar deve essere controllato da un pin, il che significa che dobbiamo definire questi dieci pin.

Il codice in ``setup()`` utilizza un ciclo for per inizializzare i pin 6~15 in modalità output a turno.

.. code-block:: C

    for(int i=6;i<=15;i++)
    {
        pinMode(i,OUTPUT);
    }   

Il ciclo for è utilizzato in ``loop()`` per far lampeggiare i LED (accensione per 0.5s, poi spegnimento per 0.5s) in sequenza.

.. code-block:: C

    for(int i=6;i<=15;i++)
    {
        digitalWrite(i,HIGH);
        delay(500);
        digitalWrite(i,LOW);
        delay(500);    
    }