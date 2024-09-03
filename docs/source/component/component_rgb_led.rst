.. note::

    Ciao, benvenuto nella Community SunFounder per appassionati di Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_rgb:

LED RGB
=================

|img_rgb|
    
I LED RGB emettono luce in vari colori. Un LED RGB racchiude tre LED, rispettivamente rosso, verde e blu, in un guscio di plastica trasparente o semitrasparente. Può visualizzare vari colori modificando la tensione di ingresso dei tre pin e sovrapponendoli, il che, secondo le statistiche, può creare 16.777.216 colori diversi.

|img_rgb_light|

I LED RGB possono essere suddivisi in anodo comune e catodo comune. In questo kit viene utilizzato il secondo tipo. Il **catodo comune**, o CC, significa che i catodi dei tre LED sono collegati insieme. Dopo averlo collegato a GND e inserito i tre pin, il LED emetterà il colore corrispondente.

Il simbolo del circuito è mostrato nella figura.

|img_rgb_symbol| 

Un LED RGB ha 4 pin: il pin più lungo è il catodo comune, che di solito è collegato a GND; il pin alla sinistra del pin più lungo è quello rosso, e i 2 pin a destra sono rispettivamente verde e blu.

|img_rgb_pin|


**Caratteristiche**

* Colore: Tri-Color (Rosso/Verde/Blu)
* Catodo Comune
* Lente Rotonda Chiara da 5mm
* Tensione Diretta: Rosso: DC 2.0 - 2.2V; Blu e Verde: DC 3.0 - 3.2V (IF=20mA)
* 0.06 Watt DIP RGB LED
* Luminanza Fino a +20% Più Brillante
* Angolo di Visione: 30°


.. Esempio
.. -------------------

.. :ref:`Luce Colorata`


**Esempio**

* :ref:`py_rgb` (For MicroPython User)
* :ref:`py_fruit_piano` (For MicroPython User)
* :ref:`ar_rgb` (For Arduino User)
* :ref:`per_rainbow_light` (For Piper Make User)