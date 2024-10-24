.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Avant-premières exclusives** : Profitez d'un accès anticipé aux annonces de nouveaux produits et aux aperçus en avant-première.
    - **Remises spéciales** : Bénéficiez de réductions exclusives sur nos nouveaux produits.
    - **Promotions et cadeaux festifs** : Participez à des promotions spéciales et à des tirages au sort pour les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _cpn_servo:

Servo
===========

|img_servo|

Un servo est généralement composé des éléments suivants : boîtier, arbre, système d'engrenages, potentiomètre, moteur DC et carte embarquée.

Son fonctionnement est le suivant : le microcontrôleur envoie des signaux PWM au servo, puis la carte embarquée dans le servo reçoit ces signaux via la broche de signal et contrôle le moteur interne pour tourner. En conséquence, le moteur entraîne le système d'engrenages et fait tourner l'arbre après réduction de la vitesse. L'arbre et le potentiomètre du servo sont connectés ensemble. Lorsque l'arbre tourne, il entraîne le potentiomètre, qui envoie alors un signal de tension à la carte embarquée. Ensuite, la carte détermine la direction et la vitesse de rotation en fonction de la position actuelle, ce qui permet de s'arrêter exactement à la position définie et de s'y maintenir.

|img_servo_i|

L'angle est déterminé par la durée d'une impulsion appliquée au fil de contrôle. C'est ce qu'on appelle la modulation de largeur d'impulsion (PWM). Le servo s'attend à recevoir une impulsion toutes les 20 ms. La durée de l'impulsion détermine à quel point le moteur se déplace. Par exemple, une impulsion de 1,5 ms fait tourner le moteur à la position de 90 degrés (position neutre).
Lorsqu'une impulsion inférieure à 1,5 ms est envoyée à un servo, celui-ci tourne vers une position et maintient son arbre de sortie à un certain nombre de degrés dans le sens antihoraire à partir du point neutre. Lorsque l'impulsion est plus large que 1,5 ms, c'est l'inverse qui se produit. La largeur minimale et maximale de l'impulsion qui commande le servo à se déplacer vers une position valide dépend de chaque servo. Généralement, l'impulsion minimale est d'environ 0,5 ms et l'impulsion maximale est de 2,5 ms.

|img_servo_duty|


.. Exemple
.. -------------------

.. :ref:`Swinging Servo`

**Exemple**

* :ref:`py_servo` (pour les utilisateurs de MicroPython)
* :ref:`py_somato_controller` (pour les utilisateurs de MicroPython)
* :ref:`ar_servo` (pour les utilisateurs d'Arduino)
* :ref:`per_water_tank` (pour les utilisateurs de Piper Make)
* :ref:`per_swing_servo` (pour les utilisateurs de Piper Make)
* :ref:`per_lucky_cat` (pour les utilisateurs de Piper Make)
