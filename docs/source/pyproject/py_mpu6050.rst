.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Explorez plus en profondeur Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Assistance d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et promotions durant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_mpu6050:

6.3 Suivi de Mouvement 6 Axes
=====================================

Le MPU-6050 est un dispositif de suivi de mouvement à 6 axes (qui combine un gyroscope 3 axes et un accéléromètre 3 axes).

Un accéléromètre est un outil qui mesure l'accélération propre. Par exemple, un accéléromètre au repos sur la surface de la Terre mesurera une accélération due à la gravité terrestre, orientée vers le haut, avec une valeur approximative de g ≈ 9,81 m/s².

Les accéléromètres ont de nombreuses applications dans l'industrie et la science, par exemple : systèmes de navigation inertielle pour les avions et les missiles, maintien des images verticales sur les tablettes et appareils photo numériques, etc.

Les gyroscopes sont utilisés pour mesurer l'orientation et la vitesse angulaire d'un dispositif. Ils sont intégrés dans des systèmes tels que les systèmes anti-retournement et les airbags pour les automobiles, les systèmes de détection de mouvement pour les appareils intelligents, les systèmes de stabilisation d'attitude pour les drones, et bien plus encore.

* :ref:`cpn_mpu6050`

**Composants requis**

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

**Schéma**

|sch_mpu6050|

**Câblage**

|wiring_mpu6050|

**Code**

.. note::

    * Ouvrez le fichier ``6.3_6axis_motion_tracking.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite. 

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.
    
    * Vous devez utiliser les bibliothèques ``imu.py`` et ``vector3d.py``, veuillez vérifier si elles ont été téléchargées sur Pico W. Pour un tutoriel détaillé, consultez :ref:`add_libraries_py`.

.. code-block:: python

    from imu import MPU6050
    from machine import I2C, Pin
    import time

    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
    mpu = MPU6050(i2c)

    while True:
        print("x: %s, y: %s, z: %s"%(mpu.accel.x, mpu.accel.y, mpu.accel.z))
        time.sleep(0.5)
        print("A: %s, B: %s, Y: %s"%(mpu.gyro.x, mpu.gyro.y, mpu.gyro.z))
        time.sleep(0.5)

Une fois le programme lancé, vous pourrez voir les valeurs de l'accéléromètre 
3 axes et du gyroscope 3 axes défiler à l'écran. À ce moment-là, faites pivoter 
le MPU6050 de manière aléatoire, et vous verrez ces valeurs changer en conséquence. 
Pour faciliter la visualisation des changements, vous pouvez commenter l'une des 
lignes de print et vous concentrer sur l'autre ensemble de données.

L'unité de mesure de l'accélération est le m/s², et celle de la vitesse angulaire est le °/s.

**Comment ça marche ?**

Dans la bibliothèque imu, nous avons intégré les fonctions pertinentes dans la classe ``MPU6050``.
Le MPU6050 est un module I2C et nécessite un ensemble de broches I2C pour être initialisé.

.. code-block:: python

    from imu import MPU6050
    from machine import I2C, Pin

    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
    mpu = MPU6050(i2c)

Ensuite, vous pourrez obtenir les valeurs en temps réel de l'accélération et de la vitesse angulaire avec ``mpu.accel.x``, ``mpu.accel.y``, ``mpu.accel.z``, ``mpu.gyro.x``, ``mpu.gyro.y``, ``mpu.gyro.z``.

.. code-block:: python

    while True:
        print("x: %s, y: %s, z: %s"%(mpu.accel.x, mpu.accel.y, mpu.accel.z))
        time.sleep(0.5)
        print("A: %s, B: %s, Y: %s"%(mpu.gyro.x, mpu.gyro.y, mpu.gyro.z))
        time.sleep(0.5)