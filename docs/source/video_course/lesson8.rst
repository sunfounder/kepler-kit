.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Lektion 8: Zusammengesetzte Bedingungen und If-Anweisungen in MicroPython
===============================================================================

Dieses Tutorial behandelt die Verwendung eines Potentiometers zur Steuerung von drei LEDs (grün, gelb und rot) mit dem Raspberry Pi Pico W und identifiziert einen kritischen logischen Fehler in der vorherigen Implementierung:

* **Überprüfung der Hausaufgabenlösung**: Fasst die vorherige Aufgabe zusammen, den logischen Fehler im Code zu finden, der die LEDs basierend auf den Potentiometerwerten steuerte.
* **Erklärung des logischen Fehlers**: Erläutert den logischen Fehler im Code, bei dem sich die LED-Zustände überlappen konnten, was zu unbeabsichtigtem Verhalten führte. Betont die Bedeutung sicherzustellen, dass logische Bedingungen sich gegenseitig ausschließen, um solche Fehler zu vermeiden.
* **Beispiel aus der Praxis**: Veranschaulicht die potenziellen Gefahren logischer Fehler anhand eines hypothetischen Szenarios von UV-Sterilisationsräumen, bei dem eine falsche LED-Steuerung Schaden verursachen könnte.
* **Einführung in zusammengesetzte Bedingungen**: Führt zusammengesetzte Bedingungen unter Verwendung logischer Operatoren (UND, ODER) ein, um präzise Bedingungen für die Steuerung der LEDs zu schaffen. Zeigt, wie man sicherstellt, dass jede Bedingung korrekt implementiert wird, um Überlappungen zu vermeiden.
* **Schaltungsaufbau und Code-Erklärung**: Bietet ein detailliertes Schaltbild und die Einrichtung zum Anschließen des Potentiometers und der LEDs an den Raspberry Pi Pico W. Diskutiert die korrekte Art, bedingte Anweisungen zu schreiben, um die LEDs basierend auf den Potentiometerwerten zu steuern.
* **Praktische Demonstration**: Zeigt den überarbeiteten Code in Aktion und hebt das korrekte LED-Verhalten ohne Überlappungen oder verpasste Bedingungen hervor. Betont die Bedeutung sorgfältiger logischer Planung in Coding-Projekten.
* **Nächste Schritte**: Vorschau auf die nächste Lektion zur Simulation analoger Ausgaben, die das Toolkit für die Arbeit mit dem Raspberry Pi Pico W weiter erweitern wird.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/uTwm3ydI69w?si=2OJPTawMlFfqO_DN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
