.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 sur Facebook ! Plongez plus profondément dans le Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos nouveaux produits.
    - **Promotions festives et cadeaux** : Participez à des concours et promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ar_water:

2.14 - Mesurer le Niveau d'Eau
=====================================

|img_water_sensor|

Le capteur d'eau est conçu pour détecter la présence d'eau, et il peut être largement utilisé pour mesurer la pluie, le niveau d'eau et même détecter des fuites de liquide.

Il mesure le niveau d'eau à l'aide d'une série de traces parallèles exposées qui captent la taille des gouttes d'eau ou le volume. Ce volume d'eau est facilement converti en un signal analogique, et la valeur analogique en sortie peut être lue directement par la carte de contrôle principale pour déclencher une alarme de niveau d'eau.

.. warning:: 
    
    Le capteur ne doit pas être entièrement immergé dans l'eau ; veuillez ne laisser que la partie où se trouvent les dix traces en contact avec l'eau. De plus, alimenter le capteur dans un environnement humide accélère la corrosion de la sonde et réduit la durée de vie du capteur. Il est donc recommandé de ne l'alimenter que lors des relevés.

* :ref:`cpn_water_level`

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
        - :ref:`cpn_water_level`
        - 1
        - 

**Schéma**

|sch_water|

**Câblage**

|wiring_water|

**Code**

.. note::

    * Vous pouvez ouvrir le fichier ``2.14_feel_the_water_level.ino`` dans le chemin ``kepler-kit-main/arduino/2.14_feel_the_water_level``. 
    * Ou copiez ce code dans **Arduino IDE**.
    * N'oubliez pas de sélectionner la carte (Raspberry Pi Pico) et le port correct avant de cliquer sur le bouton **Upload**.


.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/32ee87a1-08eb-482f-bf4c-b12b24ef05c4/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Une fois le programme lancé, plongez lentement le module capteur d'eau dans l'eau, et à mesure que la profondeur augmente, la console Shell affichera une valeur plus élevée.


**En savoir plus**

Il est possible d'utiliser le module d'entrée analogique comme un module numérique.

Tout d'abord, effectuez un relevé du capteur d'eau dans un environnement sec, enregistrez-le et utilisez-le comme valeur seuil. Ensuite, complétez le programme et relisez la valeur du capteur d'eau. Lorsque la lecture du capteur d'eau s'écarte significativement de celle en environnement sec, il détecte la présence de liquide. Autrement dit, en plaçant cet appareil près d'un tuyau d'eau, il peut détecter si un tuyau fuit.

.. note::

    * Vous pouvez ouvrir le fichier ``2.14_water_level_threshold.ino`` dans le chemin ``kepler-kit-main/arduino/2.14_water_level_threshold``. 
    * Ou copiez ce code dans **Arduino IDE**.
    * N'oubliez pas de sélectionner la carte (Raspberry Pi Pico) et le port correct avant de cliquer sur le bouton **Upload**.

.. :raw-code: