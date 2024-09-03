.. note::

    Ciao, benvenuto nella Community SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e alle anteprime.
    - **Sconti Speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

Circuito Elettronico
=========================

Ci sono molte cose che utilizzi ogni giorno alimentate dall'elettricità, come le luci di casa tua e il computer su cui stai leggendo questo testo.

Per utilizzare l'elettricità, devi creare un circuito elettrico. Un circuito elettrico è composto da fili metallici e componenti elettrici ed elettronici.

I circuiti necessitano di una fonte di alimentazione. Nella tua casa, la maggior parte degli apparecchi (ad esempio, TV, luci) è alimentata da prese a muro. Ma molti circuiti più piccoli e portatili (ad esempio, giocattoli elettronici, telefoni cellulari) sono alimentati da batterie. Una batteria ha due terminali, uno dei quali è chiamato terminale positivo ed è contrassegnato con un segno più (+). I terminali negativi sono simbolizzati da segni meno (-), ma di solito non sono stampati sulle batterie.

Per far fluire la corrente, un percorso conduttivo deve collegare il terminale positivo della batteria al terminale negativo, il che viene definito circuito chiuso (se è disconnesso, si chiama circuito aperto). La corrente elettrica scorrerà attraverso apparecchi come le lampade per farli funzionare (ad esempio, accendersi).

|bc1|

Un Pico W ha alcuni pin di uscita per l'alimentazione (positivi) e alcuni pin di massa (negativi). 
Puoi usare questi pin come i lati positivo e negativo dell'alimentazione collegando il Pico W a una fonte di energia.

|bc2|

Con l'elettricità, puoi creare opere con luce, suono e movimento.
Puoi accendere un LED collegando il pin lungo al terminale positivo e il pin corto al terminale negativo.
Il LED si romperà molto rapidamente se lo fai, quindi devi aggiungere una resistenza da 220Ω all'interno del circuito per proteggerlo.

Il circuito che formano è mostrato di seguito.

|bc2.5|

A questo punto potresti chiederti: come costruisco questo circuito? Tieni i fili con le mani, o nastro i pin e i fili?

In questa situazione, le breadboard senza saldatura saranno i tuoi alleati più forti.

.. _bc_bb:

Ciao, Breadboard!
------------------------------

Una breadboard è una piastra rettangolare di plastica con un sacco di piccoli fori. 
Questi fori ci permettono di inserire facilmente componenti elettronici e costruire circuiti elettronici. 
Le breadboard non fissano permanentemente i componenti elettronici, quindi possiamo facilmente riparare un circuito e ricominciare se qualcosa va storto.

.. note::
    Non c'è bisogno di strumenti speciali per utilizzare le breadboard. Tuttavia, molti componenti elettronici sono molto piccoli, e un paio di pinzette possono aiutarci a prendere meglio le piccole parti.

Su Internet, possiamo trovare molte informazioni sulle breadboard.

* `How to Use a Breadboard - Science Buddies <https://www.sciencebuddies.org/science-fair-projects/references/how-to-use-a-breadboard#pth-smd>`_

* `What is a BREADBOARD? - Makezine <https://cdn.makezine.com/uploads/2012/10/breadboardworkshop.pdf>`_


Ecco alcune cose che dovresti sapere sulle breadboard.

#. Ogni gruppo di mezza fila (come la colonna A-E nella fila 1 o la colonna F-J nella fila 3) è collegato. Pertanto, se un segnale elettrico entra da A1, può uscire da B1, C1, D1, E1, ma non da F1 o A2.

#. Nella maggior parte dei casi, entrambi i lati della breadboard sono utilizzati come bus di alimentazione, e i fori in ogni colonna (circa 50 fori) sono collegati tra loro. Di norma, le alimentazioni positive sono collegate ai fori vicino al filo rosso, e le alimentazioni negative ai fori vicino al filo blu.

#. In un circuito, la corrente fluisce dal polo positivo al polo negativo dopo essere passata attraverso il carico. In questo caso, può verificarsi un cortocircuito.

|bc3| 

Seguiamo la direzione della corrente per costruire il circuito!

1. In questo circuito, utilizziamo il pin 3V3 della scheda Pico W per alimentare il LED. Usa un cavo jumper maschio-maschio (M2M) per collegarlo al bus di alimentazione rosso.
#. Per proteggere il LED, la corrente deve passare attraverso una resistenza da 220 ohm. Collega un'estremità (qualsiasi estremità) della resistenza al bus di alimentazione rosso, e l'altra estremità a una fila libera della breadboard (fila 24 nel mio circuito).

    .. note::
        L'anello colorato della resistenza da 220 ohm è rosso, rosso, nero, nero e marrone.

