.. note::

    Ciao, benvenuto nella Community SunFounder per appassionati di Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_micro_switch:

Microinterruttore
========================

|img_micro_switch|

La costruzione di un microinterruttore è davvero semplice. Le principali parti dell'interruttore sono:

|img_micro_switch2|

* 1. Pistoncino (Attuatore)
* 2. Coperchio
* 3. Elemento mobile
* 4. Supporto
* 5. Custodia
* 6. Terminale NO: normalmente aperto
* 7. Terminale NC: normalmente chiuso
* 8. Contatto
* 9. Braccio mobile

Dopo che un microinterruttore entra in contatto fisico con un oggetto, i suoi contatti cambiano posizione. Il principio di funzionamento di base è il seguente.

Quando il pistoncino è nella posizione di rilascio o di riposo:

* Il circuito normalmente chiuso può condurre corrente.
* Il circuito normalmente aperto è isolato elettricamente.

Quando il pistoncino è premuto o attivato:

* Il circuito normalmente chiuso è aperto.
* Il circuito normalmente aperto è chiuso.

|img_micro_switch1|

**Esempio**

* :ref:`py_micro` (For MicroPython User)
* :ref:`ar_micro` (For Arduino User)
* :ref:`per_service_bell` (For Piper Make User)