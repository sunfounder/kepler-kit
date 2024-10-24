.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Avant-premières exclusives** : Profitez d'un accès anticipé aux annonces de nouveaux produits et aux aperçus en avant-première.
    - **Remises spéciales** : Bénéficiez de réductions exclusives sur nos nouveaux produits.
    - **Promotions et cadeaux festifs** : Participez à des promotions spéciales et à des tirages au sort pour les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _cpn_joystick:

Module Joystick
=======================

|img_joystick_pic|

Le principe de base d'un joystick est de traduire le mouvement d'un manche en informations électroniques qu'un ordinateur peut traiter.

Pour communiquer une gamme complète de mouvements à l'ordinateur, 
un joystick doit mesurer la position du manche sur deux axes – l'axe X (de gauche à droite) et l'axe Y (de haut en bas). 
Comme en géométrie de base, les coordonnées X-Y permettent de localiser précisément la position du manche.

Pour déterminer la position du manche, le système de contrôle du joystick surveille simplement la position de chaque axe. 
Le design conventionnel d'un joystick analogique utilise deux potentiomètres, ou résistances variables, pour cette tâche.

Le joystick possède également une entrée numérique qui est activée lorsque le manche est enfoncé.

|img_joystick|


*  `Joystick - Wikipedia <https://en.wikipedia.org/wiki/Analog_stick>`_


**Exemple**


* :ref:`py_joystick` (pour les utilisateurs de MicroPython)
* :ref:`ar_joystick` (pour les utilisateurs d'Arduino)
