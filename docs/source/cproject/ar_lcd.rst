.. _ar_lcd:

3.4 - Flüssigkristallanzeige
================================

Das LCD1602 ist ein Zeichen-Typ-Flüssigkristallanzeige, auf dem gleichzeitig 32 (16*2) Zeichen dargestellt werden können.

Wie allgemein bekannt ist, haben LCDs und andere Displays, obwohl sie die Mensch-Maschine-Interaktion erheblich bereichern, einen gemeinsamen Nachteil. Wenn sie an einen Controller angeschlossen sind, belegen sie mehrere I/O-Ports, was besonders problematisch ist, wenn der Controller nicht viele externe Ports hat. Dies schränkt auch andere Funktionen des Controllers ein. Um dieses Problem zu lösen, wurde das LCD1602 mit einem I2C-Bus entwickelt.

* :ref:`cpn_i2c_lcd`
* `Inter-Integrated Circuit - Wikipedia <https://de.wikipedia.org/wiki/I%C2%B2C>`_

|pin_i2c|

In diesem Projekt verwenden wir die I2C0-Schnittstelle, um das LCD1602 zu steuern und Text anzuzeigen.

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist definitiv praktisch, ein ganzes Kit zu kaufen. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - TEILE IN DIESEM KIT
        - KAUF-LINK
    *   - Kepler Kit
        - 450+
        - |link_kepler_kit|

Sie können die Teile auch separat über die folgenden Links erwerben.

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
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|

**Schaltplan**

|sch_lcd|

**Verkabelung**

|wiring_lcd|

**Code**

.. note::

    * Sie können die Datei ``3.4_liquid_crystal_display.ino`` im Pfad ``kepler-kit-main/arduino/3.4_liquid_crystal_display`` öffnen.
    * Oder kopieren Sie diesen Code in die **Arduino IDE**.
    * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den korrekten Port auszuwählen, bevor Sie auf die **Upload**-Taste klicken.
    * Die Bibliothek ``LiquidCrystal_I2C`` wird hier verwendet. Bitte lesen Sie :ref:`add_libraries_ar`, um sie der Arduino IDE hinzuzufügen.

.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/1f464967-5937-473a-8a0d-8e4577c85e7d/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Nach dem Start des Programms werden zwei Textzeilen nacheinander auf dem LCD angezeigt und dann wieder verschwinden.

.. note:: 
    Wenn der Code und die Verkabelung korrekt sind, aber das LCD trotzdem keinen Inhalt anzeigt, können Sie das Potentiometer auf der Rückseite drehen, um den Kontrast zu erhöhen.



**Wie funktioniert das?**

Durch den Aufruf der Bibliothek ``LiquidCrystal_I2C.h`` können Sie das LCD problemlos steuern.

.. code-block:: arduino

    #include "LiquidCrystal_I2C.h"

**Bibliotheksfunktionen**

.. code-block:: arduino

    LiquidCrystal_I2C(uint8_t lcd_Addr, uint8_t lcd_cols, uint8_t lcd_rows)

Erstellt eine neue Instanz der Klasse ``LiquidCrystal_I2C``, die ein bestimmtes, an Ihr Arduino-Board angeschlossenes LCD repräsentiert.

 **lcd_AddR**: Die Standardadresse des LCD beträgt 0x27.
 **lcd_cols**: Das LCD1602 hat 16 Spalten.
 **lcd_rows**: Das LCD1602 hat 2 Reihen.


.. code-block:: arduino

    void init()

Initialisiert das LCD.

.. code-block:: arduino

    void backlight()

Schaltet die (optionale) Hintergrundbeleuchtung ein.

.. code-block:: arduino

    void nobacklight()

Schaltet die (optionale) Hintergrundbeleuchtung aus.

.. code-block:: arduino

    void display()

Schaltet die LCD-Anzeige ein.

.. code-block:: arduino

    void nodisplay()

Schaltet die LCD-Anzeige schnell aus.

.. code-block:: arduino

    void clear()

Löscht die Anzeige und setzt die Cursorposition zurück.

.. code-block:: arduino

    void setCursor(uint8_t col, uint8_t row)

Setzt den Cursor auf die Position col,row.

.. code-block:: arduino

    void print(data, BASE)

Gibt den Text auf dem LCD aus.

**data**: Die auszugebende Daten (char, byte, int, long oder String).

**BASE (optional)**: Die Basis, in der Zahlen ausgegeben werden: BIN für Binär (Basis 2), DEC für Dezimal (Basis 10), OCT für Oktal (Basis 8), HEX für Hexadezimal (Basis 16).



**Weitere Informationen**

Laden Sie den Code auf das Pico W. Die im seriellen Monitor eingegebenen Inhalte werden auf dem LCD angezeigt.

.. note::

   * Sie finden die Datei ``3.4_liquid_crystal_display_2.ino`` im Verzeichnis ``kepler-kit-main/arduino/3.4_liquid_crystal_display_2``.
   * Oder kopieren Sie diesen Code direkt in die **Arduino IDE**.
   
   * Vergessen Sie nicht, das richtige Board (Raspberry Pi Pico) und den korrekten Port auszuwählen, bevor Sie auf **Hochladen** klicken.

.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/631e0380-d594-4a8b-9bac-eb0688079b97/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Zusätzlich zur Datenerfassung von elektronischen Komponenten kann das Pico W auch Daten aus dem seriellen Monitor lesen. Dazu können Sie ``Serial.read()`` als Steuerelement des Schaltungsexperiments verwenden.

Starten Sie die serielle Kommunikation in ``setup()`` und setzen Sie die Datenrate auf 9600.

.. code-block:: arduino

    Serial.begin(9600);

Der Zustand des seriellen Monitors wird in ``loop()`` überprüft. Die Datenverarbeitung erfolgt nur, wenn Daten empfangen werden.

.. code-block:: arduino

    if (Serial.available() > 0){}

Leeren Sie den Bildschirm.

.. code-block:: arduino

    lcd.clear();

Liest den Eingabewert im seriellen Monitor und speichert ihn in der Variable incomingByte.

.. code-block:: arduino

    char incomingByte = Serial.read();

Zeigt jeden eingegebenen Buchstaben auf dem LCD an und überspringt das Zeilenumbruchzeichen.

.. code-block:: arduino

    while (Serial.available() > 0) {
        char incomingByte=Serial.read();
        if(incomingByte==10){break;}// skip the line-feed character
        lcd.print(incomingByte);// display each character to the LCD  
    } 

* `Serial Read <https://www.arduino.cc/reference/de/language/functions/communication/serial/read/>`_

