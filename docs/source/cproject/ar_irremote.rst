.. note::

    Ciao, benvenuto nella community SunFounder Raspberry Pi, Arduino & ESP32 Enthusiasts su Facebook! Approfondisci l'uso di Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni l'accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ar_irremote:


6.4 - Telecomando a Infrarossi (IR)
=======================================

Nell'elettronica di consumo, i telecomandi vengono utilizzati per operare dispositivi come televisori e lettori DVD.
In alcuni casi, i telecomandi permettono alle persone di controllare dispositivi fuori dalla loro portata, come i condizionatori d'aria centralizzati.

Il ricevitore IR è un componente con fotocellula sintonizzato per ricevere la luce a infrarossi.
È quasi sempre utilizzato per la rilevazione dei telecomandi - ogni TV e lettore DVD ne ha uno nella parte anteriore per ricevere il segnale IR dal telecomando.
All'interno del telecomando c'è un LED IR corrispondente, che emette impulsi IR per dire alla TV di accendersi, spegnersi o cambiare canale.

* :ref:`cpn_ir_receiver`

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
        - :ref:`cpn_ir_receiver`
        - 1
        - |link_receiver_buy|

**Schema Elettrico**

|sch_irrecv|

**Cablaggio**

|wiring_irrecv|


**Codice**

.. note::

    * Puoi aprire il file ``6.4_ir_remote_control.ino`` nel percorso ``kepler-kit-main/arduino/6.4_ir_remote_control``. 
    * Oppure copia questo codice nell'**Arduino IDE**.
    * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.
    * La libreria ``IRremote`` è utilizzata qui, puoi installarla dal **Library Manager**.

      .. image:: img/lib_ir.png

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/71f50561-d1ad-4d9e-9db2-8eb7727df0a4/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


Il nuovo telecomando ha un pezzo di plastica all'estremità per isolare la batteria interna. È necessario rimuovere questo pezzo di plastica per alimentare il telecomando quando lo utilizzi.
Una volta che il programma è in esecuzione, quando premi il telecomando, il Serial Monitor stamperà il tasto che hai premuto.

**Come funziona?**

Questo codice è progettato per funzionare con un telecomando a infrarossi (IR) utilizzando la libreria ``IRremote``. Ecco la spiegazione:

#. Inclusione della libreria e definizione delle costanti. Per prima cosa, la libreria IRremote viene inclusa e il numero del pin per il ricevitore IR viene definito come 2.

   .. code-block:: cpp
 
     #include <IRremote.h>
     const int IR_RECEIVE_PIN = 17;

#. Inizializza la comunicazione seriale a una velocità di 9600 baud. Inizializza il ricevitore IR sul pin specificato (``IR_RECEIVE_PIN``) e abilita il feedback LED (se applicabile).

   .. code-block:: arduino

       void setup() {
           Serial.begin(9600);                                     // Avvia la comunicazione seriale a 9600 baud
           IrReceiver.begin(IR_RECEIVE_PIN, ENABLE_LED_FEEDBACK);  // Avvia il ricevitore IR
       }

#. Il ciclo principale viene eseguito continuamente per elaborare i segnali IR in arrivo.

   .. code-block:: arduino

      void loop() {
         if (IrReceiver.decode()) {  // Controlla se il ricevitore IR ha ricevuto un segnale
            bool result = 0;
            String key = decodeKeyValue(IrReceiver.decodedIRData.command);
            if (key != "ERROR") {
              Serial.println(key);  // Stampa il comando leggibile
              delay(100);
            }
         IrReceiver.resume();  // Prepara il ricevitore IR per ricevere il prossimo segnale
        }
      }

   * Controlla se è stato ricevuto un segnale IR e se è stato decodificato correttamente.
   * Decodifica il comando IR e lo memorizza in ``decodedValue`` utilizzando una funzione personalizzata ``decodeKeyValue()``.
   * Stampa il valore IR decodificato sul monitor seriale.
   * Riprende la ricezione dei segnali IR per il segnale successivo.

   .. raw:: html

        <br/>

#. Funzione di supporto per mappare i segnali IR ricevuti ai tasti corrispondenti.

   .. image:: img/ir_key.png
      :align: center
      :width: 80%

   .. code-block:: arduino

      // Function to map received IR signals to corresponding keys
      String decodeKeyValue(long result) {
        // Each case corresponds to a specific IR command
        switch (result) {
          case 0x16:
            return "0";
          case 0xC:
            return "1";
          case 0x18:
            return "2";
          case 0x5E:
            return "3";
          case 0x8:
            return "4";
          case 0x1C:
            return "5";
          case 0x5A:
            return "6";
          case 0x42:
            return "7";
          case 0x52:
            return "8";
          case 0x4A:
            return "9";
          case 0x9:
            return "+";
          case 0x15:
            return "-";
          case 0x7:
            return "EQ";
          case 0xD:
            return "U/SD";
          case 0x19:
            return "CYCLE";
          case 0x44:
            return "PLAY/PAUSE";
          case 0x43:
            return "FORWARD";
          case 0x40:
            return "BACKWARD";
          case 0x45:
            return "POWER";
          case 0x47:
            return "MUTE";
          case 0x46:
            return "MODE";
          case 0x0:
            return "ERROR";
          default:
            return "ERROR";
        }
      }


