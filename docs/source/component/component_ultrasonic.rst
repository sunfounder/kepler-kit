.. note::

    Ciao, benvenuto nella Community SunFounder per appassionati di Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_ultrasonic:

Modulo Ultrasonico
================================

|ultrasonic_pic|

* **TRIG**: Ingresso impulso di attivazione
* **ECHO**: Uscita impulso di eco
* **GND**: Massa
* **VCC**: Alimentazione 5V

Questo è il sensore di distanza ultrasonico HC-SR04, che fornisce una misurazione senza contatto da 2 cm a 400 cm con un'accuratezza del range fino a 3 mm. Il modulo include un trasmettitore ultrasonico, un ricevitore e un circuito di controllo.

È necessario collegare solo 4 pin: VCC (alimentazione), Trig (attivazione), Echo (ricezione) e GND (massa) per utilizzarlo facilmente nei tuoi progetti di misurazione.

**Caratteristiche**

* Tensione di funzionamento: DC5V
* Corrente di funzionamento: 16mA
* Frequenza di funzionamento: 40Hz
* Range massimo: 500cm
* Range minimo: 2cm
* Segnale di ingresso Trigger: impulso TTL da 10uS
* Segnale di uscita Echo: segnale di livello TTL proporzionale al range
* Connettore: XH2.54-4P
* Dimensioni: 46x20.5x15 mm

**Principio**

I principi di base sono i seguenti:

* Utilizzare il trigger IO per almeno 10us di segnale ad alto livello.

* Il modulo invia una raffica di ultrasuoni a 40 kHz composta da 8 cicli e rileva se viene ricevuto un segnale di ritorno.

* L'Echo emetterà un segnale ad alto livello se viene ricevuto un segnale di ritorno; la durata del segnale ad alto livello è il tempo trascorso dall'emissione al ritorno.

* Distanza = (tempo del segnale ad alto livello x velocità del suono (340M/S)) / 2

|ultrasonic_prin|

Formula:

* us / 58 = distanza in centimetri
* us / 148 = distanza in pollici
* distanza = tempo del segnale ad alto livello x velocità (340M/S) / 2

.. note::

    Questo modulo non deve essere collegato sotto tensione, se necessario, collegare prima il GND del modulo. Altrimenti, influirà sul funzionamento del modulo.

    L'area dell'oggetto da misurare dovrebbe essere di almeno 0,5 metri quadrati e il più piatta possibile. Altrimenti, i risultati potrebbero essere influenzati.


**Esempio**

* :ref:`py_ultrasonic` (For MicroPython User)
* :ref:`py_reversing_aid` (For MicroPython User)
* :ref:`ar_ultrasonic` (For Arduino User)
* :ref:`per_reversing_system` (For Piper Make User)