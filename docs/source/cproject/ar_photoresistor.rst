.. note::

    Ciao, benvenuto nella community di appassionati di SunFounder Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a promozioni festive e giveaway.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ar_photoresistor:

2.12 - Percepire la luce
=================================
Il fotoresistore è un tipico dispositivo per ingressi analogici e viene utilizzato in modo molto simile a un potenziometro. Il suo valore di resistenza dipende dall'intensità della luce: più forte è la luce irradiata, minore sarà il suo valore di resistenza; al contrario, aumenterà.

* :ref:`cpn_photoresistor`

**Componenti necessari**

In questo progetto, abbiamo bisogno dei seguenti componenti.

È sicuramente conveniente acquistare un kit completo, ecco il link:

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
        - 1 (10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_photoresistor`
        - 1
        - |link_photoresistor_buy|

**Schema elettrico**

|sch_photoresistor|

In questo circuito, il resistore da 10K e il fotoresistore sono collegati in serie, e la corrente che li attraversa è la stessa. Il resistore da 10K funge da protezione, e il GP28 legge il valore dopo la conversione di tensione del fotoresistore.

Quando la luce aumenta, la resistenza del fotoresistore diminuisce, quindi la sua tensione diminuisce, e il valore letto da GP28 diminuirà; se la luce è sufficientemente intensa, la resistenza del fotoresistore sarà vicina a 0, e il valore di GP28 sarà vicino a 0. In questo caso, il resistore da 10K svolge un ruolo di protezione, impedendo che i 3,3V e il GND siano collegati insieme, causando un cortocircuito.

Se posizioni il fotoresistore in una situazione di oscurità, il valore di GP28 aumenterà. In una situazione di oscurità totale, la resistenza del fotoresistore sarà infinita, e la sua tensione sarà vicina a 3,3V (il resistore da 10K è trascurabile), e il valore di GP28 sarà vicino al valore massimo di 65535.

La formula di calcolo è mostrata qui sotto.

    (Vp/3.3V) x 65535 = Ap

**Cablaggio**

|wiring_photoresistor|

**Codice**

.. note::

   * Puoi aprire il file ``2.12_feel_the_light.ino`` nel percorso ``kepler-kit-main/arduino/2.12_feel_the_light``. 
   * Oppure copia questo codice nell'**Arduino IDE**.
   * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/44074b9e-3e4e-475b-af37-689254f87ab2/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Dopo l'esecuzione del programma, il Serial Monitor stamperà i valori del fotoresistore. Puoi puntarci una torcia o coprirlo con la mano per vedere come cambiano i valori.
