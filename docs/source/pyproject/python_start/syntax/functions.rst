.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte de expertos**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Funciones
==============

En MicroPython, una función es un conjunto de instrucciones relacionadas que realizan una tarea específica.

Las funciones ayudan a dividir nuestro programa en bloques modulares más pequeños. A medida que el plan se hace más grande, las funciones lo hacen más organizado y fácil de gestionar.

Además, evitan la duplicación y hacen que el código sea reutilizable.

Crear una Función
-----------------------

.. code-block::

    def function_name(parameters): 
        """docstring"""
        statement(s)

* Una función se define usando la palabra clave ``def``

* Un nombre de función para identificarla de manera única. El nombre de la función sigue las mismas reglas que el nombre de una variable:
    
   * Puede contener números, letras y guiones bajos.
   * El primer carácter debe ser una letra o guion bajo.
   * Distingue entre mayúsculas y minúsculas.

* Parámetros (argumentos) a través de los cuales pasamos valores a una función. Son opcionales.

* Los dos puntos (:) marcan el final de la cabecera de la función.

* La docstring opcional se usa para describir la función; se suelen utilizar comillas triples para que se pueda expandir a varias líneas.

* Una o más instrucciones válidas en Micropython que constituyen el cuerpo de la función. Las instrucciones deben tener el mismo nivel de sangría (generalmente 4 espacios).

* Cada función necesita al menos una declaración, pero si por alguna razón hay una función sin contenido, utiliza la declaración pass para evitar errores.

* Una declaración ``return`` opcional para devolver un valor desde la función.


Llamar a una Función
------------------------

Para llamar a una función, añade paréntesis después del nombre de la función.

.. code-block:: python

    def my_function():
        print("Your first function")

    my_function()

>>> %Run -c $EDITOR_CONTENT
Your first function

La Instrucción return
--------------------------

La instrucción return se usa para salir de una función y volver al lugar donde fue llamada.

**Sintaxis de return**

.. code-block:: python

    return [expression_list]

La declaración puede contener una expresión que se evalúa y devuelve un valor. Si no hay ninguna expresión o si la instrucción ``return`` no existe en la función, la función devolverá un objeto ``None``.

.. code-block:: python

    def my_function():
            print("Your first function")

    print(my_function())

>>> %Run -c $EDITOR_CONTENT
Your first function
None

Aquí, ``None`` es el valor devuelto, porque no se utilizó la instrucción ``return``.

Argumentos
-------------

Se puede pasar información a la función como argumentos.

Especifica los argumentos entre paréntesis después del nombre de la función. Puedes añadir tantos argumentos como necesites, solo sepáralos con comas.

.. code-block:: python

    def welcome(name, msg):
        """This is a welcome function for
        the person with the provided message"""
        print("Hello", name + ', ' + msg)

    welcome("Lily", "Welcome to China!")

>>> %Run -c $EDITOR_CONTENT
Hello Lily, Welcome to China!

Número de Argumentos
*************************

Por defecto, se debe llamar a una función con el número correcto de argumentos. Es decir, si la función espera 2 parámetros, debes llamarla con 2 argumentos, ni más ni menos.

.. code-block:: python

    def welcome(name, msg):
        """This is a welcome function for
        the person with the provided message"""
        print("Hello", name + ', ' + msg)

    welcome("Lily", "Welcome to China!")

Aquí, la función bienvenida() tiene 2 parámetros.

Dado que llamamos a esta función con dos argumentos, se ejecuta sin problemas ni errores.

Si se llama con un número diferente de argumentos, el intérprete mostrará un mensaje de error.

A continuación se muestra la llamada a esta función, que contiene un argumento y ninguna, con sus respectivos mensajes de error.

.. code-block::

    welcome("Lily")＃Only one argument

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
TypeError: function takes 2 positional arguments but 1 were given

.. code-block::

    welcome()＃No arguments

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
TypeError: function takes 2 positional arguments but 0 were given


Argumentos Predeterminados
*****************************

En MicroPython, podemos usar el operador de asignación (=) para proporcionar un valor predeterminado a un parámetro.

Si llamamos a la función sin argumentos, se utiliza el valor predeterminado.

.. code-block:: python

    def welcome(name, msg = "Welcome to China!"):
        """This is a welcome function for
        the person with the provided message"""
        print("Hello", name + ', ' + msg)
    welcome("Lily")

>>> %Run -c $EDITOR_CONTENT
Hola Lily, ¡Bienvenido a China!

En esta función, el parámetro ``nombre`` no tiene un valor predeterminado y es obligatorio durante la llamada.

Por otro lado, el valor predeterminado del parámetro ``msg`` es "¡Bienvenido a China!". Por lo tanto, es opcional en la llamada. Si se proporciona un valor, sobrescribirá el valor predeterminado.

