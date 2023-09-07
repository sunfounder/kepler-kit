.. _py_lcd:

3.4 Flüssigkristallanzeige
===============================

LCD1602 ist eine Zeichen-Flüssigkristallanzeige, die gleichzeitig 32 (16*2) Zeichen anzeigen kann.

Wie wir alle wissen, haben LCDs und andere Displays, obwohl sie die Mensch-Maschine-Interaktion erheblich bereichern, 
eine gemeinsame Schwachstelle. Wenn sie an einen Controller angeschlossen sind, 
werden mehrere IOs des Controllers belegt, der nicht so viele externe Anschlüsse hat. 
Das schränkt auch andere Funktionen des Controllers ein. 
Deshalb wurde LCD1602 mit einem I2C-Bus entwickelt, um dieses Problem zu lösen.

* :ref:`cpn_i2c_lcd`
* `Inter-Integrated Circuit - Wikipedia <https://de.wikipedia.org/wiki/I%C2%B2C>`_

|pin_i2c|

Hier verwenden wir die I2C0-Schnittstelle, um den LCD1602 zu steuern und Text anzuzeigen.

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten. 

Es ist definitiv praktisch, ein ganzes Kit zu kaufen, hier ist der Link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ARTIKEL IN DIESEM KIT
        - LINK
    *   - Kepler Kit	
        - 450+
        - |link_kepler_kit|

Sie können diese auch separat über die untenstehenden Links kaufen.

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
        - Micro USB Kabel
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

    * Öffnen Sie die Datei ``3.4_liquid_crystal_display.py`` im Pfad ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny, dann klicken Sie auf "Aktuelles Skript ausführen" oder drücken einfach F5.

    * Vergessen Sie nicht, den "MicroPython (Raspberry Pi Pico)"-Interpreter in der unteren rechten Ecke auszuwählen. 

    * Für detaillierte Anleitungen siehe :ref:`open_run_code_py`. 

    * Hier benötigen Sie die Bibliothek ``lcd1602.py``. Bitte überprüfen Sie, ob sie auf Pico W hochgeladen wurde. Eine detaillierte Anleitung finden Sie unter :ref:`add_libraries_py`.

.. code-block:: python

    from lcd1602 import LCD
    import utime

    lcd = LCD()
    string = " Hallo!\n"
    lcd.message(string)
    utime.sleep(2)
    string = "    Sunfounder!"   
    lcd.message(string)
    utime.sleep(2)
    lcd.clear()   

Nachdem das Programm ausgeführt wurde, erscheinen nacheinander zwei Textzeilen auf dem LCD und verschwinden dann wieder.

.. note:: Wenn der Code läuft und der Bildschirm leer bleibt, können Sie das Potentiometer auf der Rückseite drehen, um den Kontrast zu erhöhen.

**Wie funktioniert das?**

In der lcd1602-Bibliothek integrieren wir die relevanten Funktionen von lcd1602 in die LCD-Klasse.

Importieren der lcd1602-Bibliothek

.. code-block:: python

    from lcd1602 import LCD    

Deklarieren eines Objekts der LCD-Klasse und nennen es lcd.

.. code-block:: python

    lcd = LCD()

Mit dieser Anweisung wird der Text auf dem LCD angezeigt. Es sollte beachtet werden, dass das Argument ein String sein muss. Wenn wir eine Ganzzahl oder Fließkommazahl übergeben wollen, müssen wir die Umwandlungsanweisung ``str()`` verwenden.

.. code-block:: python

    lcd.message(string)

Wenn Sie diese Anweisung mehrmals aufrufen, überlagert lcd die Texte. Dafür muss die folgende Anweisung verwendet werden, um die Anzeige zu löschen.

.. code-block:: python

    lcd.clear()

