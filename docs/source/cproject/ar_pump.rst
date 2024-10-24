.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des concours et promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ar_pump:

3.6 - Pompage
=======================

Les petites pompes centrifuges sont idéales pour les projets d'arrosage automatique des plantes.
Elles peuvent également être utilisées pour créer de petites fontaines intelligentes.

Leur composant moteur est un moteur électrique, entraîné de la même manière qu'un moteur classique.

* :ref:`cpn_pump`
* :ref:`cpn_motor`
* :ref:`cpn_ta6586`
* :ref:`cpn_power_module`

.. note::

    #. Connectez le tube à la sortie du moteur, plongez la pompe dans l'eau, puis allumez-la.
    #. Vous devez vous assurer que le niveau d'eau est toujours supérieur au moteur. Le fonctionnement à vide peut endommager le moteur en raison de la chaleur générée et entraîner du bruit.
    #. Si vous arrosez des plantes, évitez que la terre soit aspirée, car cela pourrait obstruer la pompe.
    #. Si l'eau ne sort pas du tube, il se peut qu'il reste de l'eau résiduelle dans le tube bloquant le flux d'air, et il faut donc le vidanger d'abord.

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
        - :ref:`cpn_lipo_charger`
        - 1
        -  
    *   - 7
        - Batterie 18650
        - 1
        -  
    *   - 8
        - Support de batterie
        - 1
        -  
    *   - 9
        - :ref:`cpn_pump`
        - 1
        -  

**Schéma**

|sch_pump|

**Câblage**

.. note::

    * Les pompes nécessitant un courant élevé, nous utilisons un module chargeur Li-po pour alimenter le moteur ici pour des raisons de sécurité.
    * Assurez-vous que votre module chargeur Li-po est connecté comme indiqué sur le schéma. Sinon, un court-circuit pourrait endommager votre batterie et votre circuit.

|wiring_pump|

**Code**

.. note::

    * Vous pouvez ouvrir le fichier ``3.6_pumping.ino`` sous le chemin ``kepler-kit-main/arduino/3.6_pumping``. 
    * Ou copiez ce code dans l'**Arduino IDE**.
    * N'oubliez pas de sélectionner la carte (Raspberry Pi Pico) et le port correct avant de cliquer sur le bouton Upload.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/4194feb8-92d4-4ab4-b51c-286d014af0a6/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe> 

Après l'exécution du code, la pompe commence à fonctionner et vous verrez l'eau s'écouler du tube en même temps.

.. note::

    * Si vous ne parvenez pas à téléverser le code à nouveau, vous devez connecter la broche **RUN** du Pico W à la terre (GND) avec un fil pour le réinitialiser, puis débrancher ce fil pour relancer le code.
    * Cela est dû au fait que le moteur fonctionne avec un courant trop élevé, ce qui peut provoquer la déconnexion du Pico W de l'ordinateur.

    |wiring_run_reset|