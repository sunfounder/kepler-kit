1.5 Quick Guide on Thonny
==================================

.. _open_run_code_py:

Open and Run Code Directly
---------------------------------------------

The code section in the projects tells you exactly which code is used, so double-click on the ``.py`` file with the serial number in the ``kepler-kit-main/micropython/`` path to open it. 

However, you must first download the package and upload the library, as described in :ref:`add_libraries_py`.

#. Open code.

    For example, ``2.1_hello_led.py``.

    If you double click on it, a new window will open on the right. You can open more than one code at the same time.

    |open_code|

#. Select correct interpreter

    Use a micro USB cable to connect the Pico W to your computer and select the "MicroPython (Raspberry Pi Pico)" interpreter.

    |sec_inter|

#. Run the code

    To run the script, click the **Run current script** button or press F5.

    |run_it|

    If the code contains any information that needs to be printed, it will appear in the Shell; otherwise, only the following information will appear.

    Click **View** -> **Edit** to open the Shell window if it doesn't appear on your Thonny.

        .. code-block::

            MicroPython vx.xx on xxxx-xx-xx; Raspberry Pi Pico W  With RP2040

            Type "help()" for more information.
            >>> %Run -c $EDITOR_CONTENT

    * The first line shows the version of MicroPython, the date, and your device information.
    * The second line prompts you to enter "help()" to get some help.
    * The third line is a command from Thonny telling the MicroPython interpreter on your Pico W to run the contents of the script area - "EDITOR_CONTENT".
    * If there is any message after the third line, it is usually a message that you tell MicroPython to print, or an error message for the code.


#. Stop running

    |stop_it|

    To stop the running code, click the **Stop/Restart backend** button. The **%RUN -c $EDITOR_CONTENT** command will disappear after stopping.

#. Save or save as

    You can save changes made to the open example by pressing **Ctrl+S** or clicking the **Save** button on Thonny.

    The code can be saved as a separate file within the Raspberry Pi Pico W by clicking on **File** -> **Save As**.

    |save_as|

    Select **Raspberry Pi Pico**.

    |sec_pico|

    Then click **OK** after entering the file name and extension **.py**. On the Raspberry Pi Pico W drive, you will see your saved file.

    |sec_name|

    .. note::
        Regardless of what name you give your code, it's best to describe what type of code it is, and not give it a meaningless name like ``abc.py``.
        When you save the code as ``main.py``, it will run automatically when the power is turned on.


Create File and Run it
---------------------------


The code is shown directly in the code section. You can copy it to Thonny and run it as follows.

#. Create a new file

    Open Thonny IDE, click **New** button to create a new blank file.

    |new_file|

#. Copy code

    Copy the code from the project to the Thonny IDE.

    |copy_file|

#. Select correct interpreter

    Plug the Pico W into your computer with a micro USB cable and select the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner.

    |sec_inter|

#. Run and save the code

    You need click **Run Current Script** or simply press F5 to run it. If your code has not been saved, a window will pop up asking to save to **This computer** or **Raspberry Pi Pico**.

    |where_save|

    .. note::
        Thonny saves your program on the Raspberry Pi Pico W hen you tell him to, so if you unplug the Pico W and plug it into someone else's computer, your program remains intact.

    Click OK after selecting the location, naming the file and adding the extension **.py**.

    |sec_name|

    .. note::
        Regardless of what name you give your code, it's best to describe what type of code it is, and not give it a meaningless name like ``abc.py``.
        When you save the code as ``main.py``, it will run automatically when the power is turned on.

    Once your program is saved, it will run automatically and you will see the following information in the Shell area.

    Click **View** -> **Edit** to open the Shell window if it does not appear on your Thonny.


    .. code-block::

        MicroPython vx.xx.x on xxxx-xx-xx; Raspberry Pi Pico W With RP2040

        Type "help()" for more information.
        >>> %Run -c $EDITOR_CONTENT


    * The first line shows the version of MicroPython, the date, and your device information.
    * The second line prompts you to enter "help()" to get some help.
    * The third line is a command from Thonny telling the MicroPython interpreter on your Pico W to run the contents of the script area - "EDITOR_CONTENT".
    * If there is any message after the third line, it is usually a message that you tell MicroPython to print, or an error message for the code.


#. Stop running

    |stop_it|

    To stop the running code, click the **Stop/Restart backend** button. The **%RUN -c $EDITOR_CONTENT** command will disappear after stopping.

#. Open file

    Here are two ways to open a saved code file.

    * The first method is to click the open icon on the Thonny toolbar, just like when you save a program, you will be asked if you want to open it from **this computer** or **Raspberry Pi Pico**, for example, click **Raspberry Pi Pico** and you will see a list of all the programs you have saved on the Pico W.
    * The second is to open the file preview directly by clicking **View**->**File**-> and then double-clicking on the corresponding ``.py`` file to open it.