Cualquier número de argumentos en la función puede tener un valor predeterminado. Sin embargo, una vez que se define un argumento predeterminado, todos los argumentos a su derecha también deben tener valores predeterminados.

Esto significa que los argumentos no predeterminados no pueden seguir a los argumentos predeterminados.

Por ejemplo, si definimos la función anterior como:

.. code-block:: python

    def welcome(name = "Lily", msg):

Recibiremos el siguiente mensaje de error:

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
SyntaxError: non-default argument follows default argument


Argumentos de Palabra Clave
********************************

Cuando llamamos a una función con ciertos valores, estos se asignan a los argumentos según su posición.

Por ejemplo, en la función bienvenida(), cuando la llamamos como bienvenida("Lily", "¡Bienvenido a China!"), el valor "Lily" se asigna al parámetro ``nombre`` y "¡Bienvenido a China!" al parámetro ``msg``.

MicroPython permite llamar a funciones con argumentos de palabra clave. Al llamar a la función de esta manera, el orden (posición) de los argumentos puede cambiar.

.. code-block:: python

    # argumentos de palabra clave
    bienvenida(nombre = "Lily", msg = "¡Bienvenido a China!")

    # argumentos de palabra clave (fuera de orden)
    bienvenida(msg = "¡Bienvenido a China!", nombre = "Lily") 

    # 1 argumento posicional, 1 argumento de palabra clave
    bienvenida("Lily", msg = "¡Bienvenido a China!")

Como vemos, podemos mezclar argumentos posicionales y de palabra clave durante la llamada a la función. Pero debemos recordar que los argumentos de palabra clave deben ir después de los argumentos posicionales.

Tener un argumento posicional después de un argumento de palabra clave dará como resultado un error.

Por ejemplo, si la llamada a la función es como sigue:

.. code-block:: python

    welcome(name="Lily","Welcome to China!")

Will result in an error:

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
SyntaxError: non-keyword arg after keyword arg


Argumentos Arbitrarios
*************************

A veces, si no conocemos la cantidad de argumentos que se pasarán a la función de antemano.

En la definición de la función, podemos agregar un asterisco (*) antes del nombre del parámetro.

.. code-block:: python

    def welcome(*names):
        """This function welcomes all the person
        in the name tuple"""
        #names is a tuple with arguments
        for name in names:
            print("Welcome to China!", name)
            
    welcome("Lily","John","Wendy")

>>> %Run -c $EDITOR_CONTENT
Welcome to China! Lily
Welcome to China! John
Welcome to China! Wendy

Aquí, hemos llamado a la función con múltiples argumentos. Estos argumentos se empaquetan en una tupla antes de pasarse a la función.

Dentro de la función, utilizamos un bucle for para recuperar todos los argumentos.

Recursividad
----------------
En Python, sabemos que una función puede llamar a otras funciones. Incluso es posible que una función se llame a sí misma. Este tipo de estructura se denomina función recursiva.

Esto permite hacer ciclos sobre datos hasta llegar a un resultado.

El desarrollador debe tener mucho cuidado con la recursividad, ya que es fácil escribir una función que nunca termine o que use cantidades excesivas de memoria o potencia de procesamiento. Sin embargo, cuando se escribe correctamente, la recursividad puede ser un enfoque eficiente y matemáticamente elegante para la programación.

.. code-block:: python

    def rec_func(i):
        if(i > 0):
            result = i + rec_func(i - 1)
            print(result)
        else:
            result = 0
        return result

    rec_func(6)

>>> %Run -c $EDITOR_CONTENT
1
3
6
10
15
21

En este ejemplo, func_recursiva() es una función que hemos definido para llamarse a sí misma ("recursividad"). Usamos la variable ``i`` como dato, y se disminuirá (-1) cada vez que la función se llame recursivamente. Cuando la condición ya no es mayor que 0 (es decir, llega a 0), la recursión termina.


Para los nuevos desarrolladores, puede tomar un tiempo comprender cómo funciona, y la mejor manera de aprender es probándola y modificándola.

**Ventajas de la Recursividad**

* Las funciones recursivas hacen que el código sea más limpio y elegante.
* Una tarea compleja se puede descomponer en subproblemas más simples mediante la recursividad.
* La generación de secuencias es más sencilla con la recursividad que usando algunas iteraciones anidadas.

**Desventajas de la Recursividad**

* A veces, la lógica detrás de la recursividad es difícil de seguir.
* Las llamadas recursivas son costosas (ineficientes), ya que ocupan mucha memoria y tiempo.
* Las funciones recursivas son difíciles de depurar.

