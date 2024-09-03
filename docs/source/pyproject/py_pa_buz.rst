.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_pa_buz:

3.2 Tono Personalizzato
==========================================


Abbiamo utilizzato il cicalino attivo nel progetto precedente, questa volta useremo il cicalino passivo.

Come il cicalino attivo, anche il cicalino passivo utilizza il fenomeno dell'induzione elettromagnetica per funzionare. La differenza è che un cicalino passivo non ha una sorgente di oscillazione, quindi non emetterà un suono se vengono utilizzati segnali DC.
Tuttavia, ciò consente al cicalino passivo di regolare la propria frequenza di oscillazione ed emettere diverse note come "do, re, mi, fa, sol, la, si".

Facciamo emettere una melodia al cicalino passivo!

* :ref:`cpn_buzzer`

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
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 1(1KΩ)
        - |link_resistor_buy|
    *   - 7
        - Passive :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|

**Schema Elettrico**

|sch_buzzer|

Quando l'uscita GP15 è alta, dopo il resistore limitatore di corrente da 1K (per proteggere il transistor), l'S8050 (transistor NPN) si condurrà, facendo suonare il cicalino.

Il ruolo dell'S8050 (transistor NPN) è di amplificare la corrente e rendere il suono del cicalino più forte. In realtà, puoi anche collegare il cicalino direttamente a GP15, ma noterai che il suono del cicalino sarà più debole.


**Collegamenti**

|img_buzzer|

Il kit include due cicalini, utilizziamo un cicalino passivo (quello con un PCB esposto sul retro).

Il cicalino necessita di un transistor per funzionare, qui utilizziamo l'S8050.

|wiring_buzzer|

.. 1. Connect 3V3 and GND of Pico W to the power bus of the breadboard.
.. #. Connect the positive pin of the buzzer to the positive power bus.
.. #. Connect the cathode pin of the buzzer to the **collector** lead of the transistor.
.. #. Connect the **base** lead of the transistor to the GP15 pin through a 1kΩ resistor.
.. #. Connect the **emitter** lead of the transistor to the negative power bus.


**Codice**

.. note::

    * Apri il file ``3.2_custom_tone.py`` nel percorso ``kepler-kit-main/micropython`` o copia questo codice in Thonny, poi clicca su "Esegui Script Corrente" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra.

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    buzzer = machine.PWM(machine.Pin(15))

    def tone(pin,frequency,duration):
        pin.freq(frequency)
        pin.duty_u16(30000)
        utime.sleep_ms(duration)
        pin.duty_u16(0)

    tone(buzzer,440,250)
    utime.sleep_ms(500)
    tone(buzzer,494,250)
    utime.sleep_ms(500)
    tone(buzzer,523,250)


**Come funziona?**

Se al cicalino passivo viene dato un segnale digitale, può solo continuare a spingere il diaframma senza produrre suono.

Pertanto, utilizziamo la funzione ``tone()`` per generare il segnale PWM e far suonare il cicalino passivo.

Questa funzione ha tre parametri:

* **pin**, il pin GPIO che controlla il cicalino.
* **frequenza**, l'intonazione del cicalino è determinata dalla frequenza, maggiore è la frequenza, più alta sarà l'intonazione.
* **Durata**, la durata della nota.

Utilizziamo la funzione ``duty_u16()`` per impostare il ciclo di lavoro a 30000 (circa il 50%). Può essere un altro valore, purché generi un segnale elettrico discontinuo per oscillare.



**Approfondisci**

Possiamo simulare un tono specifico in base alla frequenza fondamentale del pianoforte, in modo da suonare un brano musicale completo.

* `Piano key frequencies - Wikipedia <https://en.wikipedia.org/wiki/Piano_key_frequencies>`_



.. note::

    * Apri il file ``3.2_custom_tone_2.py`` nel percorso ``kepler-kit-main/micropython`` o copia questo codice in Thonny, poi clicca su "Esegui Script Corrente" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra.

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.


.. code-block:: python

    import machine
    import utime

    NOTE_C4 = 262
    NOTE_G3 = 196
    NOTE_A3 = 220
    NOTE_B3 = 247

    melody =[NOTE_C4,NOTE_G3,NOTE_G3,NOTE_A3,NOTE_G3,NOTE_B3,NOTE_C4]

    buzzer = machine.PWM(machine.Pin(15))

    def tone(pin,frequency,duration):
        pin.freq(frequency)
        pin.duty_u16(30000)
        utime.sleep_ms(duration)
        pin.duty_u16(0)

    for note in melody:
        tone(buzzer,note,250)
        utime.sleep_ms(150)
