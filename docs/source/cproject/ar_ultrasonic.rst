.. _ar_ultrasonic:

6.1 - Measuring Distance
======================================

The ultrasonic sensor module works on the principle of sonar and radar systems for determining the distance to an object.

* :ref:`cpn_ultrasonic`

**Schematic**

|sch_ultrasonic|

**Wiring**

|wiring_ultrasonic|

**Code**

.. note::

   * You can open the file ``6.1_ultrasonic.ino`` under the path of ``kepler-kit-main/arduino/6.1_ultrasonic``. 
   * Or copy this code into **Arduino IDE**.
   * For detailed tutorials, please refer to :ref:`open_run_code_ar`.
   * Or run this code directly in the `Arduino Web Editor <https://docs.arduino.cc/cloud/web-editor/tutorials/getting-started/getting-started-web-editor>`_.

    Don't forget to select the Raspberry Pi Pico W board and the correct port before clicking the Upload button.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/631a1663-ce45-4d46-b8f0-7d10f32097a9/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


Once the program is running, the Serial Monitor will print out the distance of the ultrasonic sensor from the obstacle ahead.


**How it works?**

About the application of ultrasonic sensor, we can directly check the
subfunction.

.. code-block:: arduino

    float readSensorData(){// ...}

``PING`` is triggered by a HIGH pulse of 2 or more microseconds. (Give a
short ``LOW`` pulse beforehand to ensure a clean ``HIGH`` pulse.)

.. code-block:: arduino

    digitalWrite(trigPin, LOW); 
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH); 
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW); 

The echo pin is used to read signal from PING, a ``HIGH`` pulse whose
duration is the time (in microseconds) from the sending of the ping to
the reception of echo of the object.

.. code-block:: arduino

    microsecond=pulseIn(echoPin, HIGH);

The speed of sound is 340 m/s or 29 microseconds per centimeter.

This gives the distance travelled by the ping, outbound and return, so
we divide by 2 to get the distance of the obstacle.

.. code-block:: arduino

    float distance = microsecond / 29.00 / 2;  


Note that the ultrasonic sensor will pause the program when it is working, which may cause some lagging when writing complex projects.

