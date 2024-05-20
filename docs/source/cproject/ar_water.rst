.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_water:

2.14 - Den Wasserstand erfühlen
=====================================

|img_water_sensor|

Der Wassersensor ist für die Wassererkennung konzipiert und kann vielseitig zur Erfassung von Niederschlägen, Wasserständen und sogar Flüssigkeitsaustritten eingesetzt werden.

Der Sensor misst den Wasserstand durch eine Reihe von freiliegenden parallelen Drahtspuren, um die Größe der Wassertropfen/das Volumen zu messen. Das Wasservolumen lässt sich leicht in ein analoges Signal umwandeln, und der ausgegebene analoge Wert kann direkt vom Hauptsteuerbrett abgelesen werden, um den Wasserstandsalarm zu aktivieren.

.. warning::

    Der Sensor darf nicht vollständig ins Wasser getaucht werden; bitte lassen Sie nur den Teil, an dem sich die zehn Spuren befinden, mit dem Wasser in Kontakt kommen. Das Einschalten des Sensors in einer feuchten Umgebung beschleunigt die Korrosion der Sonde und verkürzt die Lebensdauer des Sensors. Es wird daher empfohlen, den Sensor nur dann mit Strom zu versorgen, wenn Messungen durchgeführt werden.

* :ref:`cpn_water_level`

**Benötigte Bauteile**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Ein Komplettset ist natürlich praktisch, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Bezeichnung
        - INHALT DES KITS
        - KAUF-LINK
    *   - Kepler Kit
        - 450+
        - |link_kepler_kit|

Die Bauteile können auch einzeln über die untenstehenden Links erworben werden.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTENBESCHREIBUNG
        - ANZAHL
        - KAUF-LINK

    *   - 1
        - :ref:`cpn_pico_w`
        - 1
        - |link_picow_buy|
    *   - 2
        - Micro-USB-Kabel
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Mehrere
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_water_level`
        - 1
        - 

**Schaltplan**

|sch_water|

**Verkabelung**

|wiring_water|

**Code**

.. note::

   * Die Datei ``2.14_feel_the_water_level.ino`` finden Sie unter dem Pfad ``kepler-kit-main/arduino/2.14_feel_the_water_level``.
   * Alternativ können Sie den Code in die **Arduino IDE** kopieren.

   * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den richtigen Port auszuwählen, bevor Sie auf **Hochladen** klicken.

.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/32ee87a1-08eb-482f-bf4c-b12b24ef05c4/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Nachdem das Programm gestartet ist, tauchen Sie das Wassersensormodul langsam ins Wasser. Mit zunehmender Tiefe wird die Shell einen größeren Wert ausgeben.

**Mehr erfahren**

Es gibt eine Möglichkeit, das Analogeingabemodul als digitales Modul zu verwenden.

Zuerst messen Sie den Wert des Wassersensors in einer trockenen Umgebung und verwenden diesen als Schwellenwert. Anschließend führen Sie die Programmierung durch und lesen den Wert des Wassersensors erneut. Weicht der Wert des Wassersensors erheblich von dem in einer trockenen Umgebung ab, wurde er einer Flüssigkeit ausgesetzt. Das heißt, dieses Gerät kann neben einem Wasserrohr platziert werden, um festzustellen, ob das Rohr undicht ist.

.. note::

   * Die Datei ``2.14_water_level_threshold.ino`` finden Sie unter dem Pfad ``kepler-kit-main/arduino/2.14_water_level_threshold``.
   * Alternativ können Sie den Code in die **Arduino IDE** kopieren.

    * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den richtigen Port auszuwählen, bevor Sie auf **Hochladen** klicken.

.. :raw-code:

