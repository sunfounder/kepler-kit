.. note::

    Ciao, benvenuto nella Community SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e anteprime esclusive.
    - **Sconti Speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_rgb:

2.4 Luce Colorata
==============================================

Come sappiamo, la luce può essere sovrapposta. Ad esempio, mescolando la luce blu e quella verde si ottiene il ciano, mentre mescolando la luce rossa e quella verde si ottiene il giallo.
Questo è chiamato "Metodo additivo di miscelazione dei colori".

* `Additive color - Wikipedia <https://en.wikipedia.org/wiki/Additive_color>`_

Basandosi su questo metodo, possiamo utilizzare i tre colori primari per miscelare la luce visibile di qualsiasi colore secondo diverse proporzioni. Ad esempio, l'arancione può essere prodotto con più rosso e meno verde.

In questo capitolo, utilizzeremo il LED RGB per esplorare il mistero della miscelazione additiva dei colori!

Il LED RGB è equivalente a incapsulare un LED Rosso, un LED Verde e un LED Blu sotto un unico cappuccio, e i tre LED condividono un unico pin di catodo comune.
Poiché il segnale elettrico viene fornito per ogni pin di anodo, è possibile visualizzare la luce del colore corrispondente. Modificando l'intensità del segnale elettrico di ciascun anodo, è possibile produrre vari colori.

* :ref:`cpn_rgb`

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
        - 3(1-330Ω, 2-220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_rgb`
        - 1
        - |link_rgb_led_buy|

**Schema**

|sch_rgb|

I pin PWM GP13, GP14 e GP15 controllano rispettivamente i pin Rosso, Verde e Blu del LED RGB, e collegano il pin di catodo comune a GND. Questo permette al LED RGB di visualizzare un colore specifico sovrapponendo la luce su questi pin con diversi valori PWM.

**Collegamenti**

|img_rgb_pin|

Il LED RGB ha 4 pin: il pin lungo è il catodo comune, che di solito è collegato a GND; il pin a sinistra vicino al pin più lungo è il Rosso; e i due pin a destra sono Verde e Blu.

|wiring_rgb|

**Codice**

.. note::

    * Apri il file ``2.4_colorful_light.py`` nel percorso ``kepler-kit-main/micropython`` o copia questo codice in Thonny, poi clicca su "Esegui Script Corrente" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra.

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    red = machine.PWM(machine.Pin(13))
    green = machine.PWM(machine.Pin(14))
    blue = machine.PWM(machine.Pin(15))
    red.freq(1000)
    green.freq(1000)
    blue.freq(1000)

    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def color_to_duty(rgb_value):
        rgb_value = int(interval_mapping(rgb_value,0,255,0,65535))
        return rgb_value

    def color_set(red_value,green_value,blue_value):
        red.duty_u16(color_to_duty(red_value))
        green.duty_u16(color_to_duty(green_value))
        blue.duty_u16(color_to_duty(blue_value))

    color_set(255,128,0)

Qui, possiamo scegliere il nostro colore preferito in un software di disegno (come paint) e visualizzarlo con il LED RGB.

|img_take_color|

Scrivi il valore RGB in ``color_set()``, e potrai vedere il LED RGB illuminarsi con i colori che desideri.

**Come funziona?**

Per permettere ai tre colori primari di lavorare insieme, abbiamo definito una funzione ``color_set()``.

Attualmente, i pixel nell'hardware dei computer usano solitamente una rappresentazione a 24 bit. Ogni colore primario è suddiviso in 8 bit, e l'intervallo dei valori di colore è da 0 a 255. Ci sono 256 possibili combinazioni per ciascuno dei tre colori primari (non dimenticare di contare 0!), quindi 256 x 256 x 256 = 16.777.216 colori.
La funzione ``color_set()`` utilizza anche la notazione a 24 bit, quindi possiamo scegliere un colore più facilmente.

E poiché l'intervallo dei valori di ``duty_u16()`` è 0~65535 (anziché 0 a 255) quando si inviano segnali al LED RGB tramite PWM, abbiamo definito le funzioni ``color_to_duty()`` e ``interval_mapping()`` per mappare i valori di colore ai valori di duty.
