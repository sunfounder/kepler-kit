.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 sur Facebook ! Explorez plus en profondeur le Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des concours et promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ar_transistor:

2.15 - Deux types de transistors
==========================================

Ce kit est équipé de deux types de transistors, S8550 et S8050, le premier est un PNP et le second est un NPN. Ils se ressemblent beaucoup, il est donc important de bien vérifier leurs étiquettes.
Lorsqu'un signal de niveau haut traverse un transistor NPN, il est alimenté. Mais un PNP nécessite un signal de niveau bas pour être activé. Les deux types de transistors sont souvent utilisés comme interrupteurs sans contact, comme dans cette expérience.

|img_NPN&PNP|

Utilisons une LED et un bouton pour comprendre comment utiliser un transistor !

:ref:`cpn_transistor`

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
        - 3(220Ω, 1KΩ, 10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_button`
        - 1
        - |link_button_buy|
    *   - 8
        - :ref:`cpn_transistor`
        - 1(S8050/S8550)
        - |link_transistor_buy|

**Connexion du transistor NPN (S8050)**

|sch_s8050|

Dans ce circuit, lorsque le bouton est pressé, GP14 est en état haut.

En programmant GP15 pour qu'il émette un signal haut, après une résistance de limitation de courant de 1kΩ (pour protéger le transistor), le S8050 (transistor NPN) est activé, permettant ainsi à la LED de s'allumer.

|wiring_s8050|

.. 1. Connectez le 3V3 et la masse (GND) du Pico W au bus d'alimentation de la breadboard.
.. #. Connectez l'anode de la LED au bus d'alimentation positif via une résistance de 220Ω.
.. #. Connectez la cathode de la LED au **collecteur** du transistor.
.. #. Connectez la base du transistor à la broche GP15 via une résistance de 1kΩ.
.. #. Connectez l'**émetteur** du transistor au bus d'alimentation négatif.
.. #. Connectez une extrémité du bouton à la broche GP14 et utilisez une résistance de 10kΩ pour connecter la même extrémité au bus d'alimentation négatif. L'autre extrémité doit être connectée au bus d'alimentation positif.

.. .. note::
..     * Les anneaux de couleur de la résistance de 220Ω sont rouge, rouge, noir, noir et brun.
..     * Les anneaux de couleur de la résistance de 1kΩ sont brun, noir, noir, brun et brun.
..     * Les anneaux de couleur de la résistance de 10kΩ sont brun, noir, noir, rouge et brun.

**Connexion du transistor PNP (S8550)**

|sch_s8550|

Dans ce circuit, GP14 est par défaut en état bas et passe en état haut lorsque le bouton est pressé.

En programmant GP15 pour qu'il émette un signal **bas**, après une résistance de limitation de courant de 1kΩ (pour protéger le transistor), le S8550 (transistor PNP) est activé, permettant ainsi à la LED de s'allumer.

La seule différence que vous remarquerez entre ce circuit et le précédent est que dans le circuit précédent, la cathode de la LED est connectée au **collecteur** du **S8050 (transistor NPN)**, tandis que dans celui-ci, elle est connectée à l'**émetteur** du **S8550 (transistor PNP)**.

|wiring_s8550|

.. 1. Connectez le 3V3 et la masse (GND) du Pico W au bus d'alimentation de la breadboard.
.. #. Connectez l'anode de la LED au bus d'alimentation positif via une résistance de 220Ω.
.. #. Connectez la cathode de la LED à l'**émetteur** du transistor.
.. #. Connectez la base du transistor à la broche GP15 via une résistance de 1kΩ.
.. #. Connectez le **collecteur** du transistor au bus d'alimentation négatif.

**Code**

.. note::

    * Vous pouvez ouvrir le fichier ``2.15_transistor.ino`` dans le chemin ``kepler-kit-main/arduino/2.15_transistor``. 
    * Ou copiez ce code dans **Arduino IDE**.
    * N'oubliez pas de sélectionner la carte (Raspberry Pi Pico) et le port correct avant de cliquer sur le bouton **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/77c437de-028f-47c1-9d79-177e90eb0599/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Les deux types de transistors peuvent être contrôlés avec le même code. Lorsque nous appuyons sur le bouton, le Pico W envoie un signal de niveau haut au transistor ; lorsque nous le relâchons, il envoie un signal de niveau bas.
Nous pouvons observer que des phénomènes diamétralement opposés se produisent dans les deux circuits.

* Le circuit utilisant le S8050 (transistor NPN) s'allume lorsque le bouton est pressé, ce qui signifie qu'il reçoit un signal de conduction de niveau haut ;
* Le circuit utilisant le S8550 (transistor PNP) s'allume lorsqu'il est relâché, ce qui signifie qu'il reçoit un signal de conduction de niveau bas.
