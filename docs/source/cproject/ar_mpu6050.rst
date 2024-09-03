.. note::

    Ciao, benvenuto nella community di appassionati di SunFounder Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri entusiasti.

    **Perché Unirsi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni l'accesso anticipato agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a promozioni e giveaway durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ar_mpu6050:

6.3 - Tracciamento del Movimento a 6 Assi
==================================================

L'MPU-6050 è un dispositivo di tracciamento del movimento a 6 assi 
(combina un giroscopio a 3 assi e un accelerometro a 3 assi).

Un accelerometro è uno strumento che misura l'accelerazione propria. 
Ad esempio, un accelerometro a riposo sulla superficie terrestre misurerà 
un'accelerazione dovuta alla gravità terrestre, diretta verso l'alto 
(per definizione) di g ≈ 9,81 m/s².

Gli accelerometri hanno molti usi nell'industria e nella scienza. Ad esempio: 
sistemi di navigazione inerziale per aerei e missili, per mantenere verticali 
le immagini su tablet e fotocamere digitali, ecc.

I giroscopi vengono utilizzati per misurare l'orientamento e la velocità 
angolare di un dispositivo o la sua stabilità. Le applicazioni dei giroscopi 
includono sistemi anti-ribaltamento e airbag per automobili, sistemi di 
rilevamento del movimento per dispositivi intelligenti, sistemi di 
stabilizzazione dell'assetto per droni e altro ancora.

* :ref:`cpn_mpu6050`

**Componenti Necessari**

In questo progetto, abbiamo bisogno dei seguenti componenti.

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
        - :ref:`cpn_mpu6050`
        - 1
        - 

**Schema Elettrico**

|sch_mpu6050|

**Cablaggio**

|wiring_mpu6050|

**Codice**

.. note::

    * Puoi aprire il file ``6.3_6axis_motion_tracking.ino`` nel percorso ``kepler-kit-main/arduino/6.3_6axis_motion_tracking``. 
    * Oppure copia questo codice nell'**Arduino IDE**.
    * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.
    * Qui viene utilizzata la libreria ``Adafruit_MPU6050``. Si prega di fare riferimento a :ref:`add_libraries_ar` per aggiungerla all'IDE Arduino.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/318f62d3-1d7b-4ee6-a1a2-97e783cf2d5e/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>
    

Dopo aver eseguito il programma, puoi vedere i valori dell'accelerometro a 3 assi e i valori del giroscopio a 3 assi ciclicamente nell'output.
A questo punto, ruota l'MPU6050 a caso e vedrai questi valori cambiare di conseguenza.
Per rendere più facile vedere i cambiamenti, puoi commentare una delle righe di stampa e concentrarti su un altro set di dati.


**Come funziona?**

Istanzia un oggetto ``MPU6050``.

.. code-block:: arduino

    #include <Adafruit_MPU6050.h>
    #include <Wire.h>

    Adafruit_MPU6050 mpu;

Inizializza l'MPU6050 e imposta la sua precisione.

.. code-block:: arduino

    void setup(void) {
        Serial.begin(115200);
        while (!Serial)
            delay(10); // will pause Zero, Leonardo, etc until serial console opens

        Serial.println("Adafruit MPU6050 test!");

        // Try to initialize!
        if (!mpu.begin()) {
            Serial.println("Failed to find MPU6050 chip");
            while (1) {
            delay(10);
            }
        }
        Serial.println("MPU6050 Found!");

        // Set range
        mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
        mpu.setGyroRange(MPU6050_RANGE_500_DEG);
        mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);

        Serial.println("");
        delay(100);
    }

Ottieni nuovi eventi sensore con le letture.

.. code-block:: arduino

    sensors_event_t a, g, temp;
    mpu.getEvent(&a, &g, &temp);

Successivamente, sarai in grado di ottenere valori di accelerazione e velocità angolare in tempo reale nei dati ``a.acceleration.x``, ``a.acceleration.y``, ``a.acceleration.z``, ``g.gyro.x``, ``g.gyro.y``, ``g.gyro.z``.

.. code-block:: arduino

    Serial.print("Acceleration X: ");
    Serial.print(a.acceleration.x);
    Serial.print(", Y: ");
    Serial.print(a.acceleration.y);
    Serial.print(", Z: ");
    Serial.print(a.acceleration.z);
    Serial.println(" m/s^2");

    Serial.print("Rotation X: ");
    Serial.print(g.gyro.x);
    Serial.print(", Y: ");
    Serial.print(g.gyro.y);
    Serial.print(", Z: ");
    Serial.print(g.gyro.z);
    Serial.println(" rad/s");