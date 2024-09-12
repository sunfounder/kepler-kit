.. note::

    Ciao, benvenuto nella community di appassionati di SunFounder Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri entusiasti.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e affronta sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a promozioni festive e giveaway.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ar_neopixel:

3.3 - Striscia RGB WS2812
=============================

Il WS2812 è una sorgente luminosa LED a controllo intelligente in cui il circuito di controllo e il chip RGB sono integrati in un package di componenti 5050. 
Include internamente un circuito di aggancio dati della porta digitale intelligente e un circuito di amplificazione e rimodellazione del segnale. 
Include anche un oscillatore interno di precisione e una parte di controllo a corrente costante programmabile, 
garantendo efficacemente un'alta coerenza cromatica dei pixel.

Il protocollo di trasferimento dati utilizza una modalità di comunicazione NZR singola. 
Dopo il reset dell'alimentazione dei pixel, la porta DIN riceve i dati dal controller, il primo pixel raccoglie i dati iniziali a 24 bit e li invia all'aggancio dati interno; gli altri dati, rimodellati dal circuito di amplificazione del segnale interno, vengono inviati al pixel successivo attraverso la porta DO. Dopo la trasmissione di ogni pixel, il segnale si riduce di 24 bit. 
Il pixel adotta la tecnologia di trasmissione auto-rimodellante, il che rende il numero di pixel in cascata non limitato dalla trasmissione del segnale, dipendendo solo dalla velocità di trasmissione del segnale.

* :ref:`cpn_ws2812`

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
        - :ref:`cpn_ws2812`
        - 1
        - |link_ws2812_buy|

**Schema elettrico**

|sch_ws2812|

**Cablaggio**

|wiring_ws2812|


.. warning::
    Un aspetto a cui devi prestare attenzione è la corrente.

    Sebbene la striscia LED con qualsiasi numero di LED possa essere utilizzata nel Pico W, la potenza del suo pin VBUS è limitata.
    Qui utilizzeremo otto LED, che sono sicuri.
    Ma se vuoi usare più LED, devi aggiungere un'alimentazione separata.
    

**Codice**

.. note::

    * Puoi aprire il file ``3.3_rgb_led_strip.ino`` nel percorso ``kepler-kit-main/arduino/3.3_rgb_led_strip``. 
    * Oppure copia questo codice nell'**Arduino IDE**.
    * La libreria ``Adafruit_NeoPixel`` è utilizzata qui, puoi installarla dal **Library Manager**.

      .. image:: img/lib_neopixel.png

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/efe5d60f-ea0f-4446-bc5b-30c76197fedf/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


Selezioniamo alcuni colori preferiti e visualizziamoli sulla striscia LED RGB!

**Come funziona?**

Dichiara un oggetto di tipo Adafruit_NeoPixel, è connesso a ``PIXEL_PIN``, 
ci sono ``PIXEL_COUNT`` LED RGB sulla striscia.

.. code-block:: arduino

    #define PIXEL_PIN    0
    #define PIXEL_COUNT 8

    // Dichiara il nostro oggetto striscia NeoPixel:
    Adafruit_NeoPixel strip(PIXEL_COUNT, PIXEL_PIN, NEO_GRB + NEO_KHZ800);
    // Argomento 1 = Numero di pixel nella striscia NeoPixel
    // Argomento 2 = Numero di pin Arduino (la maggior parte sono validi)
    // Argomento 3 = Flag del tipo di pixel, somma secondo necessità:
    //   NEO_KHZ800  800 KHz bitstream (la maggior parte dei prodotti NeoPixel con LED WS2812)
    //   NEO_KHZ400  400 KHz (pixel classici 'v1' (non v2) FLORA, driver WS2811)
    //   NEO_GRB     I pixel sono cablati per il bitstream GRB (la maggior parte dei prodotti NeoPixel)
    //   NEO_RGB     I pixel sono cablati per il bitstream RGB (pixel FLORA v1, non v2)
    //   NEO_RGBW    I pixel sono cablati per il bitstream RGBW (prodotti NeoPixel RGBW)

Inizializza l'oggetto strip e imposta tutti i pixel su "spento".

Funzione
    * ``strip.begin()`` : Inizializza l'oggetto striscia NeoPixel (OBBLIGATORIO).
    * ``strip.setPixelColor(index, color)`` : Imposta il colore del pixel (nella RAM), il ``color`` deve essere un valore a 32 bit singolo 'packed'.
    * ``strip.Color(red, green, blue)`` : Colore come valore a 32 bit singolo 'packed'.
    * ``strip.show()`` : Aggiorna la striscia con i nuovi contenuti.
  
**Scopri di più**

Possiamo generare colori casuali e creare una luce colorata che scorre.

.. note::

   * Puoi aprire il file ``3.3_rgb_led_strip_flowing.ino`` nel percorso ``kepler-kit-main/arduino/3.3_rgb_led_strip_flowing``. 
   * Oppure copia questo codice nell'**Arduino IDE**.

   
    * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.

    

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/a3d7c520-b4f8-4445-9454-5fe7d2a24fd9/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


Oppure puoi far ciclare questa striscia LED WS2812 attraverso i colori dell'arcobaleno (intervallo 65535).

.. note::

   * Puoi aprire il file ``3.3_rgb_led_strip_rainbow.ino`` nel percorso ``kepler-kit-main/arduino/3.3_rgb_led_strip_rainbow``. 
   * Oppure copia questo codice nell'**Arduino IDE**.

   
   * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.

    

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/47d84804-3560-48fa-86df-49f8e2f6ad63/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>   


* ``strip.getPixelColor(index)`` : Interroga il colore di un pixel impostato in precedenza.
* ``strip.ColorHSV(pixelHue)`` : Converte tonalità, saturazione e valore in un colore RGB a 32 bit che può essere passato a ``setPixelColor()`` o altre funzioni compatibili con RGB.
* ``strip.gamma32()`` : Fornisce un colore più "vero" prima di assegnarlo a ciascun pixel.

