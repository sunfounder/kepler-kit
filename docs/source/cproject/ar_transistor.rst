.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a promozioni festive e concorsi a premi.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ar_transistor:

2.15 - Due Tipi di Transistori
==========================================

Questo kit è dotato di due tipi di transistori, S8550 e S8050, il primo è un PNP e il secondo un NPN. Sono molto simili nell'aspetto, quindi è necessario controllare attentamente le etichette per distinguerli.
Quando un segnale di alto livello attraversa un transistor NPN, esso si attiva. Tuttavia, un transistor PNP richiede un segnale di basso livello per funzionare. Entrambi i tipi di transistor sono frequentemente utilizzati per interruttori senza contatto, proprio come in questo esperimento.

|img_NPN&PNP|

Usiamo un LED e un pulsante per capire come utilizzare un transistor!

:ref:`cpn_transistor`

**Componenti Necessari**

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
        - 3 (220Ω, 1KΩ, 10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_button`
        - 1
        - |link_button_buy|
    *   - 8
        - :ref:`cpn_transistor`
        - 1 (S8050/S8550)
        - |link_transistor_buy|

**Collegamento del transistor NPN (S8050)**

|sch_s8050|

In questo circuito, quando il pulsante viene premuto, GP14 va a livello alto.

Programmando GP15 per emettere un livello alto, dopo un resistore di limitazione di corrente da 1k (per proteggere il transistor), il S8050 (transistor NPN) viene attivato, consentendo così al LED di accendersi.

|wiring_s8050|

.. 1. Collega 3V3 e GND del Pico W alla barra di alimentazione della breadboard.
.. #. Collega l'anodo del LED alla barra di alimentazione positiva tramite un resistore da 220Ω.
.. #. Collega il catodo del LED al **collettore** del transistor.
.. #. Collega la base del transistor al pin GP15 tramite un resistore da 1kΩ.
.. #. Collega l'**emettitore** del transistor alla barra di alimentazione negativa.
.. #. Collega un lato del pulsante al pin GP14 e utilizza un resistore da 10kΩ per collegare lo stesso lato alla barra di alimentazione negativa. L'altro lato al bus di alimentazione positivo.

.. .. nota::
..     * L'anello colorato del resistore da 220Ω è rosso, rosso, nero, nero e marrone.
..     * L'anello colorato del resistore da 1kΩ è marrone, nero, nero, marrone e marrone.
..     * L'anello colorato del resistore da 10kΩ è marrone, nero, nero, rosso e marrone.

**Collegamento del transistor PNP (S8550)**

|sch_s8550|

In questo circuito, GP14 è basso per impostazione predefinita e passerà a livello alto quando il pulsante viene premuto.

Programmando GP15 per emettere **basso**, dopo un resistore di limitazione di corrente da 1k (per proteggere il transistor), il S8550 (transistor PNP) viene attivato, consentendo così al LED di accendersi.

L'unica differenza che noterai tra questo circuito e il precedente è che nel circuito precedente il catodo del LED è collegato al **collettore** del **S8050 (transistor NPN)**, mentre in questo è collegato all'**emettitore** del **S8550 (transistor PNP)**.

|wiring_s8550|

.. 1. Collega 3V3 e GND del Pico W alla barra di alimentazione della breadboard.
.. #. Collega l'anodo del LED alla barra di alimentazione positiva tramite un resistore da 220Ω.
.. #. Collega il catodo del LED all'**emettitore** del transistor.
.. #. Collega la base del transistor al pin GP15 tramite un resistore da 1kΩ.
.. #. Collega il **collettore** del transistor alla barra di alimentazione negativa.

**Codice**

.. note::

   * Puoi aprire il file ``2.15_transistor.ino`` nel percorso ``kepler-kit-main/arduino/2.15_transistor``. 
   * Oppure copia questo codice nell'**Arduino IDE**.


    * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.



.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/77c437de-028f-47c1-9d79-177e90eb0599/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Entrambi i tipi di transistori possono essere controllati con lo stesso codice. Quando premiamo il pulsante, Pico W invierà un segnale di alto livello al transistor; quando lo rilasciamo, invierà un segnale di basso livello.
Possiamo osservare che nei due circuiti si verificano fenomeni diametralmente opposti.

* Il circuito che utilizza il S8050 (transistor NPN) si accenderà quando il pulsante viene premuto, il che significa che sta ricevendo un segnale di conduzione di alto livello;
* Il circuito che utilizza il S8550 (transistor PNP) si accenderà quando il pulsante viene rilasciato, il che significa che sta ricevendo un segnale di conduzione di basso livello.
