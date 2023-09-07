Operators
============
Operators are used to perform operations on variables and values.

* :ref:`Arithmetic operators`

* :ref:`Assignment operators`

* :ref:`Comparison operators`

* :ref:`Logical operators`

* :ref:`Identity operators`

* :ref:`Membership operators`

* :ref:`Bitwise operators`

Arithmetic Operators
----------------------
You can use arithmetic operators to do some common mathematical operations.

.. list-table:: 
    :widths: 10 30
    :header-rows: 1

    *   - Operator
        - Name
    *   - ``+``
        - Addition
    *   - ``-``
        - Subtraction
    *   - ``*``
        - Multiplication
    *   - ``/``
        - Division
    *   - ``%``
        - Modulus
    *   - ``**``
        - Exponentiation
    *   - ``//``
        - Floor division



.. code-block:: python

    x = 5
    y = 3

    a = x + y
    b = x - y
    c = x * y
    d = x / y
    e = x % y
    f = x ** y
    g = x // y

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)

>>> %Run -c $EDITOR_CONTENT
8
2
15
1.666667
2
125
1
8
2
15
>>> 

Assignment operators
---------------------

Assignment operators can used to assign values to variables.

.. list-table:: 
    :widths: 10 30 30
    :header-rows: 1

    *   - Operator
        - Example
        - Same As
    *   - ``=``
        - a = 6
        - a =6
    *   - ``+=``
        - a += 6
        - a = a + 6
    *   - ``-=``
        - a -= 6
        - a = a - 6
    *   - ``*=``
        - a \*= 6
        - a = a * 6
    *   - ``/=``
        - a /= 6
        - a = a / 6
    *   - ``%=``
        - a %= 6
        - a = a % 6
    *   - ``**=``
        - a \*\*= 6
        - a = a ** 6
    *   - ``//=``
        - a //= 6
        - a = a // 6
    *   - ``&=``
        - a &= 6
        - a = a & 6
    *   - ``|=``
        - a \|= 6
        - a = a | 6
    *   - ``^=``
        - a ^= 6
        - a = a ^ 6
    *   - ``>>=``
        - a >>= 6
        - a = a \>\> 6
    *   - ``<<=``
        - a <<= 6
        - a = a << 6



.. code-block:: python

    a = 6

    a *= 6
    print(a)

>>> %Run test.py
36
>>> 

Comparison Operators
------------------------
Comparison operators are used to compare two values.

.. list-table:: 
    :widths: 10 30
    :header-rows: 1

    *   - Operator
        - Name
    *   - ``==``
        - Equal
    *   - ``!=``
        - Not equal
    *   - ``<``
        - Less than
    *   - ``>``
        - Greater than
    *   - ``>=``
        - Greater than or equal to
    *   - ``<=``
        - Less than or equal to




.. code-block:: python

    a = 6
    b = 8

    print(a>b)

>>> %Run test.py
False
>>> 

Return **False**, beause the **a** is less than the **b**.

Logical Operators
-----------------------

Logical operators are used to combine conditional statements.

.. list-table:: 
    :widths: 10 30
    :header-rows: 1

    *   - Operator
        - Description
    *   - ``and``
        - Returns True if both statements are true
    *   - ``or``
        - Returns True if one of the statements is true
    *   - ``not``
        - Reverse the result, returns False if the result is true

.. code-block:: python

    a = 6
    print(a > 2 and a < 8)

>>> %Run -c $EDITOR_CONTENT
True
>>> 

Identity Operators
------------------------

Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.

.. list-table:: 
    :widths: 10 30
    :header-rows: 1

    *   - Operator
        - Description
    *   - ``is``
        - Returns True if both variables are the same object
    *   - ``is not``
        - Returns True if both variables are not the same object

.. code-block:: python

    a = ["hello", "welcome"]
    b = ["hello", "welcome"]
    c = a

    print(a is c)
    # returns True because z is the same object as x

    print(a is b)
    # returns False because x is not the same object as y, even if they have the same content

    print(a == b)
    # returns True because x is equal to y

>>> %Run -c $EDITOR_CONTENT
True
False
True
>>> 

Membership Operators
----------------------
Membership operators are used to test if a sequence is presented in an object.

.. list-table:: 
    :widths: 10 30
    :header-rows: 1

    *   - Operator
        - Description
    *   - ``in``
        - Returns True if a sequence with the specified value is present in the object
    *   - ``not in``
        - Returns True if a sequence with the specified value is not present in the object

.. code-block:: python

    a = ["hello", "welcome", "Goodmorning"]

    print("welcome" in a)

>>> %Run -c $EDITOR_CONTENT
True
>>> 

Bitwise Operators
------------------------

Bitwise operators are used to compare (binary) numbers.

.. list-table:: 
    :widths: 10 20 50
    :header-rows: 1

    *   - Operator
        - Name
        - Description
    *   - ``&``
        - AND
        - Sets each bit to 1 if both bits are 1
    *   - ``|``
        - OR
        - Sets each bit to 1 if one of two bits is 1
    *   - ``^``
        - XOR
        - Sets each bit to 1 if only one of two bits is 1
    *   - ``~``
        - NOT
        - Inverts all the bits
    *   - ``<<``
        - Zero fill left shift
        - Shift left by pushing zeros in from the right and let the leftmost bits fall off
    *   - ``>>``
        - Signed right shift
        - Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

.. code-block:: python

    num = 2

    print(num & 1)
    print(num | 1)
    print(num << 1)

>>> %Run -c $EDITOR_CONTENT
0
3
4
>>>