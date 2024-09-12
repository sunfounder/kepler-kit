.. note::

    Ciao, benvenuto nella community SunFounder Raspberry Pi, Arduino & ESP32 Enthusiasts su Facebook! Approfondisci l'uso di Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni l'accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ar_keypad:

4.2 Tastiera 4x4
====================

La tastiera 4x4, nota anche come tastiera a matrice, è una matrice di 16 tasti disposti in un singolo pannello.

La tastiera si trova su dispositivi che richiedono principalmente input digitali, come calcolatrici, telecomandi, telefoni a pulsante, distributori automatici, bancomat, serrature a combinazione e serrature digitali.

In questo progetto, impareremo come determinare quale tasto viene premuto e ottenere il valore del tasto corrispondente.

* :ref:`cpn_keypad`
* `E.161 - Wikipedia <https://en.wikipedia.org/wiki/E.161>`_

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
        - :ref:`cpn_resistor`
        - 4 (10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_keypad`
        - 1
        - |link_keypad_buy|

**Schema Elettrico**

|sch_keypad_ar|

4 resistori pull-down sono collegati a ciascuna delle colonne della tastiera a matrice, in modo che G6 ~ G9 ottengano un livello basso stabile quando i tasti non sono premuti.

Le righe della tastiera (G2 ~ G5) sono programmate per andare ad un livello alto; se una delle G6 ~ G9 viene letta ad un livello alto, sappiamo quale tasto è stato premuto.

Ad esempio, se G6 viene letta ad un livello alto, significa che è stato premuto il tasto numerico 1; questo perché i pin di controllo del tasto numerico 1 sono G2 e G6, e quando il tasto 1 viene premuto, G2 e G6 verranno collegati insieme e G6 sarà anche alta.


**Cablaggio**

|wiring_keypad_ar|

Per semplificare il cablaggio, nello schema sopra, le colonne della tastiera a matrice e i resistori da 10K sono inseriti nei fori dove si trovano G6 ~ G9.


**Codice**

.. note::

    * Puoi aprire il file ``4.2_4x4_keypad.ino`` nel percorso ``kepler-kit-main/arduino/4.2_4x4_keypad``. 
    * Oppure copia questo codice nell'**Arduino IDE**.
    * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.
    * La libreria ``Adafruit Keypad`` è utilizzata qui, puoi installarla dal **Library Manager**.

      .. image:: img/lib_ad_keypad.png

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/6c776dfc-cb74-49d7-8906-f1382e0e7b7b/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Dopo l'esecuzione del programma, la Shell stamperà i tasti che hai premuto sulla tastiera.


**Come Funziona**

1. Inclusione della Libreria

   Iniziamo includendo la libreria ``Adafruit_Keypad``, che ci consente di interfacciarci facilmente con il tastierino.

   .. code-block:: arduino

     #include "Adafruit_Keypad.h"

2. Configurazione del Tastierino

   .. code-block:: arduino

     const byte ROWS = 4;
     const byte COLS = 4;
     char keys[ROWS][COLS] = {
       { '1', '2', '3', 'A' },
       { '4', '5', '6', 'B' },
       { '7', '8', '9', 'C' },
       { '*', '0', '#', 'D' }
     };
     byte rowPins[ROWS] = { 2, 3, 4, 5 };
     byte colPins[COLS] = { 8, 9, 10, 11 };

   - Le costanti ``ROWS`` e ``COLS`` definiscono le dimensioni del tastierino.
   - ``keys`` è un array 2D che memorizza l'etichetta per ogni pulsante del tastierino.
   - ``rowPins`` e ``colPins`` sono array che memorizzano i pin dell'Arduino collegati alle righe e alle colonne del tastierino.

   .. raw:: html

      <br/>

3. Inizializzazione del Tastierino

   Creiamo un'istanza di ``Adafruit_Keypad`` chiamata ``myKeypad`` e la inizializziamo.

   .. code-block:: arduino

     Adafruit_Keypad myKeypad = Adafruit_Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

4. Funzione setup()

   Inizializziamo la comunicazione Serial e il tastierino personalizzato.

   .. code-block:: arduino

     void setup() {
       Serial.begin(9600);
       myKeypad.begin();
     }

5. Ciclo Principale

   Verifichiamo gli eventi di pressione dei tasti e li visualizziamo sul Monitor Seriale.

   .. code-block:: arduino

     void loop() {
       myKeypad.tick();
       while (myKeypad.available()) {
         keypadEvent e = myKeypad.read();
         Serial.print((char)e.bit.KEY);
         if (e.bit.EVENT == KEY_JUST_PRESSED) Serial.println(" pressed");
         else if (e.bit.EVENT == KEY_JUST_RELEASED) Serial.println(" released");
       }
       delay(10);
     }