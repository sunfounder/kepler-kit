Variables
==========
Variables are containers used to store data values.

Creating a variable is very simple. You only need to name it and assign it a value. You don't need to specify the data type of the variable when assigning it, because the variable is a reference, and it accesses objects of different data types through assignment.

Naming variables must follow the following rules:

* Variable names can only contain numbers, letters, and underscores
* The first character of the variable name must be a letter or underscore
* Variable names are case sensitive

Create Variable
------------------
There is no command for declaring variables in MicroPython. Variables are created when you assign a value to it for the first time. It does not need to use any specific type declaration, and you can even change the type after setting the variable.



.. code-block:: python

    x = 8       # x is of type int
    x = "lily" # x is now of type str
    print(x)

>>> %Run -c $EDITOR_CONTENT
lily


Casting
-------------
If you want to specify the data type for the variable, you can do it by casting.



.. code-block:: python

    x = int(5)    # y will be 5
    y = str(5)    # x will be '5'
    z = float(5)  # z will be 5.0
    print(x,y,z)

>>> %Run -c $EDITOR_CONTENT
5 5 5.0

Get the Type
-------------------
You can get the data type of a variable with the `type()` function.



.. code-block:: python

    x = 5
    y = "hello"
    z = 5.0
    print(type(x),type(y),type(z))

>>> %Run -c $EDITOR_CONTENT
<class 'int'> <class 'str'> <class 'float'>

Single or Double Quotes?
---------------------------

In MicroPython, single quotes or double quotes can be used to define string variables.



.. code-block:: python

    x = "hello"
    # is the same as
    x = 'hello'

Case-Sensitive
---------------------
Variable names are case-sensitive.



.. code-block:: python

    a = 5
    A = "lily"
    #A will not overwrite a
    print(a, A)

>>> %Run -c $EDITOR_CONTENT
5 lily


