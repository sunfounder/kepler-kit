.. _ar_irremote:

6.4 - IR-Fernbedienung
=======================

Im Bereich der Unterhaltungselektronik dienen Fernbedienungen zur Steuerung von Geräten wie Fernsehern und DVD-Playern. In einigen Fällen ermöglichen sie die Bedienung von Geräten, die außer Reichweite sind, etwa Zentral-Klimaanlagen.

Ein IR-Empfänger ist ein Bauteil mit einer Fotozelle, die auf Infrarotlicht abgestimmt ist. Er wird fast immer zur Fernbedienungserkennung eingesetzt - jeder Fernseher und DVD-Player hat einen solchen an der Vorderseite, um das IR-Signal vom Bediengerät zu empfangen. In der Fernbedienung selbst ist eine passende IR-LED, die IR-Impulse sendet, um den Fernseher ein- oder auszuschalten oder den Kanal zu wechseln.

* :ref:`cpn_ir_receiver`

**Benötigte Komponenten**

Für dieses Projekt werden die folgenden Komponenten benötigt. 

Es ist durchaus praktisch, ein komplettes Set zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ARTIKEL IN DIESEM SET
        - KAUF-LINK
    *   - Kepler Kit
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
        - :ref:`cpn_ir_receiver`
        - 1
        - |link_receiver_buy|

**Schaltplan**

|sch_irrecv|

**Verdrahtung**

|wiring_irrecv|

**Code**

.. note::

    * Die Datei ``6.4_ir_remote_control.ino`` finden Sie unter dem Pfad ``kepler-kit-main/arduino/6.4_ir_remote_control``.
    * Oder kopieren Sie den Code in die **Arduino IDE**.
    * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den richtigen Port auszuwählen, bevor Sie auf den **Hochladen**-Button klicken.
    * Die Bibliothek ``IRsmallDecoder`` wird hier verwendet. Bitte beziehen Sie sich auf :ref:`add_libraries_ar`, um sie in die Arduino IDE hinzuzufügen.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/71f50561-d1ad-4d9e-9db2-8eb7727df0a4/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Die neue Fernbedienung enthält ein Plastikstück am Ende, das die Batterie isoliert. Dieses Plastikstück muss entfernt werden, um die Fernbedienung in Betrieb zu nehmen. Sobald das Programm läuft und Sie die Fernbedienung drücken, wird der Serial Monitor den gedrückten Knopf ausgeben.

.. **Funktionsweise**
