.. note::

    Ciao, benvenuto nella Community SunFounder per appassionati di Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_dht11:

Sensore di Umidità e Temperatura DHT11
=============================================

Il sensore digitale di temperatura e umidità DHT11 è un sensore composito che contiene un'uscita digitale calibrata per temperatura e umidità.
La tecnologia dei moduli digitali dedicati e la tecnologia di rilevamento della temperatura e dell'umidità sono applicate per garantire che il prodotto abbia un'elevata affidabilità e un'eccellente stabilità a lungo termine.

Il sensore include un componente resistivo per il rilevamento dell'umidità e un dispositivo di misurazione della temperatura NTC, ed è collegato a un microcontrollore ad alte prestazioni a 8 bit.

.. Lo schema elettrico del modulo sensore di umidità e temperatura è mostrato di seguito: |img_Hum-sch|

Sono disponibili solo tre pin per l'uso: VCC, GND e DATA.
Il processo di comunicazione inizia con la linea DATA che invia segnali di avvio al DHT11, e il DHT11 riceve i segnali e restituisce un segnale di risposta.
Quindi l'host riceve il segnale di risposta e inizia a ricevere 40 bit di dati relativi a umidità e temperatura (8 bit per l'umidità intera + 8 bit per l'umidità decimale + 8 bit per la temperatura intera + 8 bit per la temperatura decimale + 8 bit di checksum).

|img_Dht11|

**Caratteristiche**

    #. Gamma di misurazione dell'umidità: 20 - 90%RH
    #. Gamma di misurazione della temperatura: 0 - 60℃
    #. Uscita di segnali digitali indicanti temperatura e umidità
    #. Tensione di funzionamento: DC 5V; Dimensioni PCB: 2,0 x 2,0 cm
    #. Precisione di misurazione dell'umidità: ±5%RH
    #. Precisione di misurazione della temperatura: ±2℃


* `DHT11 Datasheet <http://wiki.sunfounder.cc/images/c/c7/DHT11_datasheet.pdf>`_

**Esempio**


* :ref:`py_dht11` (Per utenti MicroPython)
* :ref:`ar_dht11` (Per utenti Arduino)
