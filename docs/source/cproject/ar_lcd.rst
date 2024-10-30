.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. ¡Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte de Expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _ar_lcd:

3.4 - Pantalla de Cristal Líquido
======================================

El LCD1602 es una pantalla de cristal líquido de tipo característico que puede mostrar 32 caracteres (16*2) simultáneamente.

Como bien se sabe, aunque las pantallas LCD y otros dispositivos visuales enriquecen enormemente la interacción hombre-máquina, 
comparten una desventaja común: cuando se conectan a un controlador, ocupan múltiples pines de E/S, lo cual puede ser problemático 
en controladores con pocos puertos externos, además de restringir otras funciones del controlador. 
Por eso, el LCD1602 con bus I2C fue desarrollado para solucionar este problema.

* :ref:`cpn_i2c_lcd`
* `Inter-Integrated Circuit - Wikipedia <https://en.wikipedia.org/wiki/I2C>`_


|pin_i2c|

Aquí usaremos la interfaz I2C0 para controlar el LCD1602 y mostrar texto.

**Componentes Necesarios**

Para este proyecto, necesitamos los siguientes componentes.

Es muy conveniente adquirir un kit completo, aquí tienes el enlace:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nombre
        - ITEMS EN ESTE KIT
        - LINK DE COMPRA
    *   - Kit Kepler
        - 450+
        - |link_kepler_kit|

También puedes comprarlos por separado en los enlaces a continuación.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - N°
        - INTRODUCCIÓN DEL COMPONENTE
        - CANTIDAD
        - LINK DE COMPRA

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

|sch_lcd_ar|

**Conexión**

|wiring_lcd_ar|

**Código**

.. note::

    * Puedes abrir el archivo ``3.4_liquid_crystal_display.ino`` en la ruta ``kepler-kit-main/arduino/3.4_liquid_crystal_display``.
    * O copia este código en el **Arduino IDE**.
    * Luego selecciona la placa Raspberry Pi Pico y el puerto correcto antes de hacer clic en el botón de carga.
    * Aquí se utiliza la librería ``LiquidCrystal I2C``, que puedes instalar desde el **Administrador de Librerías**.

      .. image:: img/lib_i2c_lcd.png

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/1f464967-5937-473a-8a0d-8e4577c85e7d/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Después de cargar el código correctamente, verás "SunFounder" y "Hello World" en el LCD I2C1602.

.. note:: 
    Si el código y la conexión están bien, pero la pantalla LCD aún no muestra contenido, puedes ajustar el potenciómetro en la parte posterior para aumentar el contraste.

**¿Cómo funciona?**

Llamando a la biblioteca ``LiquidCrystal_I2C.h``, puedes controlar fácilmente la LCD.

.. code-block:: arduino

    #include "LiquidCrystal_I2C.h"

**Funciones de la Biblioteca**

.. code-block:: arduino

    LiquidCrystal_I2C(uint8_t lcd_Addr,uint8_t lcd_cols,uint8_t lcd_rows)

Crea una nueva instancia de la clase ``LiquidCrystal_I2C`` que representa una LCD específica conectada a tu placa Arduino.

- **lcd_Addr**: La dirección de la LCD, que por defecto es 0x27.
- **lcd_cols**: El LCD1602 tiene 16 columnas.
- **lcd_rows**: El LCD1602 tiene 2 filas.

.. code-block:: arduino

    void init()

Inicializa la LCD.

.. code-block:: arduino

    void backlight()

Activa la retroiluminación (opcional).

.. code-block:: arduino

    void nobacklight()

Apaga la retroiluminación (opcional).

.. code-block:: arduino

    void display()

Activa la pantalla LCD.

.. code-block:: arduino

    void nodisplay()

Apaga rápidamente la pantalla LCD.

.. code-block:: arduino

    void clear()

Limpia la pantalla y coloca el cursor en la posición cero.

.. code-block:: arduino

    void setCursor(uint8_t col,uint8_t row)

Coloca el cursor en la posición col, row.

.. code-block:: arduino

    void print(data,BASE)

Imprime texto en la LCD.

- **data**: Los datos a imprimir (char, byte, int, long o string).

- **BASE (opcional)**: La base en la que imprimir números: BIN para binario (base 2), DEC para decimal (base 10), OCT para octal (base 8), HEX para hexadecimal (base 16).

**Aprende Más**

Sube el código al Pico W, y el contenido que ingreses en el monitor serial se imprimirá en la LCD.

.. note::

   * Puedes abrir el archivo ``3.4_liquid_crystal_display_2.ino`` en la ruta ``kepler-kit-main/arduino/3.4_liquid_crystal_display_2``.
   * O copia este código en el **Arduino IDE**.
   * No olvides seleccionar la placa (Raspberry Pi Pico) y el puerto correcto antes de hacer clic en el botón **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/631e0380-d594-4a8b-9bac-eb0688079b97/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Además de leer datos de los componentes electrónicos, el Pico W 
puede leer datos ingresados en el monitor del puerto serial, y puedes 
usar ``Serial.read()`` como controlador en el experimento del circuito.

Ejecuta la comunicación serial en ``setup()`` y configura la tasa de datos a 9600.

.. code-block:: arduino

    Serial.begin(9600);

El estado del monitor serial se evalúa en ``loop()``, y el procesamiento de información solo se realiza cuando se reciben datos.

.. code-block:: arduino

    if (Serial.available() > 0){}

Limpia la pantalla.

.. code-block:: arduino

    lcd.clear();

Lee el valor de entrada en el monitor serial y lo almacena en la variable incomingByte.

.. code-block:: arduino

    char incomingByte = Serial.read();

Muestra cada carácter en la LCD y omite el carácter de salto de línea.

.. code-block:: arduino

    while (Serial.available() > 0) {
        char incomingByte=Serial.read();
        if(incomingByte==10){break;}// omite el carácter de salto de línea
        lcd.print(incomingByte);// muestra cada carácter en la LCD  
    } 


* `Serial Read <https://www.arduino.cc/reference/en/language/functions/communication/serial/read/>`_
