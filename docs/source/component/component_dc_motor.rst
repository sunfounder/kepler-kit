.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_motor:

Gleichstrommotor
===================

|img_dc_motor|

Hierbei handelt es sich um einen 3V-Gleichstrommotor. Wenn Sie an beide der 2 Anschlüsse ein hohes und ein niedriges Signal anlegen, beginnt der Motor zu drehen.

* **Größe**: 25*20*15MM
* **Betriebsspannung**: 1-6V
* **Leerlaufstrom** (3V): 70m
* **Leerlaufdrehzahl** (3V): 13000 U/min
* **Blockierstrom** (3V): 800mA
* **Wellendurchmesser**: 2mm

Ein Gleichstrommotor ist ein kontinuierlicher Aktuator, der elektrische Energie in mechanische Energie umwandelt. Durch ihre Fähigkeit zur kontinuierlichen Winkelrotation treiben Gleichstrommotoren Rotationspumpen, Ventilatoren, Kompressoren, Laufräder und andere Geräte an.

Ein Gleichstrommotor besteht aus zwei Hauptkomponenten: dem festen Teil des Motors, genannt **Stator**, und dem beweglichen Innenbereich des Motors, bekannt als **Rotor** (oder **Anker** eines Gleichstrommotors). Der Schlüssel zur Bewegungserzeugung liegt in der Positionierung des Ankers im Magnetfeld des Permanentmagneten, dessen Feld sich von Nordpol zu Südpol erstreckt. Die Wechselwirkung zwischen diesem Magnetfeld und den bewegten geladenen Teilchen (durch den stromführenden Draht erzeugt) resultiert im Drehmoment, das den Anker rotieren lässt.

|img_dc_motor_sche|

Der Strom fließt vom positiven Pol der Batterie durch die Schaltung, über die Kupferbürsten zum Kommutator und dann zum Anker. Aufgrund der zwei Lücken im Kommutator kehrt dieser Fluss bei jeder vollständigen Rotation um. Diese kontinuierliche Umkehrung wandelt die Gleichstromversorgung der Batterie im Wesentlichen in Wechselstrom um, sodass der Anker das Drehmoment zur richtigen Zeit in die richtige Richtung erhält, um die Rotation aufrechtzuerhalten.

* `Gleichstrommotor - MagLab <https://nationalmaglab.org/education/magnet-academy/watch-play/interactive/dc-motor>`_
* `Flemings linke Handregel für Motoren - Wikipedia <https://en.wikipedia.org/wiki/Fleming%27s_left-hand_rule_for_motors>`_

**Beispiel**

* :ref:`py_motor` (Für MicroPython-Nutzer)
* :ref:`ar_motor` (Für Arduino-Nutzer)
* :ref:`per_smart_fan` (Für Piper Make-Nutzer)
