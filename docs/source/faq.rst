.. note::

    Ciao, benvenuto nella Community SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e alle anteprime.
    - **Sconti Speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

FAQ
=========

Arduino
---------------------

#. Caricamento del codice fallito nell'Arduino IDE?
    * Verifica che il tuo Pico sia correttamente riconosciuto dall'Arduino IDE, la porta dovrebbe essere COMXX (Raspberry Pi Pico), per istruzioni fai riferimento a :ref:`setup_pico_arduino`.
    * Controlla che la scheda (Raspberry Pi Pico) o la porta (COMXX (Raspberry Pi Pico)) siano selezionate correttamente.
    * Se il tuo codice è corretto e hai selezionato la scheda e la porta giuste, ma il caricamento non va a buon fine, puoi cliccare nuovamente sull'icona **Carica**; quando il progresso in basso mostra "Caricamento...", scollega il cavo USB, quindi tieni premuto il pulsante **BOOTSEL** mentre lo ricolleghi, e il codice verrà caricato con successo.

MicroPython
------------------

#. Come aprire ed eseguire il codice?
    Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.

#. Come caricare una libreria su Raspberry Pi Pico W？
    Per tutorial dettagliati, fai riferimento a :ref:`add_libraries_py`.

#. Nessuna opzione MicroPython (Raspberry Pi Pico W) nell'IDE Thonny?
    * Verifica che il tuo Pico W sia collegato al computer tramite un cavo USB.
    * Assicurati di aver installato MicroPython per Pico W (:ref:`install_micropython_on_pico`).
    * L'interprete Raspberry Pi Pico W è disponibile solo nella versione 3.3.3 o superiore di Thonny. Se stai utilizzando una versione precedente, ti preghiamo di aggiornare (:ref:`thonny_ide`).
    * Se il modulo Li-po Charger è collegato alla breadboard in questo momento, scollegalo prima e poi ricollega il Pico W al computer.

#. Impossibile aprire il codice Pico W o salvare il codice su Pico W tramite Thonny IDE?
    * Verifica che il tuo Pico W sia collegato al computer tramite un cavo USB.
    * Assicurati di aver selezionato l'interprete come **MicroPython (Raspberry Pi Pico)**.

#. Raspberry Pi Pico W può essere utilizzato contemporaneamente su Thonny e Arduino?
    NO, è necessario eseguire operazioni diverse.

    * Se l'hai utilizzato su Arduino prima, e ora vuoi usarlo su Thonny IDE, devi :ref:`install_micropython_on_pico` su di esso.
    * Se l'hai utilizzato prima su Thonny, e ora vuoi usarlo su Arduino IDE, devi :ref:`setup_pico_arduino`.

#. Se il tuo computer è win7 e Pico W non può essere rilevato.
    * Scarica il driver USB CDC da http://aem-origin.microchip.com/en-us/mindi-sw-library?swsearch=Atmel%2520USB%2520CDC%2520Virtual%2520COM%2520Driver
    * Decomprimi il file ``amtel_devices_cdc.inf`` in una cartella chiamata ``pico-serial``.
    * Cambia il nome del file ``amtel_devices_cdc.inf`` in ``pico-serial.inf``.
    * Apri/modifica il file ``pico-serial.inf`` in un editor di base come Blocco Note.
    * Rimuovi e sostituisci le righe sotto le seguenti intestazioni:

    .. code-block::

        [DeviceList]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [DeviceList.NTAMD64]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [DeviceList.NTIA64]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [DeviceList.NT]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [Strings]
        Manufacturer = "ATMEL, Inc."
        PI_CDC_PICO = "Pi Pico Serial Port"
        Serial.SvcDesc = "Pi Pico Serial Driver"

    #. Chiudi e salva e assicurati di mantenere il nome come pico-serial.inf.
    #. Vai all'elenco dei dispositivi del tuo PC, trova il Pico sotto Porte, chiamato qualcosa come CDC Device. Un punto esclamativo giallo lo indica.
    #. Fai clic con il tasto destro sul CDC Device e aggiorna o installa il driver scegliendo il file che hai creato dalla posizione in cui l'hai salvato.

Piper Make
------------------

#. Come configurare il Pico W su Piper Make?
    Per tutorial dettagliati, fai riferimento a :ref:`per_setup_pico`.

#. Come scaricare o importare il codice?
    Per tutorial dettagliati, fai riferimento a :ref:`per_save_import`.

#. Come connettersi a Pico W?
    Per tutorial dettagliati, fai riferimento a :ref:`connect_pico_per`.

