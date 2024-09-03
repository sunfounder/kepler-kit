.. note::

    Ciao, benvenuto nella Community SunFounder per appassionati di Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_ta6586:

TA6586 - Chip Driver per Motori
====================================

|img_ta6586|

Il TA6586 è un IC monolitico progettato per la guida di motori DC 
bidirezionali. Ha due pin di ingresso logico per controllare la 
direzione, avanti e indietro. Il circuito è caratterizzato da 
un'ottima resistenza alle interferenze, una bassa corrente di standby 
e una bassa caduta di pressione di saturazione in uscita. Dispone di 
un diodo di clamp integrato per invertire l'impatto della corrente di 
rilascio del carico induttivo, rendendolo sicuro e affidabile 
nell'azionamento di relè, motori DC, motori passo-passo o nel controllo 
dell'uso di alimentatori switching.

Il TA6586 è adatto per veicoli giocattolo, motori di aeromobili telecomandati, 
azionamento di valvole automatiche, serrature elettromagnetiche, strumenti di 
precisione e altri circuiti.

**Caratteristiche**

* Bassa corrente di stand-by: ≦2uA
* Ampia gamma di tensione di alimentazione
* Funzione di frenatura integrata
* Protezione contro il surriscaldamento
* Funzione di limitazione della corrente e protezione contro i cortocircuiti
* Confezione DIP8 senza piombo.

**Funzione dei Pin**

|img_ta6586_pin|


**Tabella della Verità degli Ingressi**

|img_ta6586_priciple|


**Esempio**

* :ref:`py_motor` (For MicroPython User)
* :ref:`ar_motor` (For Arduino User)
* :ref:`py_pump` (For MicroPython User)
* :ref:`ar_pump` (For Arduino User)
* :ref:`per_smart_fan` (For Piper Make User)