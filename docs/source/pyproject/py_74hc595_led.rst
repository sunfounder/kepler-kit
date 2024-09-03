.. note::

    Ciao, benvenuto nella Community di Appassionati di Raspberry Pi & Arduino & ESP32 di SunFounder su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa ai giveaway e alle promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_74hc_led:

5.1 Microchip - 74HC595
===========================

Il circuito integrato (integrated circuit) è un tipo di dispositivo elettronico o componente miniaturizzato, rappresentato dalla sigla "IC" nel circuito.

Viene utilizzato un certo processo per interconnettere transistor, resistori, condensatori, induttori e altri componenti e cablaggi necessari in un circuito, fabbricati su uno o più piccoli wafer semiconduttori o substrati dielettrici, e successivamente racchiusi in un involucro. Si crea così una microstruttura con le funzioni circuitali richieste; tutti i componenti sono strutturati come un insieme, rendendo i componenti elettronici un grande passo verso la miniaturizzazione, il basso consumo energetico, l'intelligenza e l'alta affidabilità.

Gli inventori dei circuiti integrati sono Jack Kilby (circuiti integrati basati sul germanio (Ge)) e Robert Norton Noyce (circuiti integrati basati sul silicio (Si)).

Questo kit è dotato di un IC, il 74HC595, che può notevolmente risparmiare l'uso dei pin GPIO.
In particolare, può sostituire 8 pin per l'output del segnale digitale scrivendo un numero binario a 8 bit.

* `Binary number - Wikipedia <https://en.wikipedia.org/wiki/Binary_number>`_

* :ref:`74HC595`

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
        - 8 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 8
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|

**Schema**

|sch_74hc_led|

* Quando MR (pin10) è a livello alto e OE (pin13) è a livello basso, i dati vengono inseriti al fronte di salita di SHcp e trasferiti al registro di memoria tramite il fronte di salita di SHcp.
* Se i due clock sono collegati insieme, il registro a scorrimento è sempre un impulso in anticipo rispetto al registro di memoria.
* Nel registro di memoria è presente un pin di ingresso a scorrimento seriale (Ds), un pin di uscita seriale (Q) e un pulsante di reset asincrono (a livello basso).
* Il registro di memoria emette un Bus con un'uscita parallela a 8 bit e in tre stati.
* Quando OE è abilitato (livello basso), i dati nel registro di memoria vengono emessi sul bus (Q0 ~ Q7).

**Cablaggio**

.. Il 74HC595 è un IC a 16 pin con una tacca semicircolare su un lato (di solito il lato sinistro dell'etichetta). Con la tacca rivolta verso l'alto, i suoi pin sono mostrati nel diagramma sottostante.


.. Fare riferimento alla figura sottostante per costruire il circuito.

|wiring_74hc_led|

.. 1. Collega 3V3 e GND del Pico W alla linea di alimentazione della breadboard.
.. #. Inserisci il 74HC595 nella breadboard attraverso la fessura centrale.
.. #. Collega il pin GP0 del Pico W al pin DS (pin 14) del 74HC595 con un cavo jumper.
.. #. Collega il pin GP1 del Pico W al pin STcp (pin 12) del 74HC595.
.. #. Collega il pin GP2 del Pico W al pin SHcp (pin 11) del 74HC595.
.. #. Collega il pin VCC (pin 16) e il pin MR (pin 10) sul 74HC595 alla linea di alimentazione positiva.
.. #. Collega il pin GND (pin 8) e il pin CE (pin 13) sul 74HC595 alla linea di alimentazione negativa.
.. #. Inserisci 8 LED sulla breadboard e i loro anodi sono rispettivamente collegati ai pin Q0~Q1 (15, 1, 2, 3, 4, 5, 6, 7) del 74HC595.
.. #. Collega i catodi dei LED con un resistore da 220Ω in serie alla linea di alimentazione negativa.

**Codice**

.. note::

    * Apri il file ``5.1_microchip_74hc595.py`` nel percorso ``kepler-kit-main/micropython`` oppure copia questo codice in Thonny, quindi clicca su "Run Current Script" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra.

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import time

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

    num = 0

    for i in range(16):
        if i < 8:
            num = (num<<1) + 1
        elif i>=8:
            num = (num & 0b01111111)<<1
        hc595_shift(num)
        print("{:0>8b}".format(num))
        time.sleep_ms(200)

Quando il programma è in esecuzione, ``num`` verrà scritto nel chip 74HC595 come numero binario a otto bit per controllare l'accensione e lo spegnimento degli 8 LED.
Possiamo vedere il valore corrente di ``num`` nella shell.

**Come Funziona?**

``hc595_shift()`` farà sì che il 74HC595 emetta 8 segnali digitali. Esso invia l'ultimo bit del numero binario a Q0, e il primo bit a Q7. In altre parole, scrivendo il numero binario "00000001" si farà in modo che Q0 emetta un livello alto e Q1~Q7 emettano un livello basso.
