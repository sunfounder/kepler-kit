.. note::

    Ciao, benvenuto nella Community di SunFounder per appassionati di Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_7_segment:

Display a 7 Segmenti
=========================

|img_7seg|

Un display a 7 segmenti è un componente a forma di 8 che racchiude 7 LED. Ogni LED è chiamato segmento - quando alimentato, un segmento forma parte di una cifra da visualizzare.

Esistono due tipi di connessione dei pin: Catodo Comune (CC) e Anodo Comune (CA). Come suggerisce il nome, un display CC ha tutti i catodi dei 7 LED collegati insieme, mentre un display CA ha tutti gli anodi dei 7 segmenti collegati insieme.

In questo kit, utilizziamo il display a 7 segmenti con Catodo Comune, ecco il simbolo elettronico.

|img_7seg_cathode|

Ciascuno dei LED nel display è assegnato a un segmento posizionale con uno dei suoi pin di connessione che esce dal pacchetto di plastica rettangolare. Questi pin LED sono etichettati da "a" a "g" rappresentando ciascun LED individuale. Gli altri pin LED sono collegati insieme formando un pin comune. Così, polarizzando in avanti i pin appropriati dei segmenti LED in un ordine particolare, alcuni segmenti si illumineranno e altri rimarranno spenti, mostrando così il carattere corrispondente sul display.

* `Seven-segment Display - Wikipedia <https://en.wikipedia.org/wiki/Seven-segment_display>`_

**Codici di visualizzazione** 

Per aiutarti a comprendere come i display a 7 segmenti (Catodo Comune) visualizzano i numeri, abbiamo creato la seguente tabella. I numeri rappresentano i numeri da 0 a F visualizzati sul display a 7 segmenti; (DP) GFEDCBA si riferisce al set di LED corrispondente impostato su 0 o 1. Ad esempio, 00111111 significa che DP e G sono impostati su 0, mentre gli altri sono impostati su 1. Pertanto, il numero 0 viene visualizzato sul display a 7 segmenti, mentre il codice HEX corrisponde al numero esadecimale.

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

.. Example
.. -------------------

.. :ref:`LED Segment Display`

**Esempio**

* :ref:`py_74hc_7seg` (Per utenti MicroPython)
* :ref:`ar_74hc_7seg` (Per utenti Arduino)
