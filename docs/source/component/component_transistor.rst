.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_transistor:

Transistor
============

|img_NPN&PNP|

Ein Transistor ist ein Halbleiterbauelement, das Strom mittels Strom steuert. Seine Hauptfunktionen bestehen darin, schwache Signale zu verstärken und als berührungsloser Schalter zu agieren.

Ein Transistor besteht aus einer dreischichtigen Struktur aus P-Typ und N-Typ Halbleitern. Diese bilden die drei internen Regionen: Die dünnere Mitte ist die Basisregion; die beiden anderen sind entweder N-Typ oder P-Typ – die kleinere Region mit einer hohen Anzahl an Ladungsträgern ist die Emitterregion, während die andere als Kollektorregion fungiert. Diese Anordnung ermöglicht die Verstärkerfunktion des Transistors. 
Aus diesen drei Regionen gehen jeweils drei Pole hervor: Basis (b), Emitter (e) und Kollektor (c). Sie bilden zwei P-N-Übergänge, nämlich den Emitter- und den Kollektorübergang. Die Pfeilrichtung im Transistorsymbol gibt die Richtung des Emitterübergangs an.

* `P-N-Übergang – Wikipedia <https://de.wikipedia.org/wiki/Pn-Übergang>`_

Je nach Halbleitertyp lassen sich Transistoren in zwei Gruppen einteilen: NPN und PNP. Aus den Abkürzungen geht hervor, dass der erstere aus zwei N-Typ und einem P-Typ Halbleiter besteht, während der letztere das Gegenteil darstellt. Siehe die untenstehende Abbildung.

.. note::
    Der s8550 ist ein PNP-Transistor und der s8050 ein NPN-Transistor. Sie sehen sehr ähnlich aus; es ist also wichtig, die Beschriftungen genau zu prüfen.

|img_transistor_symbol|

Ein NPN-Transistor wird durch ein Hochpegelsignal aktiviert, während für einen PNP-Transistor ein Lowpegelsignal erforderlich ist. Beide Transistortypen werden häufig als berührungslose Schalter eingesetzt, wie in diesem Experiment.

* `S8050 Transistor Datenblatt <https://components101.com/asset/sites/default/files/component_datasheet/S8050%20Transistor%20Datasheet.pdf>`_
* `S8550 Transistor Datenblatt <https://www.mouser.com/datasheet/2/149/SS8550-118608.pdf>`_

Richten Sie die beschriftete Seite zu sich und die Pins nach unten. Die Pins von links nach rechts sind Emitter (e), Basis (b) und Kollektor (c).

|img_ebc|

.. note::
    * Die Basis dient als Steuereinheit für die größere Stromquelle.
    * Im NPN-Transistor ist der Kollektor die größere Stromquelle und der Emitter der Ausgang, im PNP-Transistor ist es genau umgekehrt.

.. Beispiel
.. -------------------

.. :ref:`Zwei Arten von Transistoren`


**Beispiel**

* :ref:`py_transistor` (Für MicroPython-Nutzer)
* :ref:`py_relay` (Für MicroPython-Nutzer)
* :ref:`py_ac_buz` (Für MicroPython-Nutzer)
* :ref:`py_pa_buz` (Für MicroPython-Nutzer)
* :ref:`py_light_theremin` (Für MicroPython-Nutzer)
* :ref:`py_alarm_lamp` (Für MicroPython-Nutzer)
* :ref:`py_music_player` (Für MicroPython-Nutzer)
* :ref:`py_fruit_piano` (Für MicroPython-Nutzer)
* :ref:`py_reversing_aid` (Für MicroPython-Nutzer)
* :ref:`ar_ac_buz` (Für Arduino-Nutzer)
* :ref:`ar_pa_buz` (Für Arduino-Nutzer)
* :ref:`ar_transistor` (Für Arduino-Nutzer)
* :ref:`ar_relay` (Für Arduino-Nutzer)
* :ref:`per_service_bell` (Für Piper Make-Nutzer)
* :ref:`per_reversing_system` (Für Piper Make-Nutzer)
* :ref:`per_reaction_game` (Für Piper Make-Nutzer)
