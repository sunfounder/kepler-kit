.. note::

    Ciao, benvenuto nella Community SunFounder per appassionati di Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_ir_receiver:

Ricevitore a Infrarossi
=================================

Ricevitore IR
----------------------------

|img_irrecv|

* S: Uscita segnale
* +: VCC
* -: GND

Un ricevitore a infrarossi è un componente che riceve segnali infrarossi e può ricevere autonomamente raggi infrarossi e output compatibili con il livello TTL. È simile a un normale transistor in confezione di plastica per dimensioni ed è adatto a tutti i tipi di telecomando a infrarossi e trasmissione a infrarossi.

La comunicazione a infrarossi, o IR, è una tecnologia di comunicazione wireless popolare, a basso costo e facile da usare. La luce a infrarossi ha una lunghezza d'onda leggermente superiore rispetto alla luce visibile, quindi è impercettibile all'occhio umano, ideale per la comunicazione wireless. Uno schema di modulazione comune per la comunicazione a infrarossi è la modulazione a 38KHz.

* Sensore ricevitore IR HX1838 adottato, alta sensibilità
* Può essere utilizzato per il telecomando
* Alimentazione: 3.3~5V
* Interfaccia: Digitale
* Frequenza di modulazione: 38Khz


Telecomando
-------------------------

|img_controller|

Questo è un telecomando wireless a infrarossi sottile con 21 pulsanti funzionali e una distanza di trasmissione fino a 8 metri, adatto per operare un'ampia gamma di dispositivi in una stanza per bambini.

* Dimensioni: 85x39x6mm
* Raggio d'azione del telecomando: 8-10m
* Batteria: Batteria al litio-manganese tipo bottone da 3V
* Frequenza portante a infrarossi: 38KHz
* Materiale di rivestimento superficiale: PET da 0,125mm
* Durata effettiva: oltre 20.000 utilizzi

**Esempio**

* :ref:`py_irremote` (For MicroPython User)
* :ref:`ar_irremote` (For Arduino User)