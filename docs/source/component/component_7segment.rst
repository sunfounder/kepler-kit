.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et vos défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Remises spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions et cadeaux festifs** : Participez à des promotions spéciales et des tirages au sort pour les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _cpn_7_segment:

Afficheur 7 segments
======================

|img_7seg|


Un afficheur 7 segments est un composant en forme de 8 qui regroupe 7 LEDs. Chaque LED est appelée segment - lorsqu'elle est alimentée, elle forme une partie d'un chiffre à afficher.

Il existe deux types de connexions des broches : Cathode Commune (CC) et Anode Commune (CA). Comme leur nom l'indique, un afficheur CC a toutes les cathodes des 7 LEDs connectées ensemble, tandis qu'un afficheur CA a tous les anodes des 7 segments connectés.

Dans ce kit, nous utilisons un afficheur 7 segments à cathode commune, dont voici le symbole électronique.

|img_7seg_cathode|

Chacune des LEDs de l'afficheur est associée à un segment positionnel, avec une broche de connexion individuelle qui sort du boîtier en plastique rectangulaire. Ces broches sont étiquetées de "a" à "g", représentant chaque LED individuelle. Les autres broches des LEDs sont reliées entre elles pour former une broche commune. En polarisant les broches appropriées des segments LED dans un ordre particulier, certains segments s'allument tandis que d'autres restent éteints, permettant ainsi de montrer le caractère correspondant sur l'afficheur.


* `Seven-segment Display - Wikipedia <https://en.wikipedia.org/wiki/Seven-segment_display>`_

**Codes d'affichage** 

Pour vous aider à comprendre comment les afficheurs 7 segments (cathode commune) affichent les chiffres, nous avons créé le tableau suivant. Les "Numbers" représentent les chiffres 0-F affichés sur l'afficheur ; (DP) GFEDCBA indique les LED correspondantes réglées sur 0 ou 1. Par exemple, 00111111 signifie que DP et G sont réglés sur 0, tandis que les autres sont sur 1. Ainsi, le chiffre 0 apparaît sur l'afficheur, et le code hexadécimal correspondant est affiché sous "Hex Code".

.. list-table:: Glyph Code
    :widths: 20 20 20
    :header-rows: 1

    *   - Chiffres
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
    *   - A	
        - 01110111	
        - 0x77
    *   - B
        - 01111100	
        - 0x7c
    *   - C	
        - 00111001	
        - 0x39
    *   - D	
        - 01011110	
        - 0x5e
    *   - E	
        - 01111001	
        - 0x79
    *   - F	
        - 01110001	
        - 0x71

.. Example
.. -------------------

.. :ref:`Afficheur LED segmenté`



**Exemple**

* :ref:`py_74hc_7seg` (For MicroPython User)
* :ref:`ar_74hc_7seg` (For Arduino User)