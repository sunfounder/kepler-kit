.. note::

    Ciao, benvenuto nella Community di Appassionati di Raspberry Pi & Arduino & ESP32 di SunFounder su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa ai giveaway e alle promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _install_micropython_on_pico:

1.3 Installare MicroPython sul Tuo Pico
==========================================

Ora passiamo all'installazione di MicroPython sul Raspberry Pi Pico. Thonny IDE offre un modo molto conveniente per installarlo con un solo clic.

.. note::
    Se non desideri aggiornare Thonny, puoi utilizzare l'ufficiale |link_micropython_pi| del Raspberry Pi, trascinando e rilasciando un file ``rp2_pico_xxxx.uf2`` nel Raspberry Pi Pico.



#. Apri Thonny IDE.

    .. image:: img/set_pico1.png

#. Premi e tieni premuto il pulsante **BOOTSEL**, quindi collega il Pico al computer tramite un cavo Micro USB. Rilascia il pulsante **BOOTSEL** dopo che il tuo Pico è stato montato come dispositivo di archiviazione di massa chiamato **RPI-RP2**.

    .. image:: img/bootsel_onboard.png

#. Nell'angolo in basso a destra, fai clic sul pulsante di selezione dell'interprete e seleziona **Install Micropython**.

    .. note::
        Se il tuo Thonny non ha questa opzione, aggiorna alla versione più recente.

    .. image:: img/set_pico2.png

#. Nel campo **Target volume**, apparirà automaticamente il volume del Pico appena collegato, e nella sezione **Micropython variant**, seleziona **Raspberry Pi.Pico/Pico H**.

    .. image:: img/set_pico3.png

#. Fai clic sul pulsante **Install**, attendi il completamento dell'installazione e poi chiudi questa pagina.

    .. image:: img/set_pico4.png


Congratulazioni, ora il tuo Raspberry Pi Pico è pronto per essere utilizzato.
