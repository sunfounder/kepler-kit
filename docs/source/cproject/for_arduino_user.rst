.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 sur Facebook ! Plongez plus profondément dans le Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos nouveaux produits.
    - **Promotions festives et cadeaux** : Participez à des concours et promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _projects_arduino:

Projets Arduino
======================
Cette section présente la programmation Arduino avec le Pico W, vous guidant à travers le processus d'installation de l'IDE Arduino, de l'ajout des bibliothèques nécessaires et de la réalisation de projets passionnants. Avec des explications détaillées et des exercices pratiques, vous maîtriserez aussi bien les bases que les concepts avancés de la programmation matérielle basée sur Arduino.

**Code Source**

* :download:`SunFounder Kepler Kit <https://github.com/sunfounder/kepler-kit/archive/refs/heads/main.zip>`

* Ou consultez le code sur `Kepler Kit - GitHub <https://github.com/sunfounder/kepler-kit>`_

1. Démarrage
------------------------
Installez l'IDE Arduino et préparez-vous à programmer votre Pico W. Apprenez à installer l'IDE, configurer la carte Pico W, et ajouter les bibliothèques essentielles pour vos projets.

.. toctree::
    :maxdepth: 1

    arduino_start/install_arduino_ide
    arduino_start/introduce_ide
    arduino_start/install_pico_w
    arduino_start/add_libraries_ar 

2. Sortie & Entrée
-----------------------
Travaillez avec des LEDs, des capteurs et des interrupteurs pour apprendre les bases du contrôle des dispositifs de sortie et de la collecte des entrées du monde physique. Ces exercices fondamentaux établiront une base solide en programmation Arduino.  

.. toctree::
    :maxdepth: 1

    ar_led
    ar_led_bar
    ar_fade
    ar_rgb
    ar_button
    ar_tilt
    ar_slide
    ar_micro
    ar_reed
    ar_pir
    ar_pot
    ar_photoresistor
    ar_temp
    ar_water
    ar_transistor
    ar_relay

3. Son, Affichage & Mouvement
-------------------------------------
Explorez comment créer des effets sonores, afficher des données et contrôler les mouvements. Ce chapitre comprend des projets avec des buzzers, LEDs NeoPixel, écrans LCD, moteurs, pompes et servos pour donner vie à votre matériel.  

.. toctree::
    :maxdepth: 1

    ar_ac_buz
    ar_pa_buz
    ar_neopixel
    ar_lcd
    ar_motor
    ar_pump
    ar_servo


4. Contrôleur
---------------------
Utilisez des contrôleurs tels que des joysticks, des claviers numériques et des capteurs tactiles pour ajouter des fonctionnalités interactives à vos projets. Apprenez à traiter les entrées de ces dispositifs et à les traduire en sorties créatives.  

.. toctree::
    :maxdepth: 1

    ar_joystick
    ar_keypad
    ar_mpr121

5. Microchip
---------------------
Découvrez la puissance des registres à décalage 74HC595 pour le contrôle avancé des LEDs, des afficheurs 7 segments et des modules matriciels. Ce chapitre couvre des techniques efficaces pour gérer de multiples sorties avec moins de broches.  

.. toctree::
    :maxdepth: 1

    ar_74hc595_led
    ar_74hc595_7seg
    ar_74hc595_4dig
    ar_74hc595_matrix

6. Avancé
----------------
Plongez dans des modules et concepts avancés, tels que la mesure de distance ultrasonique, la détection environnementale avec le DHT11, le suivi des mouvements avec le MPU6050, et la communication sans fil avec RFID et télécommandes infrarouges.  

.. toctree::
    :maxdepth: 1

    ar_ultrasonic
    ar_dht11
    ar_mpu6050
    ar_irremote
    ar_rfid
