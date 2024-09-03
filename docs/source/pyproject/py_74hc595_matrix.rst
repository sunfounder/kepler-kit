.. note::

    Ciao, benvenuto nella Community di Appassionati di Raspberry Pi & Arduino & ESP32 di SunFounder su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa ai giveaway e alle promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_74hc_788bs:

5.4 Grafica 8x8 Pixel
=============================

La matrice LED è un display a matrice di punti a bassa risoluzione che utilizza una griglia di diodi emettitori di luce come pixel per visualizzare schemi.

Sono abbastanza luminosi da essere visibili alla luce del sole e puoi vederli in alcuni negozi, cartelloni pubblicitari, insegne e display a messaggi variabili (come quelli sui veicoli del trasporto pubblico).

In questo kit viene utilizzata una matrice a punti 8x8 con 16 pin. I loro anodi sono collegati in righe e i loro catodi sono collegati in colonne (a livello del circuito), che insieme controllano questi 64 LED.

Per accendere il primo LED, dovresti fornire un livello alto per Row1 e un livello basso per Col1. Per accendere il secondo LED, dovresti fornire un livello alto per Row1, un livello basso per Col2, e così via.
Controllando la corrente attraverso ogni coppia di righe e colonne, ogni LED può essere controllato individualmente per visualizzare caratteri o immagini.

* :ref:`cpn_dot_matrix`
* :ref:`cpn_74hc595`

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
        - :ref:`cpn_dot_matrix`
        - 1
        - 
    *   - 6
        - :ref:`cpn_74hc595`
        - 2
        - |link_74hc595_buy|

**Schema**

|sch_ledmatrix|

La matrice a punti 8x8 è controllata da due chip 74HC595, uno controlla le righe e l'altro le colonne, mentre questi due chip condividono G18~G20, il che consente di risparmiare notevolmente le porte I/O della scheda Pico W.

Pico W deve emettere un numero binario a 16 bit alla volta, i primi 8 bit vengono inviati al 74HC595 che controlla le righe e gli ultimi 8 bit vengono inviati al 74HC595 che controlla le colonne, in modo che la matrice di punti possa visualizzare un pattern specifico.

Q7': Pin di uscita in serie, collegato a DS di un altro 74HC595 per collegare più 74HC595 in serie.

**Cablaggio**

Costruisci il circuito. Poiché il cablaggio è complicato, facciamolo passo dopo passo.

**Passo 1:** Innanzitutto, inserisci il Pico W, la matrice a punti LED e due 
chip 74HC595 nella breadboard. Collega i 3,3V e GND del Pico W ai fori sui due 
lati della scheda, quindi collega i pin16 e 10 dei due chip 74HC595 a VCC, i 
pin 13 e 8 a GND.

.. note::
   Nell'immagine Fritzing sopra, il lato con l'etichetta si trova in basso.

|wiring_ledmatrix_4|

**Passo 2:** Collega il pin 11 dei due 74HC595 insieme, quindi a GP20; quindi il 
pin 12 dei due chip, e a GP19; successivamente, il pin 14 del 74HC595 sul lato 
sinistro a GP18 e il pin 9 al pin 14 del secondo 74HC595.

|wiring_ledmatrix_3|

**Passo 3:** Il 74HC595 sul lato destro serve a controllare le colonne della 
matrice a punti LED. Vedi la tabella qui sotto per la mappatura. Pertanto, i 
pin Q0-Q7 del 74HC595 sono mappati rispettivamente con i pin 13, 3, 4, 10, 6, 
11, 15 e 16.

+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **74HC595**        | **Q0** | **Q1** | **Q2** | **Q3** | **Q4** | **Q5** | **Q6** | **Q7** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **LED Dot Matrix** | **13** | **3**  | **4**  | **10** | **6**  | **11** | **15** | **16** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+

|wiring_ledmatrix_2|

**Passo 4:** Ora collega le RIGHE della matrice LED. Il 74HC595 sul lato sinistro 
controlla le RIGHE della matrice LED. Vedi la tabella qui sotto per la mappatura. 
Possiamo vedere che i pin Q0-Q7 del 74HC595 sul lato sinistro sono mappati 
rispettivamente con i pin 9, 14, 8, 12, 1, 7, 2 e 5.

+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **74HC595**        | **Q0** | **Q1** | **Q2** | **Q3** | **Q4** | **Q5** | **Q6** | **Q7** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **LED Dot Matrix** | **9**  | **14** | **8**  | **12** | **1**  | **7**  | **2**  | **5**  |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+

