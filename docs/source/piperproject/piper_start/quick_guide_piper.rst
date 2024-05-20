.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _quick_guide_piper:

1.2 Schnellstartanleitung für Piper Make
=========================================

1. Neues Projekt erstellen
---------------------------

Nachdem Sie Pico W eingerichtet haben, ist es an der Zeit, die Programmierung zu erlernen. 
Lassen Sie uns nun die integrierte LED einschalten.

Wechseln Sie in den ``KREATIVMODUS`` und klicken Sie auf die Schaltfläche **Neues Projekt**. 
Ein neues Projekt wird im Abschnitt **MEINE PROJEKTE** angezeigt und 
erhält einen zufälligen Namen, den Sie von der Programmierseite aus ändern können.

|media9-s|

Öffnen Sie dann das neu erstellte Projekt.

|media11-s|

Navigieren Sie zur Programmierseite von Piper Make.

|piper_intro1|

* **START**: Dient zum Ausführen des Codes. Ist es grau, besteht keine Verbindung zu Pico W.
* **Blockpalette**: Enthält verschiedene Arten von Blöcken.
* **VERBINDEN**: Dient zum Herstellen einer Verbindung zu Pico W. Wenn nicht verbunden, ist es grün; nach der Verbindung wird es zu **TRENNEN (rot)**.
* **Programmierbereich**: Ziehen Sie die Blöcke hierher, um die Programmierung abzuschließen.
* **Werkzeugbereich**: Klicken Sie auf **DIGITALANSICHT**, um die Pin-Belegung von Pico W zu sehen; Sie können die Druckinformationen im **KONSOLE** einsehen; Daten können aus **DATEN** gelesen werden, und Sie können auf **Python** klicken, um den Python-Quellcode anzuzeigen.
* **Projektname und -beschreibung**: Sie können den Projektnamen und die Beschreibung ändern.
* **HERUNTERLADEN**: Sie können auf die Schaltfläche **HERUNTERLADEN** klicken, um sie lokal zu speichern, normalerweise im **|**-Format. Das nächste Mal können Sie es über die Schaltfläche **Projekt importieren** auf der Startseite importieren.

Klicken Sie auf die **Chip**-Palette und ziehen Sie den [Start]-Block in den **Programmierbereich**.

|media12|

Ziehen Sie dann den [Schleife]-Block aus der **Schleifen**-Palette an das untere Ende des [Start]-Blocks und stellen Sie das Schleifenintervall auf 1 Sekunde ein.

|media14|

Die integrierte LED des Raspberry Pi Pico befindet sich am Pin25. Daher verwenden wir den Block [Pin () EIN/AUS] aus der **Chip**-Palette zur Steuerung.

|media15|

.. _connect_pico_per:

2. Verbindung zu Pico W herstellen
------------------------------------

Klicken Sie nun auf die Schaltfläche **VERBINDEN**, um eine Verbindung zu Pico W herzustellen. Nach dem Klick erscheint ein neues Popup-Fenster.

|media16|

Wählen Sie den erkannten **CircuitPython CDC-Steueranschluss (COMXX)** aus und klicken Sie dann auf **Verbinden**.

|pico_port|

Bei erfolgreicher Verbindung ändert sich das grüne **VERBINDEN** in der unteren linken Ecke in ein rotes **TRENNEN**.

|disconnect_per|

3. Code ausführen
-------------------

Klicken Sie jetzt auf die Schaltfläche **START**, um diesen Code auszuführen, und Sie werden sehen, dass die LED am Pico W leuchtet. Ist die Schaltfläche bei Ihnen grau, bedeutet dies, dass keine Verbindung zu Pico W besteht. Bitte stellen Sie die Verbindung erneut her.

|media166|

Schalten Sie dann den Pin25 jede Sekunde in der Schleife aus und klicken Sie erneut oben links auf **START**, damit Sie sehen können, wie die integrierte LED blinkt.

|media17|

