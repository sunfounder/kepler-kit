.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

1.5 Schnelle Einführung in Thonny
====================================

.. _open_run_code_py:

Code direkt öffnen und ausführen
------------------------------------------------

Der Codeabschnitt in den Projekten informiert Sie genau darüber, welcher Code verwendet wird. Doppelklicken Sie daher auf die ``.py``-Datei mit der Seriennummer im Pfad ``kepler-kit-main/micropython/``, um sie zu öffnen.

Vorher müssen Sie jedoch das Paket herunterladen und die Bibliothek hochladen, wie in :ref:`add_libraries_py` beschrieben.

#. Code öffnen.

   Zum Beispiel ``2.1_hello_led.py``.

   Wenn Sie darauf doppelklicken, öffnet sich ein neues Fenster rechts. Sie können gleichzeitig mehrere Codes öffnen.

   |open_code|

#. Richtigen Interpreter auswählen

   Verbinden Sie den Pico W mit einem Mikro-USB-Kabel mit Ihrem Computer und wählen Sie den Interpreter "MicroPython (Raspberry Pi Pico)" aus.

   |sec_inter|

#. Code ausführen

   Um das Skript auszuführen, klicken Sie auf die Schaltfläche **Aktuelles Skript ausführen** oder drücken Sie F5.

   |run_it|

   Falls der Code Informationen enthält, die ausgegeben werden müssen, erscheinen diese in der Shell; ansonsten erscheint nur die folgende Information.

   Klicken Sie auf **Ansicht** -> **Bearbeiten**, um das Shell-Fenster zu öffnen, falls es in Ihrem Thonny nicht angezeigt wird.

       .. code-block::

           MicroPython vx.xx on xxxx-xx-xx; Raspberry Pi Pico W mit RP2040

           Geben Sie "help()" für weitere Informationen ein.
           >>> %Run -c $EDITOR_CONTENT

   * Die erste Zeile zeigt die Version von MicroPython, das Datum und Informationen zu Ihrem Gerät.
   * Die zweite Zeile fordert Sie auf, "help()" einzugeben, um Hilfe zu erhalten.
   * Die dritte Zeile ist ein Befehl von Thonny, der dem MicroPython-Interpreter auf Ihrem Pico W sagt, den Inhalt des Skriptbereichs - "EDITOR_CONTENT" - auszuführen.
   * Falls nach der dritten Zeile eine Nachricht erscheint, handelt es sich normalerweise um eine Ausgabe, die Sie in MicroPython drucken lassen, oder um eine Fehlermeldung des Codes.

#. Ausführung stoppen

   |stop_it|

   Um den laufenden Code zu stoppen, klicken Sie auf die Schaltfläche **Stop/Backend neu starten**. Der Befehl **%RUN -c $EDITOR_CONTENT** verschwindet nach dem Anhalten.

#. Speichern oder Speichern unter

   Änderungen am geöffneten Beispiel können durch Drücken von **Strg+S** oder durch Klicken auf die Schaltfläche **Speichern** in Thonny gespeichert werden.

   Der Code kann als separate Datei innerhalb des Laufwerks Raspberry Pi Pico W gespeichert werden, indem Sie auf **Datei** -> **Speichern unter** klicken.

   |save_as|

   Wählen Sie **Raspberry Pi Pico** aus.

   |sec_pico|

   Klicken Sie nach Eingabe des Dateinamens und der Erweiterung **.py** auf **OK**. Auf dem Laufwerk des Raspberry Pi Pico W sehen Sie dann Ihre gespeicherte Datei.

   |sec_name|

   .. note::
       Unabhängig davon, welchen Namen Sie Ihrem Code geben, ist es ratsam, die Art des Codes zu beschreiben, anstatt ihm einen bedeutungslosen Namen wie ``abc.py`` zu geben.
       Wenn Sie den Code als ``main.py`` speichern, wird er automatisch ausgeführt, sobald die Stromversorgung eingeschaltet ist.


Datei erstellen und ausführen
-------------------------------

Der Code wird direkt im Codebereich angezeigt. Sie können ihn in Thonny kopieren und wie folgt ausführen.

