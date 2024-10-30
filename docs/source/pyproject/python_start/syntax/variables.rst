.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de Raspberry Pi, Arduino y ESP32 de SunFounder en Facebook. Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!


Variables
==========

Las variables son contenedores utilizados para almacenar valores de datos.

Crear una variable es muy sencillo. Solo necesitas nombrarla y asignarle un valor. No es necesario especificar el tipo de dato de la variable al asignarla, ya que la variable actúa como una referencia y accede a objetos de distintos tipos a través de la asignación.

Los nombres de las variables deben cumplir las siguientes reglas:

* Los nombres de las variables solo pueden contener números, letras y guiones bajos
* El primer carácter del nombre de la variable debe ser una letra o guion bajo
* Los nombres de las variables son sensibles a mayúsculas y minúsculas


Crear Variable
------------------

No existe un comando para declarar variables en MicroPython. Las variables se crean cuando les asignas un valor por primera vez. No es necesario utilizar ninguna declaración de tipo específica, y puedes incluso cambiar el tipo después de establecer la variable.

.. code-block:: python

    x = 8       # x es de tipo int
    x = "lily"  # x ahora es de tipo str
    print(x)

>>> %Run -c $EDITOR_CONTENT
lily

Casting
-------------

Si deseas especificar el tipo de dato para la variable, puedes hacerlo mediante casting.

.. code-block:: python

    x = int(5)    # x será 5
    y = str(5)    # y será '5'
    z = float(5)  # z será 5.0
    print(x, y, z)

>>> %Run -c $EDITOR_CONTENT
5 5 5.0

Obtener el Tipo
-------------------

Puedes obtener el tipo de dato de una variable con la función `type()`.

.. code-block:: python

    x = 5
    y = "hello"
    z = 5.0
    print(type(x),type(y),type(z))

>>> %Run -c $EDITOR_CONTENT
<class 'int'> <class 'str'> <class 'float'>

¿Comillas Simples o Dobles?
--------------------------------

En MicroPython, se pueden utilizar comillas simples o dobles para definir variables de tipo cadena.

.. code-block:: python

    x = "hello"
    # es lo mismo que
    x = 'hello'

Sensible a Mayúsculas y Minúsculas
-----------------------------------------

Los nombres de las variables distinguen entre mayúsculas y minúsculas.

.. code-block:: python

    a = 5
    A = "lily"
    # A no sobrescribirá a
    print(a, A)

>>> %Run -c $EDITOR_CONTENT
5 lily
