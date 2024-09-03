.. note::

    Ciao, benvenuto nella Community di Appassionati di Raspberry Pi & Arduino & ESP32 di SunFounder su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa ai giveaway e alle promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _add_libraries_py:

1.4 Caricare le Librerie su Pico
=====================================

In alcuni progetti, avrai bisogno di librerie aggiuntive. Quindi, caricheremo queste librerie su Raspberry Pi Pico W prima di tutto, così potremo eseguire il codice direttamente in seguito.

#. Scarica il codice pertinente dal link qui sotto.

   * :download:`SunFounder Kepler Kit <https://github.com/sunfounder/kepler-kit/archive/refs/heads/main.zip>`

#. Apri Thonny IDE, collega il Pico al tuo computer con un cavo micro USB e clicca sull'interprete "MicroPython (Raspberry Pi Pico).COMXX" nell'angolo in basso a destra.

    .. image:: img/sec_inter.png

#. Nella barra di navigazione superiore, clicca su **View** -> **Files**.

    .. image:: img/th_files.png

#. Cambia il percorso alla cartella dove hai scaricato il `code package <https://github.com/sunfounder/kepler-kit/archive/refs/heads/main.zip>`_, quindi vai alla cartella ``kepler-kit-main/libs``.

    .. image:: img/th_path.png

#. Seleziona tutti i file o le cartelle nella cartella ``libs/``, fai clic con il tasto destro e seleziona **Upload to**, ci vorrà un po' di tempo per caricare.

    .. image:: img/th_upload.png

#. Ora vedrai i file appena caricati all'interno del tuo drive ``Raspberry Pi Pico``.

    .. image:: img/th_done.png
