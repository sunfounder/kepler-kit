.. note::

    Ciao, benvenuto nella Community di Appassionati di Raspberry Pi & Arduino & ESP32 di SunFounder su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa ai giveaway e alle promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_74hc_7seg:

5.2 Visualizzazione dei Numeri
=======================================

I display a 7 segmenti sono ovunque nella vita quotidiana.
Ad esempio, su un condizionatore d'aria, possono essere utilizzati per visualizzare la temperatura; su un indicatore di traffico, possono essere utilizzati per visualizzare un timer.

Il display a 7 segmenti è essenzialmente un dispositivo composto da 8 LED, di cui 7 LED a forma di striscia formano una figura a "8", e c'è un LED puntiforme leggermente più piccolo che funge da punto decimale. Questi LED sono contrassegnati come a, b, c, d, e, f, g e dp. Hanno i loro pin di anodo e condividono i catodi. Le loro posizioni dei pin sono mostrate nella figura qui sotto.

|img_7seg_cathode|

Questo significa che ha bisogno di essere controllato da 8 segnali digitali contemporaneamente per funzionare completamente e il 74HC595 può farlo.

* :ref:`cpn_7_segment`

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
        - 1 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_7_segment`
        - 1
        - |link_7segment_buy|
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|


**Schema**

|sch_74hc_7seg|

Qui il principio di cablaggio è fondamentalmente lo stesso di :ref:`py_74hc_led`, l'unica differenza è che Q0-Q7 sono collegati ai pin da a ~ g del display a 7 segmenti.

.. list-table:: Cablaggio
    :widths: 15 25
    :header-rows: 1

    *   - :ref:`cpn_74hc595`
        - Display a Segmenti :ref:`cpn_led`
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

**Cablaggio**

.. 1. Collega 3V3 e GND del Pico W alla linea di alimentazione della breadboard.
.. #. Inserisci il 74HC595 nella breadboard attraverso la fessura centrale.
.. #. Collega il pin GP0 del Pico W al pin DS (pin 14) del 74HC595 con un cavo jumper.
.. #. Collega il pin GP1 del Pico W al pin STcp (pin 12) del 74HC595.
.. #. Collega il pin GP2 del Pico W al pin SHcp (pin 11) del 74HC595.
.. #. Collega il pin VCC (pin 16) e il pin MR (pin 10) sul 74HC595 alla linea di alimentazione positiva.
.. #. Collega il pin GND (pin 8) e il pin CE (pin 13) sul 74HC595 alla linea di alimentazione negativa.
.. #. Inserisci il Display a Segmenti LED nella breadboard e collega un resistore da 220Ω in serie con il pin GND alla linea di alimentazione negativa.
.. #. Segui la tabella sottostante per collegare il 74HC595 e il Display a Segmenti LED.

|wiring_74hc_7seg|


**Codice**

.. note::

    * Apri il file ``5.2_number_display.py`` nel percorso ``kepler-kit-main/micropython`` oppure copia questo codice in Thonny, quindi clicca su "Run Current Script" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra. 

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.


.. code-block:: python

    import machine
    import time

    SEGCODE = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]

    sdi = machine.Pin(0,machine.Pin.OUT)
    rclk = machine.Pin(1,machine.Pin.OUT)
    srclk = machine.Pin(2,machine.Pin.OUT)

    def hc595_shift(dat): 
        rclk.low()
        time.sleep_ms(5)
        for bit in range(7, -1, -1):
            srclk.low()
            time.sleep_ms(5)
            value = 1 & (dat >> bit)
            sdi.value(value)
            time.sleep_ms(5)
            srclk.high()
            time.sleep_ms(5)
        time.sleep_ms(5)
        rclk.high()
        time.sleep_ms(5)
        
    while True:
        for num in range(10):
            hc595_shift(SEGCODE[num])
            time.sleep_ms(500)

Quando il programma è in esecuzione, vedrai il Display a Segmenti LED visualizzare i numeri da 0 a 9 in sequenza.

**Come Funziona?**

``hc595_shift()`` fa sì che il 74HC595 produca 8 segnali digitali.
Esso invia l'ultimo bit del numero binario a Q0, e il primo bit a Q7. In altre parole, scrivendo il numero binario "00000001" si fa in modo che Q0 emetta un livello alto e Q1~Q7 emettano un livello basso.

Supponiamo che il Display a 7 segmenti mostri il numero "1", dobbiamo impostare un livello alto per b e c, e un livello basso per a, d, e, f, g e dg.

|img_1_segment|

Questo significa che dobbiamo scrivere il numero binario "00000110". Per leggibilità, useremo la notazione esadecimale come "0x06".

* `Hexadecimal <https://en.wikipedia.org/wiki/Hexadecimal>`_

* `BinaryHex Converter <https://www.binaryhexconverter.com/binary-to-hex-converter>`_

Allo stesso modo, possiamo anche far visualizzare altri numeri al Display a Segmenti LED nello stesso modo. La tabella seguente mostra i codici corrispondenti a questi numeri.

.. list-table:: Codici delle Cifre
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

Scrivi questi codici in ``hc595_shift()`` per far visualizzare al Display a Segmenti LED i numeri corrispondenti.
