.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte de expertos**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Comentarios
=============

Los comentarios en el código nos ayudan a entenderlo, lo hacen más legible y permiten desactivar partes específicas durante las pruebas para que esas líneas no se ejecuten.

Comentario de línea única
----------------------------

En MicroPython, los comentarios de una sola línea comienzan con #, y el texto que sigue se considera comentario hasta el final de la línea. Los comentarios pueden colocarse antes o después del código.

.. code-block:: python

    print("hello world") #Esto es un comentario

>>> %Run -c $EDITOR_CONTENT
hello world

Los comentarios no tienen que ser solo texto explicativo del código; también puedes comentar parte del código para evitar que MicroPython lo ejecute.


.. code-block:: python

    #print("No puede ejecutarse！")
    print("hello world") #Esto es un comentario

>>> %Run -c $EDITOR_CONTENT
hello world

Comentario de múltiples líneas
-----------------------------------

Si deseas comentar en varias líneas, puedes usar múltiples signos #.

.. code-block:: python

    #Esto es un comentario
    #escrito en
    #más de una línea
    print("Hello, World!")

>>> %Run -c $EDITOR_CONTENT
Hello, World!

También puedes utilizar cadenas de texto en múltiples líneas.

Como MicroPython ignora las cadenas que no están asignadas a variables, puedes añadir líneas múltiples de texto (usando comillas triples) y colocar comentarios dentro:

.. code-block:: python

    """
    This is a comment
    written in
    more than just one line
    """
    print("Hello, World!")

>>> %Run -c $EDITOR_CONTENT
Hello, World!

Mientras la cadena no esté asignada a una variable, MicroPython la ignorará y la interpretará como un comentario de varias líneas.

