.. _setup_pico_arduino:

1.2 Setup the Raspberry Pi Pico
=======================================

1. Open the Boards Manager by clicking Tools -> Board -> Boards Manager.

|ars_boards_manager|

2. Search for **Pico** and click **install** button.

|ars_install_pico|

3. Once the installation is complete, you can select the board as **Raspberry Pi Pico**.

|ars_pico_board|

4. Now open a example - blink.

|ars_test_blink|

5. Click on the upload icon to run the code

|ars_upload_blink|

    
6. When the compiling message shown in the figure below appears, press **BOOTSEL** immediately and connect Pico W to the computer with a Micro USB cable.

|ars_upload_process|

|mps_bootsel_onboard| 

.. note::
    
    This step is very important and only necessary for the first use on the Arduino IDE, otherwise your code will upload unsuccessfully.
    
    After the upload is successful this time, Pico W will be recognized by the computer as COMxx (Raspberry Pi Pico).

    You only need to plug it into the computer the next time you use it.

7. After the  **Done Uploading** appear, you will see the LED on the Pico W blinking. 

|ars_done_uploading| 