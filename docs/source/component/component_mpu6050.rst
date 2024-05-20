.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_mpu6050:

MPU6050 Modul
===========================

**MPU6050**

|img_mpu6050|

Der MPU-6050 ist ein 6-Achsen-Motion-Tracking-Gerät, das einen 3-Achsen-Gyroskop mit einem 3-Achsen-Beschleunigungsmesser kombiniert.

Die drei Koordinatensysteme sind wie folgt definiert:

Legen Sie das MPU6050 flach auf den Tisch, sodass die Seite mit dem Aufkleber nach oben zeigt und ein Punkt auf dieser Oberfläche in der oberen linken Ecke ist. Dann ist die aufrechte Richtung nach oben die Z-Achse des Chips. Die Richtung von links nach rechts wird als X-Achse betrachtet. Entsprechend ist die Richtung von hinten nach vorne als die Y-Achse definiert.

|img_mpu6050_a|

**3-Achsen-Beschleunigungsmesser**

Der Beschleunigungsmesser funktioniert nach dem Prinzip des piezoelektrischen Effekts, der Fähigkeit bestimmter Materialien, eine elektrische Ladung in Reaktion auf mechanischen Druck zu erzeugen.

Stellen Sie sich eine quaderförmige Box mit einer kleinen Kugel darin vor, wie im obigen Bild. Die Wände dieser Box bestehen aus piezoelektrischen Kristallen. Wenn Sie die Box neigen, wird die Kugel aufgrund der Schwerkraft in Richtung der Neigung bewegt. Die Wand, gegen die die Kugel prallt, erzeugt winzige piezoelektrische Ströme. Jedes Paar gegenüberliegender Wände in einem Quader entspricht einer Achse im 3D-Raum: X, Y und Z. Abhängig von dem erzeugten Strom der piezoelektrischen Wände können wir die Neigungsrichtung und deren Ausmaß bestimmen.

|img_mpu6050_a2|

Das MPU6050 kann dazu verwendet werden, die Beschleunigung auf jeder Koordinatenachse zu erkennen (im ruhenden Desktop-Zustand beträgt die Z-Achsen-Beschleunigung 1 Gravitationskraft und die X- und Y-Achsen sind 0). Bei Neigung oder in einem Zustand der Schwerelosigkeit/Überlastung ändert sich der entsprechende Messwert.

Es gibt vier programmierbare Messbereiche: +/-2g, +/-4g, +/-8g und +/-16g (standardmäßig 2g), die jeder Präzision entsprechen. Die Werte reichen von -32768 bis 32767.

Die Beschleunigung wird folgendermaßen in einen Beschleunigungswert umgewandelt:

Beschleunigung = (Rohdaten der Beschleunigungsachsen / 65536 \* voller Skalenbeschleunigungsbereich) g

Am Beispiel der X-Achse: Wenn die Rohdaten der Beschleunigung der X-Achse 16384 betragen und der Bereich als +/-2g ausgewählt ist:

**Beschleunigung entlang der X-Achse = (16384 / 65536 \* 4) g = 1g**

**3-Achsen-Gyroskop**

Gyroskope funktionieren nach dem Prinzip der Coriolis-Beschleunigung. Stellen Sie sich eine gabelähnliche Struktur vor, die ständig in Bewegung ist. Sie wird durch piezoelektrische Kristalle an Ort und Stelle gehalten. Wenn Sie diese Anordnung zu neigen versuchen, erfahren die Kristalle eine Kraft in Richtung der Neigung. Diese wird durch die Trägheit der beweglichen Gabel erzeugt. Die Kristalle erzeugen dadurch einen Strom, der mit dem piezoelektrischen Effekt in Einklang steht, und dieser Strom wird verstärkt.

|img_mpu6050_g|

Das Gyroskop hat ebenfalls vier Messbereiche: +/- 250, +/- 500, +/- 1000, +/- 2000. Die Berechnungsmethode und die Beschleunigung sind im Wesentlichen konsistent.

Die Formel zur Umwandlung des Messwerts in die Winkelgeschwindigkeit lautet:

Winkelgeschwindigkeit = (Rohdaten der Gyroskopachsen / 65536 \* voller Skalen-Gyroskopbereich) °/s

Anhand der X-Achse: Wenn die Rohdaten der X-Achse des Beschleunigungsmessers 16384 betragen und der Bereich +/- 250°/s beträgt:

**Winkelgeschwindigkeit entlang der X-Achse = (16384 / 65536 \* 500)°/s = 125°/s**

**Beispiel**

* :ref:`py_mpu6050` (Für MicroPython-Nutzer)
* :ref:`py_somato_controller` (Für MicroPython-Nutzer)
* :ref:`py_bubble_level` (Für MicroPython-Nutzer)
* :ref:`ar_mpu6050` (Für Arduino-Nutzer)