|wiring_ledmatrix_1|

**Codice**

.. note::

    * Apri il file ``5.4_8x8_pixel_graphics.py`` nel percorso ``kepler-kit-main/micropython`` oppure copia questo codice in Thonny, quindi clicca su "Run Current Script" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra.

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import time

    sdi = machine.Pin(18,machine.Pin.OUT)
    rclk = machine.Pin(19,machine.Pin.OUT)
    srclk = machine.Pin(20,machine.Pin.OUT)


    glyph = [0xFF,0xBB,0xD7,0xEF,0xD7,0xBB,0xFF,0xFF]

    # Shift the data to 74HC595
    def hc595_in(dat):
        for bit in range(7,-1, -1):
            srclk.low()
            time.sleep_us(30)
            sdi.value(1 & (dat >> bit))
            time.sleep_us(30)
            srclk.high()

    def hc595_out():
        rclk.high()
        time.sleep_us(200)
        rclk.low()

    while True:
        for i in range(0,8):
            hc595_in(glyph[i])
            hc595_in(0x80>>i)
            hc595_out()

Una volta avviato il programma, vedrai un grafico **x** visualizzato sulla matrice a punti 8x8.

**Come Funziona?**

Qui usiamo due 74HC595 per fornire segnali per le righe e le colonne della matrice a punti.
Il metodo per fornire i segnali è lo stesso di ``hc595_shift(dat)`` nei capitoli precedenti, ma la differenza è che qui dobbiamo scrivere un numero binario a 16 bit alla volta.
Quindi abbiamo suddiviso ``hc595_shift(dat)`` in due funzioni ``hc595_in(dat)`` e ``hc595_out()``.

.. code-block:: python

    def hc595_in(dat):
        for bit in range(7,-1, -1):
            srclk.low()
            time.sleep_us(30)
            sdi.value(1 & (dat >> bit))
            time.sleep_us(30)
            srclk.high()

    def hc595_out():
        rclk.high()
        time.sleep_us(200)
        rclk.low()

Successivamente, chiama ``hc595_in(dat)`` due volte nel loop principale, scrivi due numeri binari a 8 bit e poi chiama ``hc595_out()`` in modo che venga visualizzato un pattern.

Tuttavia, poiché i LED nella matrice a punti utilizzano poli comuni, controllare più righe/più colonne contemporaneamente causerà interferenze (ad esempio, se accendi contemporaneamente (1,1) e (2,2), inevitabilmente si accenderanno insieme anche (1,2) e (2,1)).
Pertanto, è necessario attivare una colonna (o una riga) alla volta, ciclare 8 volte e utilizzare il principio della persistenza dell'immagine per far sì che l'occhio umano fonda 8 pattern, ottenendo così un'immagine contenente una quantità di informazioni 8x8.

.. code-block:: python

    while True:
        for i in range(0,8):
            hc595_in(glyph[i])
            hc595_in(0x80>>i)
            hc595_out()

In questo esempio, la funzione principale annida un ciclo ``for``, e quando ``i`` è 1, solo la prima riga viene attivata (il chip di controllo della riga riceve il valore ``0x80``) e l'immagine della prima riga viene scritta. 
Quando ``i`` è 2, viene attivata la seconda riga (il chip di controllo della riga riceve il valore ``0x40``) e l'immagine della seconda riga viene scritta. E così via, completando 8 uscite.

A proposito, come per il display a 7 segmenti a 4 cifre, è necessario mantenere il tasso di aggiornamento per evitare sfarfallii agli occhi umani, quindi si dovrebbe evitare il più possibile il ``sleep()`` aggiuntivo nel loop principale.

**Approfondimenti**

Prova a sostituire ``glyph`` con il seguente array e guarda cosa appare!

.. code-block:: python

    glyph1 = [0xFF,0xEF,0xC7,0xAB,0xEF,0xEF,0xEF,0xFF]
    glyph2 = [0xFF,0xEF,0xEF,0xEF,0xAB,0xC7,0xEF,0xFF]
    glyph3 = [0xFF,0xEF,0xDF,0x81,0xDF,0xEF,0xFF,0xFF]
    glyph4 = [0xFF,0xF7,0xFB,0x81,0xFB,0xF7,0xFF,0xFF]
    glyph5 = [0xFF,0xBB,0xD7,0xEF,0xD7,0xBB,0xFF,0xFF]
    glyph6 = [0xFF,0xFF,0xF7,0xEB,0xDF,0xBF,0xFF,0xFF]

Oppure, puoi provare a disegnare i tuoi grafici.
