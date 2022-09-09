.. _apx_add_lib:

1.3 Download and Add Libraries
================================

**Download the Code**

Download the relevant code from the link below.

* :download:`SunFounder Kepler Kit Example <https://github.com/sunfounder/kepler-kit-main/archive/refs/heads/main.zip>`

* Or check out the code at `Kepler Kit - GitHub <https://github.com/sunfounder/kepler-kit-main>`_

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
may need to be added. So now let's see how to add one. There are 2
methods for that.

**Method 1**

Directly import the library in Arduino IDE (take Dht as an example
below). The advantage of this method is easy to understand and operate,
but on the other hand, only one library can be imported at a time. So it
is inconvenient when you need to add quite a lot of libraries.

Step 1: Select **Sketch** -> **Include Library** -> **Add ZIP
Library**.

|apx_add_lib1|

Step 2: Find **Library folder** , They are under the path ``arduino\libraries``. Then click **Open**. 

|apx_add_lib2| 

Step 3: When you see **Library added to your libraries. Check
"Include library" menu**, it means you have added the library
successfully. Please use the same method to add other libraries then.

|apx_add_lib3| 

**Method 2**

Directly copy the library to ``libraries/Arduino`` path. This method can
copy all libraries and add them at a time, but the drawback is that it
is difficult to find ``libraries/Arduino``.

Step 1: Click **File** -> **Preferences** and on the pop-up window
you can see the path of the libraries folder in the text box as shown
below.

|apx_add_lib4| 

Step 2: Copy all Libraries in the ``library`` folder.

|apx_add_lib5| 

Step 3: Go to the path above and you will see there is a *libraries*
folder, click to open it.

|apx_add_lib6| 

Step 4: Paste all the libraries copied before to the folder. Then
you can see them in libraries folder.

|apx_add_lib7| 