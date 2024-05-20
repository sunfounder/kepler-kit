.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_button:

Taster
==========

|img_button|

Taster sind ein häufig verwendeter Bauteil zur Steuerung elektronischer Geräte. Sie dienen meist als Schalter, um elektrische Stromkreise zu schließen oder zu unterbrechen. Obwohl Taster in verschiedenen Formen und Größen erhältlich sind, handelt es sich bei dem hier vorgestellten Modell um einen 6mm-Mini-Taster, wie auf den folgenden Bildern zu sehen ist. Pin 1 ist mit Pin 2 und Pin 3 mit Pin 4 verbunden. Man muss also lediglich entweder Pin 1 mit Pin 3 oder Pin 2 mit Pin 4 verbinden.

Nachfolgend ist die interne Struktur eines Tasters dargestellt. Das Symbol rechts unten wird üblicherweise verwendet, um einen Taster in Schaltkreisen zu kennzeichnen.

|img_button_symbol|

Da Pin 1 mit Pin 2 und Pin 3 mit Pin 4 verbunden sind, werden beim Drücken des Tasters alle 4 Pins miteinander verbunden, wodurch der Stromkreis geschlossen wird.

|img_button2|

.. Beispiele
.. -------------------

.. :ref:`Tasterwert auslesen`

**Beispiel**

* :ref:`py_button` (Für MicroPython-Anwender)
* :ref:`ar_button` (Für Arduino-Anwender)
* :ref:`per_button` (Für Piper Make-Anwender)
* :ref:`per_rainbow_light` (Für Piper Make-Anwender)
* :ref:`per_drum_kit` (Für Piper Make-Anwender)
* :ref:`per_reaction_game` (Für Piper Make-Anwender)
