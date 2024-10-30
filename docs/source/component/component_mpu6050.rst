.. note::

    ¡Hola! ¡Bienvenidos a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previews Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_mpu6050:

Módulo MPU6050
===========================

**MPU6050**

|img_mpu6050|

El MPU-6050 es un dispositivo de seguimiento de movimiento de 6 ejes 
(combina un giroscopio de 3 ejes y un acelerómetro de 3 ejes).

Sus tres sistemas de coordenadas se definen de la siguiente manera:

Coloca el MPU6050 plano sobre la mesa, asegurándote de que la cara con la 
etiqueta quede hacia arriba y un punto en esta superficie esté en la esquina 
superior izquierda. Entonces, la dirección vertical hacia arriba es el eje Z 
del chip. La dirección de izquierda a derecha se considera el eje X. En 
consecuencia, la dirección de atrás hacia adelante se define como el eje Y.

|img_mpu6050_a|

**Acelerómetro de 3 ejes**

El acelerómetro funciona bajo el principio del efecto piezoeléctrico, la 
capacidad de ciertos materiales para generar una carga eléctrica en respuesta 
a un esfuerzo mecánico aplicado.

Aquí, imagina una caja en forma de cuboide que tiene una pequeña bola dentro, 
como en la imagen de arriba. Las paredes de esta caja están hechas con cristales 
piezoeléctricos. Siempre que inclines la caja, la bola se ve obligada a moverse 
en la dirección de la inclinación debido a la gravedad. La pared con la que 
choca la bola genera pequeñas corrientes piezoeléctricas. Hay en total tres 
pares de paredes opuestas en el cuboide. Cada par corresponde a un eje en el 
espacio 3D: ejes X, Y y Z. Dependiendo de la corriente producida por las 
paredes piezoeléctricas, se puede determinar la dirección de la inclinación y 
su magnitud.

|img_mpu6050_a2|

Podemos usar el MPU6050 para detectar su aceleración en cada eje de coordenadas 
(en estado estacionario en un escritorio, la aceleración en el eje Z es 1 unidad 
de gravedad, y en los ejes X e Y es 0). Si se inclina o se encuentra en una 
condición de ingravidez/sobrecarga, la lectura correspondiente cambiará.

Hay cuatro rangos de medición que se pueden seleccionar programáticamente: 
+/-2g, +/-4g, +/-8g y +/-16g (por defecto es 2g), correspondientes a diferentes 
niveles de precisión. Los valores oscilan entre -32768 y 32767.

La lectura del acelerómetro se convierte en un valor de aceleración mapeando 
la lectura del rango de medición:

Aceleración = (Datos en bruto del eje del acelerómetro / 65536 \* rango completo 
de aceleración) g

Tomando el eje X como ejemplo, cuando los datos en bruto del eje X del 
acelerómetro son 16384 y el rango seleccionado es +/-2g:

**Aceleración a lo largo del eje X = (16384 / 65536 \* 4) g** **=1g**

**Giroscopio de 3 ejes**

Los giroscopios funcionan bajo el principio de la aceleración de Coriolis. 
Imagina una estructura en forma de horquilla que se mueve constantemente 
hacia adelante y hacia atrás. Está sostenida en su lugar por cristales 
piezoeléctricos. Siempre que intentes inclinar este arreglo, los cristales 
experimentan una fuerza en la dirección de la inclinación. Esto se debe a 
la inercia de la horquilla en movimiento. Los cristales generan una corriente 
en consenso con el efecto piezoeléctrico, y esta corriente se amplifica.

|img_mpu6050_g|

El giroscopio también tiene cuatro rangos de medición: +/- 250, +/- 500, 
+/- 1000, +/- 2000. El método de cálculo es básicamente consistente con 
el de la aceleración.

La fórmula para convertir la lectura en velocidad angular es la siguiente:

Velocidad angular = (Datos en bruto del eje del giroscopio / 65536 \* rango 
completo del giroscopio) °/s

Por ejemplo, en el eje X, si los datos en bruto del eje X del acelerómetro 
son 16384 y el rango es +/- 250°/ s:

**Velocidad angular a lo largo del eje X = (16384 / 65536 \* 500)°/s** **=125°/s**

**Ejemplos**

* :ref:`py_mpu6050` (Para usuarios de MicroPython)
* :ref:`py_somato_controller` (Para usuarios de MicroPython)
* :ref:`py_bubble_level` (Para usuarios de MicroPython)
* :ref:`ar_mpu6050` (Para usuarios de Arduino)
