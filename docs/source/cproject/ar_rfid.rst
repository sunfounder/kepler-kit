.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a promozioni festive e giveaway.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ar_rfid:

6.5 - Identificazione a Radiofrequenza
===============================================

L'Identificazione a Radiofrequenza (RFID) si riferisce a tecnologie che utilizzano la comunicazione wireless tra un oggetto (o tag) e un dispositivo interrogante (o lettore) per tracciare e identificare automaticamente tali oggetti. Il raggio di trasmissione del tag è limitato a diversi metri dal lettore. Non è necessariamente richiesta una linea di vista diretta tra il lettore e il tag.

La maggior parte dei tag contiene almeno un circuito integrato (IC) e un'antenna.
Il microchip memorizza informazioni e gestisce la comunicazione a radiofrequenza (RF) con il lettore. I tag passivi non hanno una fonte di energia indipendente e dipendono da un segnale elettromagnetico esterno, fornito dal lettore, per alimentare le loro operazioni.
I tag attivi contengono una fonte di energia indipendente, come una batteria.
Pertanto, possono avere capacità di elaborazione, trasmissione e raggio d'azione maggiori.

* :ref:`cpn_mfrc522`

**Componenti Necessari**

In questo progetto, abbiamo bisogno dei seguenti componenti.

È sicuramente conveniente acquistare un kit completo, ecco il link:

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
        - :ref:`cpn_mfrc522`
        - 1
        - |link_rfid_buy|

**Schema**

|sch_rfid|

**Cablaggio**

|wiring_rfid|

**Codice**

.. note::

    * Puoi aprire il file ``6.5_rfid_write.ino`` nel percorso ``kepler-kit-main/arduino/6.5_rfid_write``. 
    * Oppure copia questo codice nell'**Arduino IDE**.
    * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.
    * Qui viene utilizzata la libreria ``MFRC522``. Si prega di fare riferimento a :ref:`add_libraries_ar` per aggiungerla all'IDE di Arduino.

La funzione principale è divisa in due:

* ``6.5_rfid_write.ino``: Utilizzata per scrivere informazioni sulla scheda (o chiave).
* ``6.5_rfid_read.ino``: utilizzata per leggere le informazioni nella scheda (o chiave).

.. note::

   * Puoi aprire il file ``6.5_rfid_write.ino`` nel percorso ``kepler-kit-main/arduino/6.5_rfid_write``. 
   * Oppure copia questo codice nell'**Arduino IDE**.
   
   * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.

Dopo l'esecuzione, sarai in grado di inserire un messaggio nel monitor seriale, terminandolo con ``#``, e poi scrivere il messaggio sulla scheda avvicinandola al modulo MFRC522.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/b4f9156a-711a-442c-8271-329847e808dc/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


.. note::

   * Puoi aprire il file ``6.5_rfid_read.ino`` nel percorso ``kepler-kit-main/arduino/6.5_rfid_read``. 
   * Oppure copia questo codice nell'**Arduino IDE**.
   
   * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.

Dopo l'esecuzione, sarai in grado di leggere il messaggio memorizzato nella scheda (o chiave).

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/df57b5cb-9162-4b4b-b28a-7f02363885c9/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

**Come funziona?**

.. code-block:: arduino

    #include <MFRC522.h>

    #define RST_PIN         0
    #define SS_PIN          5

    MFRC522 mfrc522(SS_PIN, RST_PIN);

Per prima cosa, istanzia la classe ``MFRC522()``.

Per semplicità d'uso, la libreria ``MFRC522`` è ulteriormente incapsulata con le seguenti funzioni.

* ``void simple_mfrc522_init()`` : Avvia la comunicazione SPI e inizializza il modulo mfrc522.
* ``void simple_mfrc522_get_card()`` : Sospende il programma fino a quando la scheda (o chiave) non viene rilevata, stampa l'UID della scheda e il tipo PICC.
* ``void simple_mfrc522_write(String text)`` : Scrive una stringa sulla scheda (o chiave).
* ``void simple_mfrc522_write(byte* buffer)`` : Scrive informazioni sulla scheda (o chiave), solitamente provenienti dalla porta seriale.
* ``void simple_mfrc522_write(byte section, String text)`` : Scrive una stringa in un settore specifico. ``section`` è impostato su 0 per scrivere nei settori 1-2; ``section`` è impostato su 1 per scrivere nei settori 3-4.
* ``void simple_mfrc522_write(byte section, byte* buffer)`` : Scrive informazioni in un settore specifico, solitamente provenienti dalla porta seriale. ``section`` impostato su 0, scrive nei settori 1-2; ``section`` impostato su 1, scrive nei settori 3-4.
* ``String simple_mfrc522_read()`` : Legge le informazioni nella scheda (o chiave) e restituisce una stringa.
* ``String simple_mfrc522_read(byte section)`` : Legge le informazioni in un settore specifico e restituisce una stringa. ``section`` è impostato su 0, scrive nei settori 1-2; ``section`` è impostato su 1, scrive nei settori 3-4.

Nell'esempio ``6.5_rfid_write.ino``, viene utilizzata la funzione ``Serial.readBytesUntil()``, che è un metodo comune di input seriale.

* `Serial.readBytesUntil <https://www.arduino.cc/reference/en/language/functions/communication/serial/readbytesuntil/>`_
