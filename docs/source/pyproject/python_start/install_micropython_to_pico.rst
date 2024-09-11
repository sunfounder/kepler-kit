.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _install_micropython_on_pico:

1.3 Installation von MicroPython auf Ihrem Pico
===================================================

Jetzt geht es darum, MicroPython auf dem Raspberry Pi Pico zu installieren. Die Thonny IDE ermöglicht Ihnen eine äußerst komfortable Installation mit nur einem Klick.

.. note::
    Falls Sie Thonny nicht aktualisieren möchten, können Sie die offizielle |link_micropython_pi| der Raspberry Pi Foundation nutzen, indem Sie eine ``rp2_pico_xxxx.uf2`` Datei per Drag-and-Drop auf den Raspberry Pi Pico ziehen.

#. Öffnen Sie die Thonny IDE.

    .. image:: img/set_pico1.png

#. Halten Sie die **BOOTSEL**-Taste gedrückt und schließen Sie den Pico über ein Micro-USB-Kabel an den Computer an. Lassen Sie die **BOOTSEL**-Taste los, sobald Ihr Pico als Massenspeichergerät mit dem Namen **RPI-RP2** erkannt wird.

    .. image:: img/bootsel_onboard.png

#. Klicken Sie in der unteren rechten Ecke auf die Schaltfläche zur Interpreter-Auswahl und wählen Sie **MicroPython installieren**.

    .. note::
        Falls diese Option in Ihrer Thonny-Version nicht verfügbar ist, aktualisieren Sie bitte auf die neueste Version.

    .. image:: img/set_pico2.png

#. Im Feld **Ziellaufwerk** erscheint automatisch das Laufwerk des gerade angeschlossenen Pico, und im Feld **MicroPython-Variante** wählen Sie **Raspberry Pi.Pico W/Pico WH**.

    .. image:: img/set_pico3.png

#. Klicken Sie auf die Schaltfläche **Installieren**, warten Sie, bis die Installation abgeschlossen ist, und schließen Sie dann diese Seite.

    .. image:: img/set_pico4.png

Herzlichen Glückwunsch, Ihr Raspberry Pi Pico ist jetzt einsatzbereit.

