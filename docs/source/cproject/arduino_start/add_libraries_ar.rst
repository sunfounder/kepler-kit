1.4 Bibliotheken installieren (Wichtig)
===========================================

**Code herunterladen**

Laden Sie den relevanten Code über den untenstehenden Link herunter.

* :download:`SunFounder Kepler Kit Beispiel <https://github.com/sunfounder/kepler-kit/archive/refs/heads/main.zip>`

* Oder schauen Sie sich den Code auf `Kepler Kit - GitHub <https://github.com/sunfounder/kepler-kit>`_ an.

.. _add_libraries_ar:

Bibliotheken hinzufügen
--------------------------
Eine Bibliothek, die einige Funktionsdefinitionen und Header-Dateien zusammenfasst, enthält normalerweise zwei Dateien: .h (Header-Datei, inklusive Funktionsdeklaration, Makrodefinition, Konstruktordefinition usw.) und .cpp (Ausführungsdatei, mit Funktionsimplementierung, Variablendefinition etc.). Wenn Sie eine Funktion aus einer solchen Bibliothek nutzen möchten, müssen Sie lediglich die entsprechende Header-Datei einfügen (z.B. #include <dht.h>) und dann die Funktion aufrufen. Dies macht Ihren Code kompakter. Falls Sie die Bibliothek nicht verwenden möchten, können Sie die Funktionsdefinition auch direkt im Code hinterlegen. Dies führt jedoch zu einem längeren und weniger übersichtlichen Code.

Einige Bibliotheken sind bereits in der Arduino IDE integriert, während andere erst hinzugefügt werden müssen. Sehen wir uns nun an, wie das funktioniert.

#. Öffnen Sie die Arduino IDE und navigieren Sie zu **Skizze** -> **Bibliothek einbinden** -> **.ZIP-Bibliothek hinzufügen**.

   .. image:: img/a2dp_add_zip.png

#. Navigieren Sie zu dem Verzeichnis, in dem sich die Bibliotheksdateien befinden, etwa dem Ordner ``kepler-kit-main\arduino\libraries``, und wählen Sie die gewünschte Bibliotheksdatei aus, wie z.B. ``LiquidCrystal_I2C.zip``. Klicken Sie dann auf **Öffnen**.

   .. image:: img/a2dp_choose.png

#. Nach kurzer Zeit erhalten Sie eine Benachrichtigung, die eine erfolgreiche Installation bestätigt.

   .. image:: img/a2dp_success.png

#. Wiederholen Sie diesen Vorgang, um weitere Bibliotheken hinzuzufügen.


.. note::

   Die installierten Bibliotheken finden Sie im Standardbibliotheksverzeichnis der Arduino IDE, das normalerweise unter ``C:\Users\xxx\Documents\Arduino\libraries`` zu finden ist.

   Falls Ihr Bibliotheksverzeichnis abweicht, können Sie dieses überprüfen, indem Sie zu **Datei** -> **Einstellungen** navigieren.

      .. image:: img/install_lib1.png

