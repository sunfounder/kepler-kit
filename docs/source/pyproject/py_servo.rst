.. note::

    Ciao, benvenuto nella Community SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e alle anteprime.
    - **Sconti Speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_servo:

3.7 Servo Oscillante
============================

In questo kit, oltre al LED e al buzzer passivo, c'è anche un dispositivo controllato da segnale PWM: il Servo.

Il Servo è un dispositivo di controllo della posizione (angolo), adatto per quei sistemi di controllo che richiedono cambiamenti angolari costanti e mantenibili. È ampiamente utilizzato nei giocattoli radiocomandati di alta gamma, come aerei, modelli di sottomarini e robot radiocomandati.

Ora, proviamo a far oscillare il servo!

* :ref:`cpn_servo`

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
        - :ref:`cpn_servo`
        - 1
        - |link_servo_buy|

**Schema**

|sch_servo|

**Collegamenti**

|wiring_servo|

* Il filo arancione è il segnale ed è collegato a GP15.
* Il filo rosso è il VCC ed è collegato a VBUS (5V).
* Il filo marrone è il GND ed è collegato a GND.


.. 1. Inserisci il braccio del Servo nell'albero di uscita del Servo. Se necessario, fissalo con le viti.
.. #. Collega **VBUS** (non 3V3) e GND di Pico W al bus di alimentazione della breadboard.
.. #. Collega il filo rosso del servo al bus di alimentazione positivo con un jumper.
.. #. Collega il filo giallo del servo al pin GP15 con un cavo jumper.
.. #. Collega il filo marrone del servo al bus di alimentazione negativo con un cavo jumper.


**Codice**

.. note::

    * Apri il file ``3.7_swinging_servo.py`` nel percorso ``kepler-kit-main/micropython`` o copia questo codice in Thonny, poi clicca su "Esegui Script Corrente" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra.

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    servo = machine.PWM(machine.Pin(15))
    servo.freq(50)

    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def servo_write(pin,angle):
        pulse_width=interval_mapping(angle, 0, 180, 0.5,2.5)
        duty=int(interval_mapping(pulse_width, 0, 20, 0,65535))
        pin.duty_u16(duty)

    while True:
        for angle in range(180):
            servo_write(servo,angle)
            utime.sleep_ms(20)
        for angle in range(180,-1,-1):
            servo_write(servo,angle)
            utime.sleep_ms(20)


Quando il programma è in esecuzione, possiamo vedere il braccio del Servo oscillare avanti e indietro da 0° a 180°.

Il programma continuerà a funzionare a causa del ciclo ``while True``, quindi dovremo premere il pulsante Stop per terminare il programma.

**Come funziona?**

Abbiamo definito la funzione ``servo_write()`` per far funzionare il servo.

Questa funzione ha due parametri:

* ``pin``, il pin GPIO che controlla il servo.
* ``angle``, l'angolo dell'albero di uscita.

In questa funzione, viene chiamata ``interval_mapping()`` per mappare l'intervallo angolare 0 ~ 180 all'intervallo di larghezza dell'impulso 0,5 ~ 2,5 ms.

.. code-block:: python

    pulse_width=interval_mapping(angle, 0, 180, 0.5,2.5)

Perché è 0,5~2,5? Questo è determinato dal modo di funzionamento del Servo.

:ref:`cpn_servo`

Successivamente, la larghezza dell'impulso viene convertita da periodo a duty cycle. Poiché ``duty_u16()`` non può avere decimali quando viene utilizzato (il valore non può essere di tipo float), abbiamo usato ``int()`` per forzare la conversione del duty in un tipo int.

.. code-block:: python

    duty=int(interval_mapping(pulse_width, 0, 20, 0,65535))

Infine, il valore del duty viene scritto in ``duty_u16()``.
