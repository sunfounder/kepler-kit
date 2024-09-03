.. note::

    Ciao, benvenuto nella Community SunFounder per appassionati di Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_i2c_lcd:

LCD1602 I2C
==============

|i2c_lcd1602|

* **GND**: Massa
* **VCC**: Alimentazione, 5V.
* **SDA**: Linea dati seriale. Collegare a VCC tramite una resistenza di pullup.
* **SCL**: Linea di clock seriale. Collegare a VCC tramite una resistenza di pullup.

Come sappiamo, sebbene gli schermi LCD e altri display arricchiscano notevolmente l'interazione uomo-macchina, condividono una debolezza comune. Quando sono collegati a un controller, occupano più IO del controller che potrebbe non avere tante porte disponibili. Questo limita anche altre funzioni del controller.

Pertanto, l'LCD1602 con un modulo I2C è stato sviluppato per risolvere il problema. Il modulo I2C ha un chip I2C PCF8574 integrato che converte i dati seriali I2C in dati paralleli per il display LCD.

* `PCF8574 Datasheet <https://www.ti.com/lit/ds/symlink/pcf8574.pdf?ts=1627006546204&ref_url=https%253A%252F%252Fwww.google.com%252F>`_

**Indirizzo I2C**

L'indirizzo predefinito è fondamentalmente 0x27, in alcuni casi può essere 0x3F.

Prendendo come esempio l'indirizzo predefinito 0x27, l'indirizzo del dispositivo può essere modificato cortocircuitando i pad A0/A1/A2; nello stato predefinito, A0/A1/A2 è 1, e se il pad è cortocircuitato, A0/A1/A2 è 0.

|i2c_address|

**Retroilluminazione/Contrasto**

La retroilluminazione può essere attivata tramite il ponticello, rimuovere il ponticello per disattivare la retroilluminazione. Il potenziometro blu sul retro viene utilizzato per regolare il contrasto (il rapporto di luminosità tra il bianco più luminoso e il nero più scuro).

|back_lcd1602|

* **Ponticello**: La retroilluminazione può essere attivata tramite questo ponticello, rimuoverlo per disattivare la retroilluminazione.
* **Potenziometro**: Viene utilizzato per regolare il contrasto (la chiarezza del testo visualizzato), che aumenta in senso orario e diminuisce in senso antiorario.

**Esempio**

* :ref:`py_lcd` (For MicroPython User)
* :ref:`py_room_temp` (For MicroPython User)
* :ref:`py_guess_number` (For MicroPython User)
* :ref:`ar_lcd` (For Arduino User)