
.. _add_libraries_py:

1.4 Upload the Libraries to Pico
===================================

In some projects, you will need additional libraries. So here we upload these libraries to Raspberry Pi Pico W first, and then we can run the code directly later.

#. Download the relevant code from the link below.


   * :download:`SunFounder Kepler Kit <https://github.com/sunfounder/kepler-kit/archive/refs/heads/main.zip>`


#. Open Thonny IDE and plug the Pico into your computer with a micro USB cable and click on the "MicroPython (Raspberry Pi Pico).COMXX" interpreter in the bottom right corner.

    .. image:: img/sec_inter.png

#. In the top navigation bar, click **View** -> **Files**.

    .. image:: img/th_files.png

#. Switch the path to the folder where you downloaded the `code package <https://github.com/sunfounder/kepler-kit/archive/refs/heads/main.zip>`_ before, and then go to the ``kepler-kit-main/libs`` folder.

    .. image:: img/th_path.png

#. Select all the files or folders in the ``libs/`` folder, right-click and click **Upload to**, it will take a while to upload.

    .. image:: img/th_upload.png

#. Now you will see the files you just uploaded inside your drive ``Raspberry Pi Pico``.

    .. image:: img/th_done.png