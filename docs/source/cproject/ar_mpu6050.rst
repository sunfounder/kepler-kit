.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_mpu6050:

6.3 - 6-Achsen-Bewegungsverfolgung
===================================

Der MPU-6050 ist ein 6-Achsen-Bewegungsverfolgungsgerät, das einen 3-Achsen-Gyroskop mit einem 3-Achsen-Beschleunigungsmesser kombiniert.

Ein Beschleunigungsmesser ist ein Instrument, das die Eigengeschwindigkeitsänderung misst. Ein in Ruhe auf der Erdoberfläche liegender Beschleunigungsmesser würde beispielsweise eine Beschleunigung durch die Erdanziehungskraft von etwa g ≈ 9,81 m/s² in Richtung der Erdoberfläche messen.

Beschleunigungsmesser haben zahlreiche Anwendungen in Industrie und Wissenschaft. Beispiele hierfür sind Trägheitsnavigationssysteme für Flugzeuge und Raketen, Systeme zur Ausrichtung von Bildern auf Tablets und Digitalkameras und so weiter.

Gyroskope werden verwendet, um die Ausrichtung und Winkelgeschwindigkeit eines Geräts oder Systems zu messen. Einsatzgebiete für Gyroskope sind unter anderem Anti-Roll-Systeme und Airbags in Automobilen, Bewegungserfassungssysteme für Smart-Geräte, Lageregelungssysteme für Drohnen und mehr.

* :ref:`cpn_mpu6050`

**Erforderliche Komponenten**

Für dieses Projekt benötigen wir folgende Komponenten.

Es ist definitiv praktisch, ein komplettes Kit zu kaufen. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ARTIKEL IN DIESEM KIT
        - KAUF-LINK
    *   - Kepler-Kit
        - 450+
        - |link_kepler_kit|

Sie können die Komponenten auch einzeln über die untenstehenden Links erwerben.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTENBESCHREIBUNG
        - MENGE
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
        - :ref:`cpn_mpu6050`
        - 1
        -

**Schaltplan**

|sch_mpu6050|

**Verkabelung**

|wiring_mpu6050|

**Code**

.. note::

    * Sie können die Datei ``6.3_6axis_motion_tracking.ino`` im Verzeichnis ``kepler-kit-main/arduino/6.3_6axis_motion_tracking`` öffnen.
    * Oder kopieren Sie diesen Code in die **Arduino IDE**.
    * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den entsprechenden Port auszuwählen, bevor Sie auf die **Hochladen**-Taste klicken.
    * Die Bibliothek ``Adafruit_MPU6050`` wird hier verwendet. Bitte beziehen Sie sich auf :ref:`add_libraries_ar`, um sie zur Arduino IDE hinzuzufügen.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/318f62d3-1d7b-4ee6-a1a2-97e783cf2d5e/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


Nach dem Ausführen des Programms können Sie die Werte des 3-Achsen-Beschleunigungsmessers und des 3-Achsen-Gyroskops in der Ausgabe sehen. Wenn Sie den MPU6050 zufällig drehen, werden diese Werte entsprechend variieren. Um die Änderungen besser verfolgen zu können, können Sie eine der Ausgabezeilen auskommentieren und sich auf einen anderen Datensatz konzentrieren.


**Wie funktioniert es?**

Erzeugen Sie ein ``MPU6050``-Objekt.

.. code-block:: arduino

    #include <Adafruit_MPU6050.h>
    #include <Wire.h>

    Adafruit_MPU6050 mpu;


Initialisieren Sie den MPU6050 und konfigurieren Sie seine Genauigkeit.

.. code-block:: arduino

    void setup(void) {
        Serial.begin(115200);
        while (!Serial)
            delay(10); // will pause Zero, Leonardo, etc until serial console opens

        Serial.println("Adafruit MPU6050 test!");

        // Try to initialize!
        if (!mpu.begin()) {
            Serial.println("Failed to find MPU6050 chip");
            while (1) {
            delay(10);
            }
        }
        Serial.println("MPU6050 Found!");

        // Set range
        mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
        mpu.setGyroRange(MPU6050_RANGE_500_DEG);
        mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);

        Serial.println("");
        delay(100);
    }

Erfassen Sie neue Sensorevents mit den dazugehörigen Messwerten.

.. code-block:: arduino

    sensors_event_t a, g, temp;
    mpu.getEvent(&a, &g, &temp);

Im Anschluss können Sie Echtzeit-Werte für Beschleunigung und Winkelgeschwindigkeit aus den Daten ``a.acceleration.x``, ``a.acceleration.y``, ``a.acceleration.z``, ``g.gyro.x``, ``g.gyro.y``, ``g.gyro.z`` ablesen.

.. code-block:: arduino

    Serial.print("Acceleration X: ");
    Serial.print(a.acceleration.x);
    Serial.print(", Y: ");
    Serial.print(a.acceleration.y);
    Serial.print(", Z: ");
    Serial.print(a.acceleration.z);
    Serial.println(" m/s^2");

    Serial.print("Rotation X: ");
    Serial.print(g.gyro.x);
    Serial.print(", Y: ");
    Serial.print(g.gyro.y);
    Serial.print(", Z: ");
    Serial.print(g.gyro.z);
    Serial.println(" rad/s");

