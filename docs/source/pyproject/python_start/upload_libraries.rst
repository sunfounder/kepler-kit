.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _add_libraries_py:

1.4 Bibliotheken auf den Pico hochladen
=========================================

Für einige Projekte sind zusätzliche Bibliotheken erforderlich. In diesem Abschnitt wird erläutert, wie diese Bibliotheken zunächst auf den Raspberry Pi Pico W hochgeladen werden können, um später den Code direkt auszuführen.

#. Laden Sie den zugehörigen Code über den folgenden Link herunter.

   * :download:`SunFounder Kepler Kit <https://github.com/sunfounder/kepler-kit/archive/refs/heads/main.zip>`

#. Öffnen Sie die Thonny IDE und schließen Sie den Pico mit einem Mikro-USB-Kabel an Ihren Computer an. Klicken Sie dann in der unteren rechten Ecke auf den Interpreter "MicroPython (Raspberry Pi Pico).COMXX".

   .. image:: img/sec_inter.png

#. Navigieren Sie in der oberen Menüleiste zu **Ansicht** -> **Dateien**.

   .. image:: img/th_files.png

#. Wechseln Sie den Pfad zu dem Ordner, in dem Sie zuvor das `Code-Paket <https://github.com/sunfounder/kepler-kit/archive/refs/heads/main.zip>`_ heruntergeladen haben. Anschließend navigieren Sie zum Ordner ``kepler-kit-main/libs``.

   .. image:: img/th_path.png

#. Markieren Sie alle Dateien und Ordner im Verzeichnis ``libs/``, klicken Sie mit der rechten Maustaste und wählen Sie **Hochladen zu** aus. Der Upload kann einige Zeit dauern.

   .. image:: img/th_upload.png

#. Nun sollten Sie die gerade hochgeladenen Dateien auf Ihrem Laufwerk ``Raspberry Pi Pico`` sehen können.

   .. image:: img/th_done.png
