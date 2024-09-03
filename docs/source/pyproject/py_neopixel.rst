.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_neopixel:

3.3 Striscia LED RGB
=========================

Il WS2812 è una sorgente luminosa a LED con controllo intelligente che integra il circuito di controllo e il chip RGB in un unico pacchetto di componenti 5050.
Include internamente un latch digitale intelligente per la porta dati e un circuito di amplificazione e rimodellamento del segnale.
Include inoltre un oscillatore interno di precisione e una parte di controllo della corrente costante programmabile, 
garantendo efficacemente una coerenza elevata del colore della luce dei punti pixel.

Il protocollo di trasferimento dati utilizza una modalità di comunicazione NZR singola. 
Dopo il reset all'accensione del pixel, la porta DIN riceve i dati dal controller, il primo pixel raccoglie i primi 24 bit di dati che vengono inviati al latch dati interno, mentre gli altri dati, rimodellati dal circuito di amplificazione e rimodellamento del segnale interno, vengono inviati al pixel successivo attraverso la porta DO. Dopo la trasmissione di ciascun pixel, il segnale si riduce di 24 bit. 
I pixel adottano la tecnologia di trasmissione auto-rimodellata, rendendo il numero di pixel in cascata non limitato dalla trasmissione del segnale, ma solo dalla velocità di trasmissione del segnale.


* :ref:`cpn_ws2812`

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
        - :ref:`cpn_ws2812`
        - 1
        - |link_ws2812_buy|


**Schema Elettrico**

|sch_ws2812|


**Collegamenti**


|wiring_ws2812|

.. warning::
    Una cosa a cui devi prestare attenzione è la corrente.

    Sebbene la Striscia LED con qualsiasi numero di LED possa essere utilizzata con Pico W, la potenza del suo pin VBUS è limitata.
    Qui utilizzeremo otto LED, che sono sicuri.
    Ma se vuoi utilizzare più LED, devi aggiungere un'alimentazione separata.
    

**Codice**

.. note::

    * Apri il file ``3.3_rgb_led_strip.py`` nel percorso ``kepler-kit-main/micropython`` o copia questo codice in Thonny, poi clicca su "Esegui Script Corrente" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra.

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.
    
    * Qui è necessario utilizzare la libreria chiamata ``ws2812.py``, controlla se è stata caricata su Pico W, per un tutorial dettagliato fai riferimento a :ref:`add_libraries_py`.


.. code-block:: python

    import machine 
    from ws2812 import WS2812

    ws = WS2812(machine.Pin(0),8)

    ws[0] = [64,154,227]
    ws[1] = [128,0,128]
    ws[2] = [50,150,50]
    ws[3] = [255,30,30]
    ws[4] = [0,128,255]
    ws[5] = [99,199,0]
    ws[6] = [128,128,128]
    ws[7] = [255,100,0]
    ws.write()


Selezioniamo alcuni colori preferiti e visualizziamoli sulla Striscia LED RGB!

**Come funziona?**

Nella libreria ws2812, abbiamo integrato le funzioni correlate nella classe WS2812.

Puoi utilizzare la Striscia LED RGB con la seguente istruzione.

.. code-block:: python

    from ws2812 import WS2812

Dichiara un oggetto di tipo WS2812, chiamato "ws", è collegato al "pin", ci sono "number" LED RGB sulla striscia WS2812.

.. code-block:: python

    ws = WS2812(pin,number)

ws è un oggetto array, ogni elemento corrisponde a un LED RGB sulla striscia WS2812, ad esempio, ws[0] è il primo, ws[7] è l'ottavo.

Possiamo assegnare valori di colore a ciascun LED RGB, questi valori devono essere a 24 bit (rappresentati da sei cifre esadecimali) o una lista di 3 RGB a 8 bit.

Ad esempio, il valore rosso è "0xFF0000" o "[255,0,0]".

.. code-block:: python

    ws[i] = color value

Quindi utilizza questa istruzione per scrivere il colore sulla Striscia LED e accenderla.

.. code-block:: python

    ws.write()


Puoi anche utilizzare direttamente la seguente istruzione per far accendere tutti i LED dello stesso colore.

.. code-block:: python

    ws.write_all(color value)


**Approfondisci**

Possiamo generare colori casuali e creare una luce fluida e colorata.

.. note::

    * Apri il file ``3.3_rgb_led_strip_2.py`` nel percorso ``kepler-kit-main/micropython`` o copia questo codice in Thonny, poi clicca su "Esegui Script Corrente" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra.

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.

.. code-block:: python

    import machine 
    from ws2812 import WS2812
    import utime
    import urandom

    ws = WS2812(machine.Pin(0),8)

    def flowing_light():
        for i in range(7,0,-1):
            ws[i] = ws[i-1]
        ws[0] = int(urandom.uniform(0, 0xFFFFFF))  
        ws.write()
        utime.sleep_ms(80)

    while True:
        flowing_light()
        print(ws[0])