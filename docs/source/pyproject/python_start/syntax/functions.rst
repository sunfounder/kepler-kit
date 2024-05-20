.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

Functions
==============

In MicroPython, a function is a group of related statements that perform a specific task.

Functions help break our program into smaller modular blocks. As our plan becomes larger and larger, functions make it more organized and manageable.

In addition, it avoids duplication and makes the code reusable.

Create a Function
------------------

.. code-block::

    def function_name(parameters): 
        """docstring"""
        statement(s)

* A function is defined using the ``def`` keyword

* A function name to uniquely identify the function. Function naming is the same as variable naming, and both follow the following rules.
    
   * Can only contain numbers, letters, and underscores.
   * The first character must be a letter or underscore.
   * Case sensitive.

* Parameters (arguments) through which we pass values to a function. They are optional.

* The colon (:) marks the end of the function header.

* Optional docstring, used to describe the function of the function, we usually use triple quotes so that the docstring can be expanded to multiple lines.

* One or more valid Micropython statements that make up the function body. Statements must have the same indentation level (usually 4 spaces).

* Each function needs at least one statement, but if for some reason there is a function that does not contain any statement, please put in the pass statement to avoid errors.

* An optional ``return`` statement to return a value from the function.


Calling a Function
-------------------

To call a function, add parentheses after the function name.



.. code-block:: python

    def my_function():
        print("Your first function")

    my_function()

>>> %Run -c $EDITOR_CONTENT
Your first function

The return Statement
-----------------------

The return statement is used to exit a function and return to the place where it was called.

**Syntax of return**

.. code-block:: python

    return [expression_list]

The statement can contain an expression that is evaluated and returns a value. If there is no expression in the statement, or the ``return`` statement itself does not exist in the function, the function will return a ``None`` object.



.. code-block:: python

    def my_function():
            print("Your first function")

    print(my_function())

>>> %Run -c $EDITOR_CONTENT
Your first function
None

Here, ``None`` is the return value, because the ``return`` statement is not used.

Arguments
-------------

Information can be passed to the function as arguments.

Specify arguments in parentheses after the function name. You can add as many arguments as you need, just separate them with commas.



.. code-block:: python

    def welcome(name, msg):
        """This is a welcome function for
        the person with the provided message"""
        print("Hello", name + ', ' + msg)

    welcome("Lily", "Welcome to China!")

>>> %Run -c $EDITOR_CONTENT
Hello Lily, Welcome to China!


Number of Arguments
*************************

By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 parameters, you have to call the function with 2 arguments, not more, and not less.



.. code-block:: python

    def welcome(name, msg):
        """This is a welcome function for
        the person with the provided message"""
        print("Hello", name + ', ' + msg)

    welcome("Lily", "Welcome to China!")

Here, the function welcome() has 2 parameters.

Since we called this function with two arguments, the function runs smoothly without any errors.

If it is called with a different number of arguments, the interpreter will display an error message.

The following is the call to this function, which contains one and one no arguments and their respective error messages.

.. code-block::

    welcome("Lily")＃Only one argument

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
TypeError: function takes 2 positional arguments but 1 were given

.. code-block::

    welcome()＃No arguments

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
TypeError: function takes 2 positional arguments but 0 were given


Default Arguments
*************************

In MicroPython, we can use the assignment operator (=) to provide a default value for the parameter.

If we call the function without argument, it uses the default value.



.. code-block:: python

    def welcome(name, msg = "Welcome to China!"):
        """This is a welcome function for
        the person with the provided message"""
        print("Hello", name + ', ' + msg)
    welcome("Lily")

>>> %Run -c $EDITOR_CONTENT
Hello Lily, Welcome to China!

In this function, the parameter ``name`` has no default value and is required (mandatory) during the call.

On the other hand, the default value of the parameter ``msg`` is "Welcome to China!". Therefore, it is optional during the call. If a value is provided, it will overwrite the default value.

Any number of arguments in the function can have a default value. However, once there is a default argument, all arguments on its right must also have default values.

This means that non-default arguments cannot follow default arguments. 

For example, if we define the above function header as:

.. code-block:: python

    def welcome(name = "Lily", msg):

We will receive the following error message:

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
SyntaxError: non-default argument follows default argument


Keyword Arguments
**************************

When we call a function with certain values, these values ​​will be assigned to arguments based on their position.

For example, in the above function welcome(), when we called it as welcome("Lily", "Welcome to China"), the value "Lily" gets assigned to the ``name`` and similarly "Welcome to China" to parameter ``msg``.

MicroPython allows calling functions with keyword arguments. When we call the function in this way, the order (position) of the arguments can be changed. 

.. code-block:: python

    # keyword arguments
    welcome(name = "Lily",msg = "Welcome to China!")

    # keyword arguments (out of order)
    welcome(msg = "Welcome to China！",name = "Lily") 

    #1 positional, 1 keyword argument
    welcome("Lily", msg = "Welcome to China!")

As we can see, we can mix positional arguments and keyword arguments during function calls. But we must remember that the keyword arguments must come after the positional arguments.

Having a positional argument after a keyword argument will result in an error. 

For example, if the function call as follows:

.. code-block:: python

    welcome(name="Lily","Welcome to China!")

Will result in an error:

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
SyntaxError: non-keyword arg after keyword arg


Arbitrary Arguments
********************

Sometimes, if you do not know the number of arguments that will be passed to the function in advance. 

In the function definition, we can add an asterisk (*) before the parameter name.



.. code-block:: python

    def welcome(*names):
        """This function welcomes all the person
        in the name tuple"""
        #names is a tuple with arguments
        for name in names:
            print("Welcome to China!", name)
            
    welcome("Lily","John","Wendy")

>>> %Run -c $EDITOR_CONTENT
Welcome to China! Lily
Welcome to China! John
Welcome to China! Wendy

Here, we have called the function with multiple arguments. These arguments are packed into a tuple before being passed into the function. 

Inside the function, we use a for loop to retrieve all the arguments.

Recursion
----------------
In Python, we know that a function can call other functions. It is even possible for the function to call itself. These types of construct are termed as recursive functions.

This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.



.. code-block:: python

    def rec_func(i):
        if(i > 0):
            result = i + rec_func(i - 1)
            print(result)
        else:
            result = 0
        return result

    rec_func(6)

>>> %Run -c $EDITOR_CONTENT
1
3
6
10
15
21

In this example, rec_func() is a function that we have defined to call itself ("recursion"). We use the ``i`` variable as the data, and it will decrement (-1) every time we recurse. When the condition is not greater than 0 (that is, 0), the recursion ends.

For new developers, it may take some time to determine how it works, and the best way to test it is to test and modify it.

**Advantages of Recursion**

* Recursive functions make the code look clean and elegant.
* A complex task can be broken down into simpler sub-problems using recursion.
* Sequence generation is easier with recursion than using some nested iteration.

**Disadvantages of Recursion**

* Sometimes the logic behind recursion is hard to follow through.
* Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
* Recursive functions are hard to debug.
