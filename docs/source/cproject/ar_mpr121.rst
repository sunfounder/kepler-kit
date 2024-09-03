.. note::

    Ciao, benvenuto nella community SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni l'accesso anticipato agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a giveaway e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ar_mpr121:

4.3 - Tastiera a Elettrodi
================================

L'MPR121 è una scelta eccellente quando vuoi aggiungere un gran numero di interruttori touch al tuo progetto. Dispone di elettrodi che possono essere estesi con conduttori.
Se colleghi gli elettrodi a una banana, puoi trasformare la banana in un interruttore touch.

* :ref:`cpn_mpr121`

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
        - :ref:`cpn_mpr121`
        - 1
        - 

**Schema Elettrico**

|sch_mpr121|



**Cablaggio**

|wiring_mpr121|

**Codice**


.. note::

    * Puoi aprire il file ``4.3_electrode_keyboard.ino`` nel percorso ``kepler-kit-main/arduino/4.3_electrode_keyboard``. 
    * Oppure copia questo codice nell'**Arduino IDE**.

    * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.
    * Qui vengono utilizzate le due librerie ``Adafruit_MPR121`` e ``Adafruit_BusIO``. Si prega di fare riferimento a :ref:`add_libraries_ar` per aggiungerle all'IDE Arduino.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/f31048b7-0f98-4d49-8c2e-26b3908e98cb/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


Dopo l'esecuzione del programma, puoi toccare con la mano i dodici elettrodi sul modulo MPR121 e lo stato di tocco di questi elettrodi verrà registrato in un array di tipo Booleano a 12 bit che verrà stampato sul monitor seriale.
Se vengono toccati il primo e l'undicesimo elettrodo, verrà stampato ``100000000010``.

Puoi estendere gli elettrodi collegando altri conduttori come frutta, fili, fogli di alluminio, ecc. Questo ti darà più modi per attivare questi elettrodi.

**Come funziona?**

Inizializza l'oggetto ``MPR121``. A questo punto lo stato degli elettrodi del modulo verrà registrato come valori iniziali.
Se estendi gli elettrodi, dovrai rieseguire l'esempio per resettare i valori iniziali.

.. code-block:: arduino

    #include "Adafruit_MPR121.h"

    Adafruit_MPR121 cap = Adafruit_MPR121();

    void setup() {
        Serial.begin(9600);
        int check = cap.begin(0x5A);
        if (!check) {
            Serial.println("MPR121 not found, check wiring?");
            while (1);
        }
        Serial.println("MPR121 found!");
    }

Ottieni il valore dell'elettrodo corrente, otterrai un valore binario a 12 bit. Se tocchi il primo e l'undicesimo elettrodo, verrà ottenuto ``100000000010``.

.. code-block:: arduino

    // Ottieni i pad attualmente toccati
    currtouched = cap.touched();

Determina se lo stato dell'elettrodo è cambiato.

.. code-block:: arduino

    void loop() {
        currtouched = cap.touched();
        if (currtouched != lasttouched) {}

        // resetta il nostro stato
        lasttouched = currtouched;
    }

Se viene rilevato un cambiamento nello stato dell'elettrodo, i valori di ``currtouched`` vengono memorizzati bit per bit nell'array ``touchStates[12]``. Infine, l'array viene stampato.

.. code-block:: arduino

    if (currtouched != lasttouched) {
        for (int i = 0; i < 12; i++) {
            if (currtouched & (1 << i)) touchStates[i] = 1;
            else touchStates[i] = 0;
        }
        for (int i = 0; i < 12; i++){
            Serial.print(touchStates[i]);
        }
        Serial.println();
    }