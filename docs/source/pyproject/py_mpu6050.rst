.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_mpu6050:

6.3 Tracciamento del Movimento a 6 Assi
===========================================

L'MPU-6050 è un dispositivo di tracciamento del movimento a 6 assi (combina un giroscopio a 3 assi e un accelerometro a 3 assi).

Un accelerometro è uno strumento che misura l'accelerazione propria. Ad esempio, un accelerometro a riposo sulla superficie terrestre misurerà un'accelerazione dovuta alla gravità terrestre, verso l'alto[3] (per definizione) di g ≈ 9,81 m/s².

Gli accelerometri hanno molti usi nell'industria e nella scienza. Ad esempio: sistemi di navigazione inerziale per aerei e missili, per mantenere le immagini su tablet e fotocamere digitali verticali, ecc.

I giroscopi vengono utilizzati per misurare l'orientamento e la velocità angolare di un dispositivo o per il mantenimento. Le applicazioni dei giroscopi includono sistemi anti-ribaltamento e airbag per automobili, sistemi di rilevamento del movimento per dispositivi intelligenti, sistemi di stabilizzazione dell'assetto per droni e altro ancora.

* :ref:`cpn_mpu6050`


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
        - :ref:`cpn_mpu6050`
        - 1
        - 

**Schema Elettrico**

|sch_mpu6050|


**Collegamenti**

|wiring_mpu6050|

**Codice**

.. note::

    * Apri il file ``6.3_6axis_motion_tracking.py`` nel percorso ``kepler-kit-main/micropython`` o copia questo codice in Thonny, poi clicca su "Esegui Script Corrente" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra.

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.
    
    * Qui è necessario utilizzare ``imu.py`` e ``vector3d.py``, controlla se sono stati caricati su Pico W, per un tutorial dettagliato fai riferimento a :ref:`add_libraries_py`.


.. code-block:: python

    from imu import MPU6050
    from machine import I2C, Pin
    import time

    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
    mpu = MPU6050(i2c)

    while True:
        print("x: %s, y: %s, z: %s"%(mpu.accel.x, mpu.accel.y, mpu.accel.z))
        time.sleep(0.1)
        print("A: %s, B: %s, Y: %s"%(mpu.gyro.x, mpu.gyro.y, mpu.gyro.z))
        time.sleep(0.1)

Dopo l'esecuzione del programma, potrai vedere i valori dell'accelerometro a 3 assi e del giroscopio a 3 assi alternarsi nell'output.
A questo punto, ruotando l'MPU6050, vedrai che questi valori cambieranno di conseguenza.
Per rendere più facile la visualizzazione delle variazioni, puoi commentare una delle linee di stampa e concentrarti su un altro set di dati.

L'unità di misura dei valori di accelerazione è m/s², mentre l'unità dei valori del giroscopio è °/s.

**Come funziona?**

Nella libreria imu, abbiamo integrato le funzioni rilevanti nella classe ``MPU6050``.
MPU6050 è un modulo I2C e richiede un set di pin I2C da definire per l'inizializzazione.

.. code-block:: python

    from imu import MPU6050
    from machine import I2C, Pin

    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
    mpu = MPU6050(i2c)

Successivamente, sarai in grado di ottenere i valori in tempo reale di accelerazione e velocità angolare in ``mpu.accel.x``, ``mpu.accel.y``, ``mpu.accel.z``, ``mpu.gyro.x``, ``mpu.gyro.y``, ``mpu.gyro.z``.

.. code-block:: python

    while True:
        print("x: %s, y: %s, z: %s"%(mpu.accel.x, mpu.accel.y, mpu.accel.z))
        time.sleep(0.1)
        print("A: %s, B: %s, Y: %s"%(mpu.gyro.x, mpu.gyro.y, mpu.gyro.z))
        time.sleep(0.1)