.. note::

    Bonjour et bienvenue dans la communauté SunFounder pour les passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions et concours festifs** : Participez aux concours et aux promotions de fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_water:

2.14 Détecter le niveau d'eau
=====================================

|img_water_sensor|

Le capteur d'eau est conçu pour détecter la présence d'eau et peut être largement utilisé pour mesurer les précipitations, le niveau d'eau et même les fuites de liquide.

Il mesure le niveau d'eau en utilisant une série de traces parallèles exposées pour évaluer la taille des gouttes d'eau ou le volume. Le volume d'eau est facilement converti en un signal analogique, et la valeur analogique en sortie peut être lue directement par la carte de contrôle principale pour activer une alarme de niveau d'eau.

.. warning:: 
    
    Le capteur ne doit pas être complètement immergé dans l'eau, seule la partie où se trouvent les dix traces doit entrer en contact avec l'eau. De plus, alimenter le capteur dans un environnement humide accélérera la corrosion de la sonde et réduira sa durée de vie. Il est donc recommandé de ne le mettre sous tension que lors de la prise de mesures.

* :ref:`cpn_water_level`

**Composants requis**

Pour ce projet, nous aurons besoin des composants suivants.

Il est bien sûr plus pratique d'acheter un kit complet, voici le lien : 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nom	
        - ARTICLES DANS CE KIT
        - LIEN
    *   - Kit Kepler	
        - 450+
        - |link_kepler_kit|

Vous pouvez également les acheter séparément via les liens ci-dessous.


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - N°
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
        - :ref:`cpn_water_level`
        - 1
        - 


**Schéma**

|sch_water|


**Câblage**


|wiring_water|

**Code**

.. note::

    * Ouvrez le fichier ``2.14_feel_the_water_level.py`` situé sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite. 

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.


.. code-block:: python

    import machine
    import utime

    sensor = machine.ADC(28)

    while True:
        value=sensor.read_u16()
        print(value)
        utime.sleep_ms(200)


Après avoir lancé le programme, plongez lentement le module du capteur d'eau dans l'eau. À mesure que la profondeur augmente, la console affichera une valeur de plus en plus élevée.

**En savoir plus**

Il est possible d'utiliser le module d'entrée analogique comme un module numérique.

Commencez par prendre une lecture du capteur d'eau dans un environnement sec, enregistrez cette valeur et utilisez-la comme valeur seuil. Ensuite, terminez la programmation et reprenez les mesures du capteur d'eau. Lorsque la lecture du capteur d'eau s'écarte significativement de celle mesurée en environnement sec, cela indique la présence de liquide. En d'autres termes, en plaçant cet appareil près d'un tuyau, il peut détecter si le tuyau présente une fuite.


.. note::

    * Ouvrez le fichier ``2.14_water_level_threshold.py`` situé sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite. 

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    sensor = machine.ADC(28)
    threshold = 30000 # Cette valeur doit être ajustée en fonction de l'environnement.

    while True:
        value=sensor.read_u16()
        if value > threshold :
            print("Liquid leakage!")
        utime.sleep_ms(200)
