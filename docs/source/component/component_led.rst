.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_led:

LED
==========

|img_led|

Halbleiterlichtemittierende Dioden sind Bauteile, die elektrische Energie durch PN-Übergänge in Lichtenergie umwandeln können. Je nach Wellenlänge können sie in Laserdioden, infrarotemittierende Dioden und sichtbare lichtemittierende Dioden eingeteilt werden, wobei die letztere allgemein als lichtemittierende Diode (LED) bekannt ist.

Dioden haben eine unidirektionale Leitfähigkeit, sodass der Stromfluss so verläuft, wie im Schaltzeichensymbol durch den Pfeil angezeigt wird. Das Anodenende sollte positiv und das Kathodenende negativ polarisiert werden. Dann leuchtet die LED.

|img_led_symbol|

Eine LED hat zwei Anschlüsse. Der längere ist die Anode und der kürzere die Kathode. Achten Sie darauf, sie nicht umgekehrt anzuschließen. LEDs haben eine festgelegte Vorwärtsspannung. Sie können nicht direkt an eine Schaltung angeschlossen werden, da die Versorgungsspannung diese Vorwärtsspannung übersteigen und die LED beschädigen könnte. Die Vorwärtsspannung von roten, gelben und grünen LEDs beträgt 1,8 V, während die von weißen LEDs 2,6 V beträgt. Die meisten LEDs können einen maximalen Strom von 20 mA vertragen, daher sollte ein strombegrenzender Widerstand in Reihe geschaltet werden.

Die Formel für den Widerstandswert lautet:

    R = (Vsupply – VD)/I

Dabei steht **R** für den Widerstandswert des strombegrenzenden Widerstands, **Vsupply** für die Versorgungsspannung, **VD** für den Spannungsabfall und **I** für den Arbeitsstrom der LED.

Hier finden Sie eine detaillierte Einführung in die LED: `LED - Wikipedia <https://de.wikipedia.org/wiki/Leuchtdiode>`_.

.. **Beispiel**

.. * :ref:`Hello, Breadboard!` (Für MicroPython-Nutzer)
.. * :ref:`fading_led_micropython` (Für MicroPython-Nutzer)
.. * :ref:`fading_led_arduino` (Für C/C++(Arduino)-Nutzer)
.. * :ref:`hello_led_arduino` (Für C/C++(Arduino)-Nutzer)

**Beispiel**

* :ref:`py_led` (Für MicroPython-Nutzer)
* :ref:`py_fade` (Für MicroPython-Nutzer)
* :ref:`py_alarm_lamp` (Für MicroPython-Nutzer)
* :ref:`py_traffic_light` (Für MicroPython-Nutzer)
* :ref:`py_reversing_aid` (Für MicroPython-Nutzer)
* :ref:`ar_led` (Für Arduino-Nutzer)
* :ref:`ar_fade` (Für Arduino-Nutzer)
* :ref:`per_blink` (Für Piper Make-Nutzer)
* :ref:`per_button` (Für Piper Make-Nutzer)
* :ref:`per_service_bell` (Für Piper Make-Nutzer)
* :ref:`per_reversing_system` (Für Piper Make-Nutzer)
* :ref:`per_reaction_game` (Für Piper Make-Nutzer)

