.. note::

    Ciao, benvenuto nella community di appassionati di SunFounder Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Accedi in anteprima agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ar_button:

2.5 - Lettura del Valore di un Pulsante
==============================================

Dal nome GPIO (General-purpose input/output), possiamo capire che questi pin hanno sia funzioni di input che di output. 
Nelle lezioni precedenti, abbiamo utilizzato la funzione di output; in questo capitolo utilizzeremo la funzione di input per leggere il valore di un pulsante.

* :ref:`cpn_button`

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
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_button`
        - 1
        - |link_button_buy|

**Schema Elettrico**

|sch_button|

Un lato del pin del pulsante è collegato a 3.3v, e l'altro lato è collegato a GP14, quindi quando il pulsante viene premuto, GP14 sarà alto. Tuttavia, quando il pulsante non è premuto, GP14 si trova in uno stato sospeso e può essere alto o basso. Per ottenere un livello basso stabile quando il pulsante non è premuto, GP14 deve essere ricollegato a GND tramite una resistenza pull-down da 10K.

**Cablaggio**

|wiring_button|


.. note::
    Possiamo pensare al pulsante a quattro piedini come a un pulsante a forma di "H". I due piedini di sinistra (o destra) sono collegati tra loro, il che significa che una volta che attraversa la linea di divisione centrale, collegherà insieme le due metà delle righe con lo stesso numero. (Ad esempio, nel mio circuito, E23 e F23 sono collegati, così come E25 e F25).

    Prima che il pulsante venga premuto, i lati sinistro e destro sono indipendenti l'uno dall'altro, e la corrente non può fluire da un lato all'altro.


**Codice**

.. note::

   * Puoi aprire il file ``2.5_reading_button_value.ino`` nel percorso ``kepler-kit-main/arduino/2.5_reading_button_value``.
   * Oppure copia questo codice nell'**Arduino IDE**.


    * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.


.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/6fcb7cac-e866-4a2d-8162-8e0c6fd17660/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>



Dopo l'esecuzione del codice, fai clic sull'icona della lente d'ingrandimento nell'angolo in alto a destra dell'IDE di Arduino (Serial Monitor).

.. image:: img/open_serial_monitor.png

Ora, quando premi il pulsante, il Serial Monitor stamperà "Hai premuto il pulsante!".


**Come funziona?**

Per abilitare il Serial Monitor, è necessario avviare la comunicazione seriale in ``setup()`` e impostare la velocità di trasmissione a 9600.

.. code-block:: arduino

    Serial.begin(115200);

    
* `Serial <https://www.arduino.cc/reference/en/language/functions/communication/serial/>`_


Per il pulsante, dobbiamo impostare la loro modalità su ``INPUT`` per poter ottenere i loro valori.

.. code-block:: arduino

    pinMode(buttonPin, INPUT);

Leggi lo stato del ``buttonPin`` in ``loop()`` e assegnalo alla variabile ``buttonState``.

.. code-block:: arduino

    buttonState = digitalRead(buttonPin);
    
* `digitalRead() <https://www.arduino.cc/reference/en/language/functions/digital-io/digitalread/>`_


Se lo stato di ``buttonState`` è ALTO, il LED lampeggerà.
stampa "Hai premuto il pulsante!" sul Serial Monitor.

.. code-block:: arduino

    if (buttonState == HIGH) {
        Serial.println("You pressed the button!");
    }


**Modalità di Lavoro Pull-up**

Successivamente vediamo il cablaggio e il codice quando il pulsante è in modalità di lavoro pull-up, prova a eseguirlo.

|wiring_button_pullup|

.. 1. Collega il pin 3V3 del Pico W al bus di alimentazione positivo della breadboard.
.. #. Inserisci il pulsante nella breadboard e attraversa la linea di divisione centrale.
.. #. Usa un cavo di collegamento per connettere uno dei pin del pulsante al bus **negativo** (il mio è il pin in alto a destra).
.. #. Collega l'altro pin (in alto a sinistra o in basso a sinistra) a GP14 con un cavo di collegamento.
.. #. Usa una resistenza da 10K per collegare il pin in alto a sinistra del pulsante al bus **positivo**.
.. #. Collega il bus di alimentazione negativo della breadboard al GND del Pico.

L'unica differenza che vedrai rispetto alla modalità pull-down è che la resistenza da 10K è collegata a 3.3V e il pulsante è collegato a GND, in modo che quando il pulsante viene premuto, GP14 otterrà un livello basso, che è l'opposto del valore ottenuto in modalità pull-down.
Quindi, basta cambiare questo codice in ``if (buttonState == LOW)``.
