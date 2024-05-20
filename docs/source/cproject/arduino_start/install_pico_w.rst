.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _setup_pico_arduino:

1.3 Raspberry Pi Pico W einrichten (Wichtig)
==================================================

1. UF2-Firmware installieren
---------------------------------

Wenn Sie den Raspberry Pi Pico W zum ersten Mal anschließen oder währenddessen die BOOTSEL-Taste gedrückt halten, erscheint das Gerät als Laufwerk, dem jedoch kein COM-Port zugewiesen ist. Dies verhindert das Hochladen von Code.

Um dieses Problem zu beheben, müssen Sie die UF2-Firmware installieren. Diese Firmware ist sowohl mit MicroPython als auch mit der Arduino IDE kompatibel.

1. Laden Sie die UF2-Firmware über den folgenden Link herunter.

    * :download:`Raspberry Pi Pico W UF2-Firmware <https://micropython.org/download/rp2-pico-w/rp2-pico-w-latest.uf2>`

2. Verbinden Sie Ihren Raspberry Pi Pico W über ein Micro-USB-Kabel mit Ihrem Computer. Ihr Pico W wird als Massenspeichergerät mit dem Namen **RPI-RP2** eingebunden.

    .. image:: img/install_pico_plugin.png

3. Ziehen Sie die heruntergeladene UF2-Firmware in das Laufwerk **RPI-RP2**.

    .. image:: img/install_pico_uf2.png

4. Nach diesem Vorgang verschwindet das Laufwerk **RPI-RP2**, und Sie können mit den nächsten Schritten fortfahren.

2. Das Board-Paket installieren
--------------------------------------

Um den Raspberry Pi Pico W zu programmieren, müssen Sie das entsprechende Paket in der Arduino IDE installieren. Hier ist eine Schritt-für-Schritt-Anleitung:

1. Im **Boards Manager**-Fenster suchen Sie nach **pico**. Klicken Sie auf die Schaltfläche **Installieren**, um die Installation zu starten. Damit installieren Sie das **Arduino Mbed OS RP2040 Boards**-Paket, das die Unterstützung für den Raspberry Pi Pico W enthält.

    .. image:: img/install_pico.png

2. Während des Vorgangs erscheinen einige Popup-Aufforderungen zur Installation spezifischer Gerätetreiber. Wählen Sie **"Installieren"**.

    .. image:: img/install_pico_sa.png

3. Anschließend erscheint eine Benachrichtigung, die den erfolgreichen Abschluss der Installation bestätigt.

3. Auswahl von Board und Port
------------------------------------------

1. Um das passende Board auszuwählen, navigieren Sie zu **Werkzeuge** -> **Board** -> **Arduino Mbed OS RP2040 Boards** -> **Raspberry Pi Pico**.

    .. image:: img/install_pico_tool_board.png

2. Falls Ihr Raspberry Pi Pico W am Computer angeschlossen ist, stellen Sie den richtigen Port ein, indem Sie zu **Werkzeuge** -> **Port** navigieren.

    .. image:: img/install_pico_tool_port.png

3. Arduino 2.0 bietet eine neue Schnellauswahl-Funktion. Für den Raspberry Pi Pico W, der normalerweise nicht automatisch erkannt wird, klicken Sie auf **Andere Boards und Ports auswählen**.

    .. image:: img/install_pico_select.png

4. Geben Sie **Raspberry Pi Pico** in die Suchleiste ein, wählen Sie es aus, wenn es erscheint, wählen Sie den entsprechenden Port und klicken Sie auf **OK**.

    .. image:: img/install_pico_board.png

5. Später können Sie es über dieses Schnellzugriffsfenster einfach erneut auswählen.

    .. image:: img/install_pico_quick.png

6. Mit einer dieser Methoden können Sie das korrekte Board und den Port einstellen. Nun können Sie Code auf den Raspberry Pi Pico W hochladen.

4. Code hochladen
--------------------------

Jetzt gehen wir darauf ein, wie Sie Code auf Ihren Raspberry Pi Pico W hochladen können.

1. Öffnen Sie eine beliebige ``.ino``-Datei oder verwenden Sie den aktuell angezeigten leeren Sketch. Klicken Sie dann auf die Schaltfläche **Hochladen**.

    .. image:: img/install_pico_upload.png

2. Warten Sie, bis die Hochlademeldung erscheint, wie unten gezeigt.

    .. image:: img/install_pico_upload_dot.png

3. Halten Sie die **BOOTSEL**-Taste gedrückt, ziehen Sie Ihren Raspberry Pi Pico W kurz ab und stecken Sie ihn wieder ein.

    .. image:: img/led_onboard.png 

    .. note::
        
        * Dieser Schritt ist entscheidend, insbesondere für Erstnutzer der Arduino IDE. Wenn Sie diesen Schritt überspringen, wird das Hochladen fehlschlagen.

        * Sobald der Code erfolgreich hochgeladen wurde, wird Ihr Pico W vom Computer erkannt. Für die zukünftige Nutzung stecken Sie ihn einfach an den Computer.

4. Ein Hinweis auf den erfolgreichen Upload wird angezeigt.

    .. image:: img/install_pico_upload_done.png

