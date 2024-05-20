.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_i2c_lcd:

I2C LCD1602
===========

|i2c_lcd1602|

* **GND**: Masse
* **VCC**: Spannungsversorgung, 5V.
* **SDA**: Serielle Datenleitung. Über einen Pull-up-Widerstand mit VCC verbinden.
* **SCL**: Serielle Taktleitung. Über einen Pull-up-Widerstand mit VCC verbinden.

Wie allgemein bekannt ist, bereichern LCDs und andere Anzeigen zwar die Mensch-Maschine-Interaktion, haben jedoch eine gemeinsame Schwäche. Wenn sie an einen Controller angeschlossen werden, werden mehrere IO-Ports des Controllers belegt, der über nicht viele externe Anschlüsse verfügt. Dies schränkt auch andere Funktionen des Controllers ein.

Daher wurde das LCD1602 mit einem I2C-Modul entwickelt, um dieses Problem zu lösen. Das I2C-Modul verfügt über einen integrierten PCF8574 I2C-Chip, der I2C-Serien-Daten in parallele Daten für das LCD-Display umwandelt.

* `PCF8574 Datenblatt <https://www.ti.com/lit/ds/symlink/pcf8574.pdf?ts=1627006546204&ref_url=https%253A%252F%252Fwww.google.com%252F>`_

**I2C-Adresse**

Die Standardadresse ist im Grunde 0x27, in einigen Fällen kann sie jedoch auch 0x3F sein.

Beispielhaft für die Standardadresse 0x27 lässt sich die Geräteadresse durch das Kurzschließen der A0/A1/A2-Pads modifizieren; im Ausgangszustand sind A0/A1/A2 auf 1, und wenn das Pad kurzgeschlossen wird, sind A0/A1/A2 auf 0.

|i2c_address|

**Hintergrundbeleuchtung/Kontrast**

Die Hintergrundbeleuchtung kann durch Aufsetzen einer Jumper-Kappe aktiviert werden, zum Deaktivieren einfach die Jumper-Kappe abziehen. Das blaue Potentiometer auf der Rückseite dient zur Kontrastanpassung (Verhältnis der Helligkeit zwischen dem hellsten Weiß und dem dunkelsten Schwarz).

|back_lcd1602|

* **Kurzschlusskappe**: Die Hintergrundbeleuchtung kann mit dieser Kappe aktiviert werden, zum Deaktivieren einfach diese Kappe abziehen.
* **Potentiometer**: Dient zur Kontrasteinstellung (der Klarheit der angezeigten Texte), die im Uhrzeigersinn erhöht und gegen den Uhrzeigersinn verringert wird.

**Beispiel**

* :ref:`py_lcd` (Für MicroPython-Nutzer)
* :ref:`py_room_temp` (Für MicroPython-Nutzer)
* :ref:`py_guess_number` (Für MicroPython-Nutzer)
* :ref:`ar_lcd` (Für Arduino-Nutzer)
