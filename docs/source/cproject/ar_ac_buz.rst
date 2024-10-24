.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ar_ac_buz:

3.1 - Bip sonore
====================

Le buzzer actif est un dispositif de sortie numérique typique aussi facile à utiliser qu'une LED !

* :ref:`cpn_buzzer`

**Composants requis**

Pour ce projet, nous avons besoin des composants suivants.

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
        - :ref:`cpn_transistor`
        - 1 (S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 1 (1KΩ)
        - |link_resistor_buy|
    *   - 7
        - Buzzer actif :ref:`cpn_buzzer`
        - 1
        - 

**Schéma**

|sch_buzzer|

Lorsque la sortie GP15 est en niveau haut, après la résistance de limitation de courant de 1K (pour protéger le transistor), le S8050 (transistor NPN) se met à conduire, permettant ainsi au buzzer de sonner.

Le rôle du S8050 (transistor NPN) est d'amplifier le courant pour que le buzzer soit plus fort. En effet, vous pouvez également connecter le buzzer directement à GP15, mais vous constaterez que le son sera plus faible.

**Câblage**

Deux types de buzzers sont inclus dans le kit. 
Nous devons utiliser le buzzer actif. Tournez-les, le côté scellé (et non le PCB exposé) est celui que nous devons choisir.

|img_buzzer|

Le buzzer doit utiliser un transistor pour fonctionner, ici nous utilisons le S8050 (transistor NPN).

|wiring_beep|

**Code**

.. note::

    * Vous pouvez ouvrir le fichier ``3.1_beep.ino`` sous le chemin ``kepler-kit-main/arduino/3.1_beep``.
    * Ou copiez ce code dans l'**Arduino IDE**.
    * N'oubliez pas de sélectionner la carte (Raspberry Pi Pico) et le port correct avant de cliquer sur le bouton **Upload**.

.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/62bf2c5d-9890-4f3a-b02a-119c2f6b0bf1/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Une fois le code exécuté, vous entendrez un bip sonore toutes les secondes.
