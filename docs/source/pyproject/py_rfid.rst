.. _py_rfid:

6.5 Funkfrequenz-Identifikation
==============================================

Die Funkfrequenz-Identifikation (RFID) ist eine Technologie, die drahtlose Kommunikation zwischen einem Objekt (oder Tag) und einem abfragenden Gerät (oder Lesegerät) zur Identifizierung und Nachverfolgung nutzt. Die Übertragungsreichweite des Tags ist auf einige Meter begrenzt. Eine direkte Sichtlinie zwischen Lesegerät und Tag ist nicht zwingend erforderlich.

Die meisten Tags verfügen über einen integrierten Schaltkreis (IC) und eine Antenne.
Neben der Datenspeicherung ermöglicht der Mikrochip die Kommunikation mit dem Lesegerät via Funkfrequenz (RF).
Passive Tags haben keine eigenständige Energiequelle und sind für ihre Stromversorgung auf ein externes elektromagnetisches Signal des Lesegeräts angewiesen.
Aktive Tags hingegen verfügen über eine unabhängige Energiequelle, etwa eine Batterie, was ihnen eine höhere Leistungsfähigkeit bei der Verarbeitung, Übertragung und Reichweite ermöglicht.

* :ref:`cpn_mfrc522`

**Benötigte Komponenten**

Für dieses Projekt werden die folgenden Komponenten benötigt.

Ein Komplettset ist natürlich praktisch, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Bezeichnung	
        - ARTIKEL IN DIESEM KIT
        - LINK
    *   - Kepler Kit	
        - 450+
        - |link_kepler_kit|

Die Komponenten können auch separat über die untenstehenden Links erworben werden.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTE	
        - ANZAHL
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
        - mehrere
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_mfrc522`
        - 1
        - |link_rfid_buy|

**Schaltplan**

|sch_rfid|

**Verkabelung**

|wiring_rfid|

**Code**

Bitte verwenden Sie die Bibliotheken im Ordner ``mfrc522``. Stellen Sie sicher, dass diese auf dem Pico W hochgeladen wurden. Eine detaillierte Anleitung finden Sie unter :ref:`add_libraries_py`.

Die Hauptfunktion ist zweigeteilt:

* ``6.5_rfid_write.py``: Dient dem Beschreiben der Karte (oder des Schlüssels).
* ``6.5_rfid_read.py``: Dient dem Auslesen der Karte (oder des Schlüssels).

Öffnen Sie die Datei ``6.5_rfid_write.py`` im Pfad ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny und klicken Sie dann auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.

Nach dem Ausführen können Sie eine Nachricht im Shell-Fenster eingeben und die Karte (oder den Schlüssel) in die Nähe des MFRC522-Moduls halten, um die Nachricht darauf zu schreiben.

.. code-block:: python

    from mfrc522 import SimpleMFRC522

    reader = SimpleMFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=5,rst=0)

    def write():
        to_write = input("Please enter the message: ")
        print("Writing...Please place the card...")
        id, text = reader.write(to_write)
        print("ID: %s\nText: %s" % (id,text))

    write()

Öffnen Sie die Datei ``6.5_rfid_read.py`` im Pfad ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny und klicken Sie dann auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5, um es auszuführen.

Nach dem Ausführen können Sie die auf der Karte (oder dem Schlüssel) gespeicherte Nachricht auslesen.

.. code-block:: python

    from mfrc522 import SimpleMFRC522

    reader = SimpleMFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=5,rst=0)

    def read():
        print("Reading...Please place the card...")
        id, text = reader.read()
        print("ID: %s\nText: %s" % (id,text))

    read()

**Wie funktioniert es?**

.. code-block:: python

    from mfrc522 import SimpleMFRC522

    reader = SimpleMFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=5,rst=0)

Instanzierung der Klasse ``SimpleMFRC522()``.

.. code-block:: python

    id, text = reader.read()

Diese Funktion dient dem Auslesen der Kartendaten. Bei erfolgreichem Auslesen werden ID und Text zurückgegeben.

.. code-block:: python

    id, text = reader.write("text")

Diese Funktion dient dem Beschreiben der Karte. Drücken Sie die **Eingabetaste**, um den Vorgang abzuschließen.
``text`` sind die auf die Karte zu schreibenden Informationen.
