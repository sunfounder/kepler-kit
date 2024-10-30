.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. ¡Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte de Expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _ar_irremote:

6.4 - Control Remoto Infrarrojo (IR)
=======================================

En la electrónica de consumo, los controles remotos se utilizan para operar dispositivos como televisores y reproductores de DVD.
En algunos casos, permiten a las personas operar dispositivos fuera de su alcance, como aires acondicionados centrales.

El receptor IR es un componente con una fotocélula ajustada para recibir luz infrarroja. 
Se usa casi siempre para la detección de controles remotos; cada televisor y reproductor de DVD tiene uno de estos en la parte frontal para recibir la señal IR del mando. 
Dentro del control remoto hay un LED IR correspondiente que emite pulsos IR para indicar al televisor que se encienda, apague o cambie de canal.

* :ref:`cpn_ir_receiver`

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
        - :ref:`cpn_ir_receiver`
        - 1
        - |link_receiver_buy|

**Esquema**

|sch_irrecv|

**Conexión**

|wiring_irrecv|

**Código**

.. note::

    * Puedes abrir el archivo ``6.4_ir_remote_control.ino`` en la ruta ``kepler-kit-main/arduino/6.4_ir_remote_control``.
    * O copia este código en el **IDE de Arduino**.
    * Luego selecciona la placa Raspberry Pi Pico y el puerto correcto antes de hacer clic en el botón de carga.
    * Aquí se utiliza la librería ``IRremote``, que puedes instalar desde el **Administrador de Librerías**.

      .. image:: img/lib_ir.png

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/71f50561-d1ad-4d9e-9db2-8eb7727df0a4/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

El control remoto nuevo tiene una pieza de plástico en el extremo para aislar la batería interna. Necesitas retirar esta pieza para activar el control remoto cuando lo uses.
Una vez que el programa esté en ejecución, al presionar el control remoto, el Monitor Serial imprimirá la tecla que presionaste.


**¿Cómo funciona?**

Este código está diseñado para funcionar con un control remoto infrarrojo (IR) utilizando la librería ``IRremote``. A continuación se explica cada parte:

#. Inclusión de la librería y definición de constantes. Primero, se incluye la librería IRremote y se define el número de pin para el receptor IR como 2.

   .. code-block:: cpp
 
     #include <IRremote.h>
     const int IR_RECEIVE_PIN = 17;

#. Inicializa la comunicación serial a una velocidad de 9600 baudios. Inicializa el receptor IR en el pin especificado (``IR_RECEIVE_PIN``) y habilita el LED de retroalimentación (si corresponde).

   .. code-block:: arduino

       void setup() {
           Serial.begin(9600);                                     // Inicia la comunicación serial a 9600 baudios
           IrReceiver.begin(IR_RECEIVE_PIN, ENABLE_LED_FEEDBACK);  // Inicia el receptor IR
       }

#. El bucle se ejecuta continuamente para procesar las señales del control remoto IR.

   .. code-block:: arduino

      void loop() {
         if (IrReceiver.decode()) {  // Verifica si el receptor IR ha recibido una señal
            bool result = 0;
            String key = decodeKeyValue(IrReceiver.decodedIRData.command);
            if (key != "ERROR") {
              Serial.println(key);  // Imprime el comando decodificado
              delay(100);
            }
         IrReceiver.resume();  // Prepara el receptor IR para recibir la siguiente señal
        }
      }
   
   * Verifica si se ha recibido y decodificado correctamente una señal IR.
   * Decodifica el comando IR y lo almacena en ``decodedValue`` usando la función personalizada ``decodeKeyValue()``.
   * Imprime el valor IR decodificado en el monitor serial.
   * Restaura el receptor IR para la próxima señal.

   .. raw:: html

        <br/>

#. Función auxiliar para mapear señales IR recibidas a las teclas correspondientes.

   .. image:: img/ir_key.png
      :align: center
      :width: 80%

   .. code-block:: arduino

      // Función para mapear señales IR recibidas a las teclas correspondientes
      String decodeKeyValue(long result) {
        // Cada caso corresponde a un comando específico del control remoto IR
        switch (result) {
          case 0x16:
            return "0";
          case 0xC:
            return "1";
          case 0x18:
            return "2";
          case 0x5E:
            return "3";
          case 0x8:
            return "4";
          case 0x1C:
            return "5";
          case 0x5A:
            return "6";
          case 0x42:
            return "7";
          case 0x52:
            return "8";
          case 0x4A:
            return "9";
          case 0x9:
            return "+";
          case 0x15:
            return "-";
          case 0x7:
            return "EQ";
          case 0xD:
            return "U/SD";
          case 0x19:
            return "CYCLE";
          case 0x44:
            return "PLAY/PAUSE";
          case 0x43:
            return "FORWARD";
          case 0x40:
            return "BACKWARD";
          case 0x45:
            return "POWER";
          case 0x47:
            return "MUTE";
          case 0x46:
            return "MODE";
          case 0x0:
            return "ERROR";
          default:
            return "ERROR";
        }
      }



