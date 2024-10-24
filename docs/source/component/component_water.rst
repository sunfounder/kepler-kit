.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _cpn_water_level:

Module de Capteur de Niveau d'Eau
========================================

|img_water_sensor|

Le capteur de niveau d'eau transmet le signal de niveau d'eau détecté au 
contrôleur, et l'ordinateur du contrôleur compare le signal mesuré avec le 
signal de consigne pour en déduire la déviation, puis émet des commandes 
"marche" et "arrêt" à la vanne électrique d'alimentation en eau en fonction 
de la nature de la déviation pour garantir que le récipient atteigne le 
niveau d'eau réglé.

Le capteur de niveau d'eau dispose de dix pistes de cuivre exposées, cinq pour 
l'alimentation et cinq pour la détection, qui sont croisées et pontées par l'eau 
lorsqu'elles sont immergées. 
La carte de circuit imprimé dispose d'une LED d'alimentation qui s'allume lorsque la carte est sous tension.

La combinaison de ces pistes agit comme une résistance variable, modifiant la 
valeur de résistance en fonction du niveau d'eau. Plus précisément, plus le 
capteur est immergé dans l'eau, meilleure est la conductivité et plus faible 
est la résistance. À l'inverse, moins il est conducteur, plus la résistance est élevée. 
Ensuite, le capteur traite le signal de tension de sortie qui sera envoyé au 
microcontrôleur, nous permettant ainsi de déterminer le niveau d'eau.

.. warning:: 
    Le capteur ne doit pas être complètement immergé dans l'eau, veuillez laisser seulement la partie où se trouvent les dix pistes en contact avec l'eau. De plus, l'alimentation du capteur dans un environnement humide accélérera la corrosion de la sonde et réduira la durée de vie du capteur. Nous recommandons donc de ne l'alimenter que lors de la prise de mesures.


**Exemple**

* :ref:`py_water` (pour les utilisateurs de MicroPython)
* :ref:`ar_water` (pour les utilisateurs d'Arduino)
* :ref:`per_water_tank` (pour les utilisateurs de Piper Make)
