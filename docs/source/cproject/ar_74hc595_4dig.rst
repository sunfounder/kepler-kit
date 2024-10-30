.. note::

    ¡Hola! Bienvenidos a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. ¡Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados!

    **¿Por qué unirse?**

    - **Soporte de Expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Accede anticipadamente a anuncios de nuevos productos y adelantos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _ar_74hc_4dig:

5.3 - Contador de Tiempo
================================

La pantalla de 7 segmentos de 4 dígitos está compuesta por cuatro pantallas de 
7 segmentos que funcionan en conjunto.

La pantalla de 7 segmentos de 4 dígitos trabaja de forma independiente. Utiliza 
el principio de persistencia visual humana para mostrar rápidamente los 
caracteres 
de cada segmento en un bucle, formando cadenas continuas.

Por ejemplo, cuando en la pantalla se muestra "1234", primero se muestra el "1" 
en el primer segmento, y los otros dígitos no aparecen. Después de un breve 
intervalo, el segundo segmento muestra "2", mientras que el primer, tercer y 
cuarto segmento no se iluminan, y así sucesivamente, los cuatro dígitos se 
muestran en secuencia. Este proceso es muy rápido (generalmente 5 ms), y debido 
al efecto de postimagen óptica y al principio de persistencia visual, podemos 
ver los cuatro caracteres simultáneamente.

**Componentes Necesarios**

En este proyecto, necesitamos los siguientes componentes.

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
        - 4 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_4_dit_7_segment`
        - 1
        - 
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|

**Esquema**

|sch_4dig|

Aquí el principio de cableado es básicamente el mismo que en :ref:`ar_74hc_led`, la única diferencia es que Q0-Q7 están conectados a los pines a ~ g de la pantalla de 7 segmentos de 4 dígitos.

Luego, G10 ~ G13 seleccionarán qué pantalla de 7 segmentos estará activa.

**Conexión**

|wiring_4dig|

**Código**

.. note::

    * Puedes abrir el archivo ``5.3_time_counter.ino`` en la ruta ``kepler-kit-main/arduino/5.3_time_counter``. 
    * O copia este código en el **IDE de Arduino**.
    * No olvides seleccionar la placa (Raspberry Pi Pico) y el puerto correcto antes de hacer clic en el botón **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/0e97386e-417e-4f53-a026-5f37e36deba4/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Una vez que el programa se ejecute, verás que la pantalla de 7 segmentos de 4 dígitos actúa como un contador, incrementando el número en 1 cada segundo.

**¿Cómo funciona?**

La escritura de señales en cada pantalla de 7 segmentos se realiza de la misma manera que en :ref:`ar_74hc_7seg`, utilizando la función ``hc595_shift()``.
El punto clave de la pantalla de 7 segmentos de 4 dígitos es activar selectivamente cada segmento. El código relacionado con esto es el siguiente:

.. code-block:: arduino

    const int placePin[4] = {13,12,11,10}; 

    void setup ()
    {
        for (int i = 0; i<4;i++){
            pinMode(placePin[i],OUTPUT);
        }
    }

    void loop()
    { 
        pickDigit(0);
        hc595_shift(count%10/1);
        
        pickDigit(1);
        hc595_shift(count%100/10);
        
        pickDigit(2);
        hc595_shift(count%1000/100);
        
        pickDigit(3);
        hc595_shift(count%10000/1000);
    }

    void pickDigit(int digit){
        for(int i = 0; i < 4; i++){
            digitalWrite(placePin[i],HIGH);
        }
        digitalWrite(placePin[digit],LOW);
    }

Aquí, cuatro pines (GP10, GP11, GP12, GP13) se utilizan para controlar cada dígito de la pantalla de 7 segmentos de forma individual.
Cuando el estado de estos pines es ``LOW``, el correspondiente display de 7 segmentos está activo; cuando el estado es ``HIGH``, el display no se activa.


Aquí, la función ``pickDigit(digit)`` desactiva todas las pantallas de 7 segmentos y luego habilita un dígito particular.
Después de eso, ``hc595_shift()`` se utiliza para escribir el código de 8 bits correspondiente para el display de 7 segmentos.

La pantalla de 7 segmentos de 4 dígitos necesita ser activada continuamente en turno para que podamos ver que muestra los cuatro dígitos, lo que significa que el programa principal no puede añadir fácilmente código que afecte el tiempo.

Sin embargo, necesitamos añadir una función de temporización en este ejemplo; si añadimos un ``delay (1000)``, podremos detectar la ilusión de que las cuatro pantallas de 7 segmentos están trabajando simultáneamente, exponiendo que solo una está iluminada a la vez.

Entonces, utilizar la función ``millis()`` es una excelente manera de lograr esto.

.. code-block:: arduino

    void setup ()
    {
        timerStart = millis();
    }

    void loop()
    {
        unsigned int count = (millis()-timerStart)/1000;
    }

La función ``millis()`` obtiene el número de milisegundos transcurridos desde el inicio del programa actual. Registramos el primer valor de tiempo como ``timerStart``; 

luego, cuando necesitamos obtener el tiempo nuevamente, llamamos a la función ``millis()`` y restamos ``timerStart`` del valor obtenido para saber cuánto tiempo ha estado ejecutándose el programa.

Finalmente, convertimos este valor de tiempo y dejamos que la pantalla de 7 segmentos de 4 dígitos lo muestre.

* `millis() <https://www.arduino.cc/reference/en/language/functions/time/millis/>`_