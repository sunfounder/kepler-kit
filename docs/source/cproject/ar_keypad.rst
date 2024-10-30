.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. ¡Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte de Expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _ar_keypad:

4.2 - Teclado 4x4
========================

El teclado 4x4, también conocido como teclado matricial, es una matriz de 16 teclas dispuestas en un solo panel.

Los teclados matriciales se encuentran en dispositivos que requieren principalmente entrada digital, como calculadoras, controles remotos de TV, teléfonos con teclado, máquinas expendedoras, cajeros automáticos, cerraduras combinadas y cerraduras digitales para puertas.

En este proyecto, aprenderemos a determinar qué tecla se ha presionado y obtener el valor correspondiente.

* :ref:`cpn_keypad`
* `E.161 - Wikipedia <https://en.wikipedia.org/wiki/E.161>`_

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
        - :ref:`cpn_resistor`
        - 4 (10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_keypad`
        - 1
        - |link_keypad_buy|

**Esquema**

|sch_keypad_ar|

Las filas del teclado (G2 ~ G5) se configuran para estar en alto; si una de las columnas (G6 ~ G9) se lee en alto, sabremos qué tecla se ha presionado.

Por ejemplo, si G6 se lee en alto, entonces se ha presionado la tecla numérica 1; esto es porque los pines de control de la tecla numérica 1 son G2 y G6. Cuando se presiona la tecla 1, G2 y G6 se conectan y G6 también queda en alto.


**Conexión**

|wiring_keypad_ar|

**Código**

.. note::

    * Puedes abrir el archivo ``4.2_4x4_keypad.ino`` en la ruta ``kepler-kit-main/arduino/4.2_4x4_keypad``.
    * O copia este código en el **IDE de Arduino**.
    * Luego selecciona la placa Raspberry Pi Pico y el puerto correcto antes de hacer clic en el botón de carga.
    * Aquí se utiliza la librería ``Adafruit Keypad``, que puedes instalar desde el **Administrador de Librerías**.

      .. image:: img/lib_ad_keypad.png

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/6c776dfc-cb74-49d7-8906-f1382e0e7b7b/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Después de ejecutar el programa, la consola imprimirá las teclas que presionaste en el teclado.

**¿Cómo funciona?**

1. Incluir la Librería

   Comenzamos incluyendo la librería ``Adafruit_Keypad``, que nos permite interactuar fácilmente con el teclado.

   .. code-block:: arduino

     #include "Adafruit_Keypad.h"

2. Configuración del Teclado

   .. code-block:: arduino

     const byte ROWS = 4;
     const byte COLS = 4;
     char keys[ROWS][COLS] = {
       { '1', '2', '3', 'A' },
       { '4', '5', '6', 'B' },
       { '7', '8', '9', 'C' },
       { '*', '0', '#', 'D' }
     };
     byte rowPins[ROWS] = { 2, 3, 4, 5 };
     byte colPins[COLS] = { 8, 9, 10, 11 };

   - Las constantes ``ROWS`` y ``COLS`` definen las dimensiones del teclado.
   - ``keys`` es un array 2D que almacena la etiqueta de cada botón en el teclado.
   - ``rowPins`` y ``colPins`` son arrays que almacenan los pines de Arduino conectados a las filas y columnas del teclado.

   .. raw:: html

      <br/>


3. Inicialización del Teclado

   Crea una instancia de ``Adafruit_Keypad`` llamada ``myKeypad`` e inicialízala.

   .. code-block:: arduino

     Adafruit_Keypad myKeypad = Adafruit_Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

4. Función setup()

   Inicializa la comunicación Serial y el teclado personalizado.

   .. code-block:: arduino

     void setup() {
       Serial.begin(9600);
       myKeypad.begin();
     }

5. Bucle Principal

   Verifica los eventos de teclas y los muestra en el Monitor Serial.

   .. code-block:: arduino

     void loop() {
       myKeypad.tick();
       while (myKeypad.available()) {
         keypadEvent e = myKeypad.read();
         Serial.print((char)e.bit.KEY);
         if (e.bit.EVENT == KEY_JUST_PRESSED) Serial.println(" pressed");
         else if (e.bit.EVENT == KEY_JUST_RELEASED) Serial.println(" released");
       }
       delay(10);
     }

