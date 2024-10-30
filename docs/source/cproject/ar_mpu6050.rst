.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Explora a fondo Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirse?**

    - **Soporte de expertos**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones exclusivas**: Obtén acceso anticipado a anuncios y adelantos de nuevos productos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _ar_mpu6050:

6.3 - Seguimiento de Movimiento en 6 Ejes
=============================================

El MPU-6050 es un dispositivo de seguimiento de movimiento en 6 ejes (combinando un giroscopio de 3 ejes y un acelerómetro de 3 ejes).


Un acelerómetro es una herramienta que mide la aceleración propia. Por ejemplo, un acelerómetro en reposo en la superficie terrestre medirá una aceleración debida a la gravedad de la Tierra, orientada hacia arriba [3], con un valor aproximado de g ≈ 9.81 m/s².

Los acelerómetros tienen muchos usos en la industria y la ciencia. Ejemplos incluyen sistemas de navegación inercial para aviones y misiles, y para mantener imágenes en dispositivos como tabletas y cámaras digitales en posición vertical.

Los giroscopios se utilizan para medir la orientación y la velocidad angular de un dispositivo. Sus aplicaciones incluyen sistemas 
de antirrolido y de bolsas de aire para automóviles, sistemas de detección de movimiento para dispositivos inteligentes, sistemas de estabilización de actitud para drones, entre otros.

* :ref:`cpn_mpu6050`

**Componentes necesarios**

En este proyecto, necesitamos los siguientes componentes.

Es muy conveniente comprar un kit completo, aquí está el enlace:

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
        - :ref:`cpn_mpu6050`
        - 1
        - 

**Esquema**

|sch_mpu6050_ar|

**Conexión**

|wiring_mpu6050_ar|

**Código**

.. note::

    * Puedes abrir el archivo ``6.3_6axis_motion_tracking.ino`` en la ruta ``kepler-kit-main/arduino/6.3_6axis_motion_tracking``.
    * O copiar este código en el **IDE de Arduino**.
    * Luego selecciona la placa (Raspberry Pi Pico) y el puerto correcto antes de hacer clic en el botón **Upload**.
    * Aquí se utiliza la biblioteca ``Adafruit MPU6050``, que puedes instalar desde el **Library Manager**.

      .. image:: img/lib_mpu6050.png

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/318f62d3-1d7b-4ee6-a1a2-97e783cf2d5e/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>
    

Después de ejecutar el programa, verás que los valores del acelerómetro en 3 ejes y del giroscopio en 3 ejes 
aparecen en la salida de manera continua. En este momento, si giras el MPU6050 en cualquier dirección, notarás 
cómo estos valores cambian en consecuencia. Para facilitar la visualización, puedes comentar alguna línea de 
impresión y concentrarte en otro conjunto de datos.

**¿Cómo funciona?**

Instancia un objeto ``MPU6050``.

.. code-block:: arduino

    #include <Adafruit_MPU6050.h>
    #include <Wire.h>

    Adafruit_MPU6050 mpu;

Inicializa el MPU6050 y configura su precisión.

.. code-block:: arduino

    void setup(void) {
        Serial.begin(115200);
        while (!Serial)
            delay(10); // pausará Zero, Leonardo, etc. hasta que se abra la consola serial

        Serial.println("Adafruit MPU6050 test!");

        // Intenta inicializar
        if (!mpu.begin()) {
            Serial.println("Failed to find MPU6050 chip");
            while (1) {
                delay(10);
            }
        }
        Serial.println("MPU6050 Found!");

        // Configura el rango
        mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
        mpu.setGyroRange(MPU6050_RANGE_500_DEG);
        mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);

        Serial.println("");
        delay(100);
    }

Obtén nuevos eventos de sensor con las lecturas.

.. code-block:: arduino

    sensors_event_t a, g, temp;
    mpu.getEvent(&a, &g, &temp);

Posteriormente, podrás obtener valores de aceleración y velocidad angular en tiempo real en los datos ``a.acceleration.x``, ``a.acceleration.y``, ``a.acceleration.z``, ``g.gyro.x``, ``g.gyro.y``, ``g.gyro.z``.

.. code-block:: arduino

    Serial.print("Acceleration X: ");
    Serial.print(a.acceleration.x);
    Serial.print(", Y: ");
    Serial.print(a.acceleration.y);
    Serial.print(", Z: ");
    Serial.print(a.acceleration.z);
    Serial.println(" m/s^2");

    Serial.print("Rotation X: ");
    Serial.print(g.gyro.x);
    Serial.print(", Y: ");
    Serial.print(g.gyro.y);
    Serial.print(", Z: ");
    Serial.print(g.gyro.z);
    Serial.println(" rad/s");