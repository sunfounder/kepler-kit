.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_mpu6050:

6.3 - 6-axis Motion Tracking
===================================

The MPU-6050 is a 6-axis(combines 3-axis Gyroscope, 3-axis Accelerometer) motion tracking devices.


An accelerometer is a tool that measures proper acceleration.For example, an accelerometer at rest on the surface of the Earth will measure an acceleration due to Earth's gravity, straight upwards[3] (by definition) of g ≈ 9.81 m/s2.

Accelerometers have many uses in industry and science. For example: inertial navigation systems for aircraft and missiles, for keeping images on tablets and digital cameras vertical, etc.

Gyroscopes are used to measure orientation and angular velocity of a device or maintenance.
Applications of gyroscopes include anti-rollover and airbag systems for automobiles, motion sensing systems for smart devices, attitude stabilization systems for drones, and more.

* :ref:`cpn_mpu6050`

**Required Components**

In this project, we need the following components. 

It's definitely convenient to buy a whole kit, here's the link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ITEMS IN THIS KIT
        - PURCHASE LINK
    *   - Kepler Kit	
        - 450+
        - |link_kepler_kit|

You can also buy them separately from the links below.


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - COMPONENT INTRODUCTION	
        - QUANTITY
        - PURCHASE LINK

    *   - 1
        - :ref:`cpn_pico_w`
        - 1
        - |link_picow_buy|
    *   - 2
        - Micro USB Cable
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Several
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_mpu6050`
        - 1
        - 

**Schematic**

|sch_mpu6050_ar|

**Wiring**

|wiring_mpu6050_ar|

**Code**

.. note::

    * You can open the file ``6.3_6axis_motion_tracking.ino`` under the path of ``euler-kit/arduino/6.3_6axis_motion_tracking``. 
    * Or copy this code into **Arduino IDE**.
    * Then select the Raspberry Pi Pico board and the correct port before clicking the Upload button.
    * The ``Adafruit MPU6050`` library is used here, you can install it from the **Library Manager**.

      .. image:: img/lib_mpu6050.png

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/318f62d3-1d7b-4ee6-a1a2-97e783cf2d5e/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>
    

After running the program, you can see the 3-axis accelerometer values and 3-axis gyroscope values cycling through the output.
At this point you rotate the MPU6050 at random, and these values will appear to change accordingly.
To make it easier to see the changes, you can comment out one of the print lines and concentrate on another set of data.


**How it works?**

Instantiate an ``MPU6050`` object.

.. code-block:: arduino

    #include <Adafruit_MPU6050.h>
    #include <Wire.h>

    Adafruit_MPU6050 mpu;


Initialize the MPU6050 and set its accuracy.

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

Get new sensor events with the readings.

.. code-block:: arduino

    sensors_event_t a, g, temp;
    mpu.getEvent(&a, &g, &temp);

Subsequently, you will be able to get real-time acceleration and angular velocity values in the data ``a.acceleration.x``, ``a.acceleration.y``, ``a.acceleration.z``, ``g.gyro.x``, ``g.gyro.y``, ``g.gyro.z``.

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