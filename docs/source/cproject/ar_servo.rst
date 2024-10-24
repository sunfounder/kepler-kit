.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 sur Facebook ! Plongez dans l'univers de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des concours et promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ar_servo:

3.7 - Faire Balancer le Servo
================================

Dans ce kit, en plus de la LED et du buzzer passif, il y a aussi un dispositif contrôlé par un signal PWM, le servo.

Un servo est un dispositif de positionnement (angle) idéal pour les systèmes de contrôle nécessitant des ajustements d'angle constants et pouvant être maintenus. Il est largement utilisé dans les jouets télécommandés haut de gamme, comme les avions, les modèles de sous-marins, et les robots télécommandés.

Maintenant, essayez de faire balancer le servo !

* :ref:`cpn_servo`

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
        - :ref:`cpn_servo`
        - 1
        - |link_servo_buy|

**Schéma**

|sch_servo|

**Câblage**

|wiring_servo|

* Le fil orange est le signal et est connecté à GP15.
* Le fil rouge est le VCC et est connecté à VBUS (5V).
* Le fil marron est la masse (GND) et est connecté à GND.

**Code**

.. note::

    * Vous pouvez ouvrir le fichier ``3.7_swinging_servo.ino`` dans le chemin ``kepler-kit-main/arduino/3.7_swinging_servo``.
    * Ou copiez ce code dans **Arduino IDE**.
    * N'oubliez pas de sélectionner la carte (Raspberry Pi Pico) et le port correct avant de cliquer sur le bouton **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/d52a67be-be6b-4cbf-b411-810160f56928/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Lorsque le programme est en cours d'exécution, vous pourrez voir le bras du servo osciller d'avant en arrière de 0° à 180°.


**Comment ça marche ?**

En utilisant la bibliothèque ``Servo.h``, vous pouvez facilement contrôler le servo.

.. code-block:: arduino

    #include <Servo.h> 

**Fonctions de la bibliothèque**

.. code-block:: arduino

    Servo

Créer un objet **Servo** pour contrôler un servo.

.. code-block:: arduino

    uint8_t attach(int pin); 

Attribue une broche pour piloter le servo. Appelle pinMode. Retourne 0 en cas d'échec.

.. code-block:: arduino

    void detach();

Libère la broche du contrôle du servo.

.. code-block:: arduino

    void write(int value); 

Définit l'angle du servo en degrés, de 0 à 180.

.. code-block:: arduino

    int read();

Retourne la dernière valeur définie avec write().

.. code-block:: arduino

    bool attached(); 

Retourne 1 si le servo est actuellement connecté.
