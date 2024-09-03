.. note::

    Ciao, benvenuto nella community di appassionati di SunFounder Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a promozioni festive e giveaway.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ar_reed:

2.9 - Senti il Magnetismo
===============================

Il tipo più comune di interruttore reed contiene una coppia di lamelle metalliche magnetizzabili, flessibili, le cui estremità sono separate da un piccolo spazio quando l'interruttore è aperto.

Un campo magnetico proveniente da un elettromagnete o da un magnete permanente farà sì che le lamelle si attraggano, completando così un circuito elettrico.
La forza elastica delle lamelle le farà separare, aprendo il circuito, quando il campo magnetico cessa.

Un esempio comune di applicazione di un interruttore reed è rilevare l'apertura di una porta o finestra per un allarme di sicurezza.

* :ref:`cpn_reed`

**Componenti necessari**

In questo progetto, abbiamo bisogno dei seguenti componenti.

È sicuramente conveniente acquistare un kit completo, ecco il link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nome	
        - ELEMENTI IN QUESTO KIT
        - LINK PER L'ACQUISTO
    *   - Kepler Kit	
        - 450+
        - |link_kepler_kit|


Puoi anche acquistarli separatamente dai link qui sotto.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - INTRODUZIONE COMPONENTE	
        - QUANTITÀ
        - LINK PER L'ACQUISTO

    *   - 1
        - :ref:`cpn_pico_w`
        - 1
        - |link_picow_buy|
    *   - 2
        - Cavo Micro USB
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Diversi
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_resistor`
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_reed`
        - 1
        - 

**Schema elettrico**

|sch_reed|

Di default, GP14 è basso e diventerà alto quando il magnete si avvicina all'interruttore reed.

Lo scopo della resistenza da 10KΩ è di mantenere il GP14 a un livello basso stabile quando non ci sono magneti nelle vicinanze.

**Cablaggio**

|wiring_reed|

**Codice**

.. note::

   * Puoi aprire il file ``2.9_feel_the_magnetism.ino`` nel percorso ``kepler-kit-main/arduino/2.9_feel_the_magnetism``. 
   * Oppure copia questo codice nell'**Arduino IDE**.
   * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/62bba18c-7921-4df9-806f-deffce17de9a/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Quando un magnete si avvicina, il circuito si chiuderà. Proprio come il pulsante nel capitolo :ref:`ar_button`.


.. **Learn More**

.. This time, we tried a flexible way of using switches: interrupt requests, or IRQs.:  interrupt requests, or IRQs.

.. For example, you are reading a book page by page, as if a program is executing a thread. At this time, someone came to you to ask a question and interrupted your reading. Then the person is executing the interrupt request: asking you to stop what you are doing, answer his questions, and then let you return to reading the book after the end.

.. The interrupt request also works in the same way, it allows certain operations to interrupt the main program. 

.. .. :raw-code:

.. .. note::

..    * You can open the file ``2.9_feel_the_magnetism_irq.ino`` under the path of ``kepler-kit-main/arduino/2.9_feel_the_magnetism_irq``. 
..    * Or copy this code into **Arduino IDE**.

.. 
..     * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.




.. A callback function ``detected()`` is defined here, called the interrupt handler. It will be executed when an interrupt request is triggered.
.. Then, an interrupt request is set up in ``setup``, which contains two parts: ``mode`` and ``ISR``.

.. In this program, ``mode`` is ``RISING``, which indicates that the value of the pin is raised from low to high (i.e, button pressed).

.. ``ISR`` is ``detected`` , the callback function we defined.

.. * `attachInterrupt() - Arduino Reference <https://www.arduino.cc/reference/en/language/functions/external-interrupts/attachinterrupt/>`_