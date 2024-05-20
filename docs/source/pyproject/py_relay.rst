.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_relay:

2.16 Steuerung eines weiteren Stromkreises
==========================================

Im Alltag können wir einen Schalter betätigen, um eine Lampe ein- oder auszuschalten.
Doch was ist, wenn Sie die Lampe mit Pico W so steuern möchten, dass sie sich automatisch nach zehn Minuten ausschaltet?

Ein Relais kann Ihnen dabei helfen.

Ein Relais ist tatsächlich eine spezielle Art von Schalter, der von einer Seite des Stromkreises (in der Regel ein Niederspannungsstromkreis) gesteuert wird und dazu dient, die andere Seite des Stromkreises (in der Regel ein Hochspannungsstromkreis) zu steuern.
Das macht es praktisch, unsere Haushaltsgeräte umzurüsten, damit sie durch ein Programm gesteuert, zu intelligenten Geräten gemacht oder sogar mit dem Internet verbunden werden können.

.. warning::
    Das Modifizieren von Elektrogeräten ist mit großen Gefahren verbunden. Versuchen Sie es nicht leichtfertig und führen Sie es nur unter Anleitung von Fachleuten durch.

* :ref:`cpn_relay`

In diesem Projekt verwenden wir als Beispiel nur einen einfachen, durch ein Steckbrett-Strommodul betriebenen Stromkreis, um zu zeigen, wie man ihn mit einem Relais steuert.

* :ref:`cpn_power_module`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist definitiv praktisch, ein ganzes Set zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ARTIKEL IN DIESEM SET
        - LINK
    *   - Kepler Kit
        - 450+
        - |link_kepler_kit|

Sie können die Komponenten auch einzeln über die untenstehenden Links kaufen.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTE
        - MENGE
        - LINK

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

Zuerst erstellen wir einen Niederspannungsstromkreis zur Steuerung eines Relais.
Das Ansteuern des Relais erfordert einen hohen Strom, daher ist ein Transistor erforderlich. Hier verwenden wir den S8050.

|sch_relay_1|

|wiring_relay_1|



Hier wird eine Diode (Freilaufdiode) verwendet, um den Stromkreis zu schützen. Die Kathode ist das Ende mit dem Silberband, das an die Stromversorgung angeschlossen ist, und die Anode ist mit dem Transistor verbunden.

Wenn die Eingangsspannung von Hoch (5V) auf Niedrig (0V) wechselt, wechselt der Transistor von Sättigung (Verstärkung, Sättigung und Abschaltung) zu Abschaltung, und plötzlich gibt es keinen Weg mehr für den Strom, durch die Spule zu fließen.

An diesem Punkt, wenn diese Freilaufdiode nicht existiert, wird die Spule an beiden Enden ein selbstinduziertes elektrisches Potential erzeugen, das mehrere Male höher ist als die Versorgungsspannung, und diese Spannung zusammen mit der Spannung aus der Transistorstromversorgung reicht aus, um ihn zu verbrennen.

Nach dem Hinzufügen der Diode bilden die Spule und die Diode sofort einen neuen, durch die in der Spule gespeicherte Energie betriebenen Stromkreis zur Entladung, wodurch übermäßige Spannungen, die Bauteile wie Transistoren im Stromkreis beschädigen könnten, vermieden werden.

* :ref:`cpn_diode`
* `Freilaufdiode - Wikipedia <https://de.wikipedia.org/wiki/Freilaufdiode>`_

Jetzt ist das Programm bereit zur Ausführung. Nach dem Starten hören Sie ein "Klick-Klack"-Geräusch, das ist das Geräusch der Kontaktspule im Relais, die anzieht und löst.

Dann verbinden wir die beiden Enden des Laststromkreises mit den Pins 3 und 6 des Relais.

.. (Nehmen Sie den einfachen, durch das Steckbrett-Strommodul betriebenen Stromkreis aus dem vorherigen Artikel als Beispiel.)

|sch_relay_2|

|wiring_relay_2|

Jetzt kann das Relais den Laststromkreis ein- und ausschalten.

**Code**

.. note::

    * Öffnen Sie die Datei ``2.16_control_another_circuit.py`` im Verzeichnis ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny, und klicken Sie dann auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5, um es auszuführen.

    * Vergessen Sie nicht, den "MicroPython (Raspberry Pi Pico)"-Interpreter in der rechten unteren Ecke auszuwählen.

    * Für detaillierte Anleitungen siehe :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime
    
    relay = machine.Pin(15, machine.Pin.OUT)
    while True:
        relay.value(1)
        utime.sleep(2)
        relay.value(0)
        utime.sleep(2)

Wenn der Code ausgeführt wird, wechselt das Relais alle zwei Sekunden den Betriebszustand des gesteuerten Stromkreises.
Sie können eine der Zeilen manuell auskommentieren, um die Korrespondenz zwischen dem Relaisschaltkreis und dem Laststromkreis weiter zu klären.

**Weitere Informationen**

Pin 3 des Relais ist normalerweise offen und schließt nur, wenn die Kontaktspule in Betrieb ist; Pin 4 ist normalerweise geschlossen und schließt, wenn die Kontaktspule erregt wird.
Pin 1 ist mit Pin 6 verbunden und ist der gemeinsame Anschluss des Laststromkreises.

Indem man ein Ende des Laststromkreises von Pin 3 auf Pin 4 wechselt, erhält man genau den gegenteiligen Betriebszustand.
