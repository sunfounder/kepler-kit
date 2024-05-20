.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_buzzer:

Summer
=======

Als eine Art von elektronischem Summer mit integrierter Struktur, die von Gleichstrom versorgt werden, finden Summer weitreichende Anwendung in Computern, Druckern, Kopierern, Alarmanlagen, elektronischem Spielzeug, Kfz-Elektronik, Telefonen, Zeitgebern und anderen elektronischen Produkten oder stimmlichen Geräten.

Summer lassen sich in aktive und passive Modelle unterteilen (siehe nachstehendes Bild). Wenn die Anschlusspins des Summers nach oben zeigen, ist der Summer mit einer grünen Platine ein passiver Summer, während der mit schwarzem Klebeband umwickelte ein aktiver Summer ist.

|img_buzzer|

Unterschied zwischen einem aktiven und einem passiven Summer:

Ein aktiver Summer verfügt über eine integrierte Oszillationsquelle und gibt beim Anlegen einer Spannung einen Ton ab. Ein passiver Summer hingegen besitzt keine solche Quelle und kann daher nicht mit Gleichstromsignalen betrieben werden; stattdessen müssen Sie ihn mit Rechteckwellen antreiben, deren Frequenz zwischen 2K und 5K liegt. Aktive Summer sind aufgrund der mehreren integrierten Oszillationskreise meist teurer als passive.

Im Folgenden ist das elektrische Symbol eines Summers dargestellt. Er besitzt zwei Anschlusspins für den positiven und den negativen Pol. Ein Pluszeichen auf der Oberfläche kennzeichnet die Anode, der andere Pin ist die Kathode.

|img_buzzer_symbol|

An den Pins des Summers können Sie erkennen, dass der längere der Anodenanschluss und der kürzere der Kathodenanschluss ist. Bitte verwechseln Sie diese nicht beim Anschließen, da sonst der Summer keinen Ton abgibt.

`Summer - Wikipedia <https://de.wikipedia.org/wiki/Summer_(Elektrik)>`_

.. Beispiel
.. -------------------

.. :ref:`Einbruchsalarm`

.. :ref:`Individueller Ton`

**Beispiel**

* :ref:`py_ac_buz` (Für MicroPython-Nutzer)
* :ref:`py_pa_buz` (Für MicroPython-Nutzer)
* :ref:`py_light_theremin` (Für MicroPython-Nutzer)
* :ref:`py_alarm_lamp` (Für MicroPython-Nutzer)
* :ref:`py_music_player` (Für MicroPython-Nutzer)
* :ref:`py_fruit_piano` (Für MicroPython-Nutzer)
* :ref:`py_reversing_aid` (Für MicroPython-Nutzer)
* :ref:`ar_ac_buz` (Für Arduino-Nutzer)
* :ref:`ar_pa_buz` (Für Arduino-Nutzer)
* :ref:`per_service_bell` (Für Piper Make-Nutzer)
* :ref:`per_reversing_system` (Für Piper Make-Nutzer)
* :ref:`per_reaction_game` (Für Piper Make-Nutzer)
