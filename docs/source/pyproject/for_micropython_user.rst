.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans le monde des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes post-achat et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions spéciales durant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _projects_micropython:

Projets MicroPython
======================
Dans cette section, vous découvrirez les bases de MicroPython, de son histoire à son installation sur le Pico W. Vous plongerez également dans la syntaxe de base et travaillerez sur de nombreux projets pratiques conçus pour vous aider à maîtriser MicroPython pas à pas.  

Nous vous recommandons de lire les chapitres dans l'ordre pour maximiser votre apprentissage.  

**Code Source**

* :download:`SunFounder Kepler Kit <https://github.com/sunfounder/kepler-kit/archive/refs/heads/main.zip>`

* Ou consultez le code sur `Kepler Kit - GitHub <https://github.com/sunfounder/kepler-kit>`_

1. Démarrage
------------------------
Apprenez les bases de MicroPython et configurez votre environnement de développement, y compris l'installation de Thonny, le chargement de MicroPython sur le Pico W et l'exploration de sa syntaxe de base.  

.. toctree::
    :maxdepth: 1

    python_start/introduction_micropython
    python_start/install_thonny
    python_start/install_micropython_to_pico
    python_start/upload_libraries
    python_start/quick_guide_thonny
    python_start/syntax/micropython_basic_syntax

2. Sortie & Entrée
----------------------
Découvrez comment travailler avec des dispositifs de sortie comme des LEDs et des dispositifs d'entrée tels que des boutons et des capteurs. Ce chapitre introduit les bases de l'informatique physique à travers des projets pratiques et concrets.  

.. toctree::
    :maxdepth: 1

    py_led
    py_led_bar
    py_fade
    py_rgb
    py_button
    py_tilt
    py_slide
    py_micro
    py_reed
    py_pir
    py_pot
    py_photoresistor
    py_temp
    py_water
    py_transistor
    py_relay

3. Son, Affichage & Mouvement
--------------------------------------
Maîtrisez des modules comme les buzzers, les LEDs NeoPixel, les écrans LCD, ainsi que des actionneurs comme les moteurs, les pompes et les servos. Créez des projets interactifs produisant du son, des visuels et du mouvement.  

.. toctree::
    :maxdepth: 1

    py_ac_buz
    py_pa_buz
    py_neopixel
    py_lcd
    py_motor
    py_pump
    py_servo

4. Contrôleur
----------------------
Apprenez à utiliser des contrôleurs comme des joysticks, des claviers numériques et des capteurs tactiles pour ajouter de l'interactivité et de la complexité à vos projets.  

.. toctree::
    :maxdepth: 1

    py_joystick
    py_keypad
    py_mpr121

5. Microchip
--------------
Plongez dans des projets basés sur des microcircuits utilisant les registres à décalage 74HC595. Contrôlez des LEDs, des afficheurs 7 segments, des matrices à points, et plus encore avec des techniques avancées.  

.. toctree::
    :maxdepth: 1

    py_74hc595_led
    py_74hc595_7seg
    py_74hc595_4dig
    py_74hc595_matrix

6. Avancé
--------------------
Faites passer vos projets au niveau supérieur avec des composants avancés comme des capteurs ultrasoniques, des modules de température et d'humidité DHT11, des gyroscopes MPU6050 et des lecteurs RFID.  

.. toctree::
    :maxdepth: 1

    py_ultrasonic
    py_dht11
    py_mpu6050
    py_irremote
    py_rfid

7. Projets Amusants
----------------------
Mettez vos compétences en pratique en réalisant des applications passionnantes et concrètes comme des thérémines lumineux, des compteurs de passagers, des lecteurs de musique RFID et des contrôleurs somatosensoriels. Ces projets sont à la fois amusants et éducatifs.  

.. toctree::
    :maxdepth: 1

    py_light_theremin
    py_room_temp_meter
    py_alarm_siren_lamp
    py_passenger_counter
    py_game_10_second
    py_traffic_light
    py_game_guess_number
    py_rfid_music_player
    py_fruit_piano
    py_reversing_aid
    py_somatosensory_controller
    py_digital_bubble_level

8. Projets IoT
------------------------
Connectez votre Pico W à Internet et explorez le monde de l'IoT (Internet des Objets). Réalisez des projets tels que CheerLights, des stations météo, des systèmes de communication basés sur MQTT, et même un système de surveillance des plantes.  

.. toctree::
    :maxdepth: 1

    iotproject/1.access
    iotproject/2.cheerlight
    iotproject/3.ifttt_mail
    iotproject/4.openweather
    iotproject/5.mqtt_pub
    iotproject/6.mqtt_sub
    iotproject/7.web_page
    iotproject/8.anvil
    iotproject/9.sunfounder_controller
    iotproject/10.plant_monitor
