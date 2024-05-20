.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!


1.4 Install libraries (Important)
======================================

**Download the Code**

Download the relevant code from the link below.

* :download:`SunFounder Kepler Kit Example <https://github.com/sunfounder/kepler-kit/archive/refs/heads/main.zip>`

* Or check out the code at `Kepler Kit - GitHub <https://github.com/sunfounder/kepler-kit>`_

.. _add_libraries_ar:

Add libraries
----------------------
A library, gathering some function definitions and header files, usually
contains two files: .h (header file, including function statement, Macro
definition, constructor definition, etc.) and .cpp (execution file, with
function implementation, variable definition, and so on). When you need
to use a function in some library, you just need to add a header file
(e.g. #include <dht.h>), and then call that function. This can make your
code more concise. If you don't want to use the library, you can also
write that function definition directly. Though as a result, the code
will be long and inconvenient to read.

Some libraries are already built in the Arduino IDE, when some others
may need to be added. So now let's see how to add them.


#. Open the Arduino IDE and go to **Sketch** -> **Include Library** -> **Add .ZIP Library**.

   .. image:: img/a2dp_add_zip.png

#. Navigate to the directory where the library files are located, such as the ``kepler-kit-main\arduino\libraries`` folder, and select the desired library file, like ``LiquidCrystal_I2C.zip``. Then, click **Open**.

   .. image:: img/a2dp_choose.png

#. After a short while, you will receive a notification indicating a successful installation.

   .. image:: img/a2dp_success.png

#. Repeat the same process to add the other libraries.


.. note::

   The libraries installed can be found in the default library directory of the Arduino IDE, which is usually located at ``C:\Users\xxx\Documents\Arduino\libraries``.

   If your library directory is different, you can check it by going to **File** -> **Preferences**.

      .. image:: img/install_lib1.png