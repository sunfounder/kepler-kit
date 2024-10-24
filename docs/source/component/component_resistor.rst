.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Avant-premières exclusives** : Profitez d'un accès anticipé aux annonces de nouveaux produits et aux aperçus en avant-première.
    - **Remises spéciales** : Bénéficiez de réductions exclusives sur nos nouveaux produits.
    - **Promotions et cadeaux festifs** : Participez à des promotions spéciales et à des tirages au sort pour les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _cpn_resistor:

Résistance
============

|img_res|

Une résistance est un élément électronique capable de limiter le courant dans une branche de circuit. 
Une résistance fixe est un type de résistance dont la valeur ne peut pas être modifiée, tandis que celle d'un potentiomètre ou d'une résistance variable peut être ajustée.

Voici deux symboles de circuit généralement utilisés pour représenter une résistance. En règle générale, la valeur de la résistance est indiquée dessus. Ainsi, si vous voyez ces symboles dans un circuit, ils représentent une résistance.

|img_res_symbol|

**Ω** est l'unité de mesure de la résistance, et les unités supérieures incluent KΩ, MΩ, etc.
Leur relation est la suivante : 1 MΩ = 1000 KΩ, 1 KΩ = 1000 Ω. En général, la valeur de la résistance est indiquée sur celle-ci.

Lorsque vous utilisez une résistance, vous devez d'abord connaître sa valeur. Voici deux méthodes : vous pouvez observer les bandes colorées sur la résistance ou utiliser un multimètre pour mesurer la résistance. La première méthode est recommandée car elle est plus pratique et rapide.

|img_res_card|

Comme illustré sur la carte, chaque couleur correspond à un chiffre.

.. list-table::

   * - Noir
     - Marron
     - Rouge
     - Orange
     - Jaune
     - Vert
     - Bleu
     - Violet
     - Gris
     - Blanc
     - Or
     - Argent
   * - 0
     - 1
     - 2
     - 3
     - 4
     - 5
     - 6
     - 7
     - 8
     - 9
     - 0.1
     - 0.01

Les résistances à 4 et 5 bandes sont fréquemment utilisées, avec 4 ou 5 bandes colorées.

En général, lorsque vous avez une résistance, vous pouvez avoir du mal à déterminer par quel côté commencer pour lire les couleurs. 
Le conseil est de regarder l'espace entre la 4e et la 5e bande, qui est généralement plus large.

Ainsi, observez l'écart entre deux bandes colorées à une extrémité de la résistance ; 
s'il est plus grand que les autres écarts, alors vous pouvez lire à partir du côté opposé.

Voyons comment lire la valeur d'une résistance à 5 bandes comme illustré ci-dessous.

|img_220ohm|

Pour cette résistance, la lecture se fait de gauche à droite. 
La valeur doit être au format : 1ère bande 2ème bande 3ème bande x 10^Multiplicateur (Ω) et l'erreur tolérée est de ±Tolérance%. 
Ainsi, la valeur de cette résistance est 2 (rouge) 2 (rouge) 0 (noir) x 10^0 (noir) Ω = 220 Ω, 
et l'erreur tolérée est de ± 1% (marron).

.. list-table:: Common resistor color band
    :header-rows: 1

    * - :ref:`cpn_resistor` 
      - Code couleur  
    * - 10Ω   
      - marron noir noir argent marron
    * - 100Ω   
      - marron noir noir noir marron
    * - 220Ω 
      - rouge rouge noir noir marron
    * - 330Ω 
      - orange orange noir noir marron
    * - 1kΩ 
      - marron noir noir marron marron
    * - 2kΩ 
      - rouge noir noir marron marron
    * - 5.1kΩ 
      - vert marron noir marron marron
    * - 10kΩ 
      - marron noir noir rouge marron 
    * - 100kΩ 
      - marron noir noir orange marron 
    * - 1MΩ 
      - marron noir noir vert marron 

Vous pouvez en savoir plus sur les résistances sur Wiki : `Resistor - Wikipedia <https://en.wikipedia.org/wiki/Resistor>`_.
