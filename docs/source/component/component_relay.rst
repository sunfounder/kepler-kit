.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_relay:

Relais
==========================================

|img_relay|

Wie bekannt ist, dient ein Relais dazu, eine Verbindung zwischen zwei oder mehr Punkten oder Geräten herzustellen, die auf ein eingegebenes Signal reagieren. Anders ausgedrückt, bieten Relais eine Isolation zwischen dem Controller und dem Gerät, da diese sowohl mit Wechselstrom (AC) als auch mit Gleichstrom (DC) betrieben werden können. Da sie jedoch Signale von einem Mikrocontroller erhalten, der mit Gleichstrom arbeitet, ist ein Relais erforderlich, um die Lücke zu schließen. Relais sind besonders nützlich, wenn man einen großen Strom oder eine hohe Spannung mit einem kleinen elektrischen Signal steuern muss.

Ein Relais besteht aus fünf Hauptkomponenten:

**Elektromagnet** - Er besteht aus einem Eisenkern, der von einer Spule umwickelt ist. Wenn Strom durchfließt, wird er magnetisch. Deshalb wird er als Elektromagnet bezeichnet.

**Anker** - Der bewegliche magnetische Streifen wird als Anker bezeichnet. Wenn Strom durch die Spule fließt, wird sie magnetisiert und erzeugt ein Magnetfeld, das dazu dient, die normalerweise offenen (N/O) oder normalerweise geschlossenen (N/C) Kontakte herzustellen oder zu trennen. Der Anker kann sowohl mit Gleichstrom (DC) als auch mit Wechselstrom (AC) bewegt werden.

**Feder** - Wenn kein Strom durch die Spule des Elektromagneten fließt, zieht die Feder den Anker zurück, sodass der Stromkreis nicht geschlossen werden kann.

**Elektrische Kontakte** - Es gibt zwei Kontaktstellen:

-  Normalerweise offen - verbunden, wenn das Relais aktiviert ist, und getrennt, wenn es inaktiv ist.
  
-  Normalerweise geschlossen - nicht verbunden, wenn das Relais aktiviert ist, und verbunden, wenn es inaktiv ist.

**Gehäuse** - Relais sind zum Schutz mit Kunststoff ummantelt.

Das Funktionsprinzip eines Relais ist einfach. Wenn Strom an das Relais angelegt wird, fließt der Strom durch die Steuerspule; daraufhin beginnt der Elektromagnet sich zu magnetisieren. Der Anker wird dann zur Spule hingezogen, und der bewegliche Kontakt zieht mit und verbindet sich mit den normalerweise offenen Kontakten. Somit wird der Laststromkreis eingeschaltet. Um den Stromkreis wieder zu unterbrechen, wird der bewegliche Kontakt durch die Kraft der Feder zu den normalerweise geschlossenen Kontakten zurückgezogen. Auf diese Weise kann das Ein- und Ausschalten des Relais den Zustand eines Laststromkreises steuern.

|img_relay_sche|

* `Relais - Wikipedia <https://de.wikipedia.org/wiki/Relais>`_

**Beispiel**

* :ref:`py_relay` (Für MicroPython-Nutzer)
* :ref:`ar_relay` (Für Arduino-Nutzer)
