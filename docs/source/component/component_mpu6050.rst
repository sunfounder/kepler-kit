.. note::

    Ciao, benvenuto nella Community SunFounder per appassionati di Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_mpu6050:

Modulo MPU6050
===========================

**MPU6050**

|img_mpu6050|

L'MPU-6050 è un dispositivo di tracciamento del movimento a 
6 assi (combina giroscopio a 3 assi e accelerometro a 3 assi).

I suoi tre sistemi di coordinate sono definiti come segue:

Posiziona l'MPU6050 su una superficie piana, assicurandoti 
che la faccia con l'etichetta sia rivolta verso l'alto e che 
un punto su questa superficie si trovi nell'angolo in alto a 
sinistra. La direzione verso l'alto è l'asse z del chip. La 
direzione da sinistra a destra è considerata l'asse X. Di conseguenza, 
la direzione da dietro a davanti è definita come l'asse Y.

|img_mpu6050_a| 

**Accelerometro a 3 assi**

L'accelerometro funziona secondo il principio dell'effetto piezoelettrico, 
ossia la capacità di determinati materiali di generare una carica elettrica 
in risposta a uno stress meccanico applicato.

Immagina una scatola cuboidale con una piccola sfera all'interno, come 
nell'immagine sopra. Le pareti di questa scatola sono fatte di cristalli 
piezoelettrici. Ogni volta che inclini la scatola, la sfera è costretta a 
muoversi nella direzione dell'inclinazione, a causa della gravità. La parete 
con cui la sfera collide genera piccole correnti piezoelettriche. Ci sono in 
totale tre coppie di pareti opposte in un cuboide. Ogni coppia corrisponde a 
un asse nello spazio 3D: assi X, Y e Z. A seconda della corrente prodotta 
dalle pareti piezoelettriche, possiamo determinare la direzione 
dell'inclinazione e la sua entità.

|img_mpu6050_a2|

Possiamo utilizzare l'MPU6050 per rilevare la sua accelerazione su ciascun 
asse di coordinate (nello stato stazionario sulla scrivania, l'accelerazione 
sull'asse Z è di 1 unità di gravità, mentre sugli assi X e Y è 0). Se viene 
inclinato o in una condizione di assenza di peso/sovrappeso, la lettura 
corrispondente cambierà.

Esistono quattro tipi di intervalli di misurazione che possono essere 
selezionati a livello di programma: +/-2g, +/-4g, +/-8g e +/-16g 
(2g per impostazione predefinita), corrispondenti a ciascuna precisione. 
I valori vanno da -32768 a 32767.

La lettura dell'accelerometro viene convertita in un valore di accelerazione 
mappando la lettura dall'intervallo di lettura all'intervallo di misurazione.

Accelerazione = (Dati grezzi dell'asse accelerometro / 65536 * Intervallo di 
accelerazione a piena scala) g

Prendiamo l'asse X come esempio: quando i dati grezzi dell'asse accelerometro 
X sono 16384 e l'intervallo è selezionato a +/-2g:

**Accelerazione lungo l'asse X = (16384 / 65536 * 4) g** **=1g**

**Giroscopio a 3 assi**

I giroscopi funzionano secondo il principio dell'accelerazione di Coriolis. 
Immagina una struttura simile a un diapason, in costante movimento avanti e 
indietro. È mantenuta in posizione utilizzando cristalli piezoelettrici. Ogni 
volta che provi a inclinare questa disposizione, i cristalli sperimentano una 
forza nella direzione dell'inclinazione. Questo è causato dall'inerzia del 
diapason in movimento. I cristalli quindi producono una corrente in accordo 
con l'effetto piezoelettrico, e questa corrente viene amplificata.

|img_mpu6050_g|

Il giroscopio ha anche quattro tipi di intervalli di misurazione: +/- 250, 
+/- 500, +/- 1000, +/- 2000. Il metodo di calcolo e l'accelerazione sono 
sostanzialmente coerenti.

La formula per convertire la lettura in velocità angolare è la seguente:

Velocità angolare = (Dati grezzi dell'asse giroscopio / 65536 * Intervallo di 
velocità angolare a piena scala) °/s

Prendiamo l'asse X come esempio: i dati grezzi dell'asse giroscopio X sono 16384 e l'intervallo è + / - 250°/ s:

**Velocità angolare lungo l'asse X = (16384 / 65536 * 500)°/s** **=125°/s**

**Esempio**

* :ref:`py_mpu6050` (For MicroPython User)
* :ref:`py_somato_controller` (For MicroPython User)
* :ref:`py_bubble_level` (For MicroPython User)
* :ref:`ar_mpu6050` (For Arduino User)