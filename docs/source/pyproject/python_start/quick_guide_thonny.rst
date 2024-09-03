.. note::

    Ciao, benvenuto nella Community di Appassionati di Raspberry Pi & Arduino & ESP32 di SunFounder su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa ai giveaway e alle promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

1.5 Guida Rapida a Thonny
==================================

.. _open_run_code_py:

Aprire ed Eseguire Codice Direttamente
---------------------------------------------

La sezione del progetto dedicata al codice ti indica esattamente quale codice utilizzare, quindi fai doppio clic sul file ``.py`` con il numero seriale nel percorso ``kepler-kit-main/micropython/`` per aprirlo.

Tuttavia, è necessario prima scaricare il pacchetto e caricare la libreria, come descritto in :ref:`add_libraries_py`.

#. Apri il codice.

    Ad esempio, ``2.1_hello_led.py``.

    Se fai doppio clic su di esso, si aprirà una nuova finestra a destra. Puoi aprire più codici contemporaneamente.

    |open_code|

#. Seleziona l'interprete corretto

    Utilizza un cavo micro USB per collegare il Pico W al computer e seleziona l'interprete "MicroPython (Raspberry Pi Pico)".

    |sec_inter|

#. Esegui il codice

    Per eseguire lo script, clicca sul pulsante **Run current script** o premi F5.

    |run_it|

    Se il codice contiene informazioni da stampare, appariranno nella Shell; altrimenti, verrà visualizzata solo la seguente informazione.

    Clicca su **View** -> **Edit** per aprire la finestra della Shell se non appare nel tuo Thonny.

        .. code-block::

            MicroPython vx.xx on xxxx-xx-xx; Raspberry Pi Pico W  With RP2040

            Type "help()" for more information.
            >>> %Run -c $EDITOR_CONTENT

    * La prima riga mostra la versione di MicroPython, la data e le informazioni del tuo dispositivo.
    * La seconda riga ti invita a digitare "help()" per ottenere assistenza.
    * La terza riga è un comando di Thonny che indica all'interprete MicroPython sul tuo Pico W di eseguire il contenuto dell'area script - "EDITOR_CONTENT".
    * Se ci sono messaggi dopo la terza riga, di solito sono messaggi che hai detto a MicroPython di stampare o messaggi di errore del codice.


#. Interrompi l'esecuzione

    |stop_it|

    Per interrompere il codice in esecuzione, clicca sul pulsante **Stop/Restart backend**. Il comando **%RUN -c $EDITOR_CONTENT** scomparirà dopo l'interruzione.

#. Salva o salva con nome

    Puoi salvare le modifiche apportate all'esempio aperto premendo **Ctrl+S** o cliccando sul pulsante **Save** in Thonny.

    Il codice può essere salvato come un file separato all'interno del Raspberry Pi Pico W cliccando su **File** -> **Save As**.

    |save_as|

    Seleziona **Raspberry Pi Pico**.

    |sec_pico|

    Poi clicca **OK** dopo aver inserito il nome del file e l'estensione **.py**. Sul drive del Raspberry Pi Pico W, vedrai il file salvato.

    |sec_name|

    .. note::
        Indipendentemente dal nome che dai al tuo codice, è meglio descrivere il tipo di codice, evitando nomi senza senso come ``abc.py``.
        Quando salvi il codice come ``main.py``, verrà eseguito automaticamente all'accensione.


Creare un File ed Eseguirlo
-------------------------------

Il codice è mostrato direttamente nella sezione del codice. Puoi copiarlo in Thonny ed eseguirlo come segue.

#. Crea un nuovo file

    Apri Thonny IDE, clicca sul pulsante **New** per creare un nuovo file vuoto.

    |new_file|

#. Copia il codice

    Copia il codice dal progetto a Thonny IDE.

    |copy_file|

#. Seleziona l'interprete corretto

    Collega il Pico W al tuo computer con un cavo micro USB e seleziona l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra.

    |sec_inter|

#. Esegui e salva il codice

    Devi cliccare su **Run Current Script** o semplicemente premere F5 per eseguirlo. Se il tuo codice non è stato salvato, apparirà una finestra che chiederà di salvare su **Questo computer** o **Raspberry Pi Pico**.

    |where_save|

    .. note::
        Thonny salva il tuo programma sul Raspberry Pi Pico W quando glielo dici, quindi se scolleghi il Pico W e lo colleghi al computer di qualcun altro, il tuo programma rimane intatto.

    Clicca OK dopo aver selezionato la posizione, dato il nome al file e aggiunto l'estensione **.py**.

    |sec_name|

    .. note::
        Indipendentemente dal nome che dai al tuo codice, è meglio descrivere il tipo di codice, evitando nomi senza senso come ``abc.py``.
        Quando salvi il codice come ``main.py``, verrà eseguito automaticamente all'accensione.

    Una volta salvato il tuo programma, verrà eseguito automaticamente e vedrai le seguenti informazioni nell'area Shell.

    Clicca **View** -> **Edit** per aprire la finestra della Shell se non appare nel tuo Thonny.


    .. code-block::

        MicroPython vx.xx.x on xxxx-xx-xx; Raspberry Pi Pico W With RP2040

        Type "help()" for more information.
        >>> %Run -c $EDITOR_CONTENT


    * La prima riga mostra la versione di MicroPython, la data e le informazioni del tuo dispositivo.
    * La seconda riga ti invita a digitare "help()" per ottenere assistenza.
    * La terza riga è un comando di Thonny che indica all'interprete MicroPython sul tuo Pico W di eseguire il contenuto dell'area script - "EDITOR_CONTENT".
    * Se ci sono messaggi dopo la terza riga, di solito sono messaggi che hai detto a MicroPython di stampare o messaggi di errore del codice.


#. Interrompi l'esecuzione

    |stop_it|

    Per interrompere il codice in esecuzione, clicca sul pulsante **Stop/Restart backend**. Il comando **%RUN -c $EDITOR_CONTENT** scomparirà dopo l'interruzione.

#. Apri file

    Ecco due modi per aprire un file di codice salvato.

    * Il primo metodo è cliccare sull'icona di apertura nella barra degli strumenti di Thonny, proprio come quando salvi un programma, ti verrà chiesto se vuoi aprirlo da **questo computer** o **Raspberry Pi Pico**, ad esempio, clicca su **Raspberry Pi Pico** e vedrai un elenco di tutti i programmi che hai salvato sul Pico W.
    * Il secondo è aprire direttamente l'anteprima del file cliccando su **View** -> **File** e poi facendo doppio clic sul file ``.py`` corrispondente per aprirlo.

