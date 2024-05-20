.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_tilt:

Neigungsschalter
=============================

|img_tilt| 

Der hier verwendete Neigungsschalter ist ein Kugeltyp mit einer Metallkugel im Inneren. Er dient zur Erfassung kleiner Neigungswinkel.

Das Funktionsprinzip ist denkbar einfach. Wenn der Schalter in einem bestimmten Winkel geneigt wird, rollt die innenliegende Kugel herunter und berührt die beiden an die äußeren Pins angeschlossenen Kontakte, wodurch der Schaltkreis ausgelöst wird. Wird der Schalter nicht geneigt, bleibt die Kugel von den Kontakten entfernt und der Schaltkreis wird unterbrochen.

|img_tilt_symbol|

* `SW520D Neigungsschalter Datenblatt <https://www.tme.com/Document/f1e6cedd8cb7feeb250b353b6213ec6c/SW-520D.pdf>`_

.. * :ref:`Tastenwert auslesen`

**Beispiel**

* :ref:`py_tilt` (Für MicroPython-Nutzer)
* :ref:`py_10_second` (Für MicroPython-Nutzer)
* :ref:`ar_tilt` (Für Arduino-Nutzer)
* :ref:`per_flowing_leds` (Für Piper Make-Nutzer)
