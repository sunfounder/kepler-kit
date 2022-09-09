FAQ
=========

Arduino
---------------------

#. Code upload failed in Arduino IDE?
    * Check that your Pico is correctly recognised by the Arduino IDE, the port should be COMXX (Raspberry Pi Pico), for instructions please refer to :ref:`setup_pico_arduino`.
    * Check that the Board(Raspberry Pi Pico) or port（COMXX (Raspberry Pi Pico)）is selected correctly.
    * If your code is OK and you have selected the correct board and port, but the upload is still not successful. At this point you can click on the **Upload** icon again, when the progress below shows "Upload...", unplug the USB cable, then press and hold the **BOOTSEL** button to plug it in and the code will be uploaded successfully.


MicroPython
------------------

#. How to open and run the code?
    For detailed tutorials, please refer to :ref:`open_run_code_py`.

#. How to upload library to Raspberry Pi Pico W？
    For detailed tutorials, please refer to :ref:`add_libraries_py`.

#. NO MicroPython(Raspberry Pi Pico W) Interpreter Option on Thonny IDE?
    * Check that your Pico W is plugged into your computer via a USB cable.
    * Check that you have installed MicroPython for Pico W (:ref:`install_micropython_on_pico`).
    * The Raspberry Pi Pico W interpreter is only available in version 3.3.3 or higher version of Thonny. If you are running an older version, please update (:ref:`thonny_ide`).
    * If the Li-po Charger module is plugged into the breadboard at this point, unplug it first and then re-plug the Pico W into the computer.

#. Cannot open Pico W code or save code to Pico W via Thonny IDE?
    * Check that your Pico W is plugged into your computer via a USB cable.
    * Check that you have selected the Interpreter as **MicroPython (Raspberry Pi Pico)**.

#. Can Raspberry Pi Pico W be used on Thonny and Arduino at the same time?
    NO, you need to do some different operations.

    * If you used it on Arduino first, and now you want to use it on Thonny IDE, you need to :ref:`install_micropython_on_pico` on it.
    * If you used it on Thonny first， and now you want to use it on Arduino IDE, you need to :ref:`setup_pico_arduino`.


#. If your computer is win7 and Pico W cannot be detected.
    * Download the USB CDC driver from http://aem-origin.microchip.com/en-us/mindi-sw-library?swsearch=Atmel%2520USB%2520CDC%2520Virtual%2520COM%2520Driver
    * Unzip the ``amtel_devices_cdc.inf`` file to a folder named ``pico-serial``.
    * Change the name of ``amtel_devices_cdc.inf`` file to ``pico-serial.inf``.
    * Open/edit the ``pico-serial.inf`` in a basic editor like notepad
    * Remove and replace the lines under the following headings:

    .. code-block::

        [DeviceList]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [DeviceList.NTAMD64]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [DeviceList.NTIA64]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [DeviceList.NT]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [Strings]
        Manufacturer = "ATMEL, Inc."
        PI_CDC_PICO = "Pi Pico Serial Port"
        Serial.SvcDesc = "Pi Pico Serial Driver"

    #. Close and save and make sure your retain the name as pico-serial.inf
    #. Go to your pc device list, find the pico under Ports, named something like CDC Device. A yellow exclamation mark indicates it.
    #. Right click on the CDC Device and update or install driver choosing the file you created from the location you saved it at.




Piper Make
------------------

#. How to set up the Pico W on Piper Make?
    For detailed tutorials, please refer to :ref:`per_setup_pico`.

#. How to download or import code?
    For detailed tutorials, please refer to :ref:`per_save_import`.

#. How to connect to Pico W?
    For detailed tutorials, please refer to :ref:`connect_pico_per`.


