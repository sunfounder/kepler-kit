.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros aficionados.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas posventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

If Else
=============

La toma de decisiones es necesaria cuando queremos ejecutar un código solo si se cumple una condición específica.

if
--------------------
.. code-block:: python

    if test expression:
        statement(s)

Aquí, el programa evalúa la ``expresión_de_prueba`` y ejecuta la ``declaración`` solo cuando la ``expresión_de_prueba`` es Verdadera.

Si ``expresión_de_prueba`` es Falsa, entonces no se ejecutarán las ``declaración(es)``.

En MicroPython, la indentación significa el cuerpo de la declaración ``if``. El cuerpo comienza con una sangría y termina con la primera línea sin sangría.

Python interpreta los valores distintos de cero como "Verdadero". None y 0 se interpretan como "Falso".

**Diagrama de flujo de la declaración if**

.. image:: img/if_statement.png

**Ejemplo**

.. code-block:: python

    num = 8
    if num > 0:
        print(num, "is a positive number.")
    print("End with this line")

>>> %Run -c $EDITOR_CONTENT
8 is a positive number.
End with this line



if...else
-----------------------

.. code-block:: python

    if test expression:
        Body of if
    else:
        Body of else

La declaración ``if..else`` evalúa ``expresión_de_prueba`` y ejecutará el cuerpo de ``if`` solo cuando la condición de prueba sea ``Verdadera``.

Si la condición es ``Falsa``, se ejecuta el cuerpo de ``else``. Se usa la indentación para separar los bloques.

**Diagrama de flujo de la declaración if...else**

.. image:: img/if_else.png

**Ejemplo**

.. code-block:: python

    num = -8
    if num > 0:
        print(num, "is a positive number.")
    else:
        print(num, "is a negative number.")

>>> %Run -c $EDITOR_CONTENT
-8 is a negative number.



if...elif...else
--------------------

.. code-block:: python

    if test expression:
        Body of if
    elif test expression:
        Body of elif
    else: 
        Body of else

``Elif`` es la abreviatura de ``else if``. Nos permite verificar múltiples expresiones.

Si la condición del bloque ``if`` es Falsa, se evalúa la condición del siguiente bloque ``elif``, y así sucesivamente.

Si todas las condiciones son ``Falsas``, se ejecuta el cuerpo de ``else``.

Solo uno de los varios bloques ``if...elif...else`` se ejecuta según las condiciones.

El bloque ``if`` solo puede tener un bloque ``else``. Pero puede tener múltiples bloques ``elif``.

**Diagrama de flujo de la declaración if...elif...else**

.. image:: img/if_elif_else.png

**Ejemplo**

.. code-block:: python

    x = 10
    y = 9

    if x > y:
        print("x is greater than y")
    elif x == y:
        print("x and y are equal")
    else:
        print("x is greater than y")

>>> %Run -c $EDITOR_CONTENT
x is greater than y


If anidado
---------------------

Podemos incrustar una declaración if dentro de otra if, lo que se denomina if anidado.

**Ejemplo**

.. code-block:: python

    x = 67

    if x > 10:
        print("Above ten,")
        if x > 20:
            print("and also above 20!")
        else:
            print("but not above 20.")

>>> %Run -c $EDITOR_CONTENT
Above ten,
and also above 20!