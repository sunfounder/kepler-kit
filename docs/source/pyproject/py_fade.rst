.. note::

    Ciao, benvenuto nella Community di Appassionati di Raspberry Pi & Arduino & ESP32 di SunFounder su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa ai giveaway e alle promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_fade:

2.3 Dissolvenza del LED
===========================


Finora, abbiamo utilizzato solo due segnali di uscita: livello alto e livello basso (anche chiamati ON e OFF), che sono definiti come uscita digitale.
Tuttavia, nell'uso pratico, molti dispositivi non funzionano semplicemente con ON/OFF, ad esempio, per regolare la velocità di un motore o la luminosità di una lampada da tavolo.
In passato, per raggiungere questo obiettivo, veniva utilizzato un potenziometro per regolare la resistenza, ma questo metodo è inaffidabile e inefficiente.
Per risolvere questi problemi complessi, è stata sviluppata la modulazione a larghezza di impulso (PWM).

Un impulso è un'uscita digitale che contiene un livello alto e un livello basso. La larghezza dell'impulso può essere regolata cambiando la velocità di accensione e spegnimento.

Quando, in un breve periodo di tempo (ad esempio 20ms, che è il periodo di persistenza visiva per la maggior parte delle persone), accendiamo e spegniamo un LED ripetutamente, non noteremo che è stato spento, ma la luminosità della luce sarà leggermente inferiore.
Durante questo periodo, più tempo il LED rimane acceso, più diventa luminoso.
In altre parole, durante il ciclo, quanto più ampio è l'impulso, tanto maggiore è la "potenza del segnale elettrico" emessa dal microcontrollore.
Questo è il modo in cui la PWM controlla la luminosità del LED (o la velocità del motore).

* `Pulse-width modulation - Wikipedia <https://en.wikipedia.org/wiki/Pulse-width_modulation>`_

Ci sono alcuni punti da tenere a mente quando si utilizza la PWM con Pico W. Diamo un'occhiata a questa immagine.

|pin_pwm|

Pico W supporta PWM su ogni pin GPIO, ma in realtà ci sono 16 uscite PWM indipendenti (invece di 30), distribuite tra GP0 e GP15 sulla sinistra, e il PWM delle GPIO a destra è identico a quello di sinistra.

È importante evitare di impostare lo stesso canale PWM per scopi diversi durante la programmazione. Ad esempio, GP0 e GP16 condividono entrambi il PWM_0A.

Proviamo a ottenere l'effetto di dissolvenza del LED dopo aver compreso queste informazioni.

* :ref:`cpn_led`

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
        - 1(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|

**Schema**

|sch_led|

Questo progetto utilizza lo stesso circuito del primo progetto :ref:`py_led`, ma il tipo di segnale è diverso. Nel primo progetto, il GP15 emetteva direttamente livelli digitali alti e bassi (0&1) per accendere o spegnere i LED, mentre in questo progetto il GP15 emette un segnale PWM per controllare la luminosità del LED.

**Cablaggio**

|wiring_led|

**Codice**

.. note::

    * Apri il file ``2.3_fading_led.py`` nel percorso ``kepler-kit-main/micropython`` oppure copia questo codice in Thonny, quindi clicca su "Run Current Script" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra. 

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    led = machine.PWM(machine.Pin(15))
    led.freq(1000)

    for brightness in range(0,65535,50):
        led.duty_u16(brightness)
        utime.sleep_ms(10)
    led.duty_u16(0)

Il LED diventerà progressivamente più luminoso durante l'esecuzione del codice.

**Come Funziona?**

In questo esempio, cambiamo la luminosità del LED modificando il ciclo di lavoro dell'uscita PWM del GP15. Diamo un'occhiata a queste righe.

.. code-block:: python
    :emphasize-lines: 4,5,8

    import machine
    import utime

    led = machine.PWM(machine.Pin(15))
    led.freq(1000)

    for brightness in range(0,65535,50):
        led.duty_u16(brightness)
        utime.sleep_ms(10)
    led.duty_u16(0)

* ``led = machine.PWM(machine.Pin(15))`` imposta il pin GP15 come uscita PWM.

* La linea ``led.freq(1000)`` serve per impostare la frequenza PWM, qui è impostata a 1000Hz, il che significa che un ciclo dura 1ms (1/1000).

* La linea ``led.duty_u16()`` è utilizzata per impostare il ciclo di lavoro, che è un intero a 16 bit (2^16=65536). Un valore di 0 indica un ciclo di lavoro del 0%, il che significa che ogni ciclo ha 0% di tempo per emettere un livello alto, cioè tutti gli impulsi sono spenti. Il valore 65535 indica un ciclo di lavoro del 100%, il che significa che l'intero impulso è acceso, e il risultato è '1'. Quando è 32768, accenderà metà impulso, quindi il LED sarà luminoso a metà rispetto al massimo.

