.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_rgb:

RGB-LED
=================

|img_rgb|

RGB-LEDs emittieren Licht in verschiedenen Farben. Eine RGB-LED kombiniert drei LEDs in den Farben Rot, Grün und Blau in einem transparenten oder halbtransparenten Kunststoffgehäuse. Durch Anpassung der Eingangsspannung der drei Pins und deren Überlagerung können statistisch bis zu 16.777.216 verschiedene Farben erzeugt werden.

|img_rgb_light|

RGB-LEDs können in Gemeinsam-Anode und Gemeinsam-Kathode unterteilt werden. In diesem Bausatz wird die letztere verwendet. Der Begriff **Gemeinsam-Kathode**, oder GK, bedeutet, dass die Kathoden der drei LEDs verbunden sind. Sobald sie mit GND verbunden und die drei Pins eingesteckt sind, leuchtet die LED in der entsprechenden Farbe auf.

Das Schaltungssymbol ist als Abbildung dargestellt.

|img_rgb_symbol|

Eine RGB-LED hat 4 Pins: Der längste Pin ist der Gemeinsam-Kathode-Pin, der in der Regel mit GND verbunden ist. Der linke Pin neben dem längsten Pin ist Rot, und die beiden Pins rechts davon sind Grün und Blau.

|img_rgb_pin|

**Funktionen**

* Farbe: Drei-Farben (Rot/Grün/Blau)
* Gemeinsam-Kathode
* 5mm Klare Runde Linse
* Vorwärtsspannung: Rot: DC 2,0 - 2,2V; Blau&Grün: DC 3,0 - 3,2V (IF=20mA)
* 0,06 Watt DIP RGB-LED
* Leuchtkraft bis zu +20% heller
* Betrachtungswinkel: 30°

.. Beispiel
.. -------------------

.. :ref:`Farbenfrohes Licht`


**Beispiel**

* :ref:`py_rgb` (Für MicroPython-Nutzer)
* :ref:`py_fruit_piano` (Für MicroPython-Nutzer)
* :ref:`ar_rgb` (Für Arduino-Nutzer)
* :ref:`per_rainbow_light` (Für Piper Make-Nutzer)
