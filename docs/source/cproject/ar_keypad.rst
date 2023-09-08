.. _ar_keypad:

4.2 - 4x4 Tastenfeld
=======================

Das 4x4-Tastenfeld, auch als Matrix-Tastenfeld bekannt, besteht aus einer Matrix von 16 Tasten, die in einer einzigen Bedienoberfläche integriert sind.

Solche Tastenfelder findet man vor allem bei Geräten, die digitale Eingaben erfordern, wie zum Beispiel Taschenrechner, Fernbedienungen, Tastentelefone, Verkaufsautomaten, Geldautomaten, Zahlenschlösser und elektronische Türschlösser.

In diesem Projekt lernen wir, wie man ermittelt, welche Taste gedrückt wurde und den entsprechenden Tastenwert erhält.

* :ref:`cpn_keypad`
* `E.161 - Wikipedia <https://de.wikipedia.org/wiki/E.161>`_

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Bauteile.

Es ist natürlich praktisch, ein komplettes Set zu kaufen. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ARTIKEL IN DIESEM SET
        - KAUF-LINK
    *   - Kepler Kit	
        - 450+
        - |link_kepler_kit|

Die Teile können aber auch einzeln über die untenstehenden Links gekauft werden.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTENÜBERSICHT	
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
        - 4(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_keypad`
        - 1
        - |link_keypad_buy|

**Schaltplan**

|sch_keypad|

Vier Pull-down-Widerstände sind mit den jeweiligen Spalten des Matrix-Tastenfelds verbunden, damit G6 ~ G9 einen stabilen niedrigen Pegel erhalten, wenn keine Taste gedrückt ist.

Die Reihen des Tastenfelds (G2 ~ G5) sind so programmiert, dass sie einen hohen Pegel haben. Wird einer der Anschlüsse G6 ~ G9 als hoch gelesen, wissen wir, welche Taste gedrückt wurde.

Zum Beispiel wird bei einem hohen Signal auf G6 die Taste mit der Nummer 1 gedrückt; dies ist darauf zurückzuführen, dass die Steuerpins dieser Taste G2 und G6 sind. Wenn die Taste gedrückt wird, werden G2 und G6 miteinander verbunden und G6 ist ebenfalls hoch.

**Verdrahtung**

|wiring_keypad|

Um die Verdrahtung zu vereinfachen, sind im obigen Schema die Spalte und die Reihe des Matrix-Tastenfelds sowie die 10K-Widerstände gleichzeitig in die Löcher eingesteckt, in denen sich G6 ~ G9 befinden.

**Code**

.. note::

    * Die Datei ``4.2_4x4_keypad.ino`` finden Sie im Verzeichnis ``kepler-kit-main/arduino/4.2_4x4_keypad``.
    * Oder kopieren Sie diesen Code in die **Arduino IDE**.
    * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den korrekten Port auszuwählen, bevor Sie auf die Schaltfläche **Hochladen** klicken.
    * Die Bibliothek ``Keypad`` wird hier verwendet. Bitte beachten Sie :ref:`add_libraries_ar` für weitere Informationen zur Integration in die Arduino IDE.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/6c776dfc-cb74-49d7-8906-f1382e0e7b7b/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Nach dem Ausführen des Programms wird die Shell die Tasten ausgeben, die Sie auf dem Tastenfeld gedrückt haben.

**Funktionsweise**

Mithilfe der Bibliothek ``Keypad.h`` können Sie das Tastenfeld einfach nutzen.

.. code-block:: arduino

    #include <Keypad.h>

Bibliotheksfunktionen:

.. code-block:: arduino

    Keypad(char *userKeymap, byte *row, byte *col, byte numRows, byte numCols)

Initialisiert die interne Tastenbelegung entsprechend ``userKeymap``.

``userKeymap``: Die Symbole auf den Tasten des Tastenfelds.

``row``, ``col``: Pin-Konfiguration.

``numRows``, ``numCols``: Größe des Tastenfelds.

.. code-block:: arduino

    char getKey()

Gibt die gedrückte Taste zurück, falls vorhanden. Diese Funktion ist nicht blockierend.
