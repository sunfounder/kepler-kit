.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

FAQ
=========

Arduino
---------------------

#. Code-Upload in der Arduino IDE fehlgeschlagen?
    * Überprüfen Sie, ob Ihr Pico im Arduino IDE korrekt erkannt wird. Der Port sollte COMXX (Raspberry Pi Pico) sein. Für Anweisungen verweisen wir auf :ref:`setup_pico_arduino`.
    * Überprüfen Sie, ob das Board (Raspberry Pi Pico) und der Port (COMXX (Raspberry Pi Pico)) korrekt ausgewählt sind.
    * Wenn Ihr Code in Ordnung ist und Sie das richtige Board und den richtigen Port ausgewählt haben, der Upload jedoch immer noch nicht erfolgreich ist, klicken Sie erneut auf das **Upload**-Symbol. Wenn der Fortschrittsbalken "Upload..." anzeigt, trennen Sie das USB-Kabel und halten Sie die **BOOTSEL**-Taste gedrückt, während Sie es wieder einstecken. Der Code wird dann erfolgreich hochgeladen.

MicroPython
------------------

#. Wie öffne und führe ich den Code aus?
    Für detaillierte Anleitungen verweisen wir auf :ref:`open_run_code_py`.

#. Wie lade ich eine Bibliothek auf den Raspberry Pi Pico W hoch?
    Für detaillierte Anleitungen verweisen wir auf :ref:`add_libraries_py`.

#. Keine MicroPython (Raspberry Pi Pico W) Interpreter-Option in der Thonny IDE?
    * Stellen Sie sicher, dass Ihr Pico W über ein USB-Kabel an Ihren Computer angeschlossen ist.
    * Überprüfen Sie, ob Sie MicroPython für Pico W installiert haben (:ref:`install_micropython_on_pico`).
    * Der Raspberry Pi Pico W Interpreter ist nur in der Version 3.3.3 oder höher der Thonny IDE verfügbar. Wenn Sie eine ältere Version verwenden, aktualisieren Sie bitte (:ref:`thonny_ide`).
    * Wenn das Li-Po-Lademodul zu diesem Zeitpunkt auf dem Steckbrett eingesteckt ist, ziehen Sie es zuerst ab und stecken Sie den Pico W wieder in den Computer.

#. Kann den Pico W Code nicht öffnen oder Code über die Thonny IDE auf Pico W speichern?
    * Überprüfen Sie, ob Ihr Pico W über ein USB-Kabel an Ihren Computer angeschlossen ist.
    * Stellen Sie sicher, dass Sie den Interpreter als **MicroPython (Raspberry Pi Pico)** ausgewählt haben.

#. Kann der Raspberry Pi Pico W gleichzeitig in Thonny und Arduino verwendet werden?
    NEIN, dazu sind unterschiedliche Vorgänge erforderlich.

    * Wenn Sie es zuerst in der Arduino IDE verwendet haben und es nun in der Thonny IDE verwenden möchten, müssen Sie MicroPython darauf installieren (:ref:`install_micropython_on_pico`).
    * Wenn Sie es zuerst in der Thonny IDE verwendet haben und es nun in der Arduino IDE verwenden möchten, folgen Sie den Anweisungen unter :ref:`setup_pico_arduino`.

#. Ihr Computer ist Win7 und Pico W wird nicht erkannt.
    * Laden Sie den USB-CDC-Treiber von http://aem-origin.microchip.com/en-us/mindi-sw-library?swsearch=Atmel%2520USB%2520CDC%2520Virtual%2520COM%2520Driver herunter.
    * Entpacken Sie die Datei ``amtel_devices_cdc.inf`` in einen Ordner namens ``pico-serial``.
    * Ändern Sie den Namen der Datei ``amtel_devices_cdc.inf`` in ``pico-serial.inf``.
    * Öffnen/Bearbeiten Sie die ``pico-serial.inf`` in einem einfachen Editor wie dem Notepad.
    * Entfernen und ersetzen Sie die Zeilen unter den folgenden Überschriften:

    .. code-block::

        [DeviceList]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [DeviceList.NTAMD64]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [DeviceList.NTIA64]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [DeviceList.NT]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [Strings]
        Manufacturer = "ATMEL, Inc."
        PI_CDC_PICO = "Pi Pico Serial Port"
        Serial.SvcDesc = "Pi Pico Serial Driver"

    #. Schließen und speichern Sie die Datei, und behalten Sie den Namen ``pico-serial.inf`` bei.
    #. Gehen Sie zur Geräteliste Ihres PCs, finden Sie den Pico unter Ports, der beispielsweise als CDC-Gerät bezeichnet wird. Ein gelbes Ausrufezeichen weist darauf hin.
    #. Klicken Sie mit der rechten Maustaste auf das CDC-Gerät und aktualisieren oder installieren Sie den Treiber, indem Sie die von Ihnen erstellte Datei aus dem Speicherort auswählen, an dem Sie sie gespeichert haben.


Piper Make
------------------

#. Wie richte ich den Pico W in Piper Make ein?
    Für detaillierte Anleitungen verweisen wir auf :ref:`per_setup_pico`.

#. Wie lade ich Code herunter oder importiere ihn?
    Für detaillierte Anleitungen verweisen wir auf :ref:`per_save_import`.

#. Wie stelle ich eine Verbindung zu Pico W her?
    Für detaillierte Anleitungen verweisen wir auf :ref:`connect_pico_per`.


