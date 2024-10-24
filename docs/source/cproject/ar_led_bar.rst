.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ar_led_bar:

2.2 - Afficher le Niveau
=============================

Le premier projet consistait simplement à faire clignoter une LED. Dans ce projet, nous allons utiliser une barre de LED, composée de 10 LED regroupées dans un boîtier en plastique, généralement utilisée pour afficher des niveaux de puissance ou de volume.

|img_led_bar_pin|

* :ref:`cpn_led_bar`

**Composants requis**

Dans ce projet, nous avons besoin des composants suivants. 

Il est plus pratique d'acheter un kit complet, voici le lien : 

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
        - 10(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led_bar`
        - 1
        - 

**Schéma**

|sch_ledbar|

La barre de LED contient 10 LED, chacune étant contrôlable individuellement. Ici, l'anode de chacune des 10 LED est connectée aux broches GP6 à GP15, et la cathode est reliée à une résistance de 220 ohms, puis à la masse (GND).

**Câblage**

|wiring_ledbar|

**Code**

.. note::

    * Vous pouvez ouvrir le fichier ``2.2_display_the_level.ino`` sous le chemin ``kepler-kit-main/arduino/2.2_display_the_level``. 
    * Ou copiez ce code dans l'**Arduino IDE**.
    * N'oubliez pas de sélectionner la carte (Raspberry Pi Pico) et le port correct avant de cliquer sur le bouton **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/ae60e723-430e-4a58-ac39-566b9d1828e8/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>
    

Lorsque le programme est en cours d'exécution, vous verrez les LED de la barre s'allumer puis s'éteindre successivement.


**Comment ça fonctionne ?**

Chacune des dix LED de la barre doit être contrôlée par une broche, ce qui signifie que nous devons définir ces dix broches.

Les lignes de code dans ``setup()`` utilisent une boucle for pour initialiser les broches 6 à 15 en mode sortie.

.. code-block:: C

    for(int i=6;i<=15;i++)
    {
        pinMode(i,OUTPUT);
    }   

La boucle for est utilisée dans ``loop()`` pour faire clignoter les LED (allumées pendant 0,5s, puis éteintes pendant 0,5s) en séquence.

.. code-block:: C

    for(int i=6;i<=15;i++)
    {
        digitalWrite(i,HIGH);
        delay(500);
        digitalWrite(i,LOW);
        delay(500);    
    }
