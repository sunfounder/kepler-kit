.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_ir_receiver:

Infrarotempfänger
=================================

IR-Empfänger
----------------------------

|img_irrecv|

* S: Signalausgang
* +: VCC
* -: GND

Ein Infrarotempfänger ist eine Komponente, die Infrarotsignale empfangen kann. Er ist in der Lage, eigenständig Infrarotstrahlung zu detektieren und TTL-kompatible Signale auszugeben. Von der Größe her entspricht er einem herkömmlichen Transistor im Kunststoffgehäuse und eignet sich für alle Anwendungsgebiete von Infrarot-Fernbedienungen bis zu Infrarot-Datenübertragung.

Infrarot (IR) ist eine populäre, kosteneffiziente und einfach zu verwendende Technologie für drahtlose Kommunikation. Infrarotlicht liegt in einem Wellenlängenbereich, der für das menschliche Auge unsichtbar ist, was es ideal für drahtlose Übertragungen macht. Häufig wird eine 38-kHz-Modulation für die Infrarotkommunikation verwendet.

* Verwendet den hochsensiblen HX1838 IR-Empfänger-Sensor
* Für den Einsatz in Fernbedienungen geeignet
* Stromversorgung: 3,3 bis 5V
* Digitale Schnittstelle
* Modulationsfrequenz: 38 kHz


Fernbedienung
-------------------------

|img_controller|

Diese kompakte Infrarot-Fernbedienung verfügt über 21 Funktionstasten und eine Übertragungsreichweite von bis zu 8 Metern. Sie ist optimal zur Steuerung diverser Geräte im Kinderzimmer einsetzbar.

* Abmessungen: 85x39x6mm
* Reichweite: 8 bis 10m
* Batterietyp: 3V Knopfzellen-Lithium-Mangan-Batterie
* Trägerfrequenz für Infrarot: 38 kHz
* Oberflächenmaterial: 0,125 mm PET
* Effektive Nutzungsdauer: über 20.000 Betätigungen


**Beispiele**

* :ref:`py_irremote` (Für MicroPython-Anwender)
* :ref:`ar_irremote` (Für Arduino-Anwender)

