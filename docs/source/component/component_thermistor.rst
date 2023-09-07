.. _cpn_thermistor:

Thermistor
===============

|img_thermistor|

Ein Thermistor ist eine spezielle Form eines Widerstands, dessen Widerstandswert stark temperaturabhängig ist, viel stärker als bei Standardwiderständen. Der Begriff setzt sich aus den Wörtern "thermal" und "resistor" zusammen. Thermistoren werden häufig als Einschaltstrombegrenzer, Temperatursensoren (in der Regel vom NTC-Typ mit negativem Temperaturkoeffizienten), selbstzurücksetzende Überstromschutzvorrichtungen und selbstregelnde Heizelemente (in der Regel vom PTC-Typ mit positivem Temperaturkoeffizienten) eingesetzt.

* `Thermistor - Wikipedia <https://de.wikipedia.org/wiki/Thermistor>`_

Hier ist das Elektroniksymbol für einen Thermistor.

|img_thermistor_symbol|

Es gibt zwei grundlegend unterschiedliche Arten von Thermistoren:

* Bei NTC-Thermistoren nimmt der Widerstand mit steigender Temperatur ab. Dies ist in der Regel auf eine Zunahme der durch thermische Anregung angeregten Leitungselektronen zurückzuführen. NTCs werden häufig als Temperatursensoren eingesetzt oder in Reihe zu einer Schaltung als Einschaltstrombegrenzer.
* Bei PTC-Thermistoren steigt der Widerstand mit zunehmender Temperatur, in der Regel durch eine Zunahme der thermischen Gitteranregungen, insbesondere von Verunreinigungen und Unvollkommenheiten. PTC-Thermistoren werden oft in Reihe zu einer Schaltung eingesetzt und dienen als rückstellbare Sicherungen gegen Überstrombedingungen.

In diesem Bausatz verwenden wir einen NTC-Thermistor. Jeder Thermistor hat einen Nennwiderstand. Hier beträgt dieser 10 kOhm, gemessen bei einer Temperatur von 25 Grad Celsius.

Hier ist die Beziehung zwischen dem Widerstand und der Temperatur:

    RT = RN * exp(B * (1/TK - 1/TN))

* **RT** ist der Widerstand des NTC-Thermistors bei der Temperatur TK.
* **RN** ist der Widerstand des NTC-Thermistors bei der Nenntemperatur TN. Hier beträgt der Zahlenwert von RN 10k.
* **TK** ist eine Temperatur in Kelvin, die Einheit ist K. Hier beträgt der Zahlenwert von TK 273,15 + Grad Celsius.
* **TN** ist eine Nenntemperatur in Kelvin; die Einheit ist ebenfalls K. Hier beträgt der Zahlenwert von TN 273,15+25.
* **B(Beta)**, die Materialkonstante des NTC-Thermistors, wird auch als Temperaturkoeffizient bezeichnet und hat den Zahlenwert 3950.
* **exp** steht für die Exponentialfunktion, deren Basis die natürliche Zahl e ist und die ungefähr 2,7 beträgt.

Diese Beziehung wird durch die Formel TK=1/(ln(RT/RN)/B+1/TN) hergeleitet, wobei die resultierende Temperatur in Kelvin um 273,15 reduziert wird, um Grad Celsius zu erhalten.

Diese Beziehung ist eine empirische Formel und gilt nur, wenn Temperatur und Widerstand innerhalb des wirksamen Bereichs liegen.

.. Beispiel
.. -------------------

.. :ref:`Thermometer`

**Beispiel**

* :ref:`py_temp` (Für MicroPython-Nutzer)
* :ref:`py_room_temp` (Für MicroPython-Nutzer)
* :ref:`ar_temp` (Für Arduino-Nutzer)
