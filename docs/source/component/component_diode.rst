.. note::

    Ciao, benvenuto nella Community di SunFounder per appassionati di Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_diode:

Diodo
=================

|img_diode|

Un diodo è un componente elettronico con due elettrodi. Permette il flusso di corrente in una sola direzione, funzione comunemente chiamata "rettificazione".
Pertanto, un diodo può essere considerato come una versione elettronica di una valvola di non ritorno.

I due terminali di un diodo sono polarizzati: l'estremità positiva è chiamata anodo e l'estremità negativa è chiamata catodo.
Il catodo è generalmente argentato o ha una fascia colorata.
Controllare la direzione del flusso di corrente è una delle caratteristiche principali dei diodi — la corrente in un diodo fluisce dall'anodo al catodo. Il comportamento di un diodo è simile a quello di una valvola di non ritorno. Una delle caratteristiche più importanti di un diodo è la non linearità della corrente-tensione. Se una tensione maggiore viene collegata all'anodo, la corrente fluisce dall'anodo al catodo, e il processo è noto come polarizzazione diretta. Tuttavia, se una tensione maggiore è collegata al catodo, il diodo non conduce elettricità, e il processo è chiamato polarizzazione inversa.

Grazie alla sua conduttività unidirezionale, il diodo è utilizzato in quasi tutti i circuiti elettronici complessi. È stato uno dei primi dispositivi a semiconduttore a essere creato, e le sue applicazioni sono molto diffuse.

Tuttavia, nella realtà, i diodi non mostrano una direzionalità perfetta di on e off, ma piuttosto caratteristiche elettroniche non lineari più complesse, determinate dal tipo specifico di tecnologia del diodo.

Un diodo è una giunzione p-n formata da un semiconduttore di tipo p e un semiconduttore di tipo n, con uno strato di carica spaziale formato su entrambi i lati della sua interfaccia e un campo elettrico auto-generato, che è in equilibrio elettrico quando non è presente alcuna tensione applicata poiché la corrente di diffusione dovuta alla differenza di concentrazione dei portatori tra i due lati della giunzione p-n e la corrente di deriva dovuta al campo elettrico auto-generato sono uguali. Quando viene generata una polarizzazione di tensione diretta, la soppressione reciproca del campo elettrico esterno e del campo elettrico auto-generato aumenta la corrente di diffusione dei portatori causando la corrente diretta (cioè il motivo della conduttività). Quando viene generata una polarizzazione di tensione inversa, il campo elettrico esterno e il campo elettrico auto-generato vengono ulteriormente rafforzati per formare una corrente di saturazione inversa I0 in un certo intervallo di tensione inversa indipendente dal valore della tensione di polarizzazione inversa (che è il motivo della non conduttività). 
Quando la tensione inversa applicata è alta a un certo punto, la forza del campo elettrico nello strato di carica spaziale della giunzione p-n raggiunge un valore critico per produrre un processo di moltiplicazione dei portatori, generando un gran numero di coppie elettrone-lacuna, risultando in un grande valore della corrente di rottura inversa, chiamata fenomeno di rottura del diodo.


**1. Caratteristica diretta**

Quando viene applicata una tensione diretta esterna, all'inizio della caratteristica diretta, la tensione diretta è molto piccola, non sufficiente a superare l'effetto bloccante del campo elettrico nella giunzione p-n, la corrente diretta è quasi nulla, questa sezione è chiamata zona morta.
Questa tensione diretta che non permette al diodo di condurre è chiamata tensione di soglia. Quando la tensione diretta è maggiore della tensione di soglia, il campo elettrico della giunzione p-n viene superato, il diodo conduce in avanti e la corrente aumenta con la tensione e sale rapidamente.
Nel normale utilizzo della gamma di corrente, la tensione terminale del diodo durante la conduzione rimane quasi costante, questa tensione è chiamata tensione diretta del diodo.


**2. Caratteristica inversa**

Quando viene applicata una tensione inversa, e non supera un certo intervallo, la corrente che passa attraverso il diodo è formata da un movimento di deriva di pochi portatori, generando la corrente inversa.
Poiché la corrente inversa è molto piccola, il diodo è nello stato di interruzione. Questa corrente inversa è anche conosciuta come corrente di saturazione inversa o corrente di perdita, ed è fortemente influenzata dalla temperatura.

**3. Rottura**

Quando la tensione inversa applicata supera un certo valore, la corrente inversa aumenterà improvvisamente, un fenomeno noto come rottura elettrica.
La tensione critica che causa la rottura elettrica è chiamata tensione di rottura inversa, e il diodo perderà la sua conduttività unidirezionale al momento della rottura elettrica.
Pertanto, l'uso del diodo dovrebbe essere evitato quando la tensione inversa applicata è troppo alta.

I primi diodi erano costituiti da cristalli "Cat's Whisker" e tubi a vuoto (chiamati anche "valvole termoelettroniche"). La maggior parte dei diodi più comuni di oggi utilizza materiali semiconduttori come il silicio o il germanio.

* `P–N junction - Wikipedia <https://en.wikipedia.org/wiki/P-n_junction>`_

* `Diode - Wikipedia <https://en.wikipedia.org/wiki/Diode>`_


