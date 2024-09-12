.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto esperto**: Risolvi problemi post-vendita e affronta sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a promozioni festive e concorsi a premi.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ar_servo:

3.7 - Servo Oscillante
========================

In questo kit, oltre al LED e al cicalino passivo, c'è anche un dispositivo controllato da segnale PWM: il Servo.

Il Servo è un dispositivo di servocomando di posizione (angolo), adatto a quei sistemi di controllo che richiedono variazioni angolari costanti e possono essere mantenute. È ampiamente utilizzato nei giocattoli radiocomandati di fascia alta, come aerei, modelli di sottomarini e robot radiocomandati.

Ora, prova a far oscillare il servo!

* :ref:`cpn_servo`

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
        - :ref:`cpn_servo`
        - 1
        - |link_servo_buy|

**Schema**

|sch_servo|

**Cablaggio**

|wiring_servo|

* Il filo arancione è il segnale e va collegato a GP15.
* Il filo rosso è VCC e va collegato a VBUS (5V).
* Il filo marrone è GND e va collegato a GND.

**Codice**


.. note::

    * Puoi aprire il file ``3.7_swinging_servo.ino`` nel percorso ``kepler-kit-main/arduino/3.7_swinging_servo``. 
    * Oppure copia questo codice nell'**Arduino IDE**.

    * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.

    

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/d52a67be-be6b-4cbf-b411-810160f56928/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


Quando il programma è in esecuzione, possiamo vedere il braccio del servo oscillare avanti e indietro da 0° a 180°.


**Come funziona?**

Richiamando la libreria ``Servo.h``, puoi controllare facilmente il servo.

.. code-block:: arduino

    #include <Servo.h> 

**Funzioni della Libreria**

.. code-block:: arduino

    Servo

Crea un oggetto **Servo** per controllare un servo.

.. code-block:: arduino

    uint8_t attach(int pin); 

Trasforma un pin in un driver per servo. Richiama pinMode. Restituisce 0 in caso di errore.

.. code-block:: arduino

    void detach();

Rilascia un pin dal controllo del servo.

.. code-block:: arduino

    void write(int value); 

Imposta l'angolo del servo in gradi, da 0 a 180.

.. code-block:: arduino

    int read();

Restituisce il valore impostato con l'ultima chiamata a write().

.. code-block:: arduino

    bool attached(); 

Restituisce 1 se il servo è attualmente collegato.
