.. note::

    Ciao, benvenuto nella Community SunFounder per appassionati di Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_mpr121:

Modulo MPR121
===========================

|img_mpr121|

* **3.3V**: Alimentazione
* **IRQ**: Pin di uscita interrupt open collector, attivo basso
* **SCL**: Clock I2C
* **SDA**: Dati I2C
* **ADD**: Pin di selezione indirizzo I2C. Collega il pin ADDR alla linea VSS, VDD, SDA o SCL, gli indirizzi I2C risultanti sono rispettivamente 0x5A, 0x5B, 0x5C e 0x5D.
* **GND**: Terra
* **0~11**: Elettrodo 0~11, l'elettrodo è un sensore touch. Tipicamente, gli elettrodi possono essere semplicemente un pezzo di metallo o un filo. Tuttavia, a seconda della lunghezza del filo o del materiale su cui si trova l'elettrodo, potrebbe risultare difficile attivare il sensore. Per questo motivo, il MPR121 consente di configurare i parametri necessari per attivare e disattivare un elettrodo.

**PANORAMICA DEL MPR121**

Il MPR121 è la seconda generazione di controller per sensori tattili 
capacitivi dopo il rilascio iniziale dei dispositivi della serie MPR03x. 
Il MPR121 offre un'intelligenza interna aumentata, con alcune delle 
principali aggiunte che includono un aumento del numero di elettrodi, un 
indirizzo I2C configurabile tramite hardware, un sistema di filtraggio 
ampliato con debounce e elettrodi completamente indipendenti con 
auto-configurazione integrata. Il dispositivo presenta anche un tredicesimo 
canale di rilevamento simulato dedicato al rilevamento di prossimità 
utilizzando gli ingressi di rilevamento multiplexer.

* `MPR121 Datasheet <https://cdn-shop.adafruit.com/datasheets/MPR121.pdf>`_

**Caratteristiche**

* Operatività a basso consumo
    • Alimentazione da 1,71 V a 3,6 V
    • Corrente di alimentazione di 29 μA a un intervallo di campionamento di 16 ms
    • Corrente in modalità Stop di 3 μA
* 12 ingressi di rilevamento della capacità
    • 8 ingressi multifunzione per driver LED e GPIO
* Rilevamento completo del tocco
    • Configurazione automatica per ciascun ingresso di rilevamento
    • Auto-calibrazione per ciascun ingresso di rilevamento
    • Soglia di tocco/rilascio e debounce per il rilevamento del tocco
* Interfaccia I2C, con uscita Interrupt
* Confezione QFN a 20 pin 3 mm x 3 mm x 0,65 mm
* Intervallo di temperatura operativa da -40°C a +85°C

**Esempio**

* :ref:`py_mpr121` (For MicroPython User)
* :ref:`py_fruit_piano` (For MicroPython User)
* :ref:`ar_mpr121` (For Arduino User)