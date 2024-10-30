.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. ¡Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte de Expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _ar_dht11:

6.2 - Temperatura y Humedad
=======================================

La humedad y la temperatura están estrechamente relacionadas tanto en términos de cantidad física como en la vida cotidiana.
La temperatura y humedad del ambiente humano afectan directamente la función termorreguladora y el efecto de transferencia de 
calor del cuerpo, impactando la actividad mental y el estado de ánimo, lo que a su vez influye en nuestra eficiencia en el estudio y el trabajo.

La temperatura es una de las siete magnitudes físicas básicas del Sistema Internacional de Unidades y se utiliza para medir el 
grado de calor o frío de un objeto. La escala Celsius, representada por el símbolo "℃", es una de las escalas de temperatura más utilizadas en el mundo.

La humedad es la concentración de vapor de agua presente en el aire. En la vida cotidiana se 
utiliza comúnmente la humedad relativa del aire, expresada en %RH, la cual está estrechamente 
relacionada con la temperatura. En un volumen de gas sellado, cuanto mayor es la temperatura, 
menor es la humedad relativa, y cuanto menor es la temperatura, mayor es la humedad relativa.

|img_Dht11|

Este kit incluye un sensor básico de temperatura y humedad digital, el **DHT11**.
Utiliza un sensor capacitivo de humedad y un termistor para medir el aire circundante y emite una señal digital en los pines de datos (no se requieren pines de entrada analógicos).

* :ref:`cpn_dht11`

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
        - :ref:`cpn_dht11`
        - 1
        - |link_dht22_buy|

**Esquema**

|sch_dht11|

**Conexión**

|wiring_dht11|

**Código**

.. note::

    * Puedes abrir el archivo ``6.2_dht11.ino`` en la ruta ``kepler-kit-main/arduino/6.2_dht11``.
    * O copia este código en el **Arduino IDE**.
    * Luego selecciona la placa Raspberry Pi Pico y el puerto correcto antes de hacer clic en el botón de carga.
    * Aquí se utiliza la librería ``DHT sensor library``, que puedes instalar desde el **Administrador de Librerías**.

      .. image:: img/lib_dht.png

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/b9e96e99-59d4-48ca-b41f-c03577acfb8f/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Una vez que el código esté en ejecución, verás que el Monitor Serial imprime continuamente la temperatura y la humedad; a medida que el programa se estabiliza, estos valores serán cada vez más precisos.

**¿Cómo funciona?**

#. Inclusión de las librerías necesarias y definición de constantes.
   En esta parte del código, se incluye la librería del sensor DHT y se definen el número de pin y el tipo de sensor utilizados en este proyecto.

   .. code-block:: arduino
    
      #include <DHT.h>
      #define DHTPIN 16       // Define el pin usado para conectar el sensor
      #define DHTTYPE DHT11  // Define el tipo de sensor

#. Creación del objeto DHT.
   Aquí creamos un objeto DHT utilizando el número de pin y el tipo de sensor definidos.

   .. code-block:: arduino

      DHT dht(DHTPIN, DHTTYPE);  // Crea un objeto DHT

#. Esta función se ejecuta una vez al iniciar el Arduino. Inicializamos la comunicación serial y el sensor DHT en esta función.

   .. code-block:: arduino

      void setup() {
        Serial.begin(9600);
        Serial.println(F("Prueba de DHT11!"));
        dht.begin();  // Inicializa el sensor DHT
      }

#. Bucle principal.
   La función ``loop()`` se ejecuta continuamente después de la función setup. Aquí, leemos los valores de humedad y temperatura, calculamos el índice de calor y mostramos estos valores en el monitor serial. Si la lectura del sensor falla (retorna NaN), se imprime un mensaje de error.

   .. note::
    
      El |link_heat_index| es una forma de medir cómo se siente el calor en el ambiente, combinando la temperatura del aire y la humedad. También se le llama "temperatura aparente" o "sensación térmica".

   .. code-block:: arduino

      void loop() {
        delay(2000);
        float h = dht.readHumidity();
        float t = dht.readTemperature();
        float f = dht.readTemperature(true);
        if (isnan(h) || isnan(t) || isnan(f)) {
          Serial.println(F("Failed to read from DHT sensor!"));
          return;
        }
        float hif = dht.computeHeatIndex(f, h);
        float hic = dht.computeHeatIndex(t, h, false);
        Serial.print(F("Humidity: "));
        Serial.print(h);
        Serial.print(F("%  Temperature: "));
        Serial.print(t);
        Serial.print(F("°C "));
        Serial.print(f);
        Serial.print(F("°F  Heat index: "));
        Serial.print(hic);
        Serial.print(F("°C "));
        Serial.print(hif);
        Serial.println(F("°F"));
      }
