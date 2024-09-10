.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_rfid:


6.5 - Funkfrequenz-Identifikation
==============================================

Funkfrequenz-Identifikation (RFID) bezeichnet Technologien, die drahtlose Kommunikation zwischen einem Objekt (oder Tag) und einem Abfragegerät (oder Lesegerät) nutzen, um solche Objekte automatisch zu verfolgen und zu identifizieren. Die Reichweite der Tag-Übertragung ist auf einige Meter vom Lesegerät begrenzt. Eine direkte Sichtlinie zwischen dem Lesegerät und dem Tag ist nicht zwingend erforderlich.

Die meisten Tags enthalten mindestens einen integrierten Schaltkreis (IC) und eine Antenne. 
Der Mikrochip speichert Informationen und ist für die Verwaltung der Funkfrequenzkommunikation (RF) mit dem Lesegerät verantwortlich. Passive Tags verfügen nicht über eine unabhängige Energiequelle und sind auf ein externes elektromagnetisches Signal angewiesen, das vom Lesegerät bereitgestellt wird, um ihren Betrieb zu ermöglichen. 
Aktive Tags verfügen über eine eigenständige Energiequelle, etwa eine Batterie. 
Dadurch können sie erweiterte Verarbeitungs-, Übertragungsfähigkeiten und Reichweite haben.

* :ref:`cpn_mfrc522`

**Erforderliche Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist durchaus praktisch, ein ganzes Kit zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Bezeichnung
        - ARTIKEL IN DIESEM KIT
        - KAUF-LINK
    *   - Kepler-Kit	
        - 450+
        - |link_kepler_kit|

Sie können die einzelnen Komponenten auch separat über die folgenden Links kaufen.

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
        - :ref:`cpn_mfrc522`
        - 1
        - |link_rfid_buy|

**Schaltplan**

|sch_rfid|


**Verdrahtung**

|wiring_rfid|

**Code**

.. note::

   * Die Bibliothek ``MFRC522`` wird hier verwendet. Sie können sie über den **Bibliotheksmanager** installieren.

      .. image:: img/lib_mfrc522.png

Die Hauptfunktion ist in zwei Teile unterteilt:

* ``6.5_rfid_write``, um Informationen auf die Karte (oder den Schlüssel) zu schreiben.

  .. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/b4f9156a-711a-442c-8271-329847e808dc/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

  Nach dem Ausführen kannst du im seriellen Monitor eine Nachricht eingeben, die mit ``#`` endet, und die Nachricht dann auf die Karte schreiben, indem du die Karte (oder den Schlüssel) in die Nähe des MFRC522-Moduls hältst.

* ``6.5_rfid_read``, um die Informationen von der Karte (oder dem Schlüssel) zu lesen.

  .. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/df57b5cb-9162-4b4b-b28a-7f02363885c9/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

  Nach dem Ausführen kannst du die auf der Karte (oder dem Schlüssel) gespeicherte Nachricht lesen.

**Funktionsweise?**

.. code-block:: arduino

    #include <MFRC522.h>

    #define RST_PIN         0
    #define SS_PIN          5

    MFRC522 mfrc522(SS_PIN, RST_PIN);

Zunächst wird die Klasse ``MFRC522()`` instanziiert.

Für eine einfachere Handhabung wird die ``MFRC522``-Bibliothek durch die folgenden Funktionen weiter abstrahiert.

* ``void simple_mfrc522_init()``: Startet die SPI-Kommunikation und initialisiert das MFRC522-Modul.
* ``void simple_mfrc522_get_card()``: Hält das Programm an, bis die Karte (oder der Schlüssel) erkannt wird, und gibt die UID der Karte sowie den PICC-Typ aus.
* ``void simple_mfrc522_write(String text)``: Schreibt einen Text auf die Karte (oder den Schlüssel).
* ``void simple_mfrc522_write(byte* buffer)``: Schreibt Informationen auf die Karte (oder den Schlüssel), die üblicherweise vom seriellen Port stammen.
* ``void simple_mfrc522_write(byte section, String text)``: Schreibt einen Text in einen bestimmten Sektor. Bei ``section`` auf 0 werden die Sektoren 1-2 beschrieben; bei ``section`` auf 1 die Sektoren 3-4.
* ``void simple_mfrc522_write(byte section, byte* buffer)``: Schreibt Informationen in einen bestimmten Sektor, die üblicherweise vom seriellen Port stammen. Bei ``section`` auf 0 werden die Sektoren 1-2 beschrieben; bei ``section`` auf 1 die Sektoren 3-4.
* ``String simple_mfrc522_read()``: Liest die Informationen auf der Karte (oder dem Schlüssel) und gibt einen String zurück.
* ``String simple_mfrc522_read(byte section)``: Liest die Informationen in einem bestimmten Sektor und gibt einen String zurück. Bei ``section`` auf 0 werden die Sektoren 1-2 beschrieben; bei ``section`` auf 1 die Sektoren 3-4.

Im Beispiel ``6.5_rfid_write.ino`` wird die Funktion ``Serial.readBytesUntil()`` verwendet, eine gängige Methode für serielle Eingaben.

* `Serial.readBytesUntil <https://www.arduino.cc/reference/de/language/functions/communication/serial/readbytesuntil/>`_
