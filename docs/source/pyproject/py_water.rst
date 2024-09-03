.. note::

    Ciao, benvenuto nella Community SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e alle anteprime.
    - **Sconti Speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_water:

2.14 Misura il Livello dell'Acqua
=====================================

|img_water_sensor|

Il sensore d'acqua è progettato per il rilevamento dell'acqua, e può essere ampiamente utilizzato per rilevare pioggia, livello dell'acqua e persino perdite di liquidi.

Misura il livello dell'acqua attraverso una serie di tracce parallele esposte che rilevano la dimensione delle gocce d'acqua/volume. Il volume dell'acqua viene facilmente convertito in un segnale analogico, e il valore analogico di uscita può essere letto direttamente dalla scheda di controllo principale per ottenere l'effetto di allarme livello dell'acqua.

.. warning:: 
    
    Il sensore non può essere completamente immerso nell'acqua, lascia solo la parte in cui si trovano le dieci tracce a contatto con l'acqua. Inoltre, alimentare il sensore in un ambiente umido accelererà la corrosione della sonda e ridurrà la vita del sensore, quindi si consiglia di fornire energia solo durante la lettura.

* :ref:`cpn_water_level`

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
        - :ref:`cpn_water_level`
        - 1
        - 



**Schema**

|sch_water|


**Cablaggio**

|wiring_water|

**Codice**

.. note::

    * Apri il file ``2.14_feel_the_water_level.py`` nel percorso ``kepler-kit-main/micropython`` o copia questo codice in Thonny, poi clicca su "Esegui Script Corrente" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra.

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    sensor = machine.ADC(28)

    while True:
        value=sensor.read_u16()
        print(value)
        utime.sleep_ms(200)


Dopo l'esecuzione del programma, immergi lentamente il modulo Sensore d'Acqua nell'acqua, e man mano che la profondità aumenta, la Shell stamperà un valore sempre maggiore.

**Per saperne di più**

Esiste un modo per utilizzare il modulo di ingresso analogico come modulo digitale.

Innanzitutto, prendi una lettura del Sensore d'Acqua in un ambiente asciutto, registrala e usala come valore soglia. Poi, completa la programmazione e rileggi la lettura del sensore d'acqua. Quando la lettura del sensore d'acqua si discosta significativamente dalla lettura in un ambiente asciutto, è a contatto con un liquido. In altre parole, posizionando questo dispositivo vicino a un tubo dell'acqua, è possibile rilevare se il tubo perde.


.. note::

    * Apri il file ``2.14_water_level_threshold.py`` nel percorso ``kepler-kit-main/micropython`` o copia questo codice in Thonny, poi clicca su "Esegui Script Corrente" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra.

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    sensor = machine.ADC(28)
    threshold = 30000 #This value needs to be modified with the environment.

    while True:
        value=sensor.read_u16()
        if value > threshold :
            print("Liquid leakage!")
        utime.sleep_ms(200)
