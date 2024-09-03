.. note::

    Ciao, benvenuto nella Community SunFounder per appassionati di Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_servo:

Servo
===========

|img_servo|

Un servo è generalmente composto dalle seguenti parti: case, albero, sistema di ingranaggi, potenziometro, motore DC e scheda integrata.  

Funziona così: il microcontrollore invia segnali PWM al servo, la scheda integrata all'interno del servo riceve i segnali attraverso il pin di segnale e controlla il motore interno per farlo girare. Di conseguenza, il motore aziona il sistema di ingranaggi che, dopo la decelerazione, motiva l'albero. L'albero e il potenziometro del servo sono collegati insieme. Quando l'albero ruota, aziona il potenziometro, che a sua volta invia un segnale di tensione alla scheda integrata. Quest'ultima determina la direzione e la velocità di rotazione in base alla posizione attuale, in modo che il servo possa fermarsi esattamente nella posizione definita e mantenerla.

|img_servo_i|

L'angolo è determinato dalla durata di un impulso applicato al filo di controllo. Questo è chiamato Pulse Width Modulation (Modulazione della Larghezza di Impulso). Il servo si aspetta di ricevere un impulso ogni 20 ms. La lunghezza dell'impulso determinerà di quanto girerà il motore. Ad esempio, un impulso di 1,5 ms farà girare il motore fino alla posizione di 90 gradi (posizione neutra).
Quando viene inviato un impulso al servo inferiore a 1,5 ms, il servo ruota in una posizione e mantiene il suo albero d'uscita a un certo numero di gradi in senso antiorario rispetto al punto neutro. Quando l'impulso è più ampio di 1,5 ms avviene il contrario. La larghezza minima e massima dell'impulso che comanda il servo a girare verso una posizione valida dipendono da ciascun servo. Generalmente, l'impulso minimo sarà largo circa 0,5 ms e l'impulso massimo sarà largo 2,5 ms.

|img_servo_duty|


.. Esempio
.. -------------------

.. :ref:`Servo Oscillante`

**Esempio**

* :ref:`py_servo` (For MicroPython User)
* :ref:`py_somato_controller` (For MicroPython User)
* :ref:`ar_servo` (For Arduino User)
* :ref:`per_water_tank` (For Piper Make User)
* :ref:`per_swing_servo` (For Piper Make User)
* :ref:`per_lucky_cat` (For Piper Make User)