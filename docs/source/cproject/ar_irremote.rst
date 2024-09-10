.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_irremote:

6.4 - IR-Fernbedienung
=======================

Im Bereich der Unterhaltungselektronik dienen Fernbedienungen zur Steuerung von Geräten wie Fernsehern und DVD-Playern. In einigen Fällen ermöglichen sie die Bedienung von Geräten, die außer Reichweite sind, etwa Zentral-Klimaanlagen.

Ein IR-Empfänger ist ein Bauteil mit einer Fotozelle, die auf Infrarotlicht abgestimmt ist. Er wird fast immer zur Fernbedienungserkennung eingesetzt - jeder Fernseher und DVD-Player hat einen solchen an der Vorderseite, um das IR-Signal vom Bediengerät zu empfangen. In der Fernbedienung selbst ist eine passende IR-LED, die IR-Impulse sendet, um den Fernseher ein- oder auszuschalten oder den Kanal zu wechseln.

* :ref:`cpn_ir_receiver`

**Benötigte Komponenten**

Für dieses Projekt werden die folgenden Komponenten benötigt. 

Es ist durchaus praktisch, ein komplettes Set zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ARTIKEL IN DIESEM SET
        - KAUF-LINK
    *   - Kepler Kit
        - 450+
        - |link_kepler_kit|

Sie können die Komponenten auch einzeln über die folgenden Links erwerben.

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
        - :ref:`cpn_ir_receiver`
        - 1
        - |link_receiver_buy|

**Schaltplan**

|sch_irrecv|

**Verdrahtung**

|wiring_irrecv|

**Code**

.. note::

    * Die Datei ``6.4_ir_remote_control.ino`` finden Sie unter dem Pfad ``kepler-kit-main/arduino/6.4_ir_remote_control``.
    * Oder kopieren Sie den Code in die **Arduino IDE**.
    * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den richtigen Port auszuwählen, bevor Sie auf den **Hochladen**-Button klicken.
    * Die Bibliothek ``IRremote`` wird hier verwendet. Sie können sie über den **Bibliotheksmanager** installieren.

      .. image:: img/lib_ir.png
    
.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/71f50561-d1ad-4d9e-9db2-8eb7727df0a4/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Die neue Fernbedienung enthält ein Plastikstück am Ende, das die Batterie isoliert. Dieses Plastikstück muss entfernt werden, um die Fernbedienung in Betrieb zu nehmen. Sobald das Programm läuft und Sie die Fernbedienung drücken, wird der Serial Monitor den gedrückten Knopf ausgeben.

**Funktionsweise**

Dieser Code ist dafür ausgelegt, mit einer Infrarot (IR)-Fernbedienung unter Verwendung der ``IRremote``-Bibliothek zu arbeiten. Hier ist die Aufschlüsselung:

#. Einbindung der Bibliothek und Definition von Konstanten. Zuerst wird die IRremote-Bibliothek eingebunden, und die Pinnummer für den IR-Empfänger wird als 2 definiert.

   .. code-block:: cpp

     #include <IRremote.h>
     const int IR_RECEIVE_PIN = 17;

#. Initialisiert die serielle Kommunikation mit einer Baudrate von 9600. Initialisiert den IR-Empfänger am angegebenen Pin (``IR_RECEIVE_PIN``) und aktiviert die LED-Rückmeldung (falls zutreffend).

   .. code-block:: arduino

       void setup() {
           Serial.begin(9600);                                     // Starte serielle Kommunikation mit 9600 Baudrate
           IrReceiver.begin(IR_RECEIVE_PIN, ENABLE_LED_FEEDBACK);  // Starte den IR-Empfänger
       }

#. Die Schleife läuft kontinuierlich, um eingehende IR-Fernbedienungssignale zu verarbeiten.

   .. code-block:: arduino

      void loop() {
         if (IrReceiver.decode()) {  // Überprüfe, ob der IR-Empfänger ein Signal empfangen hat
            bool result = 0;
            String key = decodeKeyValue(IrReceiver.decodedIRData.command);
            if (key != "ERROR") {
              Serial.println(key);  // Gib den lesbaren Befehl aus
              delay(100);
            }
         IrReceiver.resume();  // Bereite den IR-Empfänger darauf vor, das nächste Signal zu empfangen
        }
      }

   * Überprüft, ob ein IR-Signal empfangen und erfolgreich dekodiert wurde.
   * Dekodiert den IR-Befehl und speichert ihn in ``decodedValue`` unter Verwendung einer benutzerdefinierten ``decodeKeyValue()``-Funktion.
   * Gibt den dekodierten IR-Wert im seriellen Monitor aus.
   * Setzt den Empfang von IR-Signalen für das nächste Signal fort.

   .. raw:: html

        <br/>

#. Hilfsfunktion zur Zuordnung der empfangenen IR-Signale zu den entsprechenden Tasten

   .. image:: img/ir_key.png
      :align: center
      :width: 80%

   .. code-block:: arduino

      // Function to map received IR signals to corresponding keys
      String decodeKeyValue(long result) {
        // Each case corresponds to a specific IR command
        switch (result) {
          case 0x16:
            return "0";
          case 0xC:
            return "1";
          case 0x18:
            return "2";
          case 0x5E:
            return "3";
          case 0x8:
            return "4";
          case 0x1C:
            return "5";
          case 0x5A:
            return "6";
          case 0x42:
            return "7";
          case 0x52:
            return "8";
          case 0x4A:
            return "9";
          case 0x9:
            return "+";
          case 0x15:
            return "-";
          case 0x7:
            return "EQ";
          case 0xD:
            return "U/SD";
          case 0x19:
            return "CYCLE";
          case 0x44:
            return "PLAY/PAUSE";
          case 0x43:
            return "FORWARD";
          case 0x40:
            return "BACKWARD";
          case 0x45:
            return "POWER";
          case 0x47:
            return "MUTE";
          case 0x46:
            return "MODE";
          case 0x0:
            return "ERROR";
          default:
            return "ERROR";
        }
      }
