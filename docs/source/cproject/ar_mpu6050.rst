.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des concours et promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ar_mpu6050:

6.3 - Suivi de Mouvement 6 Axes
===================================

Le MPU-6050 est un dispositif de suivi de mouvement à 6 axes (combinant un gyroscope à 3 axes et un accéléromètre à 3 axes).


Un accéléromètre est un outil qui mesure l'accélération propre. Par exemple, un accéléromètre au repos à la surface de la Terre mesurera une accélération due à la gravité terrestre, orientée vers le haut, avec une valeur d'environ g ≈ 9,81 m/s².

Les accéléromètres ont de nombreuses applications dans l'industrie et la science, comme les systèmes de navigation inertielle pour avions et missiles, le maintien d'images verticales sur les tablettes et les appareils photo numériques, etc.

Les gyroscopes sont utilisés pour mesurer l'orientation et la vitesse angulaire d'un appareil. Les applications incluent les systèmes anti-renversement et 
airbags pour automobiles, les systèmes de détection de mouvement pour les appareils intelligents, les systèmes de stabilisation d'attitude pour les drones, et bien plus encore.

* :ref:`cpn_mpu6050`

**Composants requis**

Dans ce projet, nous avons besoin des composants suivants. 

Il est pratique d'acheter un kit complet, voici le lien : 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nom	
        - ARTICLES DANS CE KIT
        - LIEN D'ACHAT
    *   - Kit Kepler	
        - 450+
        - |link_kepler_kit|

Vous pouvez également les acheter séparément via les liens ci-dessous.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - N°
        - INTRODUCTION DES COMPOSANTS	
        - QUANTITÉ
        - LIEN D'ACHAT

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

|sch_mpu6050_ar|

**Câblage**

|wiring_mpu6050_ar|

**Code**

.. note::

    * Vous pouvez ouvrir le fichier ``6.3_6axis_motion_tracking.ino`` sous le chemin ``kepler-kit-main/arduino/6.3_6axis_motion_tracking``. 
    * Ou copiez ce code dans l'**Arduino IDE**.
    * Ensuite, sélectionnez la carte Raspberry Pi Pico et le port correct avant de cliquer sur le bouton Upload.
    * La bibliothèque ``Adafruit MPU6050`` est utilisée ici, vous pouvez l'installer depuis le **Gestionnaire de Bibliothèques**.

      .. image:: img/lib_mpu6050.png

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/318f62d3-1d7b-4ee6-a1a2-97e783cf2d5e/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>
    

Après avoir lancé le programme, vous verrez les valeurs de l'accéléromètre à 3 axes et celles du gyroscope à 3 axes défiler dans la sortie. 
À ce moment-là, si vous faites tourner le MPU6050, ces valeurs changeront en conséquence. 
Pour rendre les changements plus visibles, vous pouvez commenter une des lignes d'impression et vous concentrer sur un autre jeu de données.


**Comment ça fonctionne ?**

Instanciez un objet ``MPU6050``.

.. code-block:: arduino

    #include <Adafruit_MPU6050.h>
    #include <Wire.h>

    Adafruit_MPU6050 mpu;

Initialisez le MPU6050 et définissez sa précision.

.. code-block:: arduino

    void setup(void) {
        Serial.begin(115200);
        while (!Serial)
            delay(10); // pause pour Zero, Leonardo, etc. jusqu'à l'ouverture de la console série

        Serial.println("Adafruit MPU6050 test!");

        // Tentez l'initialisation !
        if (!mpu.begin()) {
            Serial.println("Échec de détection de la puce MPU6050");
            while (1) {
            delay(10);
            }
        }
        Serial.println("MPU6050 Found!");

        // Définir la plage
        mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
        mpu.setGyroRange(MPU6050_RANGE_500_DEG);
        mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);

        Serial.println("");
        delay(100);
    }

Obtenez de nouveaux événements capteurs avec les lectures.

.. code-block:: arduino

    sensors_event_t a, g, temp;
    mpu.getEvent(&a, &g, &temp);

Ensuite, vous pourrez obtenir les valeurs d'accélération et de vitesse angulaire en temps réel avec les données ``a.acceleration.x``, ``a.acceleration.y``, ``a.acceleration.z``, ``g.gyro.x``, ``g.gyro.y``, ``g.gyro.z``.

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