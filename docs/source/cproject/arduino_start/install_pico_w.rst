.. note::

    Ciao, benvenuto nella community di appassionati di SunFounder Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Accedi in anteprima agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _setup_pico_arduino:

1.3 Configurazione del Raspberry Pi Pico W (Importante)
============================================================

1. Installazione del firmware UF2
-------------------------------------

Quando colleghi per la prima volta il Raspberry Pi Pico W o tieni premuto il pulsante BOOTSEL mentre lo inserisci, vedrai il dispositivo apparire come un'unità senza essere assegnato a una porta COM. Questo rende impossibile caricare il codice.

Per risolvere questo problema, è necessario installare il firmware UF2. Questo firmware supporta MicroPython ed è compatibile anche con l'Arduino IDE.

1. Scarica il firmware UF2 dal link qui sotto.

    * :download:`Raspberry Pi Pico W UF2 Firmware <https://micropython.org/download/rp2-pico-w/rp2-pico-w-latest.uf2>`

2. Collega il tuo Raspberry Pi Pico W al computer utilizzando un cavo Micro USB. Il tuo Pico W sarà montato come un dispositivo di archiviazione di massa denominato **RPI-RP2**.

    .. image:: img/install_pico_plugin.png

3. Trascina e rilascia il firmware UF2 scaricato nell'unità **RPI-RP2**.

    .. image:: img/install_pico_uf2.png

4. Dopo questo passaggio, l'unità **RPI-RP2** scomparirà e potrai procedere con i passaggi successivi.


2. Installazione del Pacchetto Board
------------------------------------------

Per programmare il Raspberry Pi Pico W, dovrai installare il pacchetto corrispondente nell'Arduino IDE. Ecco una guida passo-passo:

1. Nella finestra **Boards Manager**, cerca **pico**. Clicca sul pulsante **Installa** per avviare l'installazione. Questo installerà il pacchetto **Arduino Mbed OS RP2040 Boards**, che include il supporto per il Raspberry Pi Pico W.

    .. image:: img/install_pico.png

2. Durante il processo, appariranno alcuni prompt per l'installazione di specifici driver di dispositivo. Seleziona **"Installa"**.

    .. image:: img/install_pico_sa.png

3. Al termine, riceverai una notifica che indicherà il completamento dell'installazione.

3. Selezione della Scheda e della Porta
------------------------------------------

1. Per selezionare la scheda appropriata, vai su **Tools** -> **Board** -> **Arduino Mbed OS RP2040 Boards** -> **Raspberry Pi Pico**.

    .. image:: img/install_pico_tool_board.png

2. Se il tuo Raspberry Pi Pico W è collegato al computer, imposta la porta corretta andando su **Tools** -> **Port**.

    .. image:: img/install_pico_tool_port.png

3. Arduino 2.0 offre una nuova funzione di selezione rapida. Per il Raspberry Pi Pico W, che generalmente non viene riconosciuto automaticamente, clicca su **Select other board and port**.

    .. image:: img/install_pico_select.png

4. Digita **Raspberry Pi Pico** nella barra di ricerca, selezionalo quando appare, scegli la porta appropriata e clicca su **OK**.

    .. image:: img/install_pico_board.png

5. Potrai facilmente riselezionarlo in seguito tramite questa finestra di accesso rapido.

    .. image:: img/install_pico_quick.png

6. Uno di questi metodi ti permetterà di impostare correttamente la scheda e la porta. Ora sei pronto per caricare il codice sul Raspberry Pi Pico W.

4. Caricamento del Codice
------------------------------

Ora vediamo come caricare il codice sul tuo Raspberry Pi Pico W.

1. Apri qualsiasi file ``.ino`` o utilizza lo sketch vuoto attualmente visualizzato. Poi, clicca sul pulsante **Upload**.

    .. image:: img/install_pico_upload.png

2. Attendi che appaia il messaggio di caricamento, come mostrato di seguito.

    .. image:: img/install_pico_upload_dot.png

3. Tieni premuto il pulsante **BOOTSEL**, scollega rapidamente il tuo Raspberry Pi Pico W e ricollegalo.

    .. image:: img/led_onboard.png 

    .. note::
        
        * Questo passaggio è cruciale, soprattutto per i nuovi utenti dell'Arduino IDE. Saltare questo passaggio comporterà un caricamento fallito.

        * Una volta caricato con successo il codice, il tuo Pico W sarà riconosciuto dal computer. Per utilizzi futuri, sarà sufficiente collegarlo al computer.

4. Apparirà un prompt che indica il caricamento avvenuto con successo.

    .. image:: img/install_pico_upload_done.png
