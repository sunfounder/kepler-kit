.. _ar_relay:

2.16 - Steuern eines weiteren Stromkreises
==========================================

Im Alltag können wir einen Schalter betätigen, um eine Lampe ein- oder auszuschalten.
Aber was, wenn Sie die Lampe mit einem Pico W so steuern möchten, dass sie automatisch nach zehn Minuten ausgeht?

Ein Relais kann Ihnen dabei helfen.

Ein Relais ist im Grunde ein spezieller Schalter, der von einer Seite des Stromkreises (in der Regel einem Niederspannungsstromkreis) gesteuert wird und dazu dient, die andere Seite des Stromkreises (meist ein Hochspannungsstromkreis) zu steuern.
Dies macht es praktisch, unsere Haushaltsgeräte umzurüsten, damit sie programmgesteuert, zu intelligenten Geräten oder sogar internetfähig werden.

.. warning::
    Das Modifizieren von Elektrogeräten ist sehr gefährlich. Versuchen Sie es nicht leichtfertig und bitte nur unter professioneller Anleitung.

* :ref:`cpn_relay`

In diesem Beispiel verwenden wir einen einfachen, mit einem Breadboard-Strommodul betriebenen Stromkreis, um zu zeigen, wie man ihn mit einem Relais steuert.

* :ref:`cpn_power_module`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Bauteile.

Ein Komplettset ist definitiv praktisch, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ARTIKEL IN DIESEM KIT
        - KAUF-LINK
    *   - Kepler Kit
        - 450+
        - |link_kepler_kit|

Sie können die Teile auch einzeln über die untenstehenden Links erwerben.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTENBESCHREIBUNG
        - ANZAHL
        - KAUF-LINK

    *   - 1
        - :ref:`cpn_pico_w`
        - 1
        - |link_picow_buy|
    *   - 2
        - Micro-USB-Kabel
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Mehrere
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_transistor`
        - 1 (S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_diode`
        - 1
        - 
    *   - 7
        - :ref:`cpn_relay`
        - 1
        - |link_relay_buy|

**Verdrahtung**

Bauen Sie zunächst einen Niederspannungsstromkreis, um ein Relais zu steuern.
Für das Schalten des Relais ist ein hoher Strom erforderlich, weshalb ein Transistor erforderlich ist. Hier verwenden wir den S8050.

|sch_relay_1|

|wiring_relay_1|

Eine Diode (Freilaufdiode) dient hier zum Schutz des Stromkreises. Die Kathode ist das Ende mit dem Silberstreifen, das mit der Stromquelle verbunden ist, die Anode ist mit dem Transistor verbunden.

Wenn die Eingangsspannung von Hoch (5V) auf Niedrig (0V) wechselt, ändert der Transistor seinen Zustand von Sättigung zu Sperrzustand und der Strom kann plötzlich nicht mehr durch die Spule fließen.

Wird diese Freilaufdiode nicht eingebaut, kann die Spule eine selbstinduzierte elektrische Spannung erzeugen, die mehrere Male höher ist als die Versorgungsspannung. Diese Spannung könnte den Transistor zerstören.

Durch das Hinzufügen der Diode wird ein neuer Stromkreis zwischen Spule und Diode gebildet, der durch die in der Spule gespeicherte Energie entladen wird. Dadurch wird übermäßige Spannung vermieden, die Bauteile wie Transistoren im Stromkreis beschädigen könnte.

* :ref:`cpn_diode`
* `Flyback Diode - Wikipedia <https://de.wikipedia.org/wiki/Freilaufdiode>`_

Nach dem Hochladen des Programms hören Sie ein "Klick-Klack"-Geräusch, das vom Kontaktor im Inneren des Relais stammt.

Anschließend verbinden wir die beiden Enden des Laststromkreises mit den Pins 3 und 6 des Relais.

..(Nehmen Sie den einfachen, mit dem Breadboard-Strommodul betriebenen Stromkreis aus dem vorherigen Artikel als Beispiel.)

|sch_relay_2|

|wiring_relay_2|

Jetzt kann das Relais den Laststromkreis ein- und ausschalten.

**Code**

.. note::

   * Sie können die Datei ``2.16_relay.ino`` im Verzeichnis ``kepler-kit-main/arduino/2.16_relay`` öffnen.
   * Oder kopieren Sie diesen Code in die **Arduino IDE**.
   
   * Vergessen Sie nicht, die korrekte Platine (Raspberry Pi Pico) und den richtigen Port auszuwählen, bevor Sie auf **Hochladen** klicken.

.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/3be98f10-8223-49f2-8238-2acc53ebbf80/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Nach dem Ausführen des Codes wird das Relais den Betriebszustand des gesteuerten Stromkreises alle zwei Sekunden ändern.
Sie können eine der Zeilen manuell auskommentieren, um die Zuordnung zwischen Relaisschaltung und Laststromkreis genauer darzustellen.

**Mehr erfahren**

Pin 3 des Relais ist normalerweise offen und wird nur dann geschlossen, wenn der Kontaktor aktiv ist; Pin 4 ist normalerweise geschlossen und öffnet sich, wenn der Kontaktor aktiviert wird.
Pin 1 ist mit Pin 6 verbunden und stellt den gemeinsamen Anschluss des Laststromkreises dar.

Durch das Umschalten eines Endes des Laststromkreises von Pin 3 auf Pin 4 erhalten Sie genau den entgegengesetzten Betriebszustand.
