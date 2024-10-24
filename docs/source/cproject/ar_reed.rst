.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 sur Facebook ! Explorez en profondeur Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos nouveaux produits.
    - **Promotions festives et cadeaux** : Participez à des concours et des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ar_reed:

2.9 - Ressentir le magnétisme
===================================

Le type de contacteur à lames le plus courant contient une paire de lamelles métalliques flexibles et magnétisables, dont les extrémités sont séparées par un petit écart lorsque le contact est ouvert.

Un champ magnétique provenant d'un électroaimant ou d'un aimant permanent fera en sorte que les lamelles s'attirent, complétant ainsi un circuit électrique. 
La force de ressort des lamelles les sépare, ouvrant le circuit lorsque le champ magnétique disparaît.

Une application courante des contacteurs à lames est de détecter l'ouverture d'une porte ou d'une fenêtre pour un système d'alarme.

* :ref:`cpn_reed`

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
        - :ref:`cpn_reed`
        - 1
        - 

**Schéma**

|sch_reed|

Par défaut, GP14 est à un niveau bas ; il passera à un niveau haut lorsque l'aimant sera proche du contacteur à lames.

Le rôle de la résistance de 10KΩ est de maintenir GP14 à un niveau bas stable lorsqu'aucun aimant n'est à proximité.

**Câblage**

|wiring_reed|

**Code**

.. note::

    * Vous pouvez ouvrir le fichier ``2.9_feel_the_magnetism.ino`` sous le chemin ``kepler-kit-main/arduino/2.9_feel_the_magnetism``. 
    * Ou copiez ce code dans l'**Arduino IDE**.
    * N'oubliez pas de sélectionner la carte (Raspberry Pi Pico) et le port correct avant de cliquer sur le bouton **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/62bba18c-7921-4df9-806f-deffce17de9a/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Lorsque l'aimant s'approche, le circuit se fermera, tout comme le bouton dans le chapitre :ref:`ar_button`.

.. **En savoir plus**

.. Cette fois, nous avons essayé une méthode plus flexible d'utilisation des contacteurs : les requêtes d'interruption, ou IRQs.

.. Par exemple, vous lisez un livre page par page, comme si un programme exécutait un thread. À ce moment, quelqu'un vient vous poser une question et interrompt votre lecture. La personne exécute une requête d'interruption : vous demander d'arrêter ce que vous faites, répondre à ses questions, puis vous laisser retourner à la lecture après la fin.

.. Les requêtes d'interruption fonctionnent de la même manière, elles permettent à certaines opérations d'interrompre le programme principal.

.. .. :raw-code:

.. .. note::

..    * Vous pouvez ouvrir le fichier ``2.9_feel_the_magnetism_irq.ino`` sous le chemin ``kepler-kit-main/arduino/2.9_feel_the_magnetism_irq``. 
..    * Ou copiez ce code dans l'**Arduino IDE**.

..    * N'oubliez pas de sélectionner la carte (Raspberry Pi Pico) et le port correct avant de cliquer sur le bouton **Upload**.

.. Une fonction de rappel ``detected()`` est définie ici, appelée le gestionnaire d'interruption. Elle sera exécutée lorsqu'une requête d'interruption sera déclenchée. 
.. Ensuite, une requête d'interruption est configurée dans ``setup``, qui comprend deux parties : ``mode`` et ``ISR``.

.. Dans ce programme, ``mode`` est ``RISING``, ce qui indique que la valeur de la broche passe de bas à haut (c'est-à-dire que le bouton est pressé).

.. ``ISR`` est ``detected``, la fonction de rappel que nous avons définie.

.. * `attachInterrupt() - Référence Arduino <https://www.arduino.cc/reference/en/language/functions/external-interrupts/attachinterrupt/>`_
