.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

1.1 Einführung in MicroPython
======================================

MicroPython ist eine in C geschriebene Software-Implementierung einer Programmiersprache, die weitgehend mit Python 3 kompatibel ist und für den Betrieb auf Mikrocontrollern optimiert wurde.

MicroPython besteht aus einem Python-Compiler für Bytecode und einem Laufzeitinterpreter dieses Bytecodes. Dem Benutzer wird eine interaktive Eingabeaufforderung (die REPL) zur Verfügung gestellt, über die sofort unterstützte Befehle ausgeführt werden können. Darüber hinaus sind ausgewählte Python-Basisbibliotheken enthalten. MicroPython bietet Module, die dem Programmierer Zugang zur Low-Level-Hardware ermöglichen.

* Referenz: `MicroPython - Wikipedia <https://de.wikipedia.org/wiki/MicroPython>`_

Die Geschichte beginnt hier
--------------------------------

Die Dinge änderten sich 2013, als Damien George eine Crowdfunding-Kampagne (Kickstarter) startete.

Damien war ein Student der Universität Cambridge und ein begeisterter Roboterprogrammierer. Er wollte die Welt von Python von einer Gigabyte-Maschine auf einen Kilobyte verkleinern. Seine Kickstarter-Kampagne sollte seine Entwicklungsarbeit unterstützen, während er seinen Prototyp in eine fertige Implementierung verwandelte.

MicroPython wird von einer vielfältigen Pythonista-Gemeinschaft unterstützt, die ein großes Interesse am Erfolg des Projekts hat.

Neben dem Testen und Unterstützen des Codebasis stellten die Entwickler Tutorials, Codebibliotheken und Hardware-Portierungen bereit, sodass Damien sich auf andere Aspekte des Projekts konzentrieren konnte.

* Referenz: `realpython <https://realpython.com/micropython/>`_

Warum MicroPython?
------------------

Obwohl die ursprüngliche Kickstarter-Kampagne MicroPython als Entwicklungsboard "pyboard" mit STM32F4 herausbrachte, unterstützt MicroPython viele ARM-basierte Produktarchitekturen. Zu den hauptsächlich unterstützten Ports gehören ARM Cortex-M (viele STM32-Boards, TI CC3200/WiPy, Teensy-Boards, Nordic nRF-Serie, SAMD21 und SAMD51), ESP8266, ESP32, 16-Bit-PIC, Unix, Windows, Zephyr und JavaScript. 
Zweitens ermöglicht MicroPython schnelles Feedback, da man REPL für interaktive Befehlseingaben nutzen und sofortige Antworten erhalten kann. Man kann sogar Code anpassen und ihn sofort ausführen, anstatt den Code-Kompilieren-Hochladen-Ausführen-Zyklus zu durchlaufen.

Während Python dieselben Vorteile bietet, sind einige Mikrocontrollerboards wie der Raspberry Pi Pico klein, einfach und haben wenig Speicher, um die Python-Sprache überhaupt auszuführen. Deshalb hat sich MicroPython weiterentwickelt, hat die wichtigsten Python-Funktionen beibehalten und eine Reihe neuer Funktionen hinzugefügt, um mit diesen Mikrocontrollerboards zu arbeiten.

Als Nächstes lernen Sie, wie Sie MicroPython auf den Raspberry Pi Pico installieren können.

* Referenz: `MicroPython - Wikipedia <https://de.wikipedia.org/wiki/MicroPython>`_
* Referenz: `realpython <https://realpython.com/micropython/>`_

