.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_diode:

Diode
=================

|img_diode|

Eine Diode ist ein elektronisches Bauelement mit zwei Elektroden, das den Stromfluss nur in einer Richtung zulässt. Diese Funktion wird oft als "Gleichrichtung" bezeichnet. Somit kann die Diode als elektronisches Äquivalent eines Rückschlagventils betrachtet werden.

Die beiden Anschlüsse einer Diode sind polarisiert; das positive Ende wird Anode und das negative Ende Kathode genannt. Die Kathode ist üblicherweise aus Silber oder durch einen Farbring gekennzeichnet. Eine der Schlüsseleigenschaften von Dioden ist die Steuerung der Stromrichtung — der Strom fließt von der Anode zur Kathode. Das Verhalten einer Diode ist ähnlich dem eines Rückschlagventils. Eine wesentliche Charakteristik ist die nicht-lineare Strom-Spannungs-Kennlinie. Wird eine höhere Spannung an der Anode angelegt, fließt Strom von der Anode zur Kathode; dieser Zustand wird als Vorwärtsbias bezeichnet. Im umgekehrten Fall, also wenn die höhere Spannung an der Kathode anliegt, leitet die Diode keinen Strom; dieser Zustand wird als Rückwärtsbias bezeichnet.

Aufgrund ihrer unidirektionalen Leitfähigkeit findet die Diode in nahezu allen komplexeren elektronischen Schaltungen Verwendung. Sie war eines der ersten Halbleiterbauelemente und ihre Anwendungsgebiete sind vielfältig.

In der Realität weisen Dioden jedoch keine perfekte Ein- und Ausschaltcharakteristik auf, sondern vielmehr komplexe nicht-lineare elektronische Eigenschaften, die von der spezifischen Diodentechnologie abhängen.

Eine Diode ist ein p-n-Übergang, gebildet durch einen p-Typ- und einen n-Typ-Halbleiter. An der Grenzfläche bildet sich eine Raumladungszone mit einem Eigenfeld aus. In elektrischem Gleichgewicht gleichen sich die Drift- und Diffusionsströme aus. Bei Vorwärtsbias verstärken sich die externen und das Eigenfeld, wodurch die Leitfähigkeit zunimmt. Bei Rückwärtsbias wird ein Sättigungsstrom I0 erzeugt, der von der angelegten Spannung unabhängig ist.

**1. Vorwärtscharakteristik**

Bei Anlegen einer Vorwärtsspannung bleibt der Strom anfangs nahezu null, da die Spannung die Raumladungszone nicht überwinden kann. Dieser Bereich wird als Sperrbereich bezeichnet. Erst bei Überschreitung dieser Spannung beginnt der Strom stark anzusteigen.

**2. Rückwärtscharakteristik**

Bei Anlegen einer Rückwärtsspannung bleibt der Stromfluss gering und wird als Sättigungs- oder Leckstrom bezeichnet, der stark temperaturabhängig ist.

**3. Durchbruch**

Überschreitet die Rückwärtsspannung einen bestimmten Wert, steigt der Stromfluss schlagartig an, was als elektrischer Durchbruch bekannt ist. Die dafür erforderliche Spannung wird als Durchbruchspannung bezeichnet.

Frühe Dioden bestanden aus "Katzenfaden"-Kristallen und Vakuumröhren. Heutige Dioden verwenden Halbleitermaterialien wie Silizium oder Germanium.

* `P–N-Übergang - Wikipedia <https://de.wikipedia.org/wiki/Pn-Übergang>`_
 
* `Diode - Wikipedia <https://de.wikipedia.org/wiki/Diode>`_
