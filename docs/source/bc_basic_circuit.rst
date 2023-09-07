Elektrischer Schaltkreis
==========================

Viele Dinge, die du täglich benutzt, werden elektrisch betrieben, sei es die Beleuchtung in deinem Zuhause oder der Computer, auf dem du gerade dies liest.

Um Elektrizität nutzen zu können, muss ein elektrischer Schaltkreis geschaltet werden. Ein solcher besteht aus Metallleitungen sowie elektrischen und elektronischen Bauteilen.

Jeder Schaltkreis benötigt eine Stromquelle. In deinem Haushalt werden die meisten Geräte (z.B. Fernseher, Lampen) über Steckdosen mit Energie versorgt. Viele kleinere, mobile Schaltkreise (z.B. elektronisches Spielzeug, Mobiltelefone) hingegen laufen auf Batterien. Eine Batterie hat zwei Anschlüsse: einen positiven, der mit einem Pluszeichen (+) markiert ist, und einen negativen, der durch ein Minuszeichen (-) symbolisiert wird, jedoch meist nicht auf der Batterie vermerkt ist.

Damit ein Stromfluss entsteht, muss ein leitfähiger Pfad den positiven mit dem negativen Anschluss der Batterie verbinden. Man spricht dann von einem geschlossenen Schaltkreis (im Gegensatz dazu steht der offene Schaltkreis, bei dem die Verbindung getrennt ist). Elektrischer Strom durchfließt dann Geräte wie Lampen und bringt sie zum Leuchten.

|bc1|

Ein Pico W hat einige Ausgangspins für die Stromversorgung (positiv) und einige Massepins (negativ). Diese Pins können als positive und negative Anschlüsse für die Stromversorgung verwendet werden, indem der Pico W an eine Energiequelle angeschlossen wird.

|bc2|

Mit Elektrizität lassen sich Werke mit Licht, Ton und Bewegung realisieren. Man kann eine LED zum Leuchten bringen, indem man den längeren Pin an den positiven und den kürzeren an den negativen Anschluss anschließt. Ohne Vorkehrungen würde die LED jedoch schnell kaputtgehen, weshalb ein 220*-Ohm-Widerstand im Schaltkreis eingefügt werden muss.

Die darzustellende Schaltung sieht wie folgt aus.

|bc2.5|

Vielleicht fragst du dich jetzt: Wie baue ich diesen Schaltkreis zusammen? Halte ich die Kabel mit der Hand oder klebe ich die Pins und Kabel fest?

In diesem Fall sind steckbare Experimentierplatinen (Breadboards) deine besten Helfer.

.. _bc_bb:

Hallo, Steckplatine!
------------------------------

Eine Steckplatine ist eine rechteckige Kunststoffplatte mit vielen kleinen Löchern. Diese erlauben es uns, elektronische Bauteile einfach einzustecken und elektrische Schaltungen zu bauen. Die Bauteile werden nicht permanent fixiert, sodass wir bei einem Fehler den Schaltkreis einfach reparieren oder von vorn beginnen können.

.. note::
    Spezielle Werkzeuge sind für die Verwendung von Steckplatinen nicht erforderlich. Da jedoch viele elektronische Bauteile sehr klein sind, können Pinzetten hilfreich sein, um kleinere Teile besser greifen zu können.

Im Internet finden sich zahlreiche Informationen zu Steckplatinen.

* `Wie benutzt man eine Steckplatine - Science Buddies <https://www.sciencebuddies.org/science-fair-projects/references/how-to-use-a-breadboard#pth-smd>`_

* `Was ist eine STECKPLATINE? - Makezine <https://cdn.makezine.com/uploads/2012/10/breadboardworkshop.pdf>`_


Es gibt ein paar Dinge, die du über Steckplatinen wissen solltest.

#. Jede halbe Reihengruppe (wie die Spalte A-E in Reihe 1 oder Spalte F-J in Reihe 3) ist intern verbunden. Wenn also ein elektrisches Signal an A1 anliegt, kann es auch an B1, C1, D1, E1, jedoch nicht an F1 oder A2 austreten.

#. In den meisten Fällen werden beide Seiten der Steckplatine als Stromschienen verwendet, und die Löcher in jeder Spalte (etwa 50 Löcher) sind miteinander verbunden. Üblicherweise werden positive Stromanschlüsse in der Nähe des roten Drahts und negative in der Nähe des blauen Drahts angeschlossen.

#. In einem Schaltkreis fließt der Strom vom positiven zum negativen Pol, nachdem er die Last durchquert hat. In diesem Fall könnte ein Kurzschluss auftreten.

|bc3|

Lassen Sie uns nun den Schaltkreis entsprechend der Stromflussrichtung aufbauen!

1. In diesem Schaltkreis verwenden wir den 3V3-Pin des Pico W-Boards, um die LED mit Strom zu versorgen. Verwenden Sie ein Steckbrückenkabel (M2M), um es mit der roten Stromschiene zu verbinden.
#. Um die LED zu schützen, muss der Strom durch einen 220-Ohm-Widerstand fließen. Verbinden Sie ein Ende (es ist egal welches) des Widerstands mit der roten Stromschiene und das andere mit einer freien Reihe der Steckplatine (in meiner Schaltung Reihe 24).

   .. note::
       Die Farbringe des 220-Ohm-Widerstands sind rot, rot, schwarz, schwarz und braun.

