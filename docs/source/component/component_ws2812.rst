.. note::

    Ciao, benvenuto nella Community SunFounder per appassionati di Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_ws2812:

Striscia LED RGB WS2812 con 8 LED
=========================================

|img_ws2812|

La striscia LED RGB WS2812 è composta da 8 LED RGB. È sufficiente un 
solo pin per controllare tutti i LED. Ogni LED RGB ha un chip WS2812, 
che può essere controllato in modo indipendente. Può realizzare una 
visualizzazione della luminosità a 256 livelli e una visualizzazione a 
colori reali completa con 16.777.216 colori. Allo stesso tempo, il 
pixel contiene un circuito amplificatore di pilotaggio del segnale 
di aggancio dati digitale intelligente, e un circuito di formattazione 
del segnale è integrato per garantire l'uniformità della luminosità del 
colore del punto pixel.

È flessibile, può essere collegata, piegata e tagliata a piacere, e il 
retro è dotato di nastro adesivo, che può essere fissato su superfici 
irregolari e installato in spazi ristretti.

**Caratteristiche**

* Tensione di lavoro: DC5V
* IC: Un IC pilota un LED RGB
* Consumo: 0,3W per LED
* Temperatura di lavoro: -15-50°C
* Colore: RGB a colori pieni
* Tipo di RGB: 5050RGB (con IC WS2812B integrato)
* Spessore della striscia LED: 2mm
* Ogni LED può essere controllato individualmente

**Introduzione al WS2812B**

* `WS2812B Datasheet <https://cdn-shop.adafruit.com/datasheets/WS2812B.pdf>`_

WS2812B è una sorgente luminosa a LED a controllo intelligente in cui il 
circuito di controllo e il chip RGB sono integrati in un pacchetto di 
componenti 5050. Include internamente un circuito di amplificazione di 
ripristino del segnale digitale e una parte di controllo della corrente 
costante programmabile a 12V, garantendo efficacemente l'uniformità del 
colore dei punti pixel.

Il protocollo di trasferimento dati utilizza la modalità di comunicazione 
NZR singola. Dopo il reset all'accensione del pixel, la porta DIN riceve 
dati dal controller, il primo pixel raccoglie i primi 24 bit di dati e li 
invia al blocco dati interno, mentre gli altri dati vengono formattati dal 
circuito di amplificazione del segnale e inviati al pixel successivo tramite 
la porta DO. Dopo la trasmissione di ogni pixel, il segnale viene ridotto di 
24 bit. La tecnologia di trasmissione del pixel con autoformattazione rende 
il numero di pixel in cascata illimitato nella trasmissione del segnale, 
dipendendo solo dalla velocità di trasmissione del segnale.

LED con bassa tensione di pilotaggio, protezione ambientale e risparmio 
energetico, alta luminosità, ampio angolo di dispersione, buona uniformità, 
basso consumo energetico, lunga durata e altri vantaggi. Il chip di controllo 
integrato nel LED semplifica ulteriormente il circuito, rendendo l'installazione 
più semplice e compatta.

.. Esempio
.. -------------------

.. :ref:`Striscia LED RGB`


**Esempio**

* :ref:`py_neopixel` (For MicroPython User)
* :ref:`py_music_player` (For MicroPython User)
* :ref:`ar_neopixel` (For Arduino User)
* :ref:`per_flowing_leds` (For Piper Make User)