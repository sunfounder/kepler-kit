.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 sur Facebook ! Explorez en profondeur le Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos nouveaux produits.
    - **Promotions festives et cadeaux** : Participez à des concours et promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ar_ultrasonic:

6.1 - Mesurer la distance
======================================

Le module capteur à ultrasons fonctionne sur le principe des systèmes sonar et radar pour déterminer la distance d'un objet.

* :ref:`cpn_ultrasonic`

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
        - :ref:`cpn_ultrasonic`
        - 1
        - |link_ultrasonic_buy|

**Schéma**

|sch_ultrasonic|

**Câblage**

|wiring_ultrasonic|

**Code**

.. note::

    * Vous pouvez ouvrir le fichier ``6.1_ultrasonic.ino`` dans le chemin ``kepler-kit-main/arduino/6.1_ultrasonic``. 
    * Ou copiez ce code dans **Arduino IDE**.
    * N'oubliez pas de sélectionner la carte (Raspberry Pi Pico) et le port correct avant de cliquer sur le bouton **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/631a1663-ce45-4d46-b8f0-7d10f32097a9/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Une fois le programme en cours d'exécution, le moniteur série affichera la distance du capteur ultrasonique par rapport à l'obstacle situé devant lui.

**Comment ça marche ?**

Concernant l'utilisation du capteur à ultrasons, nous pouvons directement examiner la sous-fonction.

.. code-block:: arduino

    float readSensorData(){// ...}

Le ``PING`` est déclenché par une impulsion de niveau haut de 2 microsecondes ou plus. 
(Envoyez d'abord une courte impulsion de niveau bas pour garantir une impulsion propre de niveau haut.)

.. code-block:: arduino

    digitalWrite(trigPin, LOW); 
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH); 
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW); 

La broche écho est utilisée pour lire le signal provenant du PING, une 
impulsion de niveau haut dont la durée est le temps (en microsecondes) 
entre l'envoi du ping et la réception de l'écho de l'objet.

.. code-block:: arduino

    microsecond=pulseIn(echoPin, HIGH);

La vitesse du son est de 340 m/s ou 29 microsecondes par centimètre.

Cela donne la distance parcourue par le ping, aller-retour, donc on divise 
par 2 pour obtenir la distance de l'obstacle.

.. code-block:: arduino

    float distance = microsecond / 29.00 / 2;  

Notez que le capteur à ultrasons met le programme en pause lorsqu'il fonctionne, ce qui peut provoquer un certain décalage lors de l'écriture de projets complexes.
