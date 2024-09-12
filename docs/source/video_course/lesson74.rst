.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

lesson 74:  Creare una Classe MicroPython per Controllare un LED RGB
===================================================================================

Questo tutorial spiega come creare una libreria MicroPython per controllare un LED RGB con il Raspberry Pi Pico W:

* **Configurazione dei Collegamenti**:
  - Collega il LED RGB al Raspberry Pi Pico W:
  - Gamba R al pin GPIO 14 tramite una resistenza da 330 Ohm.
  - Gamba G al pin GPIO 13.
  - Gamba B al pin GPIO 12 tramite una resistenza da 330 Ohm.
  - Gamba di massa al binario di massa.

* **Implementazione del Codice**:
  - **Creare una Libreria**: Definisci una classe `RGB_LED` in una libreria MicroPython per gestire il LED RGB. Includi un dizionario per i valori dei colori all'interno della classe. Crea metodi per inizializzare i pin del LED e impostare i colori utilizzando il PWM.
  - **Importare le Librerie**: Importa le librerie necessarie (`machine`, `time`). Configura il PWM per i pin del LED RGB all'interno dei metodi della classe.
  - **Programma Principale**: Importa la libreria personalizzata e crea un oggetto per il LED RGB. Utilizza un ciclo while per richiedere continuamente all'utente di inserire un colore desiderato. Valida l'input e imposta il colore del LED di conseguenza. Implementa la gestione degli errori per input non validi e la funzionalità di uscita pulita utilizzando un'interruzione da tastiera.
  - **Compito**: Estendi il programma aggiungendo più funzionalità alla libreria MicroPython, come impostazioni di colore aggiuntive o modelli, e assicurati che il programma principale rimanga semplice e facile da leggere utilizzando efficacemente la libreria.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/tw-mXURNEUc?si=Ja75F1-I6MYwJgEh" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
