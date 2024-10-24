.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 sur Facebook ! Plongez plus profondément dans Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des concours et promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ar_rgb:

2.4 - Lumière colorée
==============================================

Comme nous le savons, la lumière peut être superposée. Par exemple, mélanger de la lumière bleue et verte donne de la lumière cyan, et de la lumière rouge et verte donne de la lumière jaune. 
Cela s'appelle le "mélange additif des couleurs".

* `Additive color - Wikipedia <https://en.wikipedia.org/wiki/Additive_color>`_

Sur la base de cette méthode, nous pouvons utiliser les trois couleurs primaires pour mélanger la lumière visible de n'importe quelle couleur en ajustant leur intensité respective. Par exemple, l'orange peut être produit avec plus de rouge et moins de vert.

Dans ce chapitre, nous allons utiliser une LED RGB pour explorer le mystère du mélange additif des couleurs !

Une LED RGB équivaut à encapsuler une LED rouge, une LED verte et une LED bleue sous un même capuchon, et les trois LED partagent une cathode commune.
Comme le signal électrique est fourni pour chaque anode, la lumière de la couleur correspondante peut être affichée. En changeant l'intensité du signal électrique de chaque anode, il est possible de produire diverses couleurs.

* :ref:`cpn_rgb`

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
        - 3(1-330Ω, 2-220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_rgb`
        - 1
        - |link_rgb_led_buy|

**Schéma**

|sch_rgb|

Les broches PWM GP13, GP14 et GP15 contrôlent respectivement les broches rouge, verte et bleue de la LED RGB, et la cathode commune est connectée à la masse (GND). Cela permet à la LED RGB d'afficher une couleur spécifique en superposant les lumières sur ces broches avec différentes valeurs PWM.

**Câblage**

|img_rgb_pin|

Une LED RGB possède 4 broches : la plus longue est la cathode commune, qui est généralement connectée à GND, la broche à gauche de la plus longue est la broche rouge, et les deux broches à droite sont les broches verte et bleue.

|wiring_rgb|

**Code**

Ici, nous pouvons choisir notre couleur préférée dans un logiciel de dessin (comme Paint) et l'afficher avec la LED RGB.

.. note::

    * Vous pouvez ouvrir le fichier ``2.4_colorful_light.ino`` dans le chemin ``kepler-kit-main/arduino/2.4_colorful_light``.
    * Ou copiez ce code dans **Arduino IDE**.
    * N'oubliez pas de sélectionner la carte (Raspberry Pi Pico) et le port correct avant de cliquer sur le bouton **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/c869191c-026c-4aac-8396-09eaf6ee2204/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

|img_take_color|

Écrivez la valeur RGB dans ``color_set()``, et vous verrez la LED RGB s'allumer avec les couleurs que vous souhaitez.


**Comment ça marche ?**

Dans cet exemple, la fonction utilisée pour assigner des valeurs aux trois broches de la LED RGB est encapsulée dans une sous-fonction indépendante ``color()``.

.. code-block:: C

    void color (unsigned char red, unsigned char green, unsigned char blue)
    {
        analogWrite(redPin, red);
        analogWrite(greenPin, green);
        analogWrite(bluePin, blue);
    }

Dans ``loop()``, les valeurs RGB fonctionnent comme argument d'entrée pour appeler la fonction ``color()`` afin que la LED RGB puisse émettre différentes couleurs.

.. code-block:: C

    void loop() 
    {    
        color(255, 0, 0); // rouge 
        delay(1000); 
        color(0, 255, 0); // vert  
        delay(1000);  
        color(0, 0, 255); // bleu  
        delay(1000);
    }

