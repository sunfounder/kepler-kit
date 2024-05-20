.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_dot_matrix:

LED-Punktmatrix
==========================

|img_led_matrix|

Generell lässt sich die LED-Punktmatrix in zwei Typen unterteilen: Gemeinsame Kathode (CC) und gemeinsame Anode (CA). Optisch sehen beide Typen ähnlich aus, der Unterschied liegt jedoch im Inneren. Dies lässt sich durch einen Test feststellen. Im vorliegenden Kit wird ein CA-Modell verwendet, das seitlich mit 788BS beschriftet ist.

Siehe dazu die untenstehende Abbildung. Die Pins sind an den beiden Enden der Rückseite angeordnet. Orientieren Sie sich an der beschrifteten Seite: Die Pins an diesem Ende sind die Pins 1-8, am anderen Ende sind es die Pins 9-16.

Die äußere Ansicht:

|img_788bs_i|

Die folgenden Abbildungen zeigen den internen Aufbau. In einer CA-LED-Punktmatrix repräsentiert die Zeile (ROW) die Anode der LED, während die Spalte (COL) die Kathode ist; bei einer CC-Matrix ist es umgekehrt. Gemeinsam ist beiden Typen: Die Pins 13, 3, 4, 10, 6, 11, 15 und 16 sind jeweils COL, während die Pins 9, 14, 8, 12, 1, 7, 2 und 5 alle ROW sind. Möchten Sie die erste LED in der linken oberen Ecke einschalten, setzen Sie bei einer CA-Matrix Pin 9 auf High und Pin 13 auf Low; bei einer CC-Matrix setzen Sie Pin 13 auf High und Pin 9 auf Low. Um die gesamte erste Spalte aufzuhellen, setzen Sie bei CA Pin 13 auf Low und die ROW-Pins 9, 14, 8, 12, 1, 7, 2 und 5 auf High; bei CC setzen Sie Pin 13 auf High und die ROW-Pins auf Low. Die nachfolgenden Abbildungen sollten zur weiteren Veranschaulichung dienen.

Die innere Ansicht:

|img_788bs_sche|

Zuordnung der Pinnummern zu den oben genannten Reihen und Spalten:

=========== ====== ====== ===== ====== ===== ====== ====== ======
**COL**     **1**  **2**  **3** **4**  **5** **6**  **7**  **8**
**Pin No.** **13** **3**  **4** **10** **6** **11** **15** **16**
**ROW**     **1**  **2**  **3** **4**  **5** **6**  **7**  **8**
**Pin No.** **9**  **14** **8** **12** **1** **7**  **2**  **5**
=========== ====== ====== ===== ====== ===== ====== ====== ======

Darüber hinaus werden hier zwei 74HC595-Chips verwendet. Einer steuert die Reihen der LED-Punktmatrix, der andere die Spalten.

**Beispiel**

* :ref:`py_74hc_788bs` (Für MicroPython-Nutzer)
* :ref:`py_bubble_level` (Für MicroPython-Nutzer)
* :ref:`ar_74hc_788bs` (Für Arduino-Nutzer)
