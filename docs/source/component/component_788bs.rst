.. note::

    Ciao, benvenuto nella Community di SunFounder per appassionati di Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_dot_matrix:

Matrice a LED
==========================

|img_led_matrix|

In generale, le matrici a LED possono essere suddivise in due tipologie: 
catodo comune (CC) e anodo comune (CA). Esternamente sembrano simili, ma 
internamente presentano differenze. Puoi distinguere il tipo facendo un 
test. In questo kit viene utilizzata una matrice CA, come indicato 
dall'etichetta 788BS sul lato.

Guarda la figura qui sotto. I pin sono disposti alle due estremità sul retro. 
Prendi il lato con l'etichetta come riferimento: i pin su questo lato sono i 
pin 1-8, mentre dall'altra parte troviamo i pin 9-16.

Vista esterna:

|img_788bs_i|

Le figure qui sotto mostrano la struttura interna. Nella matrice a LED CA, 
le file (ROW) rappresentano l'anodo del LED, mentre le colonne (COL) sono il 
catodo; il contrario avviene per una matrice CC. Una cosa in comune: per 
entrambi i tipi, i pin 13, 3, 4, 10, 6, 11, 15, e 16 sono tutti collegati ai 
COL, mentre i pin 9, 14, 8, 12, 1, 7, 2, e 5 sono collegati alle ROW. Se vuoi 
accendere il primo LED in alto a sinistra, per una matrice CA, imposta il pin 
9 su High e il pin 13 su Low; per una matrice CC, imposta il pin 13 su High e 
il pin 9 su Low. Se vuoi accendere l'intera prima colonna, per una matrice CA, 
imposta il pin 13 su Low e le ROW 9, 14, 8, 12, 1, 7, 2, e 5 su High; per una 
matrice CC, imposta il pin 13 su High e le ROW 9, 14, 8, 12, 1, 7, 2, e 5 su 
Low. Consulta le figure seguenti per una migliore comprensione.

Vista interna:

|img_788bs_sche|

Numerazione dei pin corrispondente alle righe e colonne sopra indicate:

=========== ====== ====== ===== ====== ===== ====== ====== ======
**COL**     **1**  **2**  **3** **4**  **5** **6**  **7**  **8**
**Pin No.** **13** **3**  **4** **10** **6** **11** **15** **16**
**ROW**     **1**  **2**  **3** **4**  **5** **6**  **7**  **8**
**Pin No.** **9**  **14** **8** **12** **1** **7**  **2**  **5**
=========== ====== ====== ===== ====== ===== ====== ====== ======

Inoltre, vengono utilizzati due chip 74HC595. Uno per controllare le righe 
della matrice a LED, l'altro per controllare le colonne.


**Esempio**

* :ref:`py_74hc_788bs` (For MicroPython User)
* :ref:`py_bubble_level` (For MicroPython User)
* :ref:`ar_74hc_788bs` (For Arduino User)