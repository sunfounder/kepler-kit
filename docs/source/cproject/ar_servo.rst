.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _ar_servo:

3.7 - Balanceo de un Servo
===============================

En este kit, además del LED y el zumbador pasivo, también tenemos un dispositivo controlado por señal PWM: el servo.

Un servo es un dispositivo de servomecanismo de posición (ángulo), adecuado para sistemas de control que requieren cambios constantes de ángulo y deben mantenerse en ese estado. Los servos son ampliamente usados en juguetes de control remoto avanzados, como aviones, modelos de submarinos y robots.

¡Ahora intentemos hacer que el servo oscile!

* :ref:`cpn_servo`

**Componentes Necesarios**

En este proyecto, necesitamos los siguientes componentes.

Es muy conveniente comprar un kit completo; aquí está el enlace:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nombre
        - ELEMENTOS EN ESTE KIT
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
        - :ref:`cpn_servo`
        - 1
        - |link_servo_buy|

**Esquema**

|sch_servo|

**Conexión**

|wiring_servo|

* El cable naranja es la señal y está conectado a GP15.
* El cable rojo es VCC y está conectado a VBUS (5V).
* El cable marrón es GND y está conectado a GND.


**Código**

.. note::

    * Puedes abrir el archivo ``3.7_swinging_servo.ino`` en la ruta ``kepler-kit-main/arduino/3.7_swinging_servo``. 
    * O copia este código en el **Arduino IDE**.
    * No olvides seleccionar la placa (Raspberry Pi Pico) y el puerto correcto antes de hacer clic en el botón **Subir**.

.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/d52a67be-be6b-4cbf-b411-810160f56928/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


Al ejecutar el programa, veremos el brazo del servo moviéndose de un lado a otro de 0° a 180°.


**¿Cómo funciona?**

Al llamar a la biblioteca ``Servo.h``, puedes controlar el servo fácilmente.

.. code-block:: arduino

    #include <Servo.h> 

**Funciones de la Biblioteca**

.. code-block:: arduino

    Servo

Crear un objeto **Servo** para controlar el servo.

.. code-block:: arduino

    uint8_t attach(int pin); 

Convierte un pin en controlador de servo. Llama a pinMode. Devuelve 0 si falla.

.. code-block:: arduino

    void detach();

Libera un pin del control de servo.

.. code-block:: arduino

    void write(int value); 

Establece el ángulo del servo en grados, de 0 a 180.

.. code-block:: arduino

    int read();

Devuelve el valor establecido con el último write().

.. code-block:: arduino

    bool attached(); 

Devuelve 1 si el servo está actualmente conectado.
