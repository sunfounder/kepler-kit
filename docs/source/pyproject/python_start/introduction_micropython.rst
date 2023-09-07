1.1 Introduction of MicroPython
======================================

MicroPython is a software implementation of a programming language largely compatible with Python 3, written in C, that is optimized to run on a microcontroller.

MicroPython consists of a Python compiler to bytecode and a runtime interpreter of that bytecode. The user is presented with an interactive prompt (the REPL) to execute supported commands immediately. Included are a selection of core Python libraries; MicroPython includes modules which give the programmer access to low-level hardware.

* Reference: `MicroPython - Wikipedia <https://en.wikipedia.org/wiki/MicroPython>`_

The Story Starts Here
--------------------------------

Things changed in 2013 when Damien George launched a crowdfunding campaign (Kickstarter).

Damien was an undergraduate student at Cambridge University and an avid robotics programmer. He wanted to reduce the world of Python from a gigabyte machine to a kilobyte. His Kickstarter campaign was to support his development while he turned his proof of concept into a finished implementation.

MicroPython is supported by a diverse Pythonista community that has a keen interest in seeing the project succeed.

Apart from testing and supporting the code base, the developers provided tutorials, code libraries, and hardware porting, so Damien was able to focus on other aspects of the project.

* Reference: `realpython <https://realpython.com/micropython/>`_

Why MicroPython？
------------------

Although the original Kickstarter campaign released MicroPython as a development board "pyboard" with STM32F4, MicroPython supports many ARM-based product architectures. The mainline supported ports are ARM Cortex-M (many STM32 boards, TI CC3200/WiPy, Teensy boards, Nordic nRF series, SAMD21 and SAMD51), ESP8266, ESP32, 16bit PIC, Unix, Windows, Zephyr and JavaScript.
Second, MicroPython allows for fast feedback. This is because you can use REPL to enter commands interactively and get responses. You can even tweak code and run it immediately instead of traversing the code-compile-upload-execute cycle.

While Python has the same advantages, for some Microcontroller boards like the Raspberry Pi Pico, they are small, simple and have little memory to run the Python language at all. That's why MicroPython has evolved, keeping the main Python features and adding a bunch of new ones to work with these Microcontroller boards.

Next you will learn to install MicroPython into the Raspberry Pi Pico.

* Reference: `MicroPython - Wikipedia <https://en.wikipedia.org/wiki/MicroPython>`_
* Reference: `realpython <https://realpython.com/micropython/>`_
