.. note::

    Ciao, benvenuto nella Community SunFounder per appassionati di Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_pump:

Pompa dell'acqua DC
===========================

|img_pump|

Questa pompa funziona essenzialmente come un motore DC, operando a una tensione di 3V e una corrente di 100mA. Quando è alimentata, la pompa aspira l'acqua dal fondo della sua custodia in plastica e la espelle attraverso il tubo di uscita. Deve sempre essere immersa nell'acqua per funzionare correttamente. Invertire la polarità non la trasformerà in un dispositivo di aspirazione dell'acqua; continuerà solo a pompare l'acqua verso l'esterno!

È particolarmente adatta per principianti che vogliono realizzare un progetto di fontana o irrigazione delle piante utilizzando questa pompa sommergibile, poiché è estremamente facile da usare!


**Caratteristiche**

* **Tensione di funzionamento**: DC 3 ~ 4.5V
* **Corrente operativa**: 120 ~ 180mA
* **Potenza**: 0.36 ~ 0.91W
* **Altezza massima dell'acqua**: 0.35 ~ 0.55M
* **Portata massima**: 80 ~ 100 L/H
* **Vita operativa continua**: 100 ore
* **Grado di impermeabilità**: IP68
* **Modalità di guida**: DC, guida magnetica
* **Materiale**: Plastica ingegneristica
* **Diametro esterno dell'uscita**: 7.8 mm
* **Diametro interno dell'uscita**: 6.5 mm
* È una pompa sommergibile e deve essere usata in questo modo. Tende a surriscaldarsi troppo e c'è il rischio di surriscaldamento se viene accesa non sommersa.
* Viene fornita con un cavo maschio da 25 cm, che consente un facile inserimento in una breadboard.


**Esempio**

* :ref:`py_pump` (For MicroPython User)
* :ref:`ar_pump` (For Arduino User)