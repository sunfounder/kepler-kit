.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des concours et promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ar_pir:

2.10 - Détecter les mouvements humains
=========================================

Le capteur infrarouge passif (PIR) est un capteur courant qui peut mesurer la lumière infrarouge (IR) émise par les objets dans son champ de vision. 
En termes simples, il capte le rayonnement infrarouge émis par le corps, permettant ainsi de détecter les mouvements des personnes et des autres animaux. 
Plus spécifiquement, il indique à la carte de contrôle principale que quelqu'un est entré dans votre pièce.

:ref:`cpn_pir`

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
        - :ref:`cpn_pir`
        - 1
        - |link_pir_buy|

**Schéma**

|sch_pir|

Lorsque le module PIR détecte quelqu'un passant à proximité, GP14 sera à un niveau haut, sinon il sera à un niveau bas.

**Câblage**

|wiring_pir|

**Code**

.. note::

    * Vous pouvez ouvrir le fichier ``2.10_detect_human_movement.ino`` sous le chemin ``kepler-kit-main/arduino/2.10_detect_human_movement``. 
    * Ou copiez ce code dans l'**Arduino IDE**.
    * N'oubliez pas de sélectionner la carte (Raspberry Pi Pico) et le port correct avant de cliquer sur le bouton Upload.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/bb3ff9f1-127d-4279-84b9-cba28b9667e8/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Après l'exécution du programme, si le module PIR détecte quelqu'un à proximité, le moniteur série affichera "Somebody here!" 

**En savoir plus**

Le capteur PIR est très sensible. Pour l'adapter à son environnement d'utilisation, il doit être ajusté. 
Avec le côté contenant les 2 potentiomètres face à vous, tournez les deux potentiomètres dans le sens 
antihoraire jusqu'à la butée et placez le cavalier sur la broche L et la broche centrale.

|img_pir_back|

1. Mode de déclenchement

    Regardons les broches avec le cavalier dans le coin.
    Elles permettent au PIR d'entrer en mode de déclenchement répétitif ou en mode de déclenchement non répétitif.

    Actuellement, notre cavalier relie la broche centrale et la broche L, ce qui place le PIR en mode de déclenchement non répétitif. 
    Dans ce mode, lorsque le PIR détecte le mouvement d'un organisme, il enverra un signal de niveau haut pendant environ 2,8 secondes à la carte de contrôle principale. 
    .. On peut voir dans les données imprimées que la durée de fonctionnement sera toujours d'environ 2800 ms.

    Ensuite, modifions la position du cavalier inférieur et connectons-le à la broche centrale et à la broche H pour placer le PIR en mode de déclenchement répétitif. 
    Dans ce mode, lorsque le PIR détecte le mouvement d'un organisme (notez qu'il s'agit de mouvement et non d'immobilité devant le capteur), tant que l'organisme continue de bouger dans la zone de détection, le PIR continuera d'envoyer un signal de niveau haut à la carte de contrôle principale.
    .. On peut voir dans les données imprimées que la durée de fonctionnement est une valeur indéterminée.

#. Réglage du délai

    Le potentiomètre de gauche est utilisé pour ajuster l'intervalle entre deux déclenchements.
    
    Actuellement, nous le tournons complètement dans le sens antihoraire, ce qui oblige le PIR à entrer dans un temps de veille d'environ 5 secondes après l'envoi du signal de niveau haut. Pendant cette période, le PIR ne détectera plus les rayons infrarouges dans la zone cible.
    .. On peut voir dans les données imprimées que la durée de sommeil est toujours d'au moins 5000 ms.

    Si nous tournons le potentiomètre dans le sens horaire, le temps de veille augmentera également. Lorsqu'il est tourné à fond dans le sens horaire, le temps de veille peut atteindre 300 secondes.

#. Réglage de la distance

    Le potentiomètre central est utilisé pour ajuster la portée de détection du PIR.

    Tournez le bouton de réglage de la distance **dans le sens horaire** pour augmenter la portée de détection, la portée maximale étant d'environ 0-7 mètres. 
    Si vous tournez **dans le sens antihoraire**, la portée de détection diminue, et la portée minimale est d'environ 0-3 mètres.
