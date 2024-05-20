.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_l293d:

IC L293D
=================

|img_l293d0|

Der L293D ist ein 4-Kanal-Motorsteuerungs-IC mit hoher Spannung und hohem Strom. 
Er ist darauf ausgelegt, mit standardmäßigen DTL- und TTL-Logikpegeln zu interagieren und induktive Lasten (wie Relaisspulen, Gleichstrom- und Schrittmotoren) sowie Leistungsschalttransistoren zu steuern.
Gleichstrommotoren sind Vorrichtungen, die Gleichstrom in mechanische Energie umwandeln und wegen ihrer hervorragenden Drehzahlregelung häufig in elektrischen Antrieben eingesetzt werden.

Die folgende Abbildung zeigt die Pin-Belegung des L293D. Er besitzt zwei Versorgungsspannungspins (Vcc1 und Vcc2).
Vcc2 dient zur Stromversorgung des Motors, während Vcc1 für den Chip selbst vorgesehen ist. Da hier ein kleiner Gleichstrommotor verwendet wird, sollten beide Pins an +5V angeschlossen werden.

|img_l293d1|

Im Folgenden sehen Sie die interne Struktur des L293D. 
Der Pin EN dient als Enable-Pin und ist nur bei hohem Pegel aktiv; A steht für Eingang und Y für Ausgang.
Die Beziehung zwischen ihnen ist am rechten unteren Rand zu sehen.
Wenn der Pin EN auf hohem Pegel ist und A ebenfalls hoch ist, gibt Y einen hohen Pegel aus; ist A niedrig, gibt Y einen niedrigen Pegel aus. Wenn EN auf niedrigem Pegel ist, ist der L293D inaktiv.

|img_l293d2|

* `L293D Datenblatt <https://cdn-shop.adafruit.com/datasheets/l293d.pdf>`_

**Beispiel**

* :ref:`py_motor` (Für MicroPython-Nutzer)
* :ref:`ar_motor` (Für Arduino-Nutzer)
* :ref:`py_pump` (Für MicroPython-Nutzer)
* :ref:`ar_pump` (Für Arduino-Nutzer)
* :ref:`per_smart_fan` (Für Piper Make-Nutzer)
