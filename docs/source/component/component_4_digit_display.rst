.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 aux côtés d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Profitez d'un accès anticipé aux annonces de nouveaux produits et aux aperçus en avant-première.
    - **Remises spéciales** : Bénéficiez de réductions exclusives sur nos derniers produits.
    - **Promotions et cadeaux festifs** : Participez à des promotions spéciales et des tirages au sort pour les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _cpn_4_dit_7_segment:

Afficheur 7 segments à 4 chiffres
======================================

L'afficheur 7 segments à 4 chiffres est composé de quatre afficheurs 7 segments fonctionnant ensemble.

|img_4-digit-sche|

L'afficheur 7 segments à 4 chiffres fonctionne de manière indépendante. 
Il utilise le principe de persistance visuelle humaine pour afficher 
rapidement les caractères de chaque segment en boucle, créant ainsi des 
chaînes continues.

Par exemple, lorsque "1234" est affiché, le chiffre "1" apparaît sur le premier 
segment, tandis que "234" ne sont pas visibles. Après un certain temps, le second 
segment affiche "2", et les 1er, 3e, et 4e segments ne montrent rien. Ce processus 
continue ainsi de suite, chaque segment affichant à son tour. Cette rotation est 
très rapide (environ 5 ms), et grâce à l'effet de rémanence optique et au principe 
de persistance visuelle, nous percevons les quatre chiffres simultanément.

|img_4-digit-sche-ca| 

**Codes d'affichage** 

Pour vous aider à comprendre comment les afficheurs 7 segments (cathode commune) affichent les nombres, nous avons créé le tableau suivant. Les "Numbers" correspondent aux chiffres 0-F affichés sur l'afficheur ; (DP) GFEDCBA représente les LED correspondantes réglées sur 0 ou 1. Par exemple, 00111111 signifie que DP et G sont réglés sur 0, tandis que les autres sont sur 1. Ainsi, le chiffre 0 est affiché sur l'afficheur, et le code hexadécimal correspondant est affiché sous "Hex Code".

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

**Exemples**

* :ref:`py_74hc_4dig` (pour les utilisateurs de MicroPython)
* :ref:`py_passage_counter` (pour les utilisateurs de MicroPython)
* :ref:`py_10_second` (pour les utilisateurs de MicroPython)
* :ref:`py_traffic_light` (pour les utilisateurs de MicroPython)
* :ref:`ar_74hc_4dig` (pour les utilisateurs d'Arduino)
