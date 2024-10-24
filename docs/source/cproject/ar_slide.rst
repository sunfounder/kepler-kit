.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 sur Facebook ! Explorez en profondeur Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des concours et promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ar_slide:

2.7 - Basculez à Gauche et à Droite
========================================

|img_slide|

Le commutateur à glissière est un dispositif à 3 broches, avec la broche 2 (centrale) comme broche commune. Lorsque l'interrupteur est basculé vers la gauche, les deux broches de gauche sont connectées ensemble, et lorsqu'il est basculé vers la droite, les deux broches de droite sont connectées ensemble.

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
        - :ref:`cpn_resistor`
        - 1 (10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_capacitor`
        - 1 (104)
        - |link_capacitor_buy|
    *   - 7
        - :ref:`cpn_slide_switch`
        - 1
        - 

**Schéma**

|sch_slide|

GP14 recevra un niveau différent lorsque vous basculez le commutateur à glissière vers la droite ou la gauche.

Le but de la résistance de 10K est de maintenir GP14 à un niveau bas pendant le basculement (ni complètement à gauche ni complètement à droite).

Le condensateur céramique 104 est utilisé ici pour éliminer les parasites.

* :ref:`cpn_slide_switch`
* :ref:`cpn_capacitor`

**Câblage**

|wiring_slide|

**Code**

.. note::

    * Vous pouvez ouvrir le fichier ``2.7_toggle_left_right.ino`` dans le chemin ``kepler-kit-main/arduino/2.7_toggle_left_right``.
    * Ou copiez ce code dans **Arduino IDE**.
    * N'oubliez pas de sélectionner la carte (Raspberry Pi Pico) et le port correct avant de cliquer sur le bouton **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/a20c0733-f234-4d4b-862d-db87f2c249e9/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


Lorsque le programme est en cours d'exécution, le moniteur série affichera "ON" ou "OFF" lorsque vous basculez l'interrupteur vers la gauche ou la droite.
