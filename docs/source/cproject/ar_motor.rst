.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 sur Facebook ! Plongez au cœur du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des concours et promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ar_motor:

3.5 - Petit Ventilateur
============================

Nous allons maintenant utiliser le TA6586 pour piloter le moteur à courant continu afin de le faire tourner dans le sens horaire et anti-horaire. 
Comme le moteur DC nécessite un courant relativement important, pour des raisons de sécurité, nous utilisons ici un module d'alimentation pour alimenter le moteur.

* :ref:`cpn_motor`
* :ref:`cpn_ta6586`
* :ref:`cpn_power_module`

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
        - :ref:`cpn_ta6586`
        - 1
        - 
    *   - 6
        - :ref:`cpn_motor`
        - 1
        - |link_motor_buy| 
    *   - 7
        - :ref:`cpn_lipo_charger`
        - 1
        -  
    *   - 8
        - Batterie 18650
        - 1
        -  
    *   - 9
        - Support de batterie
        - 1
        - 

**Schéma**

|sch_motor|

**Câblage**

.. note::

    * Comme les moteurs DC nécessitent un courant élevé, nous utilisons un module chargeur Li-po pour alimenter le moteur pour des raisons de sécurité.
    * Assurez-vous que votre module chargeur Li-po est connecté comme indiqué dans le schéma. Sinon, un court-circuit pourrait endommager votre batterie et vos circuits.


|wiring_motor|


**Code**

.. note::

    * Vous pouvez ouvrir le fichier ``3.5_small_fan.ino`` sous le chemin ``kepler-kit-main/arduino/3.5_small_fan``. 
    * Ou copiez ce code dans l'**Arduino IDE**.
    * N'oubliez pas de sélectionner la carte (Raspberry Pi Pico) et le port correct avant de cliquer sur le bouton **Upload**.


.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/26d75a18-6b91-40f4-80ab-f2cdf58644ac/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Une fois le programme lancé, le moteur tournera en avant et en arrière selon un motif régulier.


.. note::

    * Si vous ne pouvez pas recharger le code, cette fois vous devez connecter la broche **RUN** du Pico W avec un fil à GND pour le réinitialiser, puis débranchez ce fil pour exécuter à nouveau le code.
    * Cela est dû au fait que le moteur utilise trop de courant, ce qui peut entraîner la déconnexion du Pico W de l'ordinateur. 

    |wiring_run_reset|
