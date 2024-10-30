.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte de expertos**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _syntax_forloop:

Bucles For
===============

El bucle ``for`` puede recorrer cualquier secuencia de elementos, como una lista o una cadena.

La sintaxis del bucle for es la siguiente:

.. code-block:: python

    for val in sequence:
        Body of for


Aquí, ``val`` es una variable que obtiene el valor de cada elemento en la secuencia en cada iteración.

El bucle continúa hasta que alcanzamos el último elemento de la secuencia. Usa sangría para separar el cuerpo del bucle ``for`` del resto del código.

**Diagrama de flujo del bucle for**

.. image:: img/for_loop.png




.. code-block:: python

    numbers = [1, 2, 3, 4]
    sum = 0

    for val in numbers:
        sum = sum+val
        
    print("The sum is", sum)

>>> %Run -c $EDITOR_CONTENT
The sum is 10

La instrucción break
-------------------------

Con la instrucción break podemos detener el bucle antes de que haya recorrido todos los elementos:

.. code-block:: python

    numbers = [1, 2, 3, 4]
    sum = 0

    for val in numbers:
        sum = sum+val
        if sum == 6:
            break
    print("The sum is", sum)

>>> %Run -c $EDITOR_CONTENT
The sum is 6

La instrucción continue
--------------------------------------------

Con la instrucción ``continue`` podemos detener la iteración actual del bucle y continuar con la siguiente:

.. code-block:: python

    numbers = [1, 2, 3, 4]

    for val in numbers:
        if val == 3:
            continue
        print(val)

>>> %Run -c $EDITOR_CONTENT
1
2
4

La función range()
--------------------------------------------

Podemos usar la función range() para generar una secuencia de números. range(6) producirá números del 0 al 5 (6 números).

También podemos definir el inicio, fin y tamaño de paso como range(start, stop, step_size). Si no se proporciona, step_size por defecto es 1.

En el contexto de range, el objeto es "perezoso" porque al crear el objeto, no genera cada número que "contiene". Sin embargo, esto no es un iterador, ya que admite operaciones como in, len y ``__getitem__``.

Esta función no almacena todos los valores en memoria; sería ineficiente. En su lugar, recuerda el inicio, el final y el tamaño del paso para generar el siguiente número a medida que avanza.

Para forzar a esta función a que muestre todos los elementos, podemos usar la función list().

.. code-block:: python

    print(range(6))

    print(list(range(6)))

    print(list(range(2, 6)))

    print(list(range(2, 10, 2)))

>>> %Run -c $EDITOR_CONTENT
range(0, 6)
[0, 1, 2, 3, 4, 5]
[2, 3, 4, 5]
[2, 4, 6, 8]

Podemos usar ``range()`` en un bucle ``for`` para iterar sobre una secuencia de números. Se puede combinar con la función len() para usar el índice al recorrer la secuencia.

.. code-block:: python

    fruits = ['pear', 'apple', 'grape']

    for i in range(len(fruits)):
        print("I like", fruits[i])
        
>>> %Run -c $EDITOR_CONTENT
I like pear
I like apple
I like grape

Else en el bucle For
--------------------------------

El bucle ``for`` también puede tener un bloque opcional ``else``. Si se agotan los elementos en la secuencia del bucle, se ejecuta la parte ``else``.

La palabra clave ``break`` puede usarse para detener el bucle ``for``. En este caso, la parte ``else`` será ignorada.

Por lo tanto, si no se produce ninguna interrupción, la parte ``else`` del bucle ``for`` se ejecutará.

.. code-block:: python

    for val in range(5):
        print(val)
    else:
        print("Finished")

>>> %Run -c $EDITOR_CONTENT
0
1
2
3
4
Finished

El bloque else NO se ejecutará si el bucle se detiene mediante una instrucción break.

.. code-block:: python


    for val in range(5):
        if val == 2: break
        print(val)
    else:
        print("Finished")

>>> %Run -c $EDITOR_CONTENT
0
1

