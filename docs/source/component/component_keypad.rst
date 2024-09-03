.. note::

    Ciao, benvenuto nella Community SunFounder per appassionati di Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_keypad:

Tastierino 4x4
========================

Nei sistemi a microcontrollore, se si utilizzano più tasti come nel caso di una serratura elettronica o di un tastierino telefonico, generalmente sono necessari almeno 12-16 tasti, solitamente disposti in una tastiera a matrice.

Il tastierino a matrice, chiamato anche tastiera a righe, è un tastierino con quattro linee I/O come righe e quattro linee I/O come colonne. Un tasto è posizionato a ogni intersezione tra le righe e le colonne. Quindi, il numero di tasti sulla tastiera è 4x4. Questa struttura di tastiera a righe e colonne può migliorare efficacemente l'utilizzo delle porte I/O in un sistema a microcontrollore.

I loro contatti sono accessibili tramite un connettore adatto per il collegamento con un cavo a nastro o per l'inserimento in una scheda a circuito stampato. 
In alcuni tastierini, ogni pulsante è collegato a un contatto separato nel connettore, mentre tutti i pulsanti condividono un comune collegamento a terra.

|img_keypad|

Più frequentemente, i pulsanti sono codificati a matrice, il che significa che ciascuno di essi connette una coppia unica di conduttori in una matrice. 
Questa configurazione è adatta per il polling da parte di un microcontrollore, che può essere programmato per inviare un impulso di uscita a ciascuno dei quattro fili orizzontali a turno. 
Durante ogni impulso, verifica i restanti quattro fili verticali in sequenza, per determinare quale, se presente, sta trasmettendo un segnale. 
Resistenze di pullup o pulldown dovrebbero essere aggiunte ai fili di ingresso per prevenire comportamenti imprevedibili degli ingressi del microcontrollore quando non è presente alcun segnale.

* `Keypad - Wikipedia <https://en.wikipedia.org/wiki/Keypad>`_

**Esempio**

* :ref:`py_keypad` (For MicroPython User)
* :ref:`py_guess_number` (For MicroPython User)
* :ref:`ar_keypad` (For Arduino User)