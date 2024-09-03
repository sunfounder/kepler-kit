.. note::

    Ciao, benvenuto nella community di appassionati di SunFounder Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anteprima agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ar_fade:

2.3 - Dissolvenza LED
=====================

Finora, abbiamo utilizzato solo due segnali di uscita: livello alto e livello basso (o chiamati 1 e 0, ON e OFF), che sono detti uscita digitale.
Tuttavia, nell'uso reale, molti dispositivi non funzionano semplicemente accendendosi o spegnendosi, ad esempio, regolare la velocità di un motore, o la luminosità di una lampada da scrivania.
In passato, si utilizzava un cursore che poteva regolare la resistenza per ottenere questo scopo, ma questo metodo era spesso inaffidabile e inefficiente.
Perciò, la modulazione di larghezza di impulso (PWM) è emersa come una soluzione efficace a questi problemi complessi.

Un'uscita digitale composta da un livello alto e un livello basso è detta impulso. La larghezza di impulso di questi pin può essere regolata cambiando la velocità ON/OFF.

In parole povere, quando in un breve periodo (come 20ms, il tempo di persistenza visiva della maggior parte delle persone),
si fa accendere, spegnere e riaccendere il LED, non vedremo che è stato spento, ma la luminosità della luce sarà leggermente più debole.
Durante questo periodo, più tempo il LED rimane acceso, maggiore sarà la sua luminosità.
In altre parole, nel ciclo, più largo è l'impulso, maggiore sarà la "forza del segnale elettrico" emesso dal microcontrollore.
Questo è il modo in cui PWM controlla la luminosità del LED (o la velocità del motore).

* `Pulse-width modulation - Wikipedia <https://en.wikipedia.org/wiki/Pulse-width_modulation>`_

Ci sono alcuni punti a cui prestare attenzione quando Pico W utilizza il PWM. Diamo un'occhiata a questa immagine.

|pin_pwm|

Ogni pin GPIO di Pico W supporta il PWM, ma in realtà ha un totale di 16 uscite PWM indipendenti (invece di 30), distribuite tra GP0 e GP15 a sinistra, e l'uscita PWM dei GPIO a destra è equivalente a una copia di quella a sinistra.

Dobbiamo prestare attenzione a evitare di impostare lo stesso canale PWM per scopi diversi durante la programmazione. (Ad esempio, GP0 e GP16 condividono entrambi PWM_0A)

Dopo aver compreso queste informazioni, proviamo a ottenere l'effetto della dissolvenza LED.

* :ref:`cpn_led`

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

**Schema Elettrico**

|sch_led|

Questo progetto utilizza lo stesso circuito del primo progetto :ref:`ar_led`, ma con un tipo di segnale diverso. Nel primo progetto, si è utilizzata l'uscita digitale di livelli alti e bassi (0 e 1) direttamente da GP15 per accendere o spegnere i LED, mentre in questo progetto si utilizza il segnale PWM da GP15 per controllare la luminosità del LED.



**Cablaggio**


|wiring_led|


**Codice**


.. note::

   * Puoi aprire il file ``2.3_fading_led.ino`` nel percorso ``kepler-kit-main/arduino/2.3_fading_led``. 
   * Oppure copia questo codice nell'**Arduino IDE**.


    * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.



.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/86807da4-4714-4d3c-b6af-0f1b9a62223b/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


Il LED diventerà gradualmente più luminoso man mano che il programma viene eseguito.

**Come funziona?**

Dichiara il pin 15 come ledPin.

.. code-block:: C

    const int ledPin = 15;

``analogWrite()`` in ``loop()`` assegna a ledPin un valore analogico (onda PWM) compreso tra 0 e 255 per cambiare la luminosità del LED.

.. code-block:: C

    analogWrite(ledPin, value);

Utilizzando un ciclo for, il valore di ``analogWrite()`` può essere cambiato gradualmente tra il valore minimo (0) e il valore massimo (255).

.. code-block:: C

    for (int value = 0 ; value <= 255; value += 5) {
        analogWrite(ledPin, value);
    }

Per vedere chiaramente il fenomeno sperimentale, è necessario aggiungere un ``delay(30)`` al ciclo for per controllare il tempo di variazione della luminosità.

.. code-block:: C

    for (int value = 0 ; value <= 255; value += 5) {
        analogWrite(ledPin, value);
        delay(30);
    }
