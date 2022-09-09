Print()
=====================

The ``print()`` function prints the specified message to the screen, or other standard output device.
The message can be a string, or any other object, the object will be converted into a string before written to the screen.

Print multiple objects:



.. code-block:: python

    print("Welcome!", "Enjoy yourself!")

>>> %Run -c $EDITOR_CONTENT
Welcome! Enjoy yourself!

Print tuples:



.. code-block:: python

    x = ("pear", "apple", "grape")
    print(x)

>>> %Run -c $EDITOR_CONTENT
('pear', 'apple', 'grape')

Print two messages and specify the separator:



.. code-block:: python

    print("Hello", "how are you?", sep="---")

>>> %Run -c $EDITOR_CONTENT
Hello---how are you?