.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Avant-premières exclusives** : Profitez d'un accès anticipé aux annonces de nouveaux produits et aux aperçus en avant-première.
    - **Remises spéciales** : Bénéficiez de réductions exclusives sur nos nouveaux produits.
    - **Promotions et cadeaux festifs** : Participez à des promotions spéciales et à des tirages au sort pour les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _cpn_rgb:

LED RGB
=================

|img_rgb|
    
Les LEDs RGB émettent de la lumière de différentes couleurs. Une LED RGB regroupe trois LEDs - rouge, vert et bleu - dans une coque en plastique transparente ou semi-transparente. Elle peut afficher différentes couleurs en modifiant la tension d'entrée des trois broches et en les superposant, ce qui permet, selon les statistiques, de créer jusqu'à 16 777 216 couleurs différentes.

|img_rgb_light|

Les LEDs RGB peuvent être classées en anode commune et cathode commune. Dans ce kit, la cathode commune est utilisée. La **cathode commune**, ou CC, signifie que les cathodes des trois LEDs sont connectées ensemble. Une fois reliée à la masse (GND) et les trois broches branchées, la LED affichera la couleur correspondante.

Le symbole de circuit est montré ci-dessous.

|img_rgb_symbol| 

Une LED RGB possède 4 broches : la plus longue est la broche de la cathode commune, généralement connectée à la masse (GND). La broche située à gauche de la plus longue est la Rouge, et les deux broches à droite sont respectivement la Verte et la Bleue.

|img_rgb_pin|


**Caractéristiques**

* Couleur : Tri-couleur (Rouge/Vert/Bleu)
* Cathode Commune
* Lentille ronde claire de 5 mm
* Tension directe : Rouge : DC 2.0 - 2.2V ; Bleu & Vert : DC 3.0 - 3.2V (IF=20mA)
* LED RGB DIP de 0.06 Watts
* Luminosité augmentée jusqu'à +20%
* Angle de vision : 30°


.. Exemple
.. -------------------

.. :ref:`Colorful Light`


**Exemple**

* :ref:`py_rgb` (pour les utilisateurs de MicroPython)
* :ref:`py_fruit_piano` (pour les utilisateurs de MicroPython)
* :ref:`ar_rgb` (pour les utilisateurs d'Arduino)
* :ref:`per_rainbow_light` (pour les utilisateurs de Piper Make)
