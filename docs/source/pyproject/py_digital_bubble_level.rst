.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions spéciales durant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_bubble_level:

7.12 Niveau à bulle numérique
=================================

Un `bubble Level <https://en.wikipedia.org/wiki/Spirit_level>`_ est un instrument conçu pour indiquer si une surface est horizontale (de niveau) ou verticale (d'aplomb). Différents types de niveaux à bulle sont utilisés par les menuisiers, les maçons, les poseurs de briques, les ouvriers du bâtiment, les géomètres, les mécaniciens, ainsi que dans certains travaux de photographie et de vidéographie.

Ici, nous réalisons un niveau à bulle numérique en utilisant un MPU6050 et une matrice LED 8x8. Lorsque vous inclinez le MPU6050, la bulle sur la matrice LED se déplace également.

**Composants Requis**

Pour ce projet, nous avons besoin des composants suivants : 

Il est plus pratique d'acheter un kit complet, voici le lien : 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nom	
        - ARTICLES DANS CE KIT
        - LIEN
    *   - Kepler Kit	
        - 450+
        - |link_kepler_kit|

Vous pouvez également les acheter séparément via les liens ci-dessous :

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - COMPOSANT	
        - QUANTITÉ
        - LIEN

    *   - 1
        - :ref:`cpn_pico_w`
        - 1
        - |link_picow_buy|
    *   - 2
        - Câble Micro USB
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Plusieurs
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_dot_matrix`
        - 1
        - 
    *   - 6
        - :ref:`cpn_74hc595`
        - 2
        - |link_74hc595_buy|
    *   - 7
        - :ref:`cpn_mpu6050`
        - 1
        - 

**Schéma**

|sch_bubble_level|

Le MPU6050 mesure les valeurs d'accélération dans chaque direction et calcule l'angle d'inclinaison.

En conséquence, le programme dessine un point 2x2 sur la matrice en utilisant les données des deux puces 74HC595.

Lorsque l'angle d'inclinaison change, le programme envoie différentes données aux puces 74HC595, et la position du point se déplace, créant un effet de bulle.

**Câblage**

|wiring_digital_bubble_level| 

**Code**

.. note::

    * Ouvrez le fichier ``7.12_digital_bubble_level.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Exécuter le script actuel" ou appuyez simplement sur F5 pour l'exécuter.
    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite.

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.
    * Vous devez utiliser les bibliothèques ``imu.py`` et ``vector3d.py`` ; vérifiez si elles ont été téléchargées sur le Pico W. Pour un tutoriel détaillé, référez-vous à :ref:`add_libraries_py`.

.. code-block:: python

    import machine
    from machine import I2C, Pin
    import time
    import math
    from imu import MPU6050

    # Initialiser la communication I2C avec le capteur MPU6050
    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
    mpu = MPU6050(i2c)

    # Fonction pour calculer la distance entre deux points
    def dist(a, b):
        return math.sqrt((a * a) + (b * b))

    # Fonction pour calculer la rotation le long de l'axe Y
    def get_y_rotation(x, y, z):
        radians = math.atan2(x, dist(y, z))
        return -math.degrees(radians)

    # Fonction pour calculer la rotation le long de l'axe X
    def get_x_rotation(x, y, z):
        radians = math.atan2(y, dist(x, z))
        return math.degrees(radians)

    # Fonction pour obtenir les angles actuels du capteur MPU6050
    def get_angle():
        y_angle = get_y_rotation(mpu.accel.x, mpu.accel.y, mpu.accel.z)
        x_angle = get_x_rotation(mpu.accel.x, mpu.accel.y, mpu.accel.z)
        return x_angle, y_angle

    # Initialiser les broches du registre à décalage pour contrôler la matrice LED
    sdi = machine.Pin(18, machine.Pin.OUT)
    rclk = machine.Pin(19, machine.Pin.OUT)
    srclk = machine.Pin(20, machine.Pin.OUT)

    # Fonction pour décaler les données dans le registre à décalage
    def hc595_in(dat):
        for bit in range(7, -1, -1):
            srclk.low()
            time.sleep_us(30)
            sdi.value(1 & (dat >> bit))
            time.sleep_us(30)
            srclk.high()

    # Fonction pour sortir les données du registre à décalage vers la matrice LED
    def hc595_out():
        rclk.high()
        time.sleep_us(200)
        rclk.low()

    # Fonction pour afficher un glyphe (matrice 8x8) sur la matrice LED
    def display(glyph):
        for i in range(0, 8):
            hc595_in(glyph[i])
            hc595_in(0x80 >> i)
            hc595_out()

    # Convertir une matrice 2D en glyphe pour l'afficher sur la matrice LED
    def matrix_2_glyph(matrix):
        glyph = [0 for i in range(8)]
        for i in range(8):
            for j in range(8):
                glyph[i] += matrix[i][j] << j
        return glyph

    # Limiter une valeur entre un minimum et un maximum spécifiés
    def clamp_number(val, min_val, max_val):
        return min_val if val < min_val else max_val if val > max_val else val

    # Mapper une valeur d'une plage à une autre
    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    # Calculer la position de la bulle dans la matrice en fonction des lectures du MPU6050
    sensitivity = 4  # Sensibilité du mouvement de la bulle
    matrix_range = 7  # La taille de la matrice est de 8x8, donc l'intervalle est 0-7
    point_range = matrix_range - 1  # La position de la bulle doit être entre 0 et 6

    # Fonction pour calculer la position de la bulle basée sur les données du capteur
    def bubble_position():
        y, x = get_angle()  # Obtenez les angles de rotation actuels
        x = int(clamp_number(interval_mapping(x, 90, -90, 0 - sensitivity, point_range + sensitivity), 0, point_range))
        y = int(clamp_number(interval_mapping(y, -90, 90, point_range + sensitivity, 0 - sensitivity), 0, point_range))
        return [x, y]

    # Placer la bulle (représentée par l'extinction de 2x2 LEDs) dans la matrice
    def drop_bubble(matrix, bubble):
        matrix[bubble[0]][bubble[1]] = 0
        matrix[bubble[0] + 1][bubble[1]] = 0
        matrix[bubble[0]][bubble[1] + 1] = 0
        matrix[bubble[0] + 1][bubble[1] + 1] = 0
        return matrix

    # Boucle principale
    while True:
        matrix = [[1 for i in range(8)] for j in range(8)]  # Créez une matrice vide (toutes les LEDs allumées)
        bubble = bubble_position()  # Obtenez la position actuelle de la bulle selon les données du capteur
        matrix = drop_bubble(matrix, bubble)  # Placez la bulle dans la matrice
        display(matrix_2_glyph(matrix))  # Affichez la matrice sur la grille LED
        time.sleep(0.1)  # Ajoutez un court délai pour ralentir les mises à jour

Une fois le programme exécuté, placez la breadboard sur une surface plane. Un point apparaîtra au centre de la matrice LED (si ce n'est pas au centre, le MPU6050 pourrait ne pas être à niveau). Lorsque vous inclinez la breadboard, le point se déplacera dans la direction de l'inclinaison.
