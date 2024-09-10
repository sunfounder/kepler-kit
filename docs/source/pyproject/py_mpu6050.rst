.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_mpu6050:

6.3 6-Achsen-Bewegungsverfolgung
=====================================

Der MPU-6050 ist ein 6-Achsen-Sensor, der einen 3-Achsen-Gyroskop und einen 3-Achsen-Beschleunigungsmesser kombiniert.

Ein Beschleunigungsmesser ist ein Instrument zur Messung der Eigenbeschleunigung. Ein am Erdboden ruhender Beschleunigungsmesser misst beispielsweise eine Beschleunigung in Richtung der Erdanziehung von etwa g ≈ 9.81 m/s2.

Beschleunigungsmesser finden in Industrie und Wissenschaft vielfältige Anwendung, beispielsweise in Trägheitsnavigationssystemen für Flugzeuge und Raketen, zur Bilddarstellung in Tablets und Digitalkameras und vieles mehr.

Gyroskope dienen der Messung der Orientierung und der Winkelgeschwindigkeit eines Geräts. Einsatzgebiete für Gyroskope umfassen Anti-Kipp- und Airbagsysteme für Automobile, Bewegungssensoren für intelligente Geräte, Lagestabilisierungssysteme für Drohnen und vieles mehr.

* :ref:`cpn_mpu6050`

**Erforderliche Komponenten**

Für dieses Projekt benötigen wir folgende Bauteile.

Ein komplettes Kit zu erwerben, ist natürlich praktisch. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Bezeichnung
        - KOMPONENTEN IM KIT
        - LINK
    *   - Kepler-Kit
        - 450+
        - |link_kepler_kit|

Die Komponenten können auch einzeln über die folgenden Links bezogen werden:

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTE
        - MENGE
        - LINK

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

    * Öffnen Sie die Datei ``6.3_6axis_motion_tracking.py`` im Verzeichnis ``kepler-kit-main/micropython`` oder kopieren Sie den Code in Thonny. Dann klicken Sie auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.

    * Wählen Sie im rechten unteren Eck den "MicroPython (Raspberry Pi Pico)"-Interpreter.

    * Für detaillierte Anleitungen siehe :ref:`open_run_code_py`.
    
    * Hier benötigen Sie die Bibliotheken ``imu.py`` und ``vector3d.py``. Stellen Sie sicher, dass diese auf dem Pico W hochgeladen wurden. Eine detaillierte Anleitung finden Sie unter :ref:`add_libraries_py`.

.. code-block:: python

    from imu import MPU6050
    from machine import I2C, Pin
    import time

    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
    mpu = MPU6050(i2c)

    while True:
        print("x: %s, y: %s, z: %s"%(mpu.accel.x, mpu.accel.y, mpu.accel.z))
        time.sleep(0.5)
        print("A: %s, B: %s, Y: %s"%(mpu.gyro.x, mpu.gyro.y, mpu.gyro.z))
        time.sleep(0.5)

Nach dem Ausführen des Programms sehen Sie die Werte des 3-Achsen-Beschleunigungsmessers und des 3-Achsen-Gyroskops in der Ausgabe rotieren. Drehen Sie den MPU6050 beliebig, und Sie werden feststellen, dass sich die Werte entsprechend ändern.
Um die Änderungen besser erkennen zu können, können Sie eine der Ausgabelinien auskommentieren und sich auf einen Datensatz konzentrieren.

Die Einheit des Beschleunigungswerts ist „m/s²“ und die Einheit des Gyroskopwerts ist „°/s“.

**Wie funktioniert es?**

In der imu-Bibliothek haben wir die relevanten Funktionen in der Klasse ``MPU6050`` integriert.
Der MPU6050 ist ein I2C-Modul und erfordert für die Initialisierung definierte I2C-Pins.

.. code-block:: python

    from imu import MPU6050
    from machine import I2C, Pin

    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
    mpu = MPU6050(i2c)

In der Folge können Sie Echtzeit-Beschleunigungs- und Winkelgeschwindigkeitswerte in ``mpu.accel.x``, ``mpu.accel.y``, ``mpu.accel.z``, ``mpu.gyro.x``, ``mpu.gyro.y``, ``mpu.gyro.z`` abrufen.

.. code-block:: python

    while True:
        print("x: %s, y: %s, z: %s"%(mpu.accel.x, mpu.accel.y, mpu.accel.z))
        time.sleep(0.5)
        print("A: %s, B: %s, Y: %s"%(mpu.gyro.x, mpu.gyro.y, mpu.gyro.z))
        time.sleep(0.5)
