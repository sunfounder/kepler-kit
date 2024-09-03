.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché Unirti?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a promozioni festive e concorsi a premi.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _quick_guide_piper:

1.2 Guida Rapida su Piper Make
=================================

1. Crea un Nuovo Progetto
------------------------------

Ora che hai configurato Pico W, è il momento di imparare a programmarlo.
Iniziamo accendendo il LED integrato.


Passa a ``MODALITÀ CREATIVA`` e clicca sul pulsante **Nuovo Progetto**,
un nuovo progetto apparirà nella sezione **I MIEI PROGETTI** e
gli sarà assegnato un nome casuale che potrà essere cambiato dalla pagina di programmazione.

|media9-s|

Poi apri il nuovo progetto appena creato.

|media11-s|

Ora vai alla pagina di programmazione di Piper Make.

|piper_intro1|

* **START**: Utilizzato per eseguire il codice; se è grigio, significa che non è connesso a Pico W in questo momento.
* **Palette di blocchi**: Contiene diversi tipi di blocchi.
* **CONNECT**: Utilizzato per connettersi a Pico W; è verde quando non è connesso a Pico W, quando è connesso diventa **DISCONNECT (rosso)**.
* **Area di Programmazione**: Trascina qui i blocchi per completare la programmazione impilandoli.
* **Area degli Strumenti**: Puoi cliccare su **DIGITAL VIEW** per vedere la distribuzione dei pin di Pico W; puoi visualizzare le informazioni di stampa in **CONSOLE**; puoi leggere i dati da **DATA** e puoi cliccare su **Python** per vedere il codice sorgente in Python.
* **Nome e descrizione del progetto**: Puoi cambiare il nome e la descrizione del progetto.
* **DOWNLOAD**: Puoi cliccare sul pulsante **DOWNLOAD** per salvarlo localmente, solitamente in formato **|**. La prossima volta puoi importarlo tramite il pulsante **Importa Progetto** nella home page.

Clicca sulla palette **Chip** e trascina il blocco [start] nell'**Area di Programmazione**.

|media12|

Poi trascina il blocco [loop] dalla palette **loops** sotto il blocco [start], e imposta l'intervallo del ciclo a 1 secondo.

|media14|

Il LED integrato del Raspberry Pi Pico è collegato al pin 25, quindi utilizziamo il blocco [accendi/spegni pin ()] nella palette **Chip** per controllarlo.

|media15|

.. _connect_pico_per:

2. Connetti a Pico W
--------------------------

Ora clicca sul pulsante **CONNECT** per connetterti a Pico W; dopo aver cliccato, apparirà una nuova finestra popup.

|media16|

Seleziona la porta **CircuitPython CDC control (COMXX)** riconosciuta, poi clicca su **Connetti**.

|pico_port|

Quando la connessione avrà successo, il **CONNECT** verde nell'angolo in basso a sinistra cambierà in **DISCONNECT** rosso.

|disconnect_per|

3. Esegui il Codice
-----------------------

Ora clicca sul pulsante **START** per eseguire questo codice e vedrai il LED su Pico W accendersi. Se il pulsante è grigio, significa che Pico W non è connesso; per favore, riconnettilo.

|media166|

Poi spegni il pin 25 ogni secondo nel ciclo, e clicca di nuovo su **START** in alto a sinistra, così potrai vedere il LED integrato lampeggiare.

|media17|
