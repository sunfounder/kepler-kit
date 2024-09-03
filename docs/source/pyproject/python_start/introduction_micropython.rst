.. note::

    Ciao, benvenuto nella Community di Appassionati di Raspberry Pi & Arduino & ESP32 di SunFounder su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa ai giveaway e alle promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

1.1 Introduzione a MicroPython
======================================

MicroPython è un'implementazione software di un linguaggio di programmazione ampiamente compatibile con Python 3, scritto in C e ottimizzato per funzionare su un microcontrollore.

MicroPython è composto da un compilatore Python in bytecode e da un interprete runtime di quel bytecode. L'utente dispone di un prompt interattivo (REPL) per eseguire immediatamente i comandi supportati. Sono inclusi una selezione di librerie Python di base; MicroPython include moduli che offrono al programmatore accesso all'hardware di basso livello.

* Riferimento: `MicroPython - Wikipedia <https://en.wikipedia.org/wiki/MicroPython>`_

La Storia Inizia Qui
--------------------------------

Le cose cambiarono nel 2013 quando Damien George lanciò una campagna di crowdfunding (Kickstarter).

Damien era uno studente universitario a Cambridge e un appassionato programmatore di robotica. Voleva ridurre il mondo di Python da una macchina da gigabyte a una da kilobyte. La sua campagna Kickstarter era volta a sostenere il suo sviluppo mentre trasformava il suo proof of concept in un'implementazione completa.

MicroPython è supportato da una comunità diversificata di Pythonisti, fortemente interessata al successo del progetto.

Oltre a testare e supportare la base di codice, gli sviluppatori hanno fornito tutorial, librerie di codice e porting hardware, permettendo a Damien di concentrarsi su altri aspetti del progetto.

* Riferimento: `realpython <https://realpython.com/micropython/>`_

Perché MicroPython？
-----------------------

Sebbene la campagna Kickstarter originale abbia rilasciato MicroPython come una scheda di sviluppo "pyboard" con STM32F4, MicroPython supporta molte architetture di prodotti basati su ARM. I port principali supportati sono ARM Cortex-M (molte schede STM32, TI CC3200/WiPy, schede Teensy, serie Nordic nRF, SAMD21 e SAMD51), ESP8266, ESP32, PIC a 16 bit, Unix, Windows, Zephyr e JavaScript.

In secondo luogo, MicroPython consente un feedback rapido. Questo perché puoi usare REPL per inserire comandi in modo interattivo e ottenere risposte immediate. Puoi persino modificare il codice e eseguirlo subito invece di attraversare il ciclo codice-compilazione-caricamento-esecuzione.

Anche Python ha gli stessi vantaggi, ma per alcune schede Microcontroller come il Raspberry Pi Pico, sono piccole, semplici e hanno poca memoria per eseguire il linguaggio Python in generale. Ecco perché MicroPython si è evoluto, mantenendo le principali caratteristiche di Python e aggiungendone di nuove per funzionare con queste schede Microcontroller.

Successivamente imparerai a installare MicroPython sul Raspberry Pi Pico.

* Riferimento: `MicroPython - Wikipedia <https://en.wikipedia.org/wiki/MicroPython>`_
* Riferimento: `realpython <https://realpython.com/micropython/>`_