#. Wenn Sie die LED aufheben, sehen Sie, dass einer der Anschlüsse länger ist als der andere. Verbinden Sie den längeren Anschluss mit derselben Reihe wie der Widerstand und den kürzeren Anschluss mit einer Reihe auf der gegenüberliegenden Seite der Mittellücke auf der Steckplatine.

   .. note::
       Der längere Anschluss ist die Anode und repräsentiert die positive Seite des Schaltkreises; der kürzere ist die Kathode und steht für die negative Seite.

       Die Anode sollte über einen Widerstand mit dem GPIO-Pin verbunden werden; die Kathode sollte mit dem GND-Pin verbunden werden.

#. Verwenden Sie ein Steckbrückenkabel (M2M), um den kürzeren LED-Anschluss mit der negativen Stromschiene der Steckplatine zu verbinden.
#. Verbinden Sie den GND-Pin des Pico W mit der negativen Stromschiene über ein Steckbrückenkabel.

Vorsicht vor Kurzschlüssen
------------------------------
Kurzschlüsse können entstehen, wenn zwei Bauteile, die eigentlich nicht miteinander verbunden sein sollten, "versehentlich" Kontakt aufnehmen. Dieses Set beinhaltet Widerstände, Transistoren, Kondensatoren, LEDs und mehr, deren lange Metallstifte sich berühren und einen Kurzschluss verursachen können. Manche Schaltkreise funktionieren einfach nicht mehr richtig, wenn ein Kurzschluss auftritt. In Einzelfällen kann ein Kurzschluss die Bauteile dauerhaft beschädigen, insbesondere wenn die Stromversorgung und die Masseleitung betroffen sind. Das kann dazu führen, dass der Schaltkreis stark erhitzt, das Plastik auf der Steckplatine schmilzt und sogar die Bauteile verbrennen!

Stellen Sie deshalb immer sicher, dass die Stifte der elektronischen Bauteile auf der Steckplatine einander nicht berühren.

Ausrichtung des Schaltkreises
-------------------------------
Schaltkreise haben eine Orientierung, die bei bestimmten elektronischen Bauteilen eine entscheidende Rolle spielt. Einige Geräte haben eine Polarität, d.h., sie müssen gemäß ihrer positiven und negativen Pole korrekt angeschlossen werden. Falsch ausgerichtete Schaltkreise funktionieren nicht einwandfrei.

|bc3|

Wenn Sie die LED in diesem einfachen Schaltkreis, den wir zuvor gebaut haben, umdrehen, werden Sie feststellen, dass sie nicht mehr funktioniert.

Im Gegensatz dazu haben manche Bauteile keine Ausrichtung, wie zum Beispiel die Widerstände in diesem Schaltkreis. Diese können Sie umkehren, ohne den normalen Betrieb der LEDs zu beeinträchtigen.

Die meisten Komponenten und Module mit Beschriftungen wie "+", "-", "GND", "VCC" oder unterschiedlich langen Pins müssen auf eine spezielle Weise an den Schaltkreis angeschlossen werden.

Schutz des Schaltkreises
-------------------------------------
Stromstärke ist die Geschwindigkeit, mit der Elektronen an einem Punkt in einem vollständigen elektrischen Stromkreis fließen. Einfach ausgedrückt: Strom = Fluss. Ein Ampere (Amper), oder kurz Amp, ist die internationale Einheit für die Messung der Stromstärke. Sie drückt die Menge der Elektronen (manchmal als "elektrische Ladung" bezeichnet) aus, die an einem Punkt im Stromkreis über eine bestimmte Zeit hinweg fließen.

Die treibende Kraft (Spannung) hinter dem Stromfluss wird als Spannung bezeichnet und in Volt (V) gemessen.

Widerstand (R) ist die Eigenschaft des Materials, die den Stromfluss einschränkt, und wird in Ohm (Ω) gemessen.

Laut Ohmschem Gesetz (solange die Temperatur konstant bleibt), sind Stromstärke, Spannung und Widerstand proportional zueinander. Die Stromstärke eines Schaltkreises ist proportional zu seiner Spannung und umgekehrt proportional zu seinem Widerstand.

Daher gilt: Stromstärke (I) = Spannung (V) / Widerstand (R).

* `Ohmsches Gesetz - Wikipedia <https://de.wikipedia.org/wiki/Ohmsches_Gesetz>`_

Zum Ohmschen Gesetz können wir ein einfaches Experiment durchführen.

|bc3|

Wenn Sie den Draht, der 3V3 mit 5V verbindet (d.h. VBUS, der 40. Pin des Pico W), ändern, wird die LED heller. Wenn Sie den Widerstand von 220 Ohm auf 1000 Ohm ändern (Farbring: braun, schwarz, schwarz, braun, braun), werden Sie feststellen, dass die LED dunkler wird. Je größer der Widerstand, desto dunkler die LED.

.. note::
    Für eine Einführung in Widerstände und wie man den Widerstand berechnet, siehe :ref:`cpn_resistor`.


Die meisten vorgepackten Module benötigen lediglich Zugang zur richtigen Spannung (meistens 3,3V oder 5V), wie beispielsweise Ultraschallmodule.

In Ihren selbstgebauten Schaltkreisen sollten Sie jedoch auf die Versorgungsspannung und den Einsatz von Widerständen für elektrische Geräte achten.

Als Beispiel verbrauchen LEDs normalerweise 20mA und haben einen Spannungsabfall von etwa 1,8V. Laut Ohmschem Gesetz benötigen wir bei einer 5V-Stromversorgung mindestens einen 160-Ohm-Widerstand ((5-1,8)/20mA), um die LED nicht durchbrennen zu lassen.

