.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_ta6586:

TA6586 - Motorsteuerungs-Chip
=================================

|img_ta6586|

Der TA6586 ist ein monolithischer IC, der zur Steuerung bidirektionaler Gleichstrommotoren entwickelt wurde. Er verfügt über zwei Logikeingangspins zur Kontrolle der Fahrtrichtung, vorwärts und rückwärts. Der Schaltkreis zeichnet sich durch gute Störfestigkeit, geringen Ruhestrom und niedrigen Ausgangssättigungsdruckabfall aus. Ein integrierte Klemmdiode kehrt den Einfluss des Freisetzens des induktiven Laststroms um, wodurch der IC beim Steuern von Relais, Gleichstrommotoren, Schrittmotoren oder beim Einsatz in Schaltnetzteilen sicher und zuverlässig ist. Der TA6586 eignet sich für Spielzeugfahrzeuge, ferngesteuerte Flugzeugantriebe, automatische Ventilmotoren, elektromagnetische Schlossantriebe, Präzisionsinstrumente und andere Schaltungen.

**Eigenschaften**

* Niedriger Ruhestrom: ≦2uA
* Weiter Versorgungsspannungsbereich
* Integrierte Bremsfunktion
* Thermischer Überlastschutz
* Überstrombegrenzung und Kurzschlussschutz
* DIP8 bleifreies Gehäuse.

**Pin-Funktion**

|img_ta6586_pin|


**Eingangswahrheitstabelle**

|img_ta6586_priciple|


**Beispiel**

* :ref:`py_motor` (Für MicroPython-Anwender)
* :ref:`ar_motor` (Für Arduino-Anwender)
* :ref:`py_pump` (Für MicroPython-Anwender)
* :ref:`ar_pump` (Für Arduino-Anwender)
* :ref:`per_smart_fan` (Für Piper Make-Anwender)
