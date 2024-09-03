.. note::

    Ciao, benvenuto nella Community di SunFounder per appassionati di Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino e ESP32 con altri appassionati.

    **Perché unirsi a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e anteprime esclusive.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_4_dit_7_segment:

Display a 7 segmenti a 4 cifre
==================================

Il display a 7 segmenti a 4 cifre è costituito da quattro display a 7 segmenti che funzionano insieme.

|img_4-digit-sche|

Il display a 7 segmenti a 4 cifre funziona in modo indipendente. 
Utilizza il principio della persistenza visiva umana per visualizzare 
rapidamente i caratteri di ciascun segmento a 7 segmenti in un ciclo, 
formando stringhe continue.

Ad esempio, quando sul display appare "1234", "1" viene visualizzato 
sul primo segmento a 7 segmenti, mentre "234" non viene visualizzato. 
Dopo un certo periodo di tempo, il secondo segmento a 7 segmenti mostra 
"2", mentre il 1°, 3° e 4° segmento non mostrano nulla, e così via, i 
quattro display digitali vengono visualizzati a turno. Questo processo è 
molto breve (tipicamente 5 ms) e, grazie all'effetto del reticolo ottico 
e al principio della persistenza visiva, possiamo vedere quattro caratteri 
contemporaneamente.

|img_4-digit-sche-ca| 

**Codici di visualizzazione** 

Per aiutarti a comprendere come i display a 7 segmenti (Catodo Comune) visualizzano i numeri, abbiamo creato la seguente tabella. I numeri sono i numeri da 0 a F visualizzati sul display a 7 segmenti; (DP) GFEDCBA si riferisce al set di LED corrispondente impostato su 0 o 1. Ad esempio, 00111111 significa che DP e G sono impostati su 0, mentre gli altri sono impostati su 1. Pertanto, il numero 0 viene visualizzato sul display a 7 segmenti, mentre il codice HEX corrisponde al numero esadecimale.

.. list-table:: Codice dei glifi
    :widths: 20 20 20
    :header-rows: 1

    *   - Numeri	
        - Codice Binario
        - Codice Hex  
    *   - 0	
        - 00111111	
        - 0x3f
    *   - 1	
        - 00000110	
        - 0x06
    *   - 2	
        - 01011011	
        - 0x5b
    *   - 3	
        - 01001111	
        - 0x4f
    *   - 4	
        - 01100110	
        - 0x66
    *   - 5	
        - 01101101	
        - 0x6d
    *   - 6	
        - 01111101	
        - 0x7d
    *   - 7	
        - 00000111	
        - 0x07
    *   - 8	
        - 01111111	
        - 0x7f
    *   - 9	
        - 01101111	
        - 0x6f
    *   - A	
        - 01110111	
        - 0x77
    *   - B
        - 01111100	
        - 0x7c
    *   - C	
        - 00111001	
        - 0x39
    *   - D	
        - 01011110	
        - 0x5e
    *   - E	
        - 01111001	
        - 0x79
    *   - F	
        - 01110001	
        - 0x71


**Esempio**

* :ref:`py_74hc_4dig` (For MicroPython User)
* :ref:`py_passage_counter` (For MicroPython User)
* :ref:`py_10_second` (For MicroPython User)
* :ref:`py_traffic_light` (For MicroPython User)
* :ref:`ar_74hc_4dig` (For Arduino User)