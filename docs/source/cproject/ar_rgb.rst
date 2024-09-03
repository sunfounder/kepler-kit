.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a promozioni festive e giveaway.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ar_rgb:

2.4 - Luce Colorata
==============================================

Come sappiamo, la luce può essere sovrapposta. Ad esempio, mescolando la luce blu e verde si ottiene una luce ciano, mentre mescolando la luce rossa e verde si ottiene una luce gialla.
Questo processo è chiamato "Metodo additivo di miscelazione dei colori".

* `Additive color - Wikipedia <https://en.wikipedia.org/wiki/Additive_color>`_

Basandoci su questo metodo, possiamo utilizzare i tre colori primari per miscelare la luce visibile di qualsiasi colore variando le proporzioni. Ad esempio, l'arancione può essere prodotto con più rosso e meno verde.

In questo capitolo, utilizzeremo un LED RGB per esplorare il mistero della miscelazione additiva dei colori!

Un LED RGB è equivalente a incapsulare un LED Rosso, un LED Verde e un LED Blu sotto un'unica copertura, e i tre LED condividono un unico pin catodico.
Poiché il segnale elettrico viene fornito a ciascun pin anodico, è possibile visualizzare la luce del colore corrispondente. Variando l'intensità del segnale elettrico su ciascun anodo, si possono ottenere diversi colori.

* :ref:`cpn_rgb`

**Componenti Necessari**

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
        - 3(1-330Ω, 2-220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_rgb`
        - 1
        - |link_rgb_led_buy|

**Schema**

|sch_rgb|

I pin PWM GP13, GP14 e GP15 controllano rispettivamente i pin Rosso, Verde e Blu del LED RGB, e collegano il pin catodico comune a GND. Questo permette al LED RGB di visualizzare un colore specifico sovrapponendo la luce su questi pin con diversi valori PWM.

**Cablaggio**

|img_rgb_pin|

Un LED RGB ha 4 pin: il pin più lungo è il pin catodico comune, che è solitamente collegato a GND, il pin a sinistra accanto al pin più lungo è il Rosso, e i 2 pin a destra sono il Verde e il Blu.

|wiring_rgb|

**Codice**

Qui, possiamo scegliere il nostro colore preferito in un software di disegno (come Paint) e visualizzarlo con il LED RGB.

.. note::

   * Puoi aprire il file ``2.4_colorful_light.ino`` nel percorso ``kepler-kit-main/arduino/2.4_colorful_light``. 
   * Oppure copia questo codice nell'**Arduino IDE**.

    * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/c869191c-026c-4aac-8396-09eaf6ee2204/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

|img_take_color|

Scrivi il valore RGB in ``color_set()``, e potrai vedere il LED RGB accendersi con i colori che desideri.

**Come funziona?**

In questo esempio, la funzione utilizzata per assegnare valori ai tre pin del LED RGB è incapsulata in una sottoprocedura indipendente ``color()``.

.. code-block:: C

    void color (unsigned char red, unsigned char green, unsigned char blue)
    {
        analogWrite(redPin, red);
        analogWrite(greenPin, green);
        analogWrite(bluePin, blue);
    }

In ``loop()``, il valore RGB funziona come argomento di input per chiamare la funzione ``color()`` e realizzare così che il LED RGB possa emettere diversi colori.

.. code-block:: C

    void loop() 
    {    
        color(255, 0, 0); //  rosso 
        delay(1000); 
        color(0, 255, 0); //  verde  
        delay(1000);  
        color(0, 0, 255); //  blu  
        delay(1000);
    }
    
