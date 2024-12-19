.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ar_joystick:

4.1 - Utiliser le Joystick
================================

Si vous jouez beaucoup aux jeux vidéo, vous connaissez sûrement bien le joystick.
Il est généralement utilisé pour déplacer le personnage, faire pivoter l'écran, etc.

Le principe qui permet au joystick de transmettre nos actions à l'ordinateur est très simple.
Il peut être considéré comme étant composé de deux potentiomètres placés perpendiculairement l'un par rapport à l'autre.
Ces deux potentiomètres mesurent la valeur analogique du joystick verticalement et horizontalement, ce qui permet de déterminer une valeur (x, y) dans un système de coordonnées cartésien.

Le joystick fourni dans ce kit dispose également d'une entrée numérique, qui est activée lorsque l'on appuie sur le joystick.

* :ref:`cpn_joystick`

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
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_joystick`
        - 1
        - 

**Schéma**

|sch_joystick|

La broche SW est connectée à une résistance pull-up de 10KΩ, ce qui permet d'obtenir un niveau haut stable sur la broche SW (axe Z) lorsque le joystick n'est pas pressé ; sinon, la broche SW serait en état flottant et la valeur de sortie pourrait varier entre 0 et 1.

**Câblage**

|wiring_joystick|

**Code**

.. note::

    * Vous pouvez ouvrir le fichier ``4.1_toggle_the_joystick.ino`` sous le chemin ``kepler-kit-main/arduino/4.1_toggle_the_joystick``. 
    * Ou copiez ce code dans l'**Arduino IDE**.
    * N'oubliez pas de sélectionner la carte Raspberry Pi Pico et le port correct avant de cliquer sur le bouton **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/dfe53878-7cb4-4543-bb97-7f5ef5aad15a/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Une fois le programme lancé, la console affichera les valeurs x, y, z du joystick.


* Les valeurs des axes X et Y sont des valeurs analogiques qui varient de 0 à 1023.
* L'axe Z est une valeur numérique avec un statut de 1 ou 0.
