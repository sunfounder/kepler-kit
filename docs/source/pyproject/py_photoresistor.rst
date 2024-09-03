.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_photoresistor:

2.12 Senti la Luce
=============================

La fotoresistenza è un dispositivo tipico per ingressi analogici e viene utilizzata in modo molto simile a un potenziometro. Il suo valore di resistenza dipende dall'intensità della luce: più intensa è la luce irradiata, minore sarà il suo valore di resistenza; al contrario, aumenterà.


* :ref:`cpn_photoresistor`

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
        - :ref:`cpn_photoresistor`
        - 1
        - |link_photoresistor_buy|


**Schema Elettrico**

|sch_photoresistor|

In questo circuito, la resistenza da 10KΩ e la fotoresistenza sono collegate in serie, e la corrente che le attraversa è la stessa. La resistenza da 10KΩ funge da protezione, e il pin GP28 legge il valore dopo la conversione di tensione della fotoresistenza.

Quando la luce aumenta, la resistenza della fotoresistenza diminuisce, quindi anche la sua tensione diminuisce, così il valore letto dal GP28 diminuirà; se la luce è abbastanza forte, la resistenza della fotoresistenza sarà prossima a 0, e il valore del GP28 sarà prossimo a 0. In questo caso, la resistenza da 10KΩ svolge un ruolo di protezione, evitando che 3.3V e GND siano collegati insieme, causando un cortocircuito.

Se si posiziona la fotoresistenza in una situazione di oscurità, il valore del GP28 aumenterà. In una situazione abbastanza buia, la resistenza della fotoresistenza sarà infinita, e la sua tensione sarà vicina a 3.3V (la resistenza da 10KΩ è trascurabile), e il valore del GP28 sarà prossimo al valore massimo di 65535.

La formula di calcolo è mostrata di seguito.

    (Vp/3.3V) x 65535 = Ap



**Collegamenti**

|wiring_photoresistor|

**Codice**

.. note::

    * Apri il file ``2.12_feel_the_light.py`` nel percorso ``kepler-kit-main/micropython`` o copia questo codice in Thonny, poi clicca su "Esegui Script Corrente" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra.

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    photoresistor = machine.ADC(28)

    while True:
        light_value  = photoresistor.read_u16()
        print(light_value)
        utime.sleep_ms(10)

Dopo l'esecuzione del programma, la Shell stamperà i valori della fotoresistenza. Puoi puntare una torcia su di essa o coprirla con la mano per vedere come il valore cambierà.
