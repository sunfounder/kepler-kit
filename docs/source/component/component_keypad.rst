.. _cpn_keypad:

4x4 Tastenfeld
========================

Im Mikrocontroller-System, wenn mehrere Tasten wie beispielsweise in elektronischen Codeschlössern oder Telefon-Tastenfeldern verwendet werden, gibt es in der Regel mindestens 12 bis 16 Tasten. Üblicherweise kommt dabei ein Matrix-Tastenfeld zum Einsatz.

Ein Matrix-Tastenfeld wird auch Reihen-Tastenfeld genannt. Es verfügt über vier I/O-Leitungen als Reihen und vier I/O-Leitungen als Spalten. An jedem Schnittpunkt der Reihen- und Spaltenleitungen ist eine Taste angebracht. Somit beträgt die Anzahl der Tasten auf der Tastatur 4*4. Diese Reihen- und Spaltenstruktur kann die Auslastung der I/O-Ports in einem Mikrocontroller-System effektiv verbessern.

Die Kontakte werden über eine Stiftleiste erreicht, die sich für die Verbindung mit einem Flachbandkabel oder zur Einsteckmontage in eine Leiterplatte eignet.
Bei einigen Tastenfeldern stellt jede Taste eine separate Verbindung im Header her, während alle Tasten einen gemeinsamen Masseanschluss teilen.

|img_keypad|

Häufiger sind die Tasten matrixcodiert, was bedeutet, dass jede Taste ein einzigartiges Paar von Leitern in einer Matrix verbindet.
Diese Konfiguration eignet sich für die Abfrage durch einen Mikrocontroller, der so programmiert werden kann, dass er nacheinander einen Ausgangspuls an jede der vier horizontalen Leitungen sendet.
Während jedes Pulses prüft er die verbleibenden vier vertikalen Leitungen sequenziell, um festzustellen, welche davon, falls überhaupt, ein Signal trägt.
Pull-up- oder Pull-down-Widerstände sollten zu den Eingangsleitungen hinzugefügt werden, um unvorhersehbares Verhalten der Mikrocontroller-Eingänge zu verhindern, wenn kein Signal anliegt.

* `Tastenfeld - Wikipedia <https://de.wikipedia.org/wiki/Tastenfeld>`_

**Beispiel**

* :ref:`py_keypad` (Für MicroPython-Nutzer)
* :ref:`py_guess_number` (Für MicroPython-Nutzer)
* :ref:`ar_keypad` (Für Arduino-Nutzer)
