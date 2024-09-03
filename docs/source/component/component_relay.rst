.. note::

    Ciao, benvenuto nella Community SunFounder per appassionati di Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_relay:

Relè
==========================================

|img_relay|

Come sappiamo, un relè è un dispositivo utilizzato per fornire 
una connessione tra due o più punti o dispositivi in risposta al 
segnale di ingresso applicato. In altre parole, i relè forniscono 
isolamento tra il controller e il dispositivo, poiché i dispositivi 
possono funzionare sia in corrente alternata (AC) che continua (DC). 
Tuttavia, ricevono segnali da un microcontrollore che funziona in 
corrente continua, richiedendo quindi un relè per colmare il divario. 
Il relè è estremamente utile quando è necessario controllare una grande 
quantità di corrente o tensione con un piccolo segnale elettrico.

Ci sono 5 componenti in ogni relè:

**Elettromagnete** - Consiste in un nucleo di ferro avvolto da una 
bobina di fili. Quando l'elettricità passa attraverso di esso, diventa 
magnetico. Pertanto, viene chiamato elettromagnete.

**Armatura** - La striscia magnetica mobile è conosciuta come armatura. 
Quando la corrente scorre attraverso di essa, la bobina si energizza, 
producendo un campo magnetico che viene utilizzato per aprire o chiudere 
i contatti normalmente aperti (N/O) o normalmente chiusi (N/C). L'armatura 
può essere azionata sia con corrente continua (DC) che con corrente alternata (AC).

**Molla** - Quando non scorre corrente attraverso la bobina dell'elettromagnete, 
la molla tira l'armatura lontano, impedendo che il circuito si completi.

Set di **contatti elettrici** - Ci sono due punti di contatto:

- Normalmente aperti - collegati quando il relè è attivato e scollegati quando è inattivo.

- Normalmente chiusi - non collegati quando il relè è attivato e collegati quando è inattivo.

**Telaio stampato** - I relè sono coperti da plastica per protezione.

Il principio di funzionamento del relè è semplice. Quando viene fornita 
alimentazione al relè, la corrente inizia a fluire attraverso la bobina di 
controllo; di conseguenza, l'elettromagnete inizia a energizzarsi. Quindi 
l'armatura viene attratta dalla bobina, tirando verso il basso il contatto 
mobile e collegandolo ai contatti normalmente aperti. In questo modo, il 
circuito con il carico viene energizzato. Interrompere il circuito avverrà 
in modo simile, poiché il contatto mobile verrà tirato verso i contatti 
normalmente chiusi sotto la forza della molla. In questo modo, l'accensione 
e lo spegnimento del relè possono controllare lo stato di un circuito di carico.

|img_relay_sche|


* `Relay - Wikipedia <https://en.wikipedia.org/wiki/Relay>`_

**Esempio**


* :ref:`py_relay` (For MicroPython User)
* :ref:`ar_relay` (For Arduino User)