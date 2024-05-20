.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_pir:

2.10 - Detect Human Movement
=========================================

Passive infrared sensor (PIR sensor) is a common sensor that can measure infrared (IR) light emitted by objects in its field of view.
Simply put, it will receive infrared radiation emitted from the body, thereby detecting the movement of people and other animals.
More specifically, it tells the main control board that someone has entered your room.

:ref:`cpn_pir`

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
        - :ref:`cpn_pir`
        - 1
        - |link_pir_buy|


**Schematic**

|sch_pir|

When the PIR module detects someone passing by, GP14 will be high, otherwise it will be low.



**Wiring**

|wiring_pir|

**Code**

.. note::

   * You can open the file ``2.10_detect_human_movement.ino`` under the path of ``kepler-kit-main/arduino/2.10_detect_human_movement``. 
   * Or copy this code into **Arduino IDE**.


    * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.



.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/bb3ff9f1-127d-4279-84b9-cba28b9667e8/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>
    

After the program runs, if the PIR module detects someone nearby, the Serial Monitor will print out "Somebody here!" 


**Learn More**

PIR is a very sensitive sensor. In order to adapt it to the environment of use, 
it needs to be adjusted. Let the side with the 2 potentiometers facing you, 
turn both potentiometers counterclockwise to the end and insert the jumper cap on the pin with L and the middle pin.



|img_pir_back|

1. Trigger Mode

    Let's take a look at the pins with jumper cap at the corner.
    It allows PIR to enter Repeatable trigger mode or Non-repeatable trigger mode

    At present, our jumper cap connects the middle Pin and L Pin, which makes the PIR in non-repeatable trigger mode.
    In this mode, when the PIR detects the movement of the organism, it will send a high-level signal for about 2.8 seconds to the main control board.
    .. We can see in the printed data that the duration of work will always be around 2800ms.

    Next, we modify the position of the lower jumper cap and connect it to the middle Pin and H Pin to make the PIR in repeatable trigger mode.
    In this mode, when the PIR detects the movement of the organism (note that it is movement, not static in front of the sensor), as long as the organism keeps moving within the detection range, the PIR will continue to send a high-level signal to the main control board.
    .. We can see in the printed data that the duration of work is an uncertain value.

#. Delay Adjustment

    The potentiometer on the left is used to adjust the interval between two jobs.
    
    At present, we screw it counterclockwise to the end, which makes the PIR need to enter a sleep time of about 5 seconds after finishing sending the high level work. During this time, the PIR will no longer detect the infrared radiation in the target area.
    .. We can see in the printed data that the dormancy duration is always no less than 5000ms.

    If we turn the potentiometer clockwise, the sleep time will also increase. When it is turned clockwise to the end, the sleep time will be as high as 300s.

#. Distance Adjustment

    The centered potentiometer is used to adjust the sensing distance range of the PIR.

    Turn the knob of the distance adjustment potentiometer **clockwise** to increase the sensing distance range, and the maximum sensing distance range is about 0-7 meters.
    If it rotates **counterclockwise**, the sensing distance range is reduced, and the minimum sensing distance range is about 0-3 meters.