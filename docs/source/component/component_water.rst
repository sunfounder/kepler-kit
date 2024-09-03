.. note::

    Ciao, benvenuto nella Community SunFounder per appassionati di Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_water_level:

Sensore di Livello dell'Acqua
=================================

|img_water_sensor|

Il sensore di livello dell'acqua trasmette il segnale rilevato al controller, e il computer nel controller confronta il segnale misurato con quello impostato per derivare la deviazione, emettendo poi comandi di "accensione" e "spegnimento" alla valvola elettrica dell'acqua in base alla natura della deviazione per garantire che il contenitore raggiunga il livello dell'acqua impostato.

Il sensore di livello dell'acqua ha dieci tracce di rame esposte, cinque per l'alimentazione e cinque per i sensori, che vengono incrociate e collegate dall'acqua quando sommerse.
La scheda ha un LED di alimentazione che si accende quando la scheda è sotto tensione.

La combinazione di queste tracce agisce come un resistore variabile, cambiando il valore della resistenza in base al livello dell'acqua.
Per essere più precisi, più il sensore è immerso nell'acqua, migliore è la conducibilità e minore è la resistenza. Al contrario, meno è conduttivo, maggiore è la resistenza.
Successivamente, il sensore elaborerà il segnale di uscita della tensione che verrà inviato al microcontrollore, aiutandoci così a determinare il livello dell'acqua.


.. warning:: 
    Il sensore non può essere completamente immerso nell'acqua, lasciare solo la parte in cui si trovano le dieci tracce a contatto con l'acqua. Inoltre, alimentare il sensore in un ambiente umido accelererà la corrosione della sonda e ridurrà la vita del sensore, quindi raccomandiamo di alimentarlo solo durante la lettura dei dati.


**Esempio**

* :ref:`py_water` (For MicroPython User)
* :ref:`ar_water` (For Arduino User)
* :ref:`per_water_tank` (For Piper Make User)