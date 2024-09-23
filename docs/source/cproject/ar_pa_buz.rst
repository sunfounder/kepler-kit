.. note::

    Ciao, benvenuto nella community di appassionati di SunFounder Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri entusiasti.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a promozioni festive e giveaway.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ar_pa_buz:

3.2 - Tono personalizzato
==========================================


Nel progetto precedente abbiamo utilizzato un cicalino attivo, questa volta utilizzeremo un cicalino passivo.

Come il cicalino attivo, anche quello passivo utilizza il fenomeno dell'induzione elettromagnetica per funzionare. La differenza è che un cicalino passivo non ha una fonte di oscillazione, quindi non emetterà suoni se vengono utilizzati segnali DC.
Ma ciò consente al cicalino passivo di regolare la propria frequenza di oscillazione e di emettere diverse note come "do, re, mi, fa, sol, la, si".

Facciamo emettere una melodia al cicalino passivo!

* :ref:`cpn_buzzer`

**Componenti necessari**

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
        - :ref:`cpn_transistor`
        - 1 (S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 1 (1KΩ)
        - |link_resistor_buy|
    *   - 7
        - Cicalino Passivo :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|

**Schema elettrico**

|sch_buzzer|

Quando l'uscita di GP15 è alta, dopo il resistore di limitazione della corrente da 1K (per proteggere il transistor), l'S8050 (transistor NPN) condurrà, facendo suonare il cicalino.

Il ruolo dell'S8050 (transistor NPN) è quello di amplificare la corrente e rendere il suono del cicalino più forte. In realtà, puoi anche collegare il cicalino direttamente a GP15, ma noterai che il suono del cicalino sarà più debole.

**Cablaggio**

|img_buzzer|

Nel kit sono inclusi due cicalini, utilizziamo un cicalino passivo (quello con PCB esposto sul retro).

Il cicalino necessita di un transistor per funzionare, qui utilizziamo l'S8050.

|wiring_buzzer|

**Codice**

.. note::

   * Puoi aprire il file ``3.2_custom_tone.ino`` nel percorso ``kepler-kit-main/arduino/3.2_custom_tone``. 
   * Oppure copia questo codice nell'**Arduino IDE**.
   * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload** .

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/69c55e56-9eeb-46bb-b3a8-b354c500cc17/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

**Come funziona?**

Se al cicalino passivo viene dato un segnale digitale, può solo spingere il diaframma senza produrre suono.

Pertanto, utilizziamo la funzione ``tone()`` per generare il segnale PWM e far suonare il cicalino passivo.

Questa funzione ha tre parametri:

  * **pin**, il pin GPIO che controlla il cicalino.
  * **frequency**, il tono del cicalino è determinato dalla frequenza, più alta è la frequenza, più alto sarà il tono.
  * **duration**, la durata del tono.

* `tone <https://www.arduino.cc/reference/en/language/functions/advanced-io/tone/>`_

**Scopri di più**

Possiamo simulare il tono specifico secondo la frequenza fondamentale del pianoforte, così da suonare un brano musicale completo.

* `Piano key frequencies - Wikipedia <https://en.wikipedia.org/wiki/Piano_key_frequencies>`_

.. note::

   * Puoi aprire il file ``3.2_custom_tone_2.ino`` nel percorso ``kepler-kit-main/arduino/3.2_custom_tone_2``. 
   * Oppure copia questo codice nell'**Arduino IDE**.
   * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/f934c785-7204-4972-aae5-01edde3c79cc/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>
