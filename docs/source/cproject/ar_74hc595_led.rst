.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ar_74hc_led:

5.1 - Microchip - 74HC595
================================

Un circuit intégré (integrated circuit) est un dispositif électronique miniature ou composant, représenté par la lettre "IC" dans les schémas.

Un certain procédé est utilisé pour interconnecter les transistors, résistances, condensateurs, inducteurs et autres composants et câblages nécessaires dans un circuit, fabriqués sur une ou plusieurs petites plaquettes semi-conductrices ou substrats diélectriques, puis encapsulés pour former une microstructure avec les fonctions de circuit requises ; tous les composants sont structurés comme un tout, ce qui permet aux composants électroniques de faire un grand pas vers la miniaturisation, la faible consommation d'énergie, l'intelligence et la haute fiabilité.

Les inventeurs des circuits intégrés sont Jack Kilby (circuits intégrés basés sur le germanium (Ge)) et Robert Norton Noyce (circuits intégrés basés sur le silicium (Si)).

Ce kit est équipé d'un CI, le 74HC595, qui permet de réduire considérablement l'utilisation des broches GPIO.
Concrètement, il peut remplacer 8 broches pour la sortie de signaux numériques en écrivant un nombre binaire de 8 bits.

* `Binary number - Wikipedia <https://en.wikipedia.org/wiki/Binary_number>`_

* :ref:`74HC595`

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
        - :ref:`cpn_resistor`
        - 8 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 8
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|

**Schéma**

|sch_74hc_led|

* Lorsque MR (broche 10) est en niveau haut et OE (broche 13) est en niveau bas, les données sont entrées au front montant de SHcp et vont au registre de mémoire par le front montant de SHcp.
* Si les deux horloges sont connectées ensemble, le registre à décalage est toujours une impulsion plus tôt que le registre de mémoire.
* Il y a une broche d'entrée de décalage série (Ds), une broche de sortie série (Q) et un bouton de réinitialisation asynchrone (niveau bas) dans le registre de mémoire.
* Le registre de mémoire produit un bus en parallèle de 8 bits et en trois états.
* Lorsque OE est activé (niveau bas), les données du registre de mémoire sont sorties vers le bus (Q0 ~ Q7).

**Câblage**

|wiring_74hc_led|

**Code**

.. note::

    * Vous pouvez ouvrir le fichier ``5.1_microchip_74hc595.ino`` sous le chemin ``kepler-kit-main/arduino/5.1_microchip_74hc595``.
    * Ou copiez ce code dans l'**Arduino IDE**.
    * N'oubliez pas de sélectionner la carte (Raspberry Pi Pico) et le port correct avant de cliquer sur le bouton **Upload**.

.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/71854882-0c1b-4d09-b3e7-5ef7272f7293/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Lorsque le programme est en cours d'exécution, vous verrez les LED s'allumer une par une.

**Comment ça marche ?**

Déclarez un tableau, stockez plusieurs nombres binaires de 8 bits qui sont utilisés pour changer l'état de fonctionnement des huit LED contrôlées par le 74HC595.

.. code-block:: arduino

    int datArray[] = {0b00000000, 0b00000001, 0b00000011, 0b00000111, 0b00001111, 0b00011111, 0b00111111, 0b01111111, 0b11111111};

Réglez ``STcp`` sur niveau bas puis sur niveau haut. Cela générera une impulsion de front montant de ``STcp``.

.. code-block:: arduino

    digitalWrite(STcp,LOW); 

``shiftOut()`` est utilisé pour décaler un octet de données un bit à la fois, ce qui signifie déplacer un octet de données dans datArray[num] vers le registre de décalage avec la broche DS. MSBFIRST signifie déplacer à partir des bits de poids fort.

.. code-block:: arduino

    shiftOut(DS,SHcp,MSBFIRST,datArray[num]);

Après que ``digitalWrite(STcp,HIGH)`` soit exécuté, STcp sera au front montant. À ce moment, les données du registre de décalage seront déplacées vers le registre de mémoire.

.. code-block:: arduino

    digitalWrite(STcp,HIGH);

Un octet de données sera transféré dans le registre de mémoire après 8 itérations. Ensuite, les données du registre de mémoire sont sorties vers le bus (Q0-Q7). Par exemple, décaler ``B00000001`` allumera la LED contrôlée par Q0 et éteindra les LED contrôlées par Q1~Q7.
