.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des concours et promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ar_temp:

2.13 - Thermomètre
===========================

Un thermomètre est un appareil qui mesure la température ou un gradient de température (le degré de chaleur ou de froid d'un objet). 
Il possède deux éléments essentiels : (1) un capteur de température (par exemple, le bulbe d'un thermomètre à mercure ou le capteur pyrométrique d'un thermomètre infrarouge) où une variation se produit en fonction de la température ; 
et (2) un moyen de convertir cette variation en une valeur numérique (par exemple, l'échelle visible sur un thermomètre à mercure ou l'affichage numérique sur un modèle infrarouge). 
Les thermomètres sont largement utilisés en technologie et dans l'industrie pour surveiller les processus, en météorologie, en médecine et dans la recherche scientifique.

Un thermistor est un type de capteur de température dont la résistance dépend fortement de la température. Il existe deux types : 
le Coefficient de Température Négatif (NTC) et le Coefficient de Température Positif (PTC), 
également connus sous les noms de NTC et PTC. La résistance d'un thermistor PTC augmente avec la température, alors que celle d'un NTC diminue.

Dans cette expérience, nous utilisons un **thermistor NTC** pour créer un thermomètre.

* :ref:`cpn_thermistor`


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
        - :ref:`cpn_thermistor`
        - 1
        - |link_thermistor_buy|

**Schéma**

|sch_temp|

Dans ce circuit, la résistance de 10K et la thermistance sont connectées en série, et le courant qui les traverse est le même. La résistance de 10K agit comme une protection, et le GP28 lit la valeur après la conversion de la tension de la thermistance.

Lorsque la température augmente, la valeur de résistance de la thermistance NTC diminue, puis sa tension diminue, de sorte que la valeur de GP28 diminue ; si la température est suffisamment élevée, la résistance de la thermistance sera proche de 0, et la valeur de GP28 sera proche de 0. À ce moment-là, la résistance de 10K joue un rôle protecteur, empêchant que 3,3V et GND ne soient connectés ensemble, ce qui entraînerait un court-circuit.

Lorsque la température baisse, la valeur de GP28 augmentera. Lorsque la température est suffisamment basse, la résistance de la thermistance sera infinie, et sa tension sera proche de 3,3V (la résistance de 10K est négligeable), et la valeur de GP28 sera proche de la valeur maximale de 1023.

La formule de calcul est indiquée ci-dessous.

.. code-block::

  Valeur numérique = (Tension analogique / 3,3V) * 1023



**Câblage**

|wiring_temp|

.. #. Connectez les broches 3V3 et GND du Pico W au bus d'alimentation de la breadboard.
.. #. Connectez une extrémité du thermistor à la broche GP28, puis connectez la même extrémité au bus d'alimentation positif avec une résistance de 10KΩ.
.. #. Connectez l'autre extrémité du thermistor au bus d'alimentation négatif.

.. note::
    * Le thermistor est noir et marqué 103.
    * La bague de couleur de la résistance de 10KΩ est rouge, noir, noir, rouge et marron.

**Code**

.. note::

    * Vous pouvez ouvrir le fichier ``2.13_thermometer.ino`` dans le chemin ``kepler-kit-main/arduino/2.13_thermometer``. 
    * Ou copiez ce code dans **Arduino IDE**.
    * N'oubliez pas de sélectionner la carte (Raspberry Pi Pico) et le port correct avant de cliquer sur le bouton **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/1ae1a028-2647-4e4c-b647-0d4759f6fd03/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Après l'exécution du programme, le Moniteur Série affichera les températures en Celsius et en Fahrenheit.

**Comment ça marche ?**

Chaque thermistor possède une résistance nominale. 
Ici, elle est de 10k ohms, mesurée à 25 degrés Celsius. 

Lorsque la température augmente, la résistance du thermistor diminue. 
Les données de tension sont alors converties en valeurs numériques par l'adaptateur A/N. 

La température en degrés Celsius ou Fahrenheit est calculée via le programme.

.. code-block:: arduino

    long a = analogRead(analogPin);

Cette ligne permet de lire la valeur du thermistor.

.. code-block:: arduino

    float tempC = beta / (log((1025.0 * 10 / a - 10) / 10) + beta / 298.0) - 273.0;
    float tempF = 1.8 * tempC + 32.0;

Ces calculs convertissent les valeurs du thermistor en degrés Celsius et Fahrenheit.

.. note::
    Voici la relation entre la résistance et la température :

    **RT =RN expB(1/TK – 1/TN)** 

    * RT est la résistance du thermistor NTC à la température TK.
    * RN est la résistance du thermistor NTC à la température nominale TN. Ici, RN vaut 10k.
    * TK est la température en Kelvin, l'unité est K. Ici, TK équivaut à 273,15 + degrés Celsius.
    * TN est la température nominale en Kelvin ; l'unité est également K. Ici, TN équivaut à 273,15 + 25.
    * B (beta), la constante de matériau du thermistor NTC, est aussi appelée indice de sensibilité thermique avec une valeur de 3950.
    * exp est l'abréviation d'exponentiel, et la base e est un nombre naturel proche de 2,7.

    Convertissez cette formule TK=1/(ln(RT/RN)/B+1/TN) pour obtenir la température en Kelvin. La température en degrés Celsius est obtenue en soustrayant 273,15.

    Cette relation est une formule empirique. Elle est précise seulement lorsque la température et la résistance sont dans la plage effective.

Ce code permet d'insérer Rt dans la formule TK=1/(ln(RT/RN)/B+1/TN) pour obtenir la température en Kelvin.