#. Neue Datei erstellen

   Öffnen Sie die Thonny IDE und klicken Sie auf die Schaltfläche **Neu**, um eine neue leere Datei zu erstellen.

   |new_file|

#. Code kopieren

   Kopieren Sie den Code aus dem Projekt in die Thonny IDE.

   |copy_file|

#. Richtigen Interpreter auswählen

   Schließen Sie den Pico W mit einem Mikro-USB-Kabel an Ihren Computer an und wählen Sie im unteren rechten Eck den Interpreter "MicroPython (Raspberry Pi Pico)" aus.

   |sec_inter|

#. Code ausführen und speichern

   Klicken Sie auf **Aktuelles Skript ausführen** oder drücken Sie einfach F5, um den Code auszuführen. Falls Ihr Code noch nicht gespeichert ist, erscheint ein Fenster, in dem Sie wählen können, ob Sie ihn auf **diesem Computer** oder dem **Raspberry Pi Pico** speichern möchten.

   |where_save|

   .. note::
       Thonny speichert Ihr Programm auf dem Raspberry Pi Pico, wenn Sie dies anweisen. Wenn Sie den Pico W abziehen und an einen anderen Computer anschließen, bleibt Ihr Programm erhalten.

   Klicken Sie nach der Auswahl des Speicherorts und der Benennung der Datei sowie der Hinzufügung der Erweiterung **.py** auf OK.

   |sec_name|

   .. note::
       Unabhängig vom Namen, den Sie Ihrem Code geben, ist es am besten, seine Art zu beschreiben und ihm keinen sinnlosen Namen wie ``abc.py`` zu geben.
       Wenn Sie den Code als ``main.py`` speichern, wird er automatisch ausgeführt, sobald die Stromversorgung eingeschaltet ist.

   Sobald Ihr Programm gespeichert ist, wird es automatisch ausgeführt und die folgenden Informationen werden im Shell-Bereich angezeigt.

   Klicken Sie auf **Ansicht** -> **Bearbeiten**, um das Shell-Fenster zu öffnen, falls es in Ihrem Thonny nicht angezeigt wird.

   .. code-block::

       MicroPython vx.xx.x on xxxx-xx-xx; Raspberry Pi Pico W mit RP2040

       Geben Sie "help()" für weitere Informationen ein.
       >>> %Run -c $EDITOR_CONTENT

   * Die erste Zeile zeigt die Version von MicroPython, das Datum und Informationen zu Ihrem Gerät.
   * Die zweite Zeile fordert Sie auf, "help()" einzugeben, um Hilfe zu erhalten.
   * Die dritte Zeile ist ein Befehl von Thonny, der dem MicroPython-Interpreter auf Ihrem Pico W sagt, den Inhalt des Skriptbereichs - "EDITOR_CONTENT" - auszuführen.
   * Falls nach der dritten Zeile eine Nachricht erscheint, handelt es sich normalerweise um eine Ausgabe, die Sie in MicroPython drucken lassen, oder um eine Fehlermeldung des Codes.

#. Ausführung stoppen

   |stop_it|

   Um den laufenden Code zu stoppen, klicken Sie auf die Schaltfläche **Stop/Backend neu starten**. Der Befehl **%Run -c $EDITOR_CONTENT** verschwindet nach dem Stoppen.

#. Datei öffnen

   Es gibt zwei Möglichkeiten, eine gespeicherte Code-Datei zu öffnen.

   * Die erste Möglichkeit besteht darin, auf das Öffnen-Symbol in der Thonny-Symbolleiste zu klicken. Genau wie beim Speichern eines Programms werden Sie gefragt, ob Sie es von **diesem Computer** oder dem **Raspberry Pi Pico** öffnen möchten. Wählen Sie beispielsweise **Raspberry Pi Pico**, erscheint eine Liste aller Programme, die Sie auf dem Pico W gespeichert haben.
   * Die zweite Möglichkeit besteht darin, die Dateivorschau direkt zu öffnen, indem Sie auf **Ansicht**-> **Datei**-> klicken und dann die entsprechende ``.py``-Datei doppelklicken, um sie zu öffnen.
