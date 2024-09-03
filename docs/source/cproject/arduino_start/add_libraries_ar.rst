.. note::

    Ciao, benvenuto nella community di appassionati di SunFounder Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Accedi in anteprima agli annunci di nuovi prodotti e alle anticipazioni.
    - **Sconti Speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!


1.4 Installare le librerie (Importante)
===========================================

**Scarica il Codice**

Scarica il codice pertinente dal link sottostante.

* :download:`SunFounder Kepler Kit Example <https://github.com/sunfounder/kepler-kit/archive/refs/heads/main.zip>`

* Oppure consulta il codice su `Kepler Kit - GitHub <https://github.com/sunfounder/kepler-kit>`_

.. _add_libraries_ar:

Aggiungere librerie
------------------------
Una libreria, che raccoglie alcune definizioni di funzioni e file header, di solito
contiene due file: .h (file header, che include la dichiarazione delle funzioni, la 
definizione delle Macro, la definizione del costruttore, ecc.) e .cpp (file di esecuzione, 
con implementazione delle funzioni, definizione delle variabili, e così via). Quando hai bisogno
di usare una funzione di una libreria, devi solo aggiungere un file header
(ad es. #include <dht.h>), e poi chiamare quella funzione. Questo può rendere il tuo
codice più conciso. Se non vuoi usare la libreria, puoi anche
scrivere direttamente la definizione di quella funzione. Tuttavia, il codice
risulterà lungo e difficile da leggere.

Alcune librerie sono già integrate nell'IDE di Arduino, mentre altre
potrebbero dover essere aggiunte. Vediamo quindi come aggiungerle.


#. Apri l'IDE di Arduino e vai su **Sketch** -> **Include Library** -> **Add .ZIP Library**.

   .. image:: img/a2dp_add_zip.png

#. Naviga nella directory in cui si trovano i file della libreria, come la cartella ``kepler-kit-main\arduino\libraries``, e seleziona il file della libreria desiderata, come ``LiquidCrystal_I2C.zip``. Quindi, fai clic su **Open**.

   .. image:: img/a2dp_choose.png

#. Dopo un breve momento, riceverai una notifica che indica l'installazione avvenuta con successo.

   .. image:: img/a2dp_success.png

#. Ripeti lo stesso processo per aggiungere le altre librerie.


.. note::

   Le librerie installate si trovano nella directory predefinita delle librerie dell'IDE di Arduino, che di solito si trova in ``C:\Users\xxx\Documents\Arduino\libraries``.

   Se la tua directory delle librerie è diversa, puoi controllarla andando su **File** -> **Preferences**.

      .. image:: img/install_lib1.png
