.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte de expertos**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Tipos de Datos
====================

Tipos de datos integrados
--------------------------------
MicroPython tiene los siguientes tipos de datos:

* Tipo de texto: str
* Tipos numéricos: int, float, complex
* Tipos de secuencia: list, tuple, range
* Tipo de mapeo: dict
* Tipos de conjunto: set, frozenset
* Tipo booleano: bool
* Tipos binarios: bytes, bytearray, memoryview

Obteniendo el tipo de dato
--------------------------------
Puedes obtener el tipo de dato de cualquier objeto utilizando la función ``type()``:



.. code-block:: python

    a = 6.8
    print(type(a))

>>> %Run -c $EDITOR_CONTENT
<class 'float'>

Configurando el tipo de dato
---------------------------------
MicroPython no requiere establecer el tipo de dato explícitamente; se determina cuando se asigna un valor a la variable.



.. code-block:: python

    x = "welcome"
    y = 45
    z = ["apple", "banana", "cherry"]

    print(type(x))
    print(type(y))
    print(type(z))

>>> %Run -c $EDITOR_CONTENT
<class 'str'>
<class 'int'>
<class 'list'>
>>> 

Estableciendo un tipo de dato específico
----------------------------------------------

Si deseas especificar el tipo de dato, puedes usar las siguientes funciones de constructor:

.. list-table:: 
    :widths: 25 10
    :header-rows: 1

    *   - Ejemplo
        - Tipo de Dato
    *   - x = int(20)
        - int
    *   - x = float(20.5)
        - float
    *   - x = complex(1j)
        - complex
    *   - x = str("Hello World")
        - str
    *   - x = list(("apple", "banana", "cherry"))
        - list
    *   - x = tuple(("apple", "banana", "cherry"))
        - tuple
    *   - x = range(6)
        - range
    *   - x = dict(name="John", age=36)
        - dict
    *   - x = set(("apple", "banana", "cherry"))
        - set
    *   - x = frozenset(("apple", "banana", "cherry"))
        - frozenset
    *   - x = bool(5)
        - bool
    *   - x = bytes(5)
        - bytes
    *   - x = bytearray(5)
        - bytearray
    *   - x = memoryview(bytes(5))
        - memoryview

Puedes imprimir algunos de ellos para ver el resultado.



.. code-block:: python

    a = float(20.5)
    b = list(("apple", "banana", "cherry"))
    c = bool(5)

    print(a)
    print(b)
    print(c)

>>> %Run -c $EDITOR_CONTENT
20.5
['apple', 'banana', 'cherry']
True
>>> 

Conversión de tipos
--------------------------
Puedes convertir de un tipo a otro con los métodos int(), float() y complex():
La conversión en Python se realiza utilizando funciones constructoras:

* int() - construye un número entero a partir de un literal entero, un literal flotante (eliminando todos los decimales) o un literal de cadena (siempre que la cadena represente un número entero)
* float() - construye un número flotante a partir de un literal entero, un literal flotante o un literal de cadena (siempre que la cadena represente un número flotante o un número entero)
* str() - construye una cadena a partir de una variedad de tipos de datos, incluidas cadenas, literales enteros y literales flotantes



.. code-block:: python

    a = float("5")
    b = int(3.7)
    c = str(6.0)

    print(a)
    print(b)
    print(c)

Nota: No puedes convertir números complejos a otro tipo de número.
