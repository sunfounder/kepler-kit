.. note::

    Ciao, benvenuto nella Community SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e alle anteprime.
    - **Sconti Speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_temp:


2.13 Termometro
===========================

Un termometro è un dispositivo che misura la temperatura o un gradiente di temperatura (il grado di caldo o freddo di un oggetto). 
Un termometro ha due elementi importanti: (1) un sensore di temperatura (ad esempio, il bulbo di un termometro a mercurio o il sensore pirometrico di un termometro a infrarossi) in cui avviene un cambiamento con il variare della temperatura; 
e (2) un mezzo per convertire questo cambiamento in un valore numerico (ad esempio, la scala visibile su un termometro a mercurio o il display digitale su un modello a infrarossi). 
I termometri sono ampiamente utilizzati in tecnologia e industria per monitorare i processi, in meteorologia, in medicina e nella ricerca scientifica.

Un termistore è un tipo di sensore di temperatura la cui resistenza dipende fortemente dalla temperatura, e ne esistono due tipi: 
Coefficiente di Temperatura Negativo (NTC) e Coefficiente di Temperatura Positivo (PTC). La resistenza del termistore PTC aumenta con la temperatura, mentre nel caso dell'NTC avviene l'opposto.

In questo esperimento utilizziamo un **termistore NTC** per realizzare un termometro.


* :ref:`cpn_thermistor`

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
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_thermistor`
        - 1
        - |link_thermistor_buy|


**Schema**

|sch_temp|

In questo circuito, il resistore da 10K e il termistore sono collegati in serie, e la corrente che li attraversa è la stessa. Il resistore da 10K agisce come protezione, e il GP28 legge il valore dopo la conversione di tensione del termistore.

Quando la temperatura aumenta, il valore di resistenza del termistore NTC diminuisce, di conseguenza la sua tensione diminuisce, quindi il valore di GP28 diminuirà; Se la temperatura è sufficientemente alta, la resistenza del termistore sarà vicina a 0, e il valore di GP28 sarà vicino a 0. In questo caso, il resistore da 10K svolge un ruolo protettivo, impedendo che i 3.3V e il GND siano collegati insieme, causando un cortocircuito.

Quando la temperatura scende, il valore di GP28 aumenterà. Quando la temperatura è abbastanza bassa, la resistenza del termistore sarà infinita, e la sua tensione sarà vicina a 3.3V (il resistore da 10K è trascurabile), e il valore di GP28 sarà vicino al valore massimo di 65535.

La formula di calcolo è mostrata di seguito.

    (Vp/3.3V) x 65535 = Ap


**Collegamenti**

|wiring_temp|
 
.. #. Collega 3V3 e GND del Pico W alla barra di alimentazione della breadboard.
.. #. Collega un terminale del termistore al pin GP28, quindi collega lo stesso terminale alla barra di alimentazione positiva con un resistore da 10K ohm.
.. #. Collega l'altro terminale del termistore alla barra di alimentazione negativa.

.. note::
    * Il termistore è nero e contrassegnato con 103.
    * L'anello colorato del resistore da 10K ohm è rosso, nero, nero, rosso e marrone.


**Codice**

.. note::

    * Apri il file ``2.13_thermometer.py`` nel percorso ``kepler-kit-main/micropython`` o copia questo codice in Thonny, poi clicca su "Esegui Script Corrente" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra. 

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime
    import math

    thermistor = machine.ADC(28)  

    while True:
        temperature_value = thermistor.read_u16()
        Vr = 3.3 * float(temperature_value) / 65535
        Rt = 10000 * Vr / (3.3 - Vr)
        temp = 1/(((math.log(Rt / 10000)) / 3950) + (1 / (273.15+25)))
        Cel = temp - 273.15
        Fah = Cel * 1.8 + 32
        print ('Celsius: %.2f C  Fahrenheit: %.2f F' % (Cel, Fah))
        utime.sleep_ms(200)

Dopo l'esecuzione del programma, la Shell stamperà le temperature in gradi Celsius e Fahrenheit.

**Come funziona?**

Ogni termistore ha una resistenza normale. Qui è di 10k ohm, misurata a 25 gradi Celsius. 

Quando la temperatura aumenta, la resistenza del termistore diminuisce. Poi i dati di tensione vengono convertiti in quantità digitali dall'adattatore A/D. 

La temperatura in gradi Celsius o Fahrenheit è fornita dal programma.

.. code-block:: python

    import math 

Esiste una libreria numerica che dichiara un insieme di funzioni per eseguire operazioni matematiche comuni e trasformazioni.

* `math <https://docs.micropython.org/en/latest/library/math.html>`_

.. code-block:: python

    temperature_value = thermistor.read_u16()

Questa funzione viene utilizzata per leggere il valore del termistore. 

.. code-block:: python

    Vr = 3.3 * float(temperature_value) / 65535
    Rt = 10000 * Vr / (3.3 - Vr)
    temp = 1/(((math.log(Rt / 10000)) / 3950) + (1 / (273.15+25)))
    Cel = temp - 273.15
    Fah = Cel * 1.8 + 32
    print ('Celsius: %.2f C  Fahrenheit: %.2f F' % (Cel, Fah))
    utime.sleep_ms(200)

Questi calcoli convertono i valori del termistore in gradi centigradi e Fahrenheit.

.. code-block:: python

    Vr = 3.3 * float(temperature_value) / 65535
    Rt = 10000 * Vr / (3.3 - Vr)

Nelle due righe di codice sopra, la tensione viene prima calcolata utilizzando il valore analogico letto, e poi si ottiene Rt (la resistenza del termistore).

.. code-block:: python

    temp = 1/(((math.log(Rt / 10000)) / 3950) + (1 / (273.15+25))) 

.. note::
    Ecco la relazione tra resistenza e temperatura: 

    **RT =RN expB(1/TK – 1/TN)** 

    * RT è la resistenza del termistore NTC quando la temperatura è TK. 
    * RN è la resistenza del termistore NTC alla temperatura nominale TN. Qui, il valore numerico di RN è 10k. 
    * TK è una temperatura Kelvin e l'unità è K. Qui, il valore numerico di TK è 273,15 + gradi Celsius. 
    * TN è una temperatura Kelvin nominale; l'unità è K. Qui, il valore numerico di TN è 273,15 + 25.
    * E B(beta), la costante del materiale del termistore NTC, è anche chiamata indice di sensibilità termica con un valore numerico di 3950. 
    * exp è l'abbreviazione di esponenziale, e il numero base e è un numero naturale ed è approssimativamente uguale a 2,7.

    Converti questa formula TK=1/(ln(RT/RN)/B+1/TN) per ottenere la temperatura Kelvin che, sottratta di 273,15, equivale ai gradi Celsius.

    Questa relazione è una formula empirica. È precisa solo quando la temperatura e la resistenza sono entro l'intervallo efficace.

Questo codice si riferisce all'inserimento di Rt nella formula TK=1/(ln(RT/RN)/B+1/TN) per ottenere la temperatura Kelvin. 

.. code-block:: python

    temp = temp - 273.15 

Converti la temperatura Kelvin in gradi centigradi.

.. code-block:: python

    Fah = Cel * 1.8 + 32 

Converti i gradi centigradi in gradi Fahrenheit. 

.. code-block:: python

    print ('Celsius: %.2f °C Fahrenheit: %.2f ℉' % (Cel, Fah)) 

Stampa i gradi centigradi, i gradi Fahrenheit e le loro unità nella shell.