#. Se sollevi il LED, vedrai che uno dei suoi piedini è più lungo dell'altro. Collega il piedino più lungo alla stessa fila della resistenza, e il piedino più corto alla stessa fila dall'altra parte della fessura centrale sulla breadboard.

    .. note::
        Il piedino più lungo è l'anodo, che rappresenta il lato positivo del circuito; il piedino più corto è il catodo, che rappresenta il lato negativo.

        L'anodo deve essere collegato al pin GPIO tramite una resistenza; il catodo deve essere collegato al pin GND.

#. Usando un cavo jumper maschio-maschio (M2M), collega il piedino corto del LED al bus di alimentazione negativo della breadboard.
#. Collega il pin GND del Pico W al bus di alimentazione negativo utilizzando un cavo jumper.

Attenzione ai cortocircuiti
--------------------------------
I cortocircuiti possono verificarsi quando due componenti che non dovrebbero essere collegati sono "accidentalmente" collegati. 
Questo kit include resistenze, transistor, condensatori, LED, ecc. che hanno lunghi piedini metallici che possono urtarsi tra loro e causare un cortocircuito. Alcuni circuiti sono semplicemente impediti dal funzionare correttamente quando si verifica un cortocircuito. Occasionalmente, un cortocircuito può danneggiare permanentemente i componenti, specialmente tra l'alimentazione e il bus di massa, causando un surriscaldamento del circuito, sciogliendo la plastica sulla breadboard e persino bruciando i componenti!

Pertanto, assicurati sempre che i piedini di tutti i componenti elettronici sulla breadboard non si tocchino tra loro.

Orientamento del circuito
---------------------------------
I circuiti hanno un orientamento, e l'orientamento gioca un ruolo significativo in alcuni componenti elettronici. Alcuni dispositivi hanno polarità, il che significa che devono essere collegati correttamente in base ai loro poli positivo e negativo. I circuiti costruiti con l'orientamento sbagliato non funzioneranno correttamente.

|bc3|

Se inverti l'orientamento del LED in questo semplice circuito che abbiamo costruito in precedenza, scoprirai che non funziona più.

Al contrario, alcuni dispositivi non hanno direzione, come le resistenze in questo circuito, quindi puoi provare a invertirle senza influire sul funzionamento normale del LED.

La maggior parte dei componenti e moduli con etichette come "+", "-", "GND", "VCC" o che hanno piedini di lunghezze diverse devono essere collegati al circuito in un modo specifico.

Protezione del circuito
-------------------------------------

La corrente è la velocità con cui gli elettroni passano attraverso un punto in un circuito elettrico completo. Alla base, la corrente = flusso. Un ampere (AM-pir), o ampere, è l'unità internazionale utilizzata per misurare la corrente. Esprime la quantità di elettroni (a volte chiamata "carica elettrica") che passa attraverso un punto in un circuito in un determinato periodo di tempo.

La forza motrice (voltaggio) dietro il flusso di corrente si chiama tensione ed è misurata in volt (V).

La resistenza (R) è la proprietà del materiale che limita il flusso di corrente, ed è misurata in ohm (Ω).

Secondo la legge di Ohm (purché la temperatura rimanga costante), corrente, tensione e resistenza sono proporzionali.
La corrente di un circuito è proporzionale alla sua tensione e inversamente proporzionale alla sua resistenza. 

Pertanto, corrente (I) = tensione (V) / resistenza (R).

* `Ohm's law - Wikipedia <https://en.wikipedia.org/wiki/Ohm%27s_law>`_

Sulla legge di Ohm possiamo fare un semplice esperimento.

|bc3|

Cambiando il filo che collega 3V3 a 5V (cioè VBUS, il 40º pin del Pico W), il LED diventerà più luminoso.
Se cambi la resistenza da 220ohm a 1000ohm (anello colorato: marrone, nero, nero, marrone e marrone), noterai che il LED diventa più fioco di prima. Più grande è la resistenza, più fioco sarà il LED.

.. note::
    Per un'introduzione alle resistenze e su come calcolare i valori di resistenza, vedi :ref:`cpn_resistor`.

La maggior parte dei moduli confezionati richiede solo l'accesso alla giusta tensione (di solito 3.3V o 5V), come il modulo ultrasonico.

Tuttavia, nei tuoi circuiti costruiti autonomamente, devi essere consapevole della tensione di alimentazione e dell'uso delle resistenze per i dispositivi elettrici.

Ad esempio, i LED di solito consumano 20mA di corrente, e la loro caduta di tensione è di circa 1.8V. Secondo la legge di Ohm, se utilizziamo una fonte di alimentazione da 5V, dobbiamo collegare una resistenza minima di 160ohm ((5-1.8)/20mA) per non bruciare il LED.

