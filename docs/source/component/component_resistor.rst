.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_resistor:

Widerstand
==========

|img_res|

Ein Widerstand ist ein elektronisches Bauelement, das den Strom in einem Zweig begrenzen kann. Ein Festwiderstand ist eine Form von Widerstand, dessen Widerstandswert nicht verändert werden kann, während der Widerstand eines Potentiometers oder eines variablen Widerstands einstellbar ist.

Es gibt zwei allgemein verwendete Schaltsymbole für Widerstände. Normalerweise ist der Widerstandswert darauf gekennzeichnet. Wenn Sie also diese Symbole in einer Schaltung sehen, handelt es sich um einen Widerstand.

|img_res_symbol|

**Ω** ist die Einheit des elektrischen Widerstands, und größere Einheiten umfassen KΩ, MΩ usw. 
Die Beziehung zwischen ihnen lässt sich wie folgt darstellen: 1 MΩ = 1000 KΩ, 1 KΩ = 1000 Ω. In der Regel ist der Widerstandswert darauf markiert.

Bevor man einen Widerstand verwendet, muss man seinen Widerstandswert kennen. Es gibt zwei Methoden: Man kann die Farbringe auf dem Widerstand ablesen oder einen Multimeter verwenden, um den Widerstand zu messen. Die erste Methode wird empfohlen, da sie bequemer und schneller ist.

|img_res_card|

Wie auf der Karte gezeigt, steht jede Farbe für eine Nummer.


+---------+---------+------+--------+------+--------+
| Schwarz | Braun   | Rot  | Orange | Gelb | Grün   |
+=========+=========+======+========+======+========+
| 0       | 1       | 2    | 3      | 4    | 5      |
+---------+---------+------+--------+------+--------+

+---------+---------+------+--------+------+--------+
| Blau    | Violett | Grau | Weiß   | Gold | Silber |
+=========+=========+======+========+======+========+
| 6       | 7       | 8    | 9      | 0.1  | 0.01   |
+---------+---------+------+--------+------+--------+

Vier- und fünfbändige Widerstände werden häufig verwendet und haben jeweils vier bzw. fünf farbige Ringe.

Normalerweise ist es nicht sofort ersichtlich, an welchem Ende man beginnen sollte, die Farben abzulesen. Ein Hinweis ist, dass der Abstand zwischen dem 4. und 5. Ring vergleichsweise größer ist.

Daher kann man die Lücke zwischen den beiden farbigen Ringen an einem Ende des Widerstands betrachten; ist sie größer als alle anderen Lücken, dann kann man von der gegenüberliegenden Seite ablesen.

Sehen wir uns an, wie man den Widerstandswert eines 5-bändigen Widerstands abliest, wie unten gezeigt.

|img_220ohm|

Für diesen Widerstand sollte der Widerstandswert von links nach rechts abgelesen werden. 
Der Wert sollte in folgendem Format vorliegen: 1. Band 2. Band 3. Band x 10^Multiplikator (Ω) und der zulässige Fehler beträgt ±Toleranz%. 
So beträgt der Widerstandswert dieses Widerstands 2(rot) 2(rot) 0(schwarz) x 10^0(schwarz) Ω = 220 Ω,
und der zulässige Fehler beträgt ± 1 % (braun).

.. list-table:: Übliche Widerstands-Farbcodes
   :header-rows: 1

   * - :ref:`cpn_resistor` 
     - Farbcode
   * - 10Ω   
     - braun schwarz schwarz silber braun
   * - 100Ω   
     - braun schwarz schwarz schwarz braun
   * - 220Ω 
     - rot rot schwarz schwarz braun
   * - 330Ω 
     - orange orange schwarz schwarz braun
   * - 1kΩ 
     - braun schwarz schwarz braun braun
   * - 2kΩ 
     - rot schwarz schwarz braun braun
   * - 5.1kΩ 
     - grün braun schwarz braun braun
   * - 10kΩ 
     - braun schwarz schwarz rot braun 
   * - 100kΩ 
     - braun schwarz schwarz orange braun 
   * - 1MΩ 
     - braun schwarz schwarz grün braun 


Mehr über Widerstände erfahren Sie auf der Wikipedia-Seite: `Widerstand – Wikipedia <https://de.wikipedia.org/wiki/Widerstand_(Bauelement)>`_.

