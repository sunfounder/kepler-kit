.. _install_arduino:

1.1 Arduino IDE installieren (Wichtig)
==========================================

Die Arduino-IDE, bekannt als Arduino Integrated Development Environment, bietet die gesamte notwendige Softwareunterstützung für die Fertigstellung eines Arduino-Projekts. Es handelt sich um eine speziell für Arduino entwickelte Programmiersoftware, die vom Arduino-Team bereitgestellt wird und das Schreiben von Programmen sowie deren Upload auf das Arduino-Board ermöglicht.

Die Arduino IDE 2.0 ist ein Open-Source-Projekt und stellt einen großen Fortschritt gegenüber ihrem robusten Vorgänger, der Arduino IDE 1.x, dar. Sie kommt mit einer überarbeiteten Benutzeroberfläche, einem verbesserten Board- und Bibliotheksmanager, einem Debugger, einer Autocomplete-Funktion und vielem mehr.

In diesem Tutorial zeigen wir, wie Sie die Arduino IDE 2.0 auf Ihrem Windows-, Mac- oder Linux-Computer herunterladen und installieren können.

Voraussetzungen
-------------------

* Windows - Win 10 oder neuer, 64-Bit
* Linux - 64-Bit
* Mac OS X - Version 10.14 "Mojave" oder neuer, 64-Bit

Arduino IDE 2.0 herunterladen
-------------------------------

#. Besuchen Sie die |link_download_arduino|-Seite.

#. Laden Sie die IDE für Ihre Betriebssystemversion herunter.

    .. image:: img/sp_001.png

Installation
------------------------------

Windows
^^^^^^^^^^^^^

#. Doppelklicken Sie auf die Datei ``arduino-ide_xxxx.exe``, um die heruntergeladene Datei auszuführen.

#. Lesen Sie die Lizenzvereinbarung und stimmen Sie dieser zu.

    .. image:: img/sp_002.png

#. Wählen Sie die Installationsoptionen aus.

    .. image:: img/sp_003.png

#. Wählen Sie den Installationsort. Es wird empfohlen, die Software auf einem anderen Laufwerk als dem Systemlaufwerk zu installieren.

    .. image:: img/sp_004.png

#. Abschließend klicken Sie auf "Fertigstellen".

    .. image:: img/sp_005.png

macOS
^^^^^^^^^^^^^^^^

Doppelklicken Sie auf die heruntergeladene Datei ``arduino_ide_xxxx.dmg`` und folgen Sie den Anweisungen, um die **Arduino IDE.app** in den **Anwendungen**-Ordner zu kopieren. Nach wenigen Sekunden sollte die Arduino IDE erfolgreich installiert sein.

.. image:: img/macos_install_ide.png
    :width: 800

Linux
^^^^^^^^^^^^

Für das Tutorial zur Installation der Arduino IDE 2.0 unter Linux verweisen wir auf: https://docs.arduino.cc/software/ide-v2/tutorials/getting-started/ide-v2-downloading-and-installing#linux

IDE öffnen
--------------

#. Wenn Sie die Arduino IDE 2.0 zum ersten Mal öffnen, werden automatisch die Arduino AVR Boards, integrierte Bibliotheken und weitere erforderliche Dateien installiert.

    .. image:: img/sp_901.png

#. Zudem könnte Ihre Firewall oder Ihr Sicherheitszentrum einige Male nachfragen, ob Sie bestimmte Gerätetreiber installieren möchten. Bitte installieren Sie alle davon.

    .. image:: img/sp_104.png

#. Nun ist Ihre Arduino IDE einsatzbereit!

    .. note::
        Falls einige Installationen aufgrund von Netzwerkproblemen oder aus anderen Gründen nicht funktioniert haben sollten, können Sie die Arduino IDE erneut öffnen, und der Rest der Installation wird abgeschlossen. Das Ausgabefenster wird erst dann automatisch geöffnet, wenn alle Installationen abgeschlossen sind und Sie auf "Überprüfen" oder "Hochladen" klicken.
