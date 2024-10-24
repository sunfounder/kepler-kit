.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ar_74hc_7seg:

5.2 - Affichage de nombre
==============================

Les afficheurs à segments LED se retrouvent partout dans la vie quotidienne.
Par exemple, sur un climatiseur, il peut afficher la température ; sur un 
indicateur de trafic, il peut servir de minuterie.

L'afficheur à segments LED est essentiellement un dispositif constitué de 8 LED, 
dont 7 LED en forme de bande forment un chiffre "8", avec une LED ponctuelle 
légèrement plus petite servant de point décimal. Ces LED sont marquées comme 
a, b, c, d, e, f, g, et dp. Elles possèdent leurs propres broches d'anode et 
partagent les cathodes. Leurs positions de broches sont illustrées dans le 
schéma ci-dessous.

|img_7seg_cathode|

Cela signifie qu'il doit être contrôlé par 8 signaux numériques en même temps 
pour fonctionner pleinement, et le 74HC595 peut accomplir cela.

* :ref:`cpn_7_segment`


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
        - 1 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_7_segment`
        - 1
        - |link_7segment_buy|
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|

**Schéma**

|sch_74hc_7seg|

**Câblage**

|wiring_74hc_7seg|

.. list-table:: Câblage
    :widths: 15 25
    :header-rows: 1

    *   - :ref:`cpn_74hc595`
        - :ref:`cpn_led` Segment Display
    *   - Q0
        - a
    *   - Q1
        - b
    *   - Q2
        - c
    *   - Q3
        - d
    *   - Q4
        - e
    *   - Q5
        - f
    *   - Q6
        - g
    *   - Q7
        - dp

**Code**

.. note::

    * Vous pouvez ouvrir le fichier ``5.2_number_display.ino`` sous le chemin ``kepler-kit-main/arduino/5.2_number_display``.
    * Ou copiez ce code dans l'**Arduino IDE**.
    * N'oubliez pas de sélectionner la carte (Raspberry Pi Pico) et le port correct avant de cliquer sur le bouton **Upload**.

.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/a237801f-40d7-4920-80fb-a349307b1e05/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Lorsque le programme fonctionne, vous verrez l'afficheur à segments LED afficher les chiffres de 0 à 9 en séquence.

**Comment ça marche ?**

``shiftOut()`` fera en sorte que le 74HC595 sorte 8 signaux numériques.
Il envoie le dernier bit du nombre binaire à Q0, et le premier bit à Q7. En d'autres termes, écrire le nombre binaire "00000001" fera que Q0 envoie un signal haut et que Q1~Q7 envoient des signaux bas.

Supposons que l'afficheur 7 segments affiche le nombre "1", il faut envoyer un signal haut pour b, c, et un signal bas pour a, d, e, f, g et dp.
Autrement dit, le nombre binaire "00000110" doit être envoyé. Pour plus de lisibilité, nous utiliserons la notation hexadécimale "0x06".

* `Hexadecimal <https://en.wikipedia.org/wiki/Hexadecimal>`_

* `BinaryHex Converter <https://www.binaryhexconverter.com/binary-to-hex-converter>`_

De la même manière, nous pouvons également faire en sorte que l'afficheur LED affiche d'autres chiffres. Le tableau ci-dessous montre les codes correspondants à ces chiffres.

.. list-table:: Glyph Code
    :widths: 20 20 20
    :header-rows: 1

    *   - Nombres
        - Code binaire
        - Code hexadécimal
    *   - 0
        - 00111111
        - 0x3f
    *   - 1
        - 00000110
        - 0x06
    *   - 2
        - 01011011
        - 0x5b
    *   - 3
        - 01001111
        - 0x4f
    *   - 4
        - 01100110
        - 0x66
    *   - 5
        - 01101101
        - 0x6d
    *   - 6
        - 01111101
        - 0x7d
    *   - 7
        - 00000111
        - 0x07
    *   - 8
        - 01111111
        - 0x7f
    *   - 9
        - 01101111
        - 0x6f

Écrivez ces codes dans ``shiftOut()`` pour faire afficher les chiffres correspondants par l'afficheur à segments LED.
