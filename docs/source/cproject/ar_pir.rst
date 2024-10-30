.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Explora a fondo Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte de expertos**: Resuelve problemas postventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _ar_pir:

2.10 - Detectar Movimiento Humano
=========================================

El sensor de infrarrojos pasivo (sensor PIR) es un dispositivo común que 
puede medir la luz infrarroja (IR) emitida por objetos dentro de su campo 
de visión. En términos simples, detecta la radiación infrarroja emitida 
por el cuerpo humano, permitiendo así la detección de movimientos de personas 
y otros animales. Más específicamente, informa a la placa de control principal 
que alguien ha ingresado en tu espacio.

:ref:`cpn_pir`

**Componentes necesarios**

En este proyecto, necesitamos los siguientes componentes.

Es muy conveniente comprar un kit completo; aquí está el enlace:

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
        - :ref:`cpn_pir`
        - 1
        - |link_pir_buy|

**Esquema**

|sch_pir|

Cuando el módulo PIR detecta movimiento cercano, el pin GP14 estará en alto; de lo contrario, estará en bajo.

**Conexión**

|wiring_pir|

**Código**

.. note::

    * Puedes abrir el archivo ``2.10_detect_human_movement.ino`` en la ruta ``kepler-kit-main/arduino/2.10_detect_human_movement``.
    * O copiar este código en el **Arduino IDE**.
    * No olvides seleccionar la placa Raspberry Pi Pico y el puerto correcto antes de hacer clic en el botón **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/bb3ff9f1-127d-4279-84b9-cba28b9667e8/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Después de ejecutar el programa, si el módulo PIR detecta a alguien cerca, el Monitor Serial mostrará "¡Alguien está aquí!"

**Más información**

El PIR es un sensor muy sensible. Para adaptarlo al entorno, es necesario ajustarlo. Coloca la cara con los 2 potenciómetros 
frente a ti, gira ambos potenciómetros completamente en sentido contrario a las agujas del reloj y conecta el jumper en el pin 
L y el pin central.

|img_pir_back|

1. Modo de Disparo


    Observa los pines con el jumper en la esquina.
    Esto permite al PIR funcionar en modo de disparo repetitivo o no repetitivo.

    Actualmente, el jumper conecta el pin central y el pin L, configurando el PIR en modo de disparo no repetitivo. En este modo, cuando el PIR detecta movimiento, enviará una señal de nivel alto de aproximadamente 2.8 segundos a la placa de control.
    .. En los datos impresos, la duración del disparo será siempre de alrededor de 2800 ms.

    Ahora, modifica el jumper conectándolo al pin central y el pin H para configurar el PIR en modo de disparo repetitivo. En este modo, cuando el PIR detecta movimiento (notar que es movimiento, no estático), siempre que haya movimiento en el rango de detección, el PIR continuará enviando señal de nivel alto.
    .. En los datos impresos, la duración del disparo será variable.

#. Ajuste de Retardo

    El potenciómetro a la izquierda ajusta el intervalo entre dos detecciones.

    Actualmente, está completamente en sentido contrario a las agujas del reloj, configurando un tiempo de reposo de aproximadamente 5 segundos tras enviar una señal de nivel alto. Durante este tiempo, el PIR no detectará radiación infrarroja.
    .. En los datos impresos, la duración del reposo es siempre de al menos 5000 ms.

    Si giramos el potenciómetro en sentido horario, el tiempo de reposo aumentará. Cuando está completamente en sentido horario, el tiempo de reposo llega a los 300 segundos.

#. Ajuste de Distancia

    El potenciómetro central ajusta el rango de detección del PIR.

    Gira el potenciómetro **en sentido horario** para aumentar el rango de detección, 
    con un máximo de aproximadamente 0-7 metros. Si lo giras **en sentido contrario a las agujas del reloj**, 
    el rango disminuye, siendo el mínimo de aproximadamente 0-3 metros.
