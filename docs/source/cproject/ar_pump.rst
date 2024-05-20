.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_pump:

3.6 - Pumpensteuerung
=======================

Kleine Kreiselpumpen eignen sich hervorragend für Projekte zur automatischen Pflanzenbewässerung.
Sie können ebenfalls für den Bau kleiner, intelligenter Wasserspiele verwendet werden.

Als Antriebskomponente dient ein Elektromotor, der genau wie ein herkömmlicher Motor betrieben wird.

* :ref:`cpn_pump`
* :ref:`cpn_motor`
* :ref:`cpn_ta6586`
* :ref:`cpn_power_module`

.. note::

    #. Schließen Sie den Schlauch an den Motoranschluss an, tauchen Sie die Pumpe ins Wasser und schalten Sie sie ein.
    #. Achten Sie darauf, dass der Wasserstand stets höher als der des Motors ist. Leerlauf kann den Motor durch Hitzegenerierung beschädigen und zusätzlich Lärm verursachen.
    #. Falls Sie Pflanzen bewässern, sollte vermieden werden, dass Erde angesaugt wird, da dies die Pumpe verstopfen könnte.
    #. Wenn kein Wasser aus dem Schlauch kommt, könnte Restwasser im Schlauch den Luftstrom blockieren und muss zuerst abgelassen werden.

**Erforderliche Komponenten**

Für dieses Projekt werden die folgenden Bauteile benötigt.

Ein Komplettset zu kaufen ist definitiv praktisch, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Bezeichnung
        - KOMPONENTEN IM SET
        - KAUF-LINK
    *   - Kepler-Kit
        - 450+
        - |link_kepler_kit|

Sie können die Komponenten auch einzeln über die folgenden Links erwerben.

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
        - :ref:`cpn_ta6586`
        - 1
        - 
    *   - 6
        - :ref:`cpn_lipo_charger`
        - 1
        -  
    *   - 7
        - 18650-Akku
        - 1
        -  
    *   - 8
        - Batteriehalter
        - 1
        -  
    *   - 9
        - :ref:`cpn_pump`
        - 1
        -  

**Schaltplan**

|sch_pump|

**Verkabelung**

.. note::

    * Da Pumpen einen hohen Strombedarf haben, nutzen wir hier aus Sicherheitsgründen ein Li-Po-Ladegerät-Modul zur Stromversorgung des Motors.
    * Achten Sie darauf, dass Ihr Li-Po-Ladegerät-Modul wie im Diagramm dargestellt angeschlossen ist. Andernfalls könnte ein Kurzschluss Ihren Akku und die Schaltung beschädigen.

|wiring_pump|

**Code**

.. note::

   * Sie können die Datei ``3.6_pumping.ino`` im Pfad ``kepler-kit-main/arduino/3.6_pumping`` öffnen.
   * Oder kopieren Sie den Code in die **Arduino IDE**.

   * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den richtigen Port auszuwählen, bevor Sie auf die **Upload**-Schaltfläche klicken.

.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/4194feb8-92d4-4ab4-b51c-286d014af0a6/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe> 

Nachdem der Code ausgeführt wurde, beginnt die Pumpe zu arbeiten, und Sie werden gleichzeitig sehen, wie das Wasser aus dem Schlauch fließt.

.. note::

    * Wenn ein erneutes Hochladen des Codes nicht möglich ist, verbinden Sie den **RUN**-Pin am Pico W mit einem Draht mit GND, um ihn zurückzusetzen. Dann entfernen Sie den Draht, um den Code erneut auszuführen.
    * Dies liegt daran, dass der Motor mit zu hohem Strom betrieben wird, was dazu führen kann, dass der Pico W die Verbindung zum Computer verliert.

    |wiring_run_reset|
