

.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_somato_controller:


7.11 Somatosensorische Steuerung
====================================

Wenn Sie viele Robotik-Filme gesehen haben, ist Ihnen diese Vorstellung wahrscheinlich nicht fremd. Der Protagonist bewegt sein Handgelenk und der riesige Roboter folgt der Bewegung; der Protagonist ballt die Faust, und auch der Roboter tut dies. Es sieht einfach cool aus.

Diese Technologie findet bereits breite Anwendung in Universitäten und Forschungsinstituten. Die Einführung von 5G wird ihre Einsatzmöglichkeiten erheblich erweitern. Ein typisches Beispiel hierfür ist die Fernbedienung des "Chirurgie-Roboters da Vinci".

Ein Robotiksystem dieser Art besteht in der Regel aus zwei Modulen: einem Modul zur Erfassung menschlicher Bewegungen und einem Aktuator-Modul für den Roboterarm (in manchen Anwendungen gibt es auch ein Datenkommunikationsmodul).

Hier kommt der MPU6050 zum Einsatz, um menschliche Bewegungen zu erfassen (indem er an einem Handschuh befestigt wird), während ein Servomotor die Bewegung des Roboterarms simuliert.

**Benötigte Komponenten**

Für dieses Projekt werden die folgenden Komponenten benötigt.

Ein Gesamtkit zu erwerben ist definitiv praktisch. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Bezeichnung	
        - ARTIKEL IN DIESEM KIT
        - LINK
    *   - Kepler-Set	
        - 450+
        - |link_kepler_kit|

Alternativ können die Komponenten auch einzeln über die unten stehenden Links gekauft werden.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTE	
        - ANZAHL
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
    *   - 6
        - :ref:`cpn_servo`
        - 1
        - |link_servo_buy|


**Schaltplan**

|sch_somato|

Der MPU6050 berechnet den Neigungswinkel basierend auf den Beschleunigungswerten in jeder Richtung.

Das Programm steuert den Servomotor so, dass er den entsprechenden Auslenkwinkel gemäß dem sich ändernden Neigungswinkel ausführt.

**Verdrahtung**

|wiring_somatosensory_controller|


**Code**

.. note::

    * Öffnen Sie die Datei ``7.11_somatosensory_controller.py`` im Verzeichnis ``kepler-kit-main/micropython`` oder kopieren Sie den unten stehenden Code in Thonny. Klicken Sie dann auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.
    * Vergewissern Sie sich, dass der Interpreter "MicroPython (Raspberry Pi Pico)" in der unteren rechten Ecke ausgewählt ist.

    * Für detaillierte Anleitungen siehe :ref:`open_run_code_py`.
    * Hier müssen Sie auch die Dateien ``imu.py`` und ``vector3d.py`` verwenden. Bitte überprüfen Sie, ob sie auf Pico W hochgeladen wurden. Detaillierte Anweisungen finden Sie unter :ref:`add_libraries_py`.


.. code-block:: python

    from imu import MPU6050
    from machine import I2C, Pin
    import time
    import math

    # Initialize I2C communication for MPU6050 accelerometer
    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
    mpu = MPU6050(i2c)

    # Initialize PWM for the servo on pin 16 with a frequency of 50Hz
    servo = machine.PWM(machine.Pin(16))
    servo.freq(50)

    # Function to map a value from one range to another
    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    # Function to calculate the Euclidean distance between two points
    def dist(a, b):
        return math.sqrt((a * a) + (b * b))

    # Function to calculate the rotation along the y-axis
    def get_y_rotation(x, y, z):
        radians = math.atan2(x, dist(y, z))
        return -math.degrees(radians)

    # Function to calculate the rotation along the x-axis
    def get_x_rotation(x, y, z):
        radians = math.atan2(y, dist(x, z))
        return math.degrees(radians)

    # Function to control the servo based on the angle
    # Maps the angle (0-180) to the PWM duty cycle for servo control
    def servo_write(pin, angle):
        pulse_width = interval_mapping(angle, 0, 180, 0.5, 2.5)  # Map angle to pulse width in ms (0.5ms to 2.5ms)
        duty = int(interval_mapping(pulse_width, 0, 20, 0, 65535))  # Convert pulse width to PWM duty cycle (0-65535)
        pin.duty_u16(duty)  # Set the duty cycle for the servo PWM

    # Define the number of readings to average for smoother motion
    times = 25

    # Main loop
    while True:
        total = 0
        # Take multiple readings to average the angle for smoothness
        for i in range(times):
            angle = get_y_rotation(mpu.accel.x, mpu.accel.y, mpu.accel.z)  # Get the y-axis rotation value from the accelerometer
            total += angle  # Accumulate the readings

        average_angle = int(total / times)  # Calculate the average angle
        # Map the average angle (-90 to 90) to the servo's movement range (0 to 180 degrees)
        servo_write(servo, interval_mapping(average_angle, -90, 90, 0, 180))

        time.sleep(0.1)  # Add a small delay to reduce jitter in the servo movement

Sobald das Programm läuft, wird der Servomotor sich nach links und rechts drehen, wenn Sie den MPU6050 neigen (oder Ihr Handgelenk bewegen, falls er an einem Handschuh montiert ist).


