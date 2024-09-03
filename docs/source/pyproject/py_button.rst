.. note::

    Ciao, benvenuto nella Community di Appassionati di Raspberry Pi & Arduino & ESP32 di SunFounder su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa ai giveaway e alle promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_button:

2.5 Lettura del Valore del Pulsante
==============================================

Questi pin hanno sia funzioni di input che di output, come indicato dal loro nome GPIO (General-purpose input/output). In precedenza, abbiamo utilizzato la funzione di output; in questo capitolo, utilizzeremo la funzione di input per leggere il valore del pulsante.

* :ref:`cpn_button`

**Componenti Necessari**

In questo progetto, abbiamo bisogno dei seguenti componenti.

È sicuramente conveniente acquistare un kit completo, ecco il link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nome
        - ELEMENTI IN QUESTO KIT
        - LINK
    *   - Kepler Kit
        - 450+
        - |link_kepler_kit|

Puoi anche acquistarli separatamente dai link sottostanti.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - COMPONENTE
        - QUANTITÀ
        - LINK

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
        - :ref:`cpn_button`
        - 1
        - |link_button_buy|

**Schema**

|sch_button|

Finché un lato del pin del pulsante è collegato a 3.3V e l'altro lato è collegato a GP14, quando il pulsante viene premuto, GP14 sarà alto. Tuttavia, quando il pulsante non è premuto, GP14 è in uno stato sospeso e può essere alto o basso. Per ottenere un livello basso stabile quando il pulsante non è premuto, GP14 deve essere ricollegato a GND attraverso una resistenza pull-down da 10K.

**Cablaggio**

|wiring_button|

.. Seguiamo la direzione del circuito per costruirlo!

.. 1. Collega il pin 3V3 di Pico W alla barra di alimentazione positiva della breadboard.
.. #. Inserisci il pulsante nella breadboard in modo che attraversi la linea di separazione centrale.

.. note::
    Un pulsante a quattro pin ha la forma di una "H". I suoi due pin di sinistra o i due di destra sono collegati, il che significa che, quando attraversa il gap centrale, collega due metà di file con lo stesso numero di fila. (Ad esempio, nel mio circuito, E23 e F23 sono già collegati, così come E25 e F25).

    Finché il pulsante non viene premuto, i pin di sinistra e di destra sono indipendenti l'uno dall'altro e la corrente non può fluire da un lato all'altro.

.. #. Usa un filo jumper per collegare uno dei pin del pulsante alla barra positiva (il mio è il pin in alto a destra).
.. #. Collega l'altro pin (in alto a sinistra o in basso a sinistra) a GP14 con un filo jumper.
.. #. Usa una resistenza da 10K per collegare il pin nell'angolo in alto a sinistra del pulsante alla barra negativa.
.. #. Collega la barra di alimentazione negativa della breadboard a GND di Pico.

**Codice**

.. note::

    * Apri il file ``2.5_read_button_value.py`` nel percorso ``kepler-kit-main/micropython`` oppure copia questo codice in Thonny, quindi clicca su "Run Current Script" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra.

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime
    button = machine.Pin(14, machine.Pin.IN)
    while True:
        if button.value() == 1:
            print("You pressed the button!")
            utime.sleep(1)

Non appena il codice viene eseguito, la shell stampa "Hai premuto il pulsante!"

**Modalità di Lavoro Pull-up**

La parte successiva mostra il cablaggio e il codice quando si utilizza il pulsante in modalità pull-up.

|sch_button_pullup|

|wiring_button_pullup|

L'unica differenza che vedrai rispetto alla modalità pull-down è che la resistenza da 10K è collegata a 3.3V e il pulsante è collegato a GND, in modo che quando il pulsante viene premuto, GP14 ottiene un livello basso, il che è l'opposto del valore ottenuto in modalità pull-down.
Quindi basta modificare questo codice in ``if button.value() == 0:``.

Consulta anche il riferimento qui:  

* `machine.Pin <https://docs.micropython.org/en/latest/library/machine.Pin.html>`_