.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_rfid:

6.5 Identificazione a Radiofrequenza
================================================

L'Identificazione a Radiofrequenza (RFID) è una tecnologia che utilizza la comunicazione wireless tra un oggetto (o tag) e un dispositivo interrogante (o lettore) per tracciarlo e identificarlo. Il raggio di trasmissione del tag è limitato a diversi metri. Lettori e tag non richiedono necessariamente una linea di vista.

La maggior parte dei tag contiene un circuito integrato (IC) e un'antenna.
Oltre a memorizzare informazioni, il microchip gestisce la comunicazione con il lettore tramite radiofrequenza (RF).
Nei tag passivi, non c'è una fonte di energia indipendente e si affidano a un segnale elettromagnetico esterno dal lettore per alimentarsi.
Un tag attivo è alimentato da una fonte di energia indipendente, come una batteria. Di conseguenza, possono essere più potenti in termini di elaborazione, trasmissione e portata.

* :ref:`cpn_mfrc522`

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
        - :ref:`cpn_mfrc522`
        - 1
        - |link_rfid_buy|

**Schema**


|sch_rfid|


**Collegamenti**

|wiring_rfid|

**Codice**

Qui è necessario utilizzare le librerie nella cartella ``mfrc522``, verifica se sono state caricate su Pico W, per un tutorial dettagliato fai riferimento a :ref:`add_libraries_py`.

La funzione principale è suddivisa in due parti:

* ``6.5_rfid_write.py``: Utilizzata per scrivere informazioni sulla scheda (o chiave).
* ``6.5_rfid_read.py``: Utilizzata per leggere le informazioni nella scheda (o chiave).

Apri il file ``6.5_rfid_write.py`` nel percorso ``kepler-kit-main/micropython`` o copia questo codice in Thonny, poi clicca su "Esegui Script Corrente" o semplicemente premi F5 per eseguirlo.

Dopo l'esecuzione, potrai digitare un messaggio nella shell e poi avvicinare la scheda (o chiave) al modulo MFRC522 per scrivere il messaggio.

.. code-block:: python

    from mfrc522 import SimpleMFRC522

    reader = SimpleMFRC522(spi_id=0,sck=18,miso=16,mosi=19,cs=17,rst=9)

    def write():
        to_write = input("Please enter the message: ")
        print("Writing...Please place the card...")
        id, text = reader.write(to_write)
        print("ID: %s\nText: %s" % (id,text))

    write()

Apri il file ``6.5_rfid_read.py`` nel percorso ``kepler-kit-main/micropython`` o copia questo codice in Thonny, poi clicca su "Esegui Script Corrente" o semplicemente premi F5 per eseguirlo.

Dopo l'esecuzione, potrai leggere il messaggio memorizzato nella scheda (o chiave).

.. code-block:: python

    from mfrc522 import SimpleMFRC522

    reader = SimpleMFRC522(spi_id=0,sck=18,miso=16,mosi=19,cs=17,rst=9)

    def read():
        print("Reading...Please place the card...")
        id, text = reader.read()
        print("ID: %s\nText: %s" % (id,text))

    read()

**Come funziona?**

.. code-block:: python

    from mfrc522 import SimpleMFRC522

    reader = SimpleMFRC522(spi_id=0,sck=18,miso=16,mosi=19,cs=17,rst=9)

Istanziamento della classe ``SimpleMFRC522()``.

.. code-block:: python

    id, text = reader.read()

Questa funzione viene utilizzata per leggere i dati della scheda. Se la lettura ha successo, verranno restituiti id e text.

.. code-block:: python

    id, text = reader.write("text")

Questa funzione viene utilizzata per scrivere informazioni sulla scheda, premi il tasto **Enter** per terminare la scrittura. 
``text`` è l'informazione da scrivere sulla scheda.
