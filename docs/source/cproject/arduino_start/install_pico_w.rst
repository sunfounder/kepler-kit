.. _setup_pico_arduino:

1.3 Setting Up the Raspberry Pi Pico W (Important)
==================================================

1. Installing UF2 Firmware
---------------------------------

When you initially connect the Raspberry Pi Pico W or hold down the BOOTSEL button while inserting it, you'll see the device showing up as a drive without being assigned a COM port. This makes it impossible to upload code.

To fix this, you need to install UF2 firmware. This firmware supports MicroPython and is also compatible with the Arduino IDE.

1. Download the UF2 Firmware from the link below.

    * :download:`Raspberry Pi Pico W UF2 Firmware <https://micropython.org/download/rp2-pico-w/rp2-pico-w-latest.uf2>`

2. Connect your Raspberry Pi Pico W to your computer using a Micro USB cable. Your Pico W will mount as a Mass Storage Device named **RPI-RP2**.

    .. image:: img/install_pico_plugin.png

3. Drag and drop the downloaded UF2 firmware into the **RPI-RP2** drive.

    .. image:: img/install_pico_uf2.png

4. After this, the **RPI-RP2** drive will disappear, and you can proceed with the following steps.


2. Installing the Board Package
--------------------------------------

To program the Raspberry Pi Pico W, you'll need to install the corresponding package in the Arduino IDE. Here's a step-by-step guide:

1. In the **Boards Manager** window, search for **pico**. Click the **Install** button to commence the installation. This will install the **Arduino Mbed OS RP2040 Boards** package, which includes support for the Raspberry Pi Pico W.

    .. image:: img/install_pico.png

2. During the process, a few pop-up prompts will appear for the installation of specific device drivers. Select **"Install"**.

    .. image:: img/install_pico_sa.png

3. Afterwards, there will be a notification indicating that the installation is complete.

3. Selecting the Board and Port
------------------------------------------

1. To select the appropriate board, navigate to **Tools** -> **Board** -> **Arduino Mbed OS RP2040 Boards** -> **Raspberry Pi Pico**.

    .. image:: img/install_pico_tool_board.png

2. If your Raspberry Pi Pico W is connected to the computer, set the right port by navigating to **Tools** -> **Port**.

    .. image:: img/install_pico_tool_port.png

3. Arduino 2.0 offers a new quick-select feature. For the Raspberry Pi Pico W, which is typically not auto-recognized, click **Select other board and port**.

    .. image:: img/install_pico_select.png

4. Type **Raspberry Pi Pico** into the search bar, select it when it shows up, choose the appropriate port, and click **OK**.

    .. image:: img/install_pico_board.png

5. You can easily reselect it later through this quick access window.

    .. image:: img/install_pico_quick.png

6. Either of these methods will enable you to set the correct board and port. You're now all set to upload code to the Raspberry Pi Pico W.

4. Uploading Code
--------------------------

Now let's dive into how to upload code to your Raspberry Pi Pico W.

1. Open any ``.ino`` file or use the empty sketch currently displayed. Then, click the **Upload** button.

    .. image:: img/install_pico_upload.png

2. Wait for the uploading message to appear, as shown below.

    .. image:: img/install_pico_upload_dot.png

3. Hold down the **BOOTSEL** button, quickly unplug your Raspberry Pi Pico W, and plug it back in.

    .. image:: img/led_onboard.png 

    .. note::
        
        * This step is crucial, especially for first-time users on the Arduino IDE. Skipping this step will result in a failed upload.

        * Once you successfully upload the code this time, your Pico W will be recognized by the computer. For future uses, simply plug it into the computer.

4. A prompt indicating successful upload will appear.

    .. image:: img/install_pico_upload_done.png
