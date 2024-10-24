.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Avant-premières exclusives** : Profitez d'un accès anticipé aux annonces de nouveaux produits et aux aperçus en avant-première.
    - **Remises spéciales** : Bénéficiez de réductions exclusives sur nos nouveaux produits.
    - **Promotions et cadeaux festifs** : Participez à des promotions spéciales et à des tirages au sort pour les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _cpn_motor:

Moteur à courant continu (DC)
===============================
|img_dc_motor|

Il s'agit d'un moteur à courant continu de 3V. Lorsque vous appliquez un niveau haut et un niveau bas aux deux bornes, il commence à tourner.

* **Dimensions** : 25*20*15 mm
* **Tension de fonctionnement** : 1-6V
* **Courant à vide** (3V) : 70mA
* **Vitesse à vide** (3V) : 13000 tr/min
* **Courant de blocage** (3V) : 800mA
* **Diamètre de l'arbre** : 2mm

Le moteur à courant continu (DC) est un actionneur continu qui convertit l'énergie électrique en énergie mécanique. Les moteurs DC font fonctionner des pompes rotatives, ventilateurs, compresseurs, turbines et autres dispositifs en produisant une rotation angulaire continue.

Un moteur DC se compose de deux parties : la partie fixe du moteur appelée **stator**, et la partie interne appelée **rotor** (ou **induit** pour un moteur DC) qui tourne pour produire le mouvement.
La clé pour générer du mouvement réside dans le positionnement de l'induit au sein du champ magnétique de l'aimant permanent (dont le champ s'étend du pôle nord au pôle sud). L'interaction entre le champ magnétique et les particules chargées en mouvement (le fil traversé par un courant génère le champ magnétique) produit le couple qui fait tourner l'induit.

|img_dc_motor_sche|

Le courant circule de la borne positive de la batterie à travers le circuit, passe par les balais en cuivre vers le collecteur, puis vers l'induit.
Cependant, en raison des deux interruptions sur le collecteur, ce flux de courant s'inverse à mi-parcours de chaque rotation complète.
Cette inversion continue permet essentiellement de convertir l'alimentation DC de la batterie en AC, permettant à l'induit de recevoir le couple dans la bonne direction et au bon moment pour maintenir la rotation.

* `DC Motor - MagLab <https://nationalmaglab.org/education/magnet-academy/watch-play/interactive/dc-motor>`_
* `Fleming's left-hand rule for motors - Wikipedia <https://en.wikipedia.org/wiki/Fleming%27s_left-hand_rule_for_motors>`_



**Exemple**

* :ref:`py_motor` (pour les utilisateurs de MicroPython)
* :ref:`ar_motor` (pour les utilisateurs d'Arduino)
* :ref:`per_smart_fan` (pour les utilisateurs de Piper Make)
