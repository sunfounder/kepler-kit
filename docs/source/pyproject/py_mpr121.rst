.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_mpr121:

4.3 Tastiera a Elettrodi
================================

L'MPR121 è una scelta eccellente quando desideri aggiungere un gran numero di interruttori touch al tuo progetto. Ha elettrodi che possono essere estesi con conduttori.
Se colleghi gli elettrodi a una banana, puoi trasformarla in un interruttore touch.

* :ref:`cpn_mpr121`

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
        - :ref:`cpn_mpr121`
        - 1
        - 

**Schema Elettrico**

|sch_mpr121|

**Collegamenti**

|wiring_mpr121|

**Codice**

.. note::

    * Apri il file ``4.3_electrode_keyboard.py`` nel percorso ``kepler-kit-main/micropython`` o copia questo codice in Thonny, poi clicca su "Esegui Script Corrente" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra.

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.
    
    * Qui è necessario utilizzare la libreria chiamata ``mpr121.py``, controlla se è stata caricata su Pico W, per un tutorial dettagliato fai riferimento a :ref:`add_libraries_py`.


.. code-block:: python

    from mpr121 import MPR121
    from machine import Pin, I2C
    import time

    i2c = I2C(1, sda=Pin(6), scl=Pin(7))
    mpr = MPR121(i2c)

    # check all keys
    while True:
        value = mpr.get_all_states()
        if len(value) != 0:
            print(value)
        time.sleep_ms(100)

Dopo l'esecuzione del programma, puoi toccare con la mano i dodici elettrodi sull'MPR121 e gli elettrodi toccati verranno stampati a schermo.

Puoi estendere gli elettrodi per collegare altri conduttori come frutta, fili, fogli di alluminio, ecc. Questo ti darà più modi per attivare questi elettrodi.

**Come funziona?**

Nella libreria mpr121, abbiamo integrato la funzionalità nella classe ``MPR121``.

.. code-block:: python

    from mpr121 import MPR121

L'MPR121 è un modulo I2C che richiede un set di pin I2C da definire per inizializzare l'oggetto ``MPR121``. A questo punto lo stato degli elettrodi del modulo verrà registrato come valori iniziali. Se gli elettrodi vengono estesi, è necessario rieseguire l'esempio per reimpostare i valori iniziali.

.. code-block:: python

    from machine import Pin, I2C
    i2c = I2C(1, sda=Pin(6), scl=Pin(7))
    mpr = MPR121(i2c)

* `Inter-Integrated Circuit - Wikipedia <https://en.wikipedia.org/wiki/I2C>`_

Quindi utilizza ``mpr.get_all_states()`` per leggere se gli elettrodi sono attivati. Se gli elettrodi 2 e 3 sono attivati, verrà generato il valore ``[2, 3]``.


.. code-block::

    while True:
        value = mpr.get_all_states()
        if len(value) ! = 0:
            print(value)
        time.sleep_ms(100)

Puoi anche usare ``mpr.is_touched(electrode)`` per rilevare un elettrodo specifico. Quando viene attivato, restituisce ``True``, altrimenti restituisce ``False``.

.. code-block:: python

    while True:
        value = mpr.is_touched(0)
        print(value)
        time.sleep_ms(100)