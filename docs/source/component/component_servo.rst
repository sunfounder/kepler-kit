.. _cpn_servo:

Servo
===========

|img_servo|

Ein Servo setzt sich in der Regel aus den folgenden Teilen zusammen: Gehäuse, Welle, Getriebesystem, Potentiometer, Gleichstrommotor und eingebettete Platine. 

Die Funktionsweise ist wie folgt: Der Mikrocontroller sendet PWM-Signale an den Servo, welche von der eingebetteten Platine im Servo über den Signaleingang empfangen werden. Die Platine steuert daraufhin den internen Motor an, der das Getriebe in Bewegung setzt und so die Welle antreibt. Die Welle und das Potentiometer des Servos sind miteinander verbunden. Wenn die Welle sich dreht, wird das Potentiometer mitbewegt, das dann eine Spannung an die Platine sendet. Basierend auf dieser Spannung bestimmt die Platine die Drehrichtung und -geschwindigkeit und stoppt die Welle exakt in der vorgegebenen Position.

|img_servo_i|

Der Winkel wird durch die Dauer eines Pulses bestimmt, der auf das Steuerkabel aufgebracht wird. Dies wird als Pulsweitenmodulation bezeichnet. Der Servo erwartet alle 20 ms einen Puls. Die Länge dieses Pulses bestimmt, wie weit sich der Motor dreht. Ein 1,5 ms langer Puls beispielsweise bringt den Motor in die 90-Grad-Position (Neutralstellung). Wird ein kürzerer Puls als 1,5 ms an den Servo gesendet, dreht dieser seine Ausgangswelle um eine bestimmte Anzahl von Grad gegen den Uhrzeigersinn von der Neutralposition aus. Ein Puls, der länger als 1,5 ms ist, bewirkt das Gegenteil. Die minimale und maximale Pulsbreite, die den Servo zu einer gültigen Position steuert, hängt vom jeweiligen Servo ab. Üblicherweise beträgt die minimale Pulsbreite etwa 0,5 ms und die maximale etwa 2,5 ms.

|img_servo_duty|

.. Beispiel
.. -------------------

.. :ref:`Schwingender Servo`

**Beispiel**

* :ref:`py_servo` (Für MicroPython-Nutzer)
* :ref:`py_somato_controller` (Für MicroPython-Nutzer)
* :ref:`ar_servo` (Für Arduino-Nutzer)
* :ref:`per_water_tank` (Für Piper Make-Nutzer)
* :ref:`per_swing_servo` (Für Piper Make-Nutzer)
* :ref:`per_lucky_cat` (Für Piper Make-Nutzer)
