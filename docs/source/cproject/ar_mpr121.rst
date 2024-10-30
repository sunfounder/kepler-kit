.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. ¡Explora en profundidad Raspberry Pi, Arduino y ESP32 junto a otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte de expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones exclusivas**: Accede de forma anticipada a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _ar_mpr121:

4.3 - Teclado de Electrodos
================================

El MPR121 es una excelente opción cuando deseas agregar un gran número de interruptores táctiles a tu proyecto. Tiene electrodos que se pueden extender con conductores. 
Si conectas los electrodos a un plátano, puedes convertirlo en un interruptor táctil.

* :ref:`cpn_mpr121`

**Componentes necesarios**

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
        - :ref:`cpn_mpr121`
        - 1
        - 

**Esquema**

|sch_mpr121_ar|


**Conexión**

|wiring_mpr121_ar|

**Código**

.. note::

    * Puedes abrir el archivo ``4.3_electrode_keyboard.ino`` en la ruta ``kepler-kit-main/arduino/4.3_electrode_keyboard``. 
    * O copia este código en **Arduino IDE**.
    * Luego selecciona la placa (Raspberry Pi Pico) y el puerto correcto antes de hacer clic en el botón **Upload**.
    * Aquí se utiliza la biblioteca ``Adafruit MPR121``, puedes instalarla desde el **Library Manager**.

      .. image:: img/lib_mpr121.png

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/f31048b7-0f98-4d49-8c2e-26b3908e98cb/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Después de ejecutar el programa, puedes tocar con la mano los doce electrodos en el módulo MPR121 y el estado táctil de estos electrodos se registrará en un array booleano de 12 bits, que se imprimirá en el monitor serial.
Si se tocan el primer y el undécimo electrodo, se imprimirá ``100000000010``.

Puedes extender los electrodos conectando otros conductores, como fruta, cables, papel de aluminio, etc., lo que te dará más formas de activar estos electrodos.

**¿Cómo funciona?**

Inicializa el objeto ``MPR121``. En este punto, el estado de los electrodos del módulo se registrará como valores iniciales.
Si extiendes los electrodos, necesitas volver a ejecutar el ejemplo para restablecer los valores iniciales.

.. code-block:: arduino

    #include "Adafruit_MPR121.h"

    Adafruit_MPR121 cap = Adafruit_MPR121();

    void setup() {
        Serial.begin(9600);
        int check = cap.begin(0x5A);
        if (!check) {
            Serial.println("MPR121 not found, check wiring?");
            while (1);
        }
        Serial.println("MPR121 found!");
    }

Obtén el valor del electrodo actual; obtendrá un valor binario de 12 bits. Si tocas el primer y el undécimo electrodo, obtendrás ``100000000010``.

.. code-block:: arduino

    // Obtener los pads tocados actualmente
    currtouched = cap.touched();

Determina si el estado del electrodo ha cambiado.

.. code-block:: arduino

    void loop() {
        currtouched = cap.touched();
        if (currtouched != lasttouched) {}

        // restablece nuestro estado
        lasttouched = currtouched;
    }

Si se detecta un cambio en el estado del electrodo, los valores de ``currtouched`` se almacenan en el array ``touchStates[12]`` bit a bit. Finalmente, se imprime el array.

.. code-block:: arduino

    if (currtouched != lasttouched) {
        for (int i = 0; i < 12; i++) {
            if (currtouched & (1 << i)) touchStates[i] = 1;
            else touchStates[i] = 0;
        }
        for (int i = 0; i < 12; i++){
            Serial.print(touchStates[i]);
        }
        Serial.println();
    }