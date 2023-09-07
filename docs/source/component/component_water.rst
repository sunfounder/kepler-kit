.. _cpn_water_level:

Wasserspiegelsensor-Modul
=================================

|img_water_sensor|

Der Wasserspiegelsensor übermittelt das erfasste Wasserspiegelsignal an die Steuereinheit. Der in der Steuereinheit integrierte Computer vergleicht das gemessene Signal mit dem voreingestellten Sollwert, ermittelt die Abweichung und gibt entsprechend "Ein-" oder "Aus"-Befehle an das Wassernachspeise-Elektroventil. So wird sichergestellt, dass der Behälter den eingestellten Wasserspiegel erreicht.

Der Wasserspiegelsensor verfügt über zehn freiliegende Kupferbahnen, von denen fünf für die Stromversorgung und fünf für die Sensorik zuständig sind. Bei Überflutung werden diese Bahnen durch das Wasser überbrückt. Auf der Platine befindet sich eine Betriebs-LED, die aufleuchtet, wenn die Platine mit Strom versorgt wird.

Die Kombination dieser Bahnen wirkt wie ein variabler Widerstand, dessen Widerstandswert sich je nach Wasserspiegel ändert. Genauer gesagt, je mehr Wasser den Sensor bedeckt, desto besser ist die Leitfähigkeit und desto geringer der Widerstand. Umgekehrt steigt der Widerstand, wenn die Leitfähigkeit abnimmt. Anschließend wird das Ausgangsspannungssignal vom Sensor verarbeitet und an den Mikrocontroller übermittelt, um uns bei der Bestimmung des Wasserspiegels zu unterstützen.


.. warning::
    Der Sensor darf nicht vollständig unter Wasser getaucht werden. Lassen Sie nur den Bereich, in dem sich die zehn Bahnen befinden, mit Wasser in Kontakt kommen. Zudem beschleunigt die Stromversorgung des Sensors in einer feuchten Umgebung die Korrosion der Sonde und verkürzt die Lebensdauer des Sensors. Daher empfehlen wir, den Sensor nur während der Messungen mit Strom zu versorgen.


**Beispiel**

* :ref:`py_water` (Für MicroPython-Anwender)
* :ref:`ar_water` (Für Arduino-Anwender)
* :ref:`per_water_tank` (Für Piper Make-Anwender)
