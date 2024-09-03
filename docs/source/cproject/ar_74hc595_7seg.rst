.. note::

    Ciao, benvenuto nella community di appassionati di SunFounder Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Accedi in anteprima agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ar_74hc_7seg:

5.2 - Visualizzazione Numeri
==================================

Il display a 7 segmenti LED è molto comune nella vita quotidiana.
Ad esempio, in un condizionatore d'aria, può essere utilizzato per visualizzare la temperatura; in un indicatore stradale, può essere usato per mostrare un timer.

Il display a 7 segmenti LED è essenzialmente un dispositivo composto da 8 LED, di cui 7 a forma di striscia formano la figura di un "8", e un LED puntiforme più piccolo funge da punto decimale. Questi LED sono etichettati come a, b, c, d, e, f, g, e dp. Ogni LED ha un proprio pin di anodo e condivide il catodo. La disposizione dei pin è mostrata nella figura sottostante.

|img_7seg_cathode|

Questo significa che per funzionare completamente, il display deve essere controllato da 8 segnali digitali contemporaneamente, e il 74HC595 può gestire questa operazione.

* :ref:`cpn_7_segment`


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
        - Alcuni
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_resistor`
        - 1(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_7_segment`
        - 1
        - |link_7segment_buy|
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|

**Schema Elettrico**

|sch_74hc_7seg|

**Cablaggio**

|wiring_74hc_7seg|


.. list-table:: Cablaggio
    :widths: 15 25
    :header-rows: 1

    *   - :ref:`cpn_74hc595`
        - :ref:`cpn_led` Segment Display
    *   - Q0
        - a
    *   - Q1
        - b
    *   - Q2
        - c
    *   - Q3
        - d
    *   - Q4
        - e
    *   - Q5
        - f
    *   - Q6
        - g
    *   - Q7
        - dp


**Codice**

.. note::

   * Puoi aprire il file ``5.2_number_display.ino`` nel percorso ``kepler-kit-main/arduino/5.2_number_display``.
   * Oppure copia questo codice nell'**Arduino IDE**.
   * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.


.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/a237801f-40d7-4920-80fb-a349307b1e05/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>
    
Quando il programma è in esecuzione, vedrai il display a 7 segmenti LED visualizzare i numeri da 0 a 9 in sequenza.

**Come funziona?**

``shiftOut()`` farà in modo che il 74HC595 emetta 8 segnali digitali.
Il bit più basso del numero binario sarà emesso su Q0, mentre il bit più alto su Q7. In altre parole, scrivendo il numero binario "00000001", Q0 emetterà un livello alto e Q1~Q7 emetteranno un livello basso.

Supponiamo che il display a 7 segmenti debba mostrare il numero "1", dobbiamo impostare un livello alto su b, c, e un livello basso su a, d, e, f, g e dp.
Quindi, il numero binario "00000110" deve essere scritto. Per migliorare la leggibilità, utilizzeremo la notazione esadecimale "0x06".

* `Hexadecimal <https://en.wikipedia.org/wiki/Hexadecimal>`_

* `BinaryHex Converter <https://www.binaryhexconverter.com/binary-to-hex-converter>`_

Allo stesso modo, possiamo fare in modo che il display a 7 segmenti LED mostri altri numeri nello stesso modo. La tabella seguente mostra i codici corrispondenti a questi numeri.

.. list-table:: Codici Caratteri
    :widths: 20 20 20
    :header-rows: 1

    *   - Numeri	
        - Codice Binario
        - Codice Esadecimale
    *   - 0	
        - 00111111	
        - 0x3f
    *   - 1	
        - 00000110	
        - 0x06
    *   - 2	
        - 01011011	
        - 0x5b
    *   - 3	
        - 01001111	
        - 0x4f
    *   - 4	
        - 01100110	
        - 0x66
    *   - 5	
        - 01101101	
        - 0x6d
    *   - 6	
        - 01111101	
        - 0x7d
    *   - 7	
        - 00000111	
        - 0x07
    *   - 8	
        - 01111111	
        - 0x7f
    *   - 9	
        - 01101111	
        - 0x6f

Scrivi questi codici in ``shiftOut()`` per far visualizzare i numeri corrispondenti sul display a 7 segmenti.
