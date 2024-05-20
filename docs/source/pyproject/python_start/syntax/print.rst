.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

Print()
=====================

Die Funktion ``print()`` gibt die angegebene Nachricht auf dem Bildschirm oder einem anderen Standardausgabegerät aus. Die Nachricht kann eine Zeichenkette oder ein beliebiges anderes Objekt sein. Das Objekt wird vor der Ausgabe auf dem Bildschirm in eine Zeichenkette umgewandelt.

Mehrere Objekte ausgeben:



.. code-block:: python

    print("Willkommen!", "Viel Spaß!")

>>> %Run -c $EDITOR_CONTENT
Willkommen! Viel Spaß!

Tupel ausgeben:



.. code-block:: python

    x = ("Birne", "Apfel", "Traube")
    print(x)

>>> %Run -c $EDITOR_CONTENT
('Birne', 'Apfel', 'Traube')

Zwei Nachrichten ausgeben und das Trennzeichen festlegen:



.. code-block:: python

    print("Hallo", "wie geht's?", sep="---")

>>> %Run -c $EDITOR_CONTENT
Hallo---wie geht's?
