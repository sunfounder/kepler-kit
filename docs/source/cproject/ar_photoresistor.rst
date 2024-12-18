.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_photoresistor:

2.12 - Das Licht erfassen
=================================

Der Fotowiderstand ist ein typisches Bauelement für analoge Eingänge und wird ähnlich wie ein Potentiometer verwendet. Sein Widerstandswert hängt von der Lichtintensität ab: Je stärker das einfallende Licht, desto geringer der Widerstandswert; umgekehrt nimmt er zu.

* :ref:`cpn_photoresistor`

**Erforderliche Bauteile**

Für dieses Projekt benötigen wir die folgenden Bauteile.

Ein komplettes Set zu kaufen, ist definitiv praktisch. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Bezeichnung
        - ELEMENTE IN DIESEM KIT
        - KAUF-LINK
    *   - Kepler Kit
        - 450+
        - |link_kepler_kit|

Alternativ können Sie die Teile auch einzeln über die folgenden Links erwerben.

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
        - :ref:`cpn_resistor`
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_photoresistor`
        - 1
        - |link_photoresistor_buy|

**Schaltbild**

|sch_photoresistor|

In diesem Schaltkreis sind der 10K-Widerstand und der Fotowiderstand in Serie geschaltet, und der Strom, der durch sie fließt, ist derselbe. Der 10K-Widerstand dient als Schutz, und GP28 liest den Wert nach der Spannungsumwandlung des Fotowiderstands.

Wenn das Licht stärker wird, verringert sich der Widerstand des Fotowiderstands, wodurch seine Spannung sinkt, und der Wert von GP28 wird ebenfalls sinken; wenn das Licht stark genug ist, wird der Widerstand des Fotowiderstands nahe 0 sein, und der Wert von GP28 wird nahe 0 sein. In diesem Moment spielt der 10K-Widerstand eine Schutzrolle, sodass 3,3V und GND nicht direkt verbunden werden, was zu einem Kurzschluss führen würde.

Wenn Sie den Fotowiderstand in eine dunkle Umgebung bringen, wird der Wert von GP28 steigen. In einer ausreichend dunklen Umgebung wird der Widerstand des Fotowiderstands unendlich sein, und seine Spannung wird nahe 3,3V sein (der 10K-Widerstand ist vernachlässigbar), und der Wert von GP28 wird nahe dem Maximalwert von 1023 sein.

Die Berechnungsformel ist unten dargestellt.

.. code-block::

  Digitaler Wert = (Analogspannung / 3,3V) * 1023


**Verkabelung**

|wiring_photoresistor|

**Programmcode**

.. note::

   * Die Datei ``2.12_feel_the_light.ino`` befindet sich im Verzeichnis ``kepler-kit-main/arduino/2.12_feel_the_light``.
   * Alternativ können Sie den Code auch direkt in die **Arduino IDE** kopieren.
   
   * Denken Sie daran, vor dem Hochladen des Programms die richtige Platine (Raspberry Pi Pico) und den entsprechenden Port auszuwählen.


.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/44074b9e-3e4e-475b-af37-689254f87ab2/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Nach dem Start des Programms gibt der serielle Monitor die Werte des Fotowiderstands aus. Sie können die Werte verändern, indem Sie eine Taschenlampe darauf richten oder ihn mit der Hand abdecken.
