.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

Comments
=============

The comments in the code help us understand the code, make the entire code more readable and comment out part of the code during testing, so that this part of the code does not run.

Single-line Comment
----------------------------

Single-line comments in MicroPython begin with #, and the following text is considered a comment until the end of the line. Comments can be placed before or after the code.

.. code-block:: python

    print("hello world") #This is a annotationhello world

>>> %Run -c $EDITOR_CONTENT
hello world

Comments are not necessarily text used to explain the code. You can also comment out part of the code to prevent micropython from running the code.


.. code-block:: python

    #print("Can't run it！")
    print("hello world") #This is a annotationhello world

>>> %Run -c $EDITOR_CONTENT
hello world

Multi-line comment
------------------------------

If you want to comment on multiple lines, you can use multiple # signs.

.. code-block:: python

    #This is a comment
    #written in
    #more than just one line
    print("Hello, World!")

>>> %Run -c $EDITOR_CONTENT
Hello, World!

Or, you can use multi-line strings instead of expected.

Since MicroPython ignores string literals that are not assigned to variables, you can add multiple lines of strings (triple quotes) to the code and put comments in them:

.. code-block:: python

    """
    This is a comment
    written in
    more than just one line
    """
    print("Hello, World!")

>>> %Run -c $EDITOR_CONTENT
Hello, World!

As long as the string is not assigned to a variable, MicroPython will ignore it after reading the code and treat it as if you made a multi-line comment.
