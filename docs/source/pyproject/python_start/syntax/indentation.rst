.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirte?**

    - **Soporte de Expertos**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Obtén acceso anticipado a anuncios y adelantos de nuevos productos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

Indentación
===============

La indentación se refiere a los espacios al comienzo de una línea de código.
Al igual que en los programas estándar de Python, los programas de MicroPython generalmente se ejecutan de arriba hacia abajo:
Recorre cada línea en orden, la ejecuta en el intérprete y luego continúa con la siguiente,
tal como si las escribieras línea por línea en el Shell.
Sin embargo, un programa que solo recorre la lista de instrucciones línea por línea no es muy inteligente, por lo que MicroPython, al igual que Python, tiene su propio método para controlar la secuencia de ejecución de su programa: la indentación.

Debes colocar al menos un espacio antes de print(), de lo contrario aparecerá un mensaje de error "SyntaxError: invalid syntax". Por lo general, se recomienda estandarizar los espacios presionando uniformemente la tecla Tabulador.

.. code-block:: python

    if 8 > 5:
    print("Eight is greater than Five!")

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 2
SyntaxError: invalid syntax

Debes usar el mismo número de espacios en el mismo bloque de código, o Python te dará un error.

.. code-block:: python

    if 8 > 5:
    print("Eight is greater than Five!")
            print("Eight is greater than Five")
                
>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 2
SyntaxError: invalid syntax
