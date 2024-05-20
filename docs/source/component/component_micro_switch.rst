.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_micro_switch:

Mikroschalter
========================

|img_micro_switch|

Der Aufbau eines Mikroschalters ist wirklich simpel. Die Hauptkomponenten des Schalters sind:

|img_micro_switch2|

* 1. Betätigungsstößel (Aktuator)
* 2. Abdeckung
* 3. Bewegliches Teil
* 4. Halterung
* 5. Gehäuse
* 6. NO-Klemme: normalerweise offen
* 7. NC-Klemme: normalerweise geschlossen
* 8. Kontakt
* 9. Bewegungsarm

Nachdem der Mikroschalter physischen Kontakt mit einem Objekt hergestellt hat, ändert er die Position seiner Kontakte. Das grundlegende Funktionsprinzip ist wie folgt.

Wenn der Betätigungsstößel in der Ausgangs- oder Ruheposition ist:

* Der normalerweise geschlossene Stromkreis ist stromführend.
* Der normalerweise offene Stromkreis ist elektrisch isoliert.

Wenn der Betätigungsstößel gedrückt oder umgeschaltet wird:

* Der normalerweise geschlossene Stromkreis ist unterbrochen.
* Der normalerweise offene Stromkreis ist geschlossen.

|img_micro_switch1|

**Beispiel**

* :ref:`py_micro` (Für MicroPython-Anwender)
* :ref:`ar_micro` (Für Arduino-Anwender)
* :ref:`per_service_bell` (Für Piper Make-Anwender)
