.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Explora en profundidad sobre Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_lcd:

3.4 Pantalla de Cristal Líquido
=====================================

El LCD1602 es una pantalla de cristal líquido de tipo carácter, capaz de 
mostrar 32 caracteres (16*2) simultáneamente.

Como bien sabemos, aunque el LCD y otras pantallas enriquecen la interacción 
entre el usuario y la máquina, todas comparten una debilidad común. Cuando se 
conectan a un controlador, ocupan múltiples puertos de entrada/salida (IO), 
lo cual es una limitación si el controlador no cuenta con muchos puertos. 
Además, esto restringe otras funciones del controlador. Por lo tanto, el LCD1602 
con un bus I2C se desarrolló para resolver este problema.

* :ref:`cpn_i2c_lcd`
* `Inter-Integrated Circuit - Wikipedia <https://en.wikipedia.org/wiki/I2C>`_

|pin_i2c|

Aquí utilizaremos la interfaz I2C0 para controlar el LCD1602 y mostrar texto.


**Componentes Necesarios**

En este proyecto, necesitaremos los siguientes componentes.

Es más conveniente adquirir un kit completo. Aquí tienes el enlace:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nombre
        - ELEMENTOS EN ESTE KIT
        - ENLACE
    *   - Kit Kepler
        - 450+
        - |link_kepler_kit|

También puedes comprarlos por separado en los enlaces a continuación.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - COMPONENTE
        - CANTIDAD
        - ENLACE

    *   - 1
        - :ref:`cpn_pico_w`
        - 1
        - |link_picow_buy|
    *   - 2
        - Cable Micro USB
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Varios
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|

**Esquema**

|sch_lcd|

**Conexiones**

|wiring_lcd|

**Código**

.. note::

    * Abre el archivo ``3.4_liquid_crystal_display.py`` en la ruta ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

    * Aquí necesitas usar la biblioteca llamada ``lcd1602.py``, verifica si ha sido cargada en Pico W. Para un tutorial detallado, consulta :ref:`add_libraries_py`.

.. code-block:: python

    from machine import I2C, Pin
    from lcd1602 import LCD
    import time

    # Inicializar la comunicación I2C
    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)

    # Crear un objeto LCD para interactuar con la pantalla LCD1602
    lcd = LCD(i2c)

    # Mostrar el primer mensaje en el LCD
    # Utilizar '\n' para crear una nueva línea.
    string = "SunFounder\n    LCD Tutorial"
    lcd.message(string)
    # Esperar 2 segundos
    time.sleep(2)
    # Limpiar la pantalla
    lcd.clear()

    # Mostrar el segundo mensaje en el LCD
    string = "Hello\n  World!"
    lcd.message(string)
    # Esperar 5 segundos
    time.sleep(5)
    # Limpiar la pantalla antes de salir
    lcd.clear()

Después de que el programa se ejecute, podrás ver dos líneas de texto que aparecerán en el LCD en secuencia y luego desaparecerán.

.. note:: When the code is running, if the screen is blank, you can turn the potentiometer on the back to increase the contrast.

**¿Cómo funciona?**

#. Configuración de la Comunicación I2C

   El módulo ``machine`` se utiliza para configurar la comunicación I2C. Se definen los pines SDA (Serial Data) y SCL (Serial Clock) (pines 20 y 21 respectivamente), junto con la frecuencia de I2C (400kHz).

   .. code-block:: python
      
      from machine import I2C, Pin
      i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)

#. Inicialización de la Pantalla LCD

   La clase ``LCD`` del módulo ``lcd1602`` se instancia para manejar la comunicación con la pantalla LCD a través de I2C. Se crea un objeto ``LCD`` usando el objeto ``i2c``.

   Para más detalles sobre el uso de la biblioteca ``lcd1602``, consulta el archivo ``lcd1602.py``.

   .. code-block:: python
      
      from lcd1602 import LCD
      lcd = LCD(i2c)

#. Mostrando Mensajes en la Pantalla LCD

   El método ``message`` del objeto ``LCD`` se usa para mostrar texto en la pantalla. El carácter ``\n`` crea una nueva línea en el LCD. La función ``time.sleep()`` pausa la ejecución durante el número de segundos especificado.

   .. code-block:: python
      
      string = "SunFounder\n    LCD Tutorial"
      lcd.message(string)
      time.sleep(2)
      lcd.clear()

#. Limpiar la Pantalla

   El método ``clear`` del objeto ``LCD`` se llama para borrar el texto de la pantalla.

   .. code-block:: python
      
      lcd.clear()

#. Mostrando un Segundo Mensaje

   Se muestra un nuevo mensaje, seguido de una demora y luego se borra nuevamente la pantalla.

   .. code-block:: python
      
      string = "Hello\n  World!"
      lcd.message(string)
      time.sleep(5)
      lcd.clear()

