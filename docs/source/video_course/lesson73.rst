.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

lesson 73 :  Controllare un LED RGB Utilizzando un Dizionario in MicroPython
===================================================================================

Questo tutorial copre il controllo di un LED RGB con il Raspberry Pi Pico W utilizzando i dizionari:

* **Configurazione dei Collegamenti**:
- Collega il LED RGB al Raspberry Pi Pico W:
  - Gamba R al pin GPIO 14 tramite una resistenza da 330 Ohm.
  - Gamba G al pin GPIO 13.
  - Gamba B al pin GPIO 12 tramite una resistenza da 330 Ohm.
  - Gamba di massa al binario di massa.
* **Implementazione del Codice**:
- **Creare un Dizionario**:
   - Definisci un dizionario con i nomi dei colori come chiavi e i rispettivi valori RGB come liste.
- **Importare le Librerie**:
   - Importa le librerie necessarie (`machine`, `time`).
   - Configura il PWM per i pin del LED RGB.
- **Ciclo Principale del Programma**:
   - Richiedi continuamente all'utente di inserire un colore desiderato.
   - Converti l'input in minuscolo e verifica se è un colore valido.
   - Se valido, regola i colori del LED utilizzando i cicli di duty del PWM basati sui valori del dizionario.
   - Implementa la gestione degli errori per input non validi.
- **Funzione per Impostare il Colore**:
   - Definisci una funzione `make_color` che prende il colore desiderato e imposta il LED RGB di conseguenza utilizzando il PWM.
   
* **Compito**:
   - Estendi il programma spostando la funzione `make_color` in una libreria e importandola nel programma principale.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/1CHcjlaBvGY?si=feXCiEMKRkdsLx4y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
