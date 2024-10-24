.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des concours et promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ar_photoresistor:


2.12 - Ressentir la lumière
=================================
La photorésistance est un dispositif typique pour les entrées analogiques et s'utilise de manière très similaire à un potentiomètre. Sa valeur de résistance dépend de l'intensité lumineuse : plus la lumière est forte, plus la résistance diminue ; à l'inverse, elle augmente lorsque la lumière faiblit.

* :ref:`cpn_photoresistor`

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
        - :ref:`cpn_photoresistor`
        - 1
        - |link_photoresistor_buy|

**Schéma**

|sch_photoresistor|

Dans ce circuit, la résistance de 10KΩ et la photorésistance sont connectées en série, et le courant qui les traverse est identique. La résistance de 10KΩ agit comme protection, et le GP28 lit la valeur après la conversion de la tension de la photorésistance.

Lorsque la lumière s'intensifie, la résistance de la photorésistance diminue, ce qui entraîne une baisse de sa tension ; par conséquent, la valeur lue par le GP28 diminue. Si la lumière est suffisamment forte, la résistance de la photorésistance se rapproche de 0, et la valeur du GP28 sera également proche de 0. À ce moment-là, la résistance de 10KΩ joue un rôle de protection pour éviter que le 3,3V et la masse (GND) ne se retrouvent directement connectés, ce qui entraînerait un court-circuit.

Si vous placez la photorésistance dans un environnement sombre, la valeur du GP28 augmentera. Dans une obscurité totale, la résistance de la photorésistance deviendra infinie, sa tension sera proche de 3,3V (la résistance de 10KΩ devient négligeable), et la valeur du GP28 sera proche du maximum de 65535.


La formule de calcul est la suivante :

    (Vp/3.3V) x 65535 = Ap


**Câblage**

|wiring_photoresistor|

**Code**

.. note::

    * Vous pouvez ouvrir le fichier ``2.12_feel_the_light.ino`` sous le chemin ``kepler-kit-main/arduino/2.12_feel_the_light``. 
    * Ou copiez ce code dans l'**Arduino IDE**.
    * N'oubliez pas de sélectionner la carte (Raspberry Pi Pico) et le port correct avant de cliquer sur le bouton Upload.



.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/44074b9e-3e4e-475b-af37-689254f87ab2/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Après avoir exécuté le programme, le moniteur série affichera les valeurs de la photorésistance. Vous pouvez diriger une lampe de poche vers elle ou la couvrir avec votre main pour voir comment les valeurs varient.
