.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el fascinante mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas posventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales en días festivos.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _quick_guide_piper:

1.2 Guía Rápida en Piper Make
=================================

1. Crear un Nuevo Proyecto
------------------------------

Una vez que hayas configurado el Pico W, es hora de aprender a programarlo. 
Vamos a encender el LED incorporado.

Cambia a ``CREATIVE MODE`` y haz clic en el botón **New Project**. Un nuevo 
proyecto aparecerá en la sección **MY PROJECTS** con un nombre aleatorio que 
puedes cambiar desde la página de programación.

|media9-s|

Luego abre el nuevo proyecto que acabas de crear.

|media11-s|

Ahora accede a la página de programación de Piper Make.

|piper_intro1|

* **START**: Se usa para ejecutar el código. Si está en gris, significa que el Pico W no está conectado en este momento.
* **Paleta de Bloques**: Contiene diferentes tipos de bloques.
* **CONNECT**: Se usa para conectar el Pico W; cuando no está conectado aparece en verde, y al conectarse cambia a **DISCONNECT (rojo)**.
* **Área de Programación**: Arrastra los bloques aquí y complétalo apilándolos.
* **Área de Herramientas**: Puedes hacer clic en **DIGITAL VIEW** para ver la distribución de pines del Pico W; visualizar información en **CONSOLE**; leer datos en **DATA** y hacer clic en **Python** para ver el código fuente en Python.
* **Nombre y Descripción del Proyecto**: Puedes cambiar el nombre y la descripción del proyecto.
* **DOWNLOAD**: Puedes hacer clic en el botón **DOWNLOAD** para guardarlo localmente. La próxima vez podrás importarlo usando el botón **Import Project** en la página principal.

Haz clic en la paleta **Chip** y arrastra el bloque [start] al **Área de Programación**.

|media12|

Luego, arrastra el bloque [loop] desde la paleta **loops** debajo del bloque [start] y establece el intervalo de repetición en 1 segundo.

|media14|

El LED incorporado de la Raspberry Pi Pico está en el pin25, por lo que usaremos el bloque [turn pin () ON/OFF] en la paleta **Chip** para controlarlo.

|media15|

.. _connect_pico_per:

2. Conectar el Pico W
--------------------------

Haz clic en el botón **CONNECT** para conectar el Pico W; al hacerlo, aparecerá una nueva ventana emergente.

|media16|

Selecciona el puerto **CircuitPython CDC control (COMXX)** reconocido y luego haz clic en **Connect**.

|pico_port|

Cuando la conexión sea exitosa, el **CONNECT** verde en la esquina inferior izquierda cambiará a **DISCONNECT** en rojo.

|disconnect_per|

3. Ejecutar el Código
-------------------------

Haz clic en el botón **START** para ejecutar el código y verás el LED del Pico W encenderse. Si el botón está en gris, significa que el Pico W no está conectado; por favor, vuelve a conectarlo.

|media166|

Luego, apaga el pin25 cada segundo en el ciclo y haz clic nuevamente en **START** en la esquina superior izquierda, así podrás ver el LED parpadeando.

|media17|
