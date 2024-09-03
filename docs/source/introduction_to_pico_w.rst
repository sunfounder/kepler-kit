.. note::

    Ciao, benvenuto nella Community SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e alle anteprime.
    - **Sconti Speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_pico_w:

Raspberry Pi Pico W
=======================================

|pico_w_side|

Raspberry Pi Pico W porta la connettività wireless nella linea di prodotti 
Raspberry Pi Pico, il best-seller della gamma. Basato sulla nostra piattaforma 
di silicio RP2040, i prodotti Pico offrono i nostri valori distintivi di alte 
prestazioni, basso costo e facilità d'uso nel campo dei microcontrollori.

Raspberry Pi Pico W offre supporto per LAN wireless 802.11 b/g/n a 2.4GHz, 
con un'antenna integrata e certificazione di conformità modulare. È in grado 
di operare sia in modalità stazione che punto di accesso. L'accesso completo 
alla funzionalità di rete è disponibile sia per sviluppatori C che MicroPython.
Raspberry Pi Pico W abbina il chip RP2040 con 2MB di memoria flash, e un chip 
di alimentazione che supporta tensioni di ingresso da 1.8 a 5.5V. Fornisce 26 
pin GPIO, tre dei quali possono funzionare come ingressi analogici, su pad 
passanti con bordo castellato a passo 0,1”.
Raspberry Pi Pico W è disponibile come unità singola o in bobine da 480 unità 
per l'assemblaggio automatizzato.

Caratteristiche
------------------

* Fattore di forma da 21 mm x 51 mm
* Microcontrollore RP2040 progettato da Raspberry Pi nel Regno Unito
* Processore dual-core Arm Cortex-M0+, clock flessibile fino a 133 MHz
* 264kB di SRAM on-chip
* 2MB di flash QSPI on-board
* LAN wireless 802.11n a 2.4GHz
* 26 pin GPIO multifunzione, inclusi 3 ingressi analogici
* 2 x UART, 2 x controller SPI, 2 x controller I2C, 16 x canali PWM
* 1 x controller USB 1.1 e PHY, con supporto per host e dispositivo
* 8 x macchine a stati PIO programmabili per supporto periferico personalizzato
* Alimentazione in ingresso supportata 1.8-5.5V DC
* Temperatura operativa -20°C a +70°C
* Modulo castellato che consente la saldatura diretta su schede carrier
* Programmazione drag-and-drop utilizzando l'archiviazione di massa via USB
* Modalità di sospensione e inattività a basso consumo
* Orologio on-chip preciso
* Sensore di temperatura
* Librerie on-chip accelerate per interi e floating-point

Pin di Pico
---------------

|pico_pin|

.. list-table::
    :widths: 3 5 10
    :header-rows: 1

    *   - Nome
        - Descrizione
        - Funzione
    *   - GP0-GP28
        - Pin di ingresso/uscita generali
        - Funzionano come ingressi o uscite e non hanno uno scopo fisso.
    *   - GND
        - Massa a 0 volt
        - Vari pin GND intorno a Pico W per facilitare il cablaggio.
    *   - RUN
        - Abilita o disabilita il tuo Pico
        - Avvia e ferma il tuo Pico W da un altro microcontrollore.
    *   - GPxx_ADCx
        - Ingresso/uscita generali o ingresso analogico
        - Utilizzato come ingresso analogico oltre che come ingresso o uscita digitale, ma non entrambi contemporaneamente.
    *   - ADC_VREF
        - Riferimento di tensione per il convertitore analogico-digitale (ADC)
        - Un pin di ingresso speciale che imposta una tensione di riferimento per qualsiasi ingresso analogico.
    *   - AGND
        - Massa a 0 volt per il convertitore analogico-digitale (ADC)
        - Un collegamento di massa speciale per l'uso con il pin ADC_VREF.
    *   - 3V3(O)
        - Alimentazione a 3.3 volt
        - Una fonte di alimentazione a 3.3V, la stessa tensione a cui funziona internamente il tuo Pico W, generata dall'ingresso VSYS.
    *   - 3v3(E)
        - Abilita o disabilita l'alimentazione
        - Accende o spegne l'alimentazione 3V3(O), può anche spegnere il tuo Pico W.
    *   - VSYS
        - Alimentazione a 2-5 volt
        - Un pin direttamente collegato all'alimentazione interna del tuo Pico, che non può essere spento senza spegnere anche Pico W.
    *   - VBUS
        - Alimentazione a 5 volt
        - Una fonte di alimentazione a 5V presa dalla porta micro USB del tuo Pico, e utilizzata per alimentare l'hardware che richiede più di 3.3V.

Il posto migliore per trovare tutto ciò di cui hai bisogno per iniziare con il tuo Raspberry Pi Pico W è `qui <https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html>`_

Oppure puoi cliccare sui link seguenti:

* `Raspberry Pi Pico W product brief <https://datasheets.raspberrypi.com/picow/pico-w-product-brief.pdf>`_
* `Raspberry Pi Pico W datasheet <https://datasheets.raspberrypi.com/picow/pico-w-datasheet.pdf>`_
* `Getting started with Raspberry Pi Pico: C/C++ development <https://datasheets.raspberrypi.org/pico/getting-started-with-pico.pdf>`_
* `Raspberry Pi Pico C/C++ SDK <https://datasheets.raspberrypi.org/pico/raspberry-pi-pico-c-sdk.pdf>`_
* `API-level Doxygen documentation for the Raspberry Pi Pico C/C++ SDK <https://raspberrypi.github.io/pico-sdk-doxygen/>`_
* `Raspberry Pi Pico Python SDK <https://datasheets.raspberrypi.org/pico/raspberry-pi-pico-python-sdk.pdf>`_
* `Raspberry Pi RP2040 datasheet <https://datasheets.raspberrypi.org/rp2040/rp2040-datasheet.pdf>`_
* `Hardware design with RP2040 <https://datasheets.raspberrypi.org/rp2040/hardware-design-with-rp2040.pdf>`_
* `Raspberry Pi Pico W design files <https://datasheets.raspberrypi.com/picow/RPi-PicoW-PUBLIC-20220607.zip>`_
* `Raspberry Pi Pico W STEP file <https://datasheets.raspberrypi.com/picow/PicoW-step.zip>`_
