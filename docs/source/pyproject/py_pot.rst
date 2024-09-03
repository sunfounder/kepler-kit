.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_pot:

2.11 Ruota la Manopola
===========================

Nei progetti precedenti, abbiamo utilizzato l'ingresso digitale su Pico W.
Ad esempio, un pulsante può cambiare il pin da livello basso (spento) a livello alto (acceso). Questo è uno stato di funzionamento binario.

Tuttavia, Pico W può ricevere un altro tipo di segnale di ingresso: l'ingresso analogico.
Può essere in qualsiasi stato, da completamente chiuso a completamente aperto, e ha una gamma di valori possibili.
L'ingresso analogico consente al microcontrollore di percepire l'intensità della luce, l'intensità del suono, la temperatura, l'umidità, ecc. del mondo fisico.

Di solito, un microcontrollore necessita di un hardware aggiuntivo per implementare l'ingresso analogico: il convertitore analogico-digitale (ADC).
Ma Pico W ha un ADC integrato che possiamo usare direttamente.


|pin_adc|

Pico W ha tre pin GPIO che possono utilizzare l'ingresso analogico: GP26, GP27, GP28. Questi corrispondono ai canali analogici 0, 1 e 2.
Inoltre, c'è un quarto canale analogico, che è collegato al sensore di temperatura integrato, che non sarà trattato qui.

In questo progetto, proviamo a leggere il valore analogico del potenziometro.

* :ref:`cpn_potentiometer`

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
        - Several
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_resistor`
        - 1(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_potentiometer`
        - 1
        - |link_potentiometer_buy|


**Schema Elettrico**

|sch_pot|

Il potenziometro è un dispositivo analogico e funziona ruotandolo in due direzioni diverse.

Collega il pin centrale del potenziometro al pin analogico GP28. Il Raspberry Pi Pico W contiene un convertitore analogico-digitale multicanale a 16 bit. Ciò significa che mappa la tensione di ingresso tra 0 e la tensione di esercizio (3.3V) su un valore intero tra 0 e 65535, quindi il valore di GP28 varia da 0 a 65535.

La formula di calcolo è mostrata di seguito.

    (Vp/3.3V) x 65535 = Ap

Successivamente, programma il valore di GP28 (potenziometro) come valore PWM di GP15 (LED).
In questo modo noterai che ruotando il potenziometro, la luminosità del LED cambierà contemporaneamente.

**Collegamenti**



|wiring_pot|


**Codice**


.. note::

    * Apri il file ``2.11_turn_the_knob.py`` nel percorso ``kepler-kit-main/micropython`` o copia questo codice in Thonny, poi clicca su "Esegui Script Corrente" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra.

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    potentiometer = machine.ADC(28)
    led = machine.PWM(machine.Pin(15))
    led.freq(1000)

    while True:
        value=potentiometer.read_u16()
        print(value)
        led.duty_u16(value)
        utime.sleep_ms(200)

Quando il programma è in esecuzione, possiamo vedere nella shell il valore analogico attualmente letto dal pin GP28.
Ruota la manopola e il valore cambierà da 0 a 65535.
Allo stesso tempo, la luminosità del LED aumenterà man mano che il valore analogico aumenta.

**Come funziona?**

.. code-block:: python

    potentiometer = machine.ADC(28)

Accedi all'ADC associato a una sorgente identificata dall'ID. In questo esempio è GP28.

.. code-block:: python

    potentiometer.read_u16()

Effettua una lettura analogica e restituisce un intero nell'intervallo 0-65535. Il valore restituito rappresenta la lettura grezza presa dall'ADC, scalata in modo che il valore minimo sia 0 e il massimo 65535.

* `machine.ADC - MicroPython Docs <https://docs.micropython.org/en/latest/library/machine.ADC.html>`_