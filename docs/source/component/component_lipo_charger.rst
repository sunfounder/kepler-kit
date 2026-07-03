.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_lipo_charger:

Li-Po-Lademodul
=================================================

|lipo_module|

Dies ist ein Li-Po-Lademodul, konzipiert für Raspberry Pi Pico/Pico H/Pico W. Einfach einstecken und den Pico auf dem Steckbrett wie unten gezeigt positionieren. Danach die Batterie am anderen Ende anschließen und schon kann es losgehen.

Wenn das Pico W über ein USB-Kabel an einen Computer oder eine Steckdose angeschlossen wird, leuchtet die Kontrollleuchte auf dem Li-Po-Lademodul auf. Dies signalisiert, dass die Batterie gleichzeitig geladen wird. Wird das USB-Kabel entfernt, wird das Pico W von der Batterie versorgt, sodass Ihr Projekt weiterhin läuft.

.. note::
    Bei einigen leistungsschwachen Computern kann es vorkommen, dass das Pico W nicht erkannt wird, wenn es mit dem angeschlossenen Lademodul an den Computer angeschlossen wird.

    Der Grund dafür ist, dass die USB-Port-Spannung beim Laden der Batterie abfällt, was dazu führt, dass die Stromversorgung des Pico W nicht ausreicht, um vom Computer erkannt zu werden.

    In diesem Fall muss das Li-Po-Lademodul entfernt und das Pico W erneut eingesteckt werden.

|lipo_wire|

**Eigenschaften**

* Eingangsspannung: 5V
* Ausgangsspannung: 3,3V
* Größe: 20mmx7mm
* Schnittstellenmodell: PH2.0
* Es gibt einen passenden 1A-Batteriehalter sowie einen 800mAh Power Pack, der zusammen verwendet werden kann.

**Schaltplan**

|sch_lipo_charger|

