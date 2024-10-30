.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de Raspberry Pi, Arduino y ESP32 de SunFounder en Facebook. Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _py_syntax_while:

Bucles While
====================

La declaración ``while`` se utiliza para ejecutar un programa en bucle, es decir, para realizar un proceso repetitivo bajo ciertas condiciones y así manejar una misma tarea de manera continua.

Su forma básica es:

.. code-block:: python

    while test expression:
        Body of while


En el bucle ``while``, primero se evalúa la ``test expression``. Solo cuando ``test expression`` se evalúa como ``True``, se ingresa al cuerpo del while. Después de cada iteración, se vuelve a verificar la ``test expression``. Este proceso continúa hasta que ``test expression`` se evalúa como ``False``.

En MicroPython, el cuerpo del bucle ``while`` se define mediante la indentación.

El cuerpo comienza con una línea indentada y termina con la primera línea sin indentación.

Python interpreta cualquier valor diferente de cero como ``True``. Ningún valor o 0 se interpretan como ``False``.

**Diagrama de Flujo del bucle while**

.. image:: img/while_loop.png



.. code-block:: python

    x = 10

    while x > 0:
        print(x)
        x -= 1

>>> %Run -c $EDITOR_CONTENT
10
9
8
7
6
5
4
3
2
1


Declaración Break
--------------------

Con la declaración break podemos detener el bucle, incluso si la condición del while sigue siendo verdadera:

.. code-block:: python

    x = 10

    while x > 0:
        print(x)
        if x == 6:
            break
        x -= 1

>>> %Run -c $EDITOR_CONTENT
10
9
8
7
6

Bucle While con Else
----------------------

Al igual que el bucle ``if``, el bucle ``while`` también puede tener un bloque ``else`` opcional.

Si la condición en el bucle ``while`` se evalúa como ``False``, se ejecuta la parte ``else``.

.. code-block:: python

    x = 10

    while x > 0:
        print(x)
        x -= 1
    else:
        print("Game Over")

>>> %Run -c $EDITOR_CONTENT
10
9
8
7
6
5
4
3
2
1
Game Over