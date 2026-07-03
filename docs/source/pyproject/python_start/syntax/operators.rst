.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de Raspberry Pi, Arduino y ESP32 de SunFounder en Facebook. Profundiza en Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios y adelantos de nuevos productos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

Operadores
==============

Los operadores se utilizan para realizar operaciones en variables y valores.


Arithmetic operators
---------------------------

Puedes utilizar operadores aritméticos para realizar algunas operaciones matemáticas comunes.

.. list-table:: 
    :widths: 10 30
    :header-rows: 1

    *   - Operador
        - Nombre
    *   - ``+``
        - Suma
    *   - ``-``
        - Resta
    *   - ``*``
        - Multiplicación
    *   - ``/``
        - División
    *   - ``%``
        - Módulo
    *   - ``**``
        - Exponenciación
    *   - ``//``
        - División entera

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
----------------------------

Los operadores de asignación se pueden usar para asignar valores a variables.

.. list-table:: 
    :widths: 10 30 30
    :header-rows: 1

    *   - Operador
        - Ejemplo
        - Equivale a
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
-----------------------------

Los operadores de comparación se utilizan para comparar dos valores.

.. list-table:: 
    :widths: 10 30
    :header-rows: 1

    *   - Operador
        - Nombre
    *   - ``==``
        - Igual a
    *   - ``!=``
        - Distinto de
    *   - ``<``
        - Menor que
    *   - ``>``
        - Mayor que
    *   - ``>=``
        - Mayor o igual que
    *   - ``<=``
        - Menor o igual que

.. code-block:: python

    a = 6
    b = 8

    print(a>b)

>>> %Run test.py
False
>>> 

Devuelve **False**, porque **a** es menor que **b**.

Logical Operators
-----------------------

Los operadores lógicos se utilizan para combinar declaraciones condicionales.

.. list-table:: 
    :widths: 10 30
    :header-rows: 1

    *   - Operador
        - Descripción
    *   - ``and``
        - Devuelve True si ambas declaraciones son verdaderas
    *   - ``or``
        - Devuelve True si una de las declaraciones es verdadera
    *   - ``not``
        - Invierte el resultado, devuelve False si el resultado es verdadero

.. code-block:: python

    a = 6
    print(a > 2 and a < 8)

>>> %Run -c $EDITOR_CONTENT
True
>>> 

Identity Operators
----------------------------

Los operadores de identidad se utilizan para comparar objetos, no si son iguales, sino si realmente son el mismo objeto, con la misma ubicación en memoria.

.. list-table:: 
    :widths: 10 30
    :header-rows: 1

    *   - Operador
        - Descripción
    *   - ``is``
        - Devuelve True si ambas variables son el mismo objeto
    *   - ``is not``
        - Devuelve True si ambas variables no son el mismo objeto

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
-------------------------------

Los operadores de pertenencia se utilizan para comprobar si una secuencia está presente en un objeto.

.. list-table:: 
    :widths: 10 30
    :header-rows: 1

    *   - Operador
        - Descripción
    *   - ``in``
        - Devuelve True si una secuencia con el valor especificado está presente en el objeto
    *   - ``not in``
        - Devuelve True si una secuencia con el valor especificado no está presente en el objeto

.. code-block:: python

    a = ["hello", "welcome", "Goodmorning"]

    print("welcome" in a)

>>> %Run -c $EDITOR_CONTENT
True
>>> 

Bitwise Operators
------------------------

Los operadores bit a bit se utilizan para comparar números (binarios).

.. list-table:: 
    :widths: 10 20 50
    :header-rows: 1

    *   - Operador
        - Nombre
        - Descripción
    *   - ``&``
        - AND
        - Establece cada bit en 1 si ambos bits son 1
    *   - ``|``
        - OR
        - Establece cada bit en 1 si uno de los bits es 1
    *   - ``^``
        - XOR
        - Establece cada bit en 1 si solo uno de los bits es 1
    *   - ``~``
        - NOT
        - Invierte todos los bits
    *   - ``<<``
        - Desplazamiento a la izquierda con relleno de ceros
        - Desplaza a la izquierda insertando ceros desde la derecha y dejando que los bits más a la izquierda se pierdan
    *   - ``>>``
        - Desplazamiento a la derecha con signo
        - Desplaza a la derecha insertando copias del bit más a la izquierda desde la izquierda, y dejando que los bits más a la derecha se pierdan

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