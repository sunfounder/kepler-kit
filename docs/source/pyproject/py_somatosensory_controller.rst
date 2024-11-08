.. note::

    Bonjour, bienvenue dans la communauté SunFounder des passionnés de Raspberry Pi, Arduino & ESP32 sur Facebook ! Approfondissez vos connaissances en matière de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions festives.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_somato_controller:


7.11 Contrôleur Somatosensoriel
==================================

Si vous regardez beaucoup de films de robots, vous avez probablement vu ce genre de scènes.
Le protagoniste tourne son poignet et le robot géant suit ; le protagoniste serre son poing, et le robot imite, ce qui est très impressionnant.

L'utilisation de cette technologie est déjà courante dans les universités et les instituts de recherche, et l'arrivée de la 5G va considérablement étendre ses domaines d'application. 
La chirurgie à distance avec le robot chirurgical "da Vinci" en est un exemple typique.

Un système robotique de ce type est généralement composé de deux modules : un module de capture des mouvements humains et un module d'actionnement de bras robotique (certains scénarios incluent également un module de communication de données).

Le MPU6050 est utilisé ici pour implémenter la capture des mouvements humains (en le fixant sur un gant) et le servo est utilisé pour représenter le mouvement du bras robotique.

**Composants Requis**

Dans ce projet, nous aurons besoin des composants suivants.

Il est plus pratique d'acheter un kit complet, voici le lien :

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nom
        - ÉLÉMENTS DANS CE KIT
        - LIEN
    *   - Kit Kepler
        - 450+
        - |link_kepler_kit|

Vous pouvez également les acheter séparément via les liens ci-dessous.

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
        - :ref:`cpn_mpu6050`
        - 1
        - 
    *   - 6
        - :ref:`cpn_servo`
        - 1
        - |link_servo_buy|

**Schéma**

|sch_somato|

Le MPU6050 calcule l'angle d'attitude en fonction des valeurs d'accélération dans chaque direction.

Le programme contrôlera le servo pour effectuer l'angle de déviation correspondant au changement de l'angle d'attitude.

**Câblage**

|wiring_somatosensory_controller| 

**Code**

.. note::

    * Ouvrez le fichier ``7.11_somatosensory_controller.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.
    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite.

    * Pour des tutoriels détaillés, veuillez consulter :ref:`open_run_code_py`.
    * Vous devez utiliser les fichiers ``imu.py`` et ``vector3d.py``, assurez-vous qu'ils sont bien téléchargés sur le Pico W, pour un tutoriel détaillé, consultez :ref:`add_libraries_py`.

.. code-block:: python

    from imu import MPU6050
    from machine import I2C, Pin
    import time
    import math

    # Initialiser la communication I2C pour l'accéléromètre MPU6050
    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
    mpu = MPU6050(i2c)

    # Initialiser le PWM pour le servo sur la broche 15 avec une fréquence de 50Hz
    servo = machine.PWM(machine.Pin(15))
    servo.freq(50)

    # Fonction pour mapper une valeur d'une plage à une autre
    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    # Fonction pour calculer la distance euclidienne entre deux points
    def dist(a, b):
        return math.sqrt((a * a) + (b * b))

    # Fonction pour calculer la rotation autour de l'axe y
    def get_y_rotation(x, y, z):
        radians = math.atan2(x, dist(y, z))
        return -math.degrees(radians)

    # Fonction pour calculer la rotation autour de l'axe x
    def get_x_rotation(x, y, z):
        radians = math.atan2(y, dist(x, z))
        return math.degrees(radians)

    # Fonction pour contrôler le servo en fonction de l'angle
    # Mappe l'angle (0-180) au cycle de travail PWM pour le contrôle du servo
    def servo_write(pin, angle):
        pulse_width = interval_mapping(angle, 0, 180, 0.5, 2.5)  # Mapper l'angle à une largeur d'impulsion en ms (0,5 ms à 2,5 ms)
        duty = int(interval_mapping(pulse_width, 0, 20, 0, 65535))  # Convertir la largeur d'impulsion en cycle de travail PWM (0-65535)
        pin.duty_u16(duty)  # Régler le cycle de travail pour le PWM du servo

    # Définir le nombre de lectures à moyenner pour un mouvement plus fluide
    times = 25

    # Boucle principale
    while True:
        total = 0
        # Prendre plusieurs lectures pour moyenner l'angle pour plus de fluidité
        for i in range(times):
            angle = get_y_rotation(mpu.accel.x, mpu.accel.y, mpu.accel.z)  # Obtenir la valeur de rotation de l'axe y à partir de l'accéléromètre
            total += angle  # Accumuler les lectures

        average_angle = int(total / times)  # Calculer l'angle moyen
        # Mapper l'angle moyen (-90 à 90) à la plage de mouvement du servo (0 à 180 degrés)
        servo_write(servo, interval_mapping(average_angle, -90, 90, 0, 180))

        time.sleep(0.1)  # Ajouter un petit délai pour réduire les vibrations dans le mouvement du servo

Dès que le programme est exécuté, le servo pivotera à gauche et à droite lorsque vous inclinerez le MPU6050 (ou tournerez votre poignet s'il est fixé sur un gant).
