.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_potentiometer:

Potentiometer
===============

|img_pot|

Ein Potentiometer ist ebenfalls ein Widerstandselement mit drei Anschlüssen, dessen Widerstandswert nach einer bestimmten Regelung variiert werden kann.

Potentiometer gibt es in verschiedenen Formen, Größen und Werten, sie haben jedoch alle folgende Gemeinsamkeiten:

* Sie verfügen über drei Anschlüsse (oder Kontaktpunkte).
* Sie besitzen einen Drehknopf, eine Schraube oder einen Schieber, mit dem der Widerstand zwischen dem mittleren und einem der äußeren Anschlüsse verändert werden kann.
* Der Widerstand zwischen dem mittleren und einem der äußeren Anschlüsse variiert von 0 Ω bis zum maximalen Widerstand des Potentiometers, wenn der Drehknopf, die Schraube oder der Schieber bewegt wird.

Hier ist das Schaltzeichen für ein Potentiometer.

|img_pot_symbol|

Die Funktionen des Potentiometers im Stromkreis sind wie folgt:

#. Als Spannungsteiler

    Das Potentiometer ist ein stufenlos einstellbarer Widerstand. Wenn Sie die Achse oder den Schiebegriff des Potentiometers verstellen, gleitet der bewegliche Kontakt über den Widerstand. An dieser Stelle kann eine Spannung abhängig von der am Potentiometer angelegten Spannung und dem Drehwinkel oder dem Verfahrweg des beweglichen Arms ausgegeben werden.

#. Als Rheostat

    Wenn das Potentiometer als Rheostat verwendet wird, verbinden Sie den mittleren Pin mit einem der beiden anderen Pins im Stromkreis. So erhalten Sie einen stufenlos und kontinuierlich veränderbaren Widerstandswert innerhalb des Verfahrwegs des beweglichen Kontakts.

#. Als Stromregler

    Wenn das Potentiometer als Stromregler fungiert, muss der Schiebekontakt als einer der Ausgangsanschlüsse verbunden sein.

Wenn Sie mehr über Potentiometer erfahren möchten, siehe: `Potentiometer - Wikipedia <https://de.wikipedia.org/wiki/Potentiometer>`_

.. Beispiel
.. -------------------

.. * :ref:`Dreh den Knopf` (Für MicroPython-Anwender)
.. * :ref:`Tischlampe` (Für C/C++(Arduino)-Anwender)

**Beispiel**

* :ref:`py_pot` (Für MicroPython-Anwender)
* :ref:`ar_pot` (Für Arduino-Anwender)
* :ref:`per_swing_servo` (Für Piper Make-Anwender)
