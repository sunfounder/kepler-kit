.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Avant-premières exclusives** : Profitez d'un accès anticipé aux annonces de nouveaux produits et aux aperçus en avant-première.
    - **Remises spéciales** : Bénéficiez de réductions exclusives sur nos nouveaux produits.
    - **Promotions et cadeaux festifs** : Participez à des promotions spéciales et à des tirages au sort pour les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _cpn_pir:

Module Capteur de Mouvement PIR
==================================

|img_pir|

Le capteur PIR détecte le rayonnement infrarouge thermique, ce qui permet de repérer la présence d'organismes émettant ce type de rayonnement.

Le capteur PIR est divisé en deux fentes connectées à un amplificateur différentiel. Lorsqu'un objet stationnaire se trouve devant le capteur, les deux fentes reçoivent la même quantité de rayonnement et la sortie est nulle. En revanche, lorsqu'un objet en mouvement se trouve devant le capteur, l'une des fentes reçoit plus de rayonnement que l'autre, ce qui fait fluctuer la sortie, soit vers le haut, soit vers le bas. Ce changement de tension de sortie résulte de la détection du mouvement.

|img_PIR_working_principle|

Après avoir câblé le module de détection, une phase d'initialisation d'une minute est nécessaire. Pendant cette phase, le module peut émettre une sortie de 0 à 3 fois par intervalles. Ensuite, il se met en mode veille. Veuillez éloigner les sources de lumière et autres sources de perturbation de la surface du module afin d'éviter des déclenchements intempestifs dus aux signaux d'interférence. Il est également préférable d'utiliser le module dans un environnement sans trop de vent, car celui-ci peut aussi interférer avec le capteur.

|img_pir_back|

**Réglage de la distance**

En tournant le bouton du potentiomètre de réglage de la distance dans le sens horaire, la portée de détection augmente, avec une distance maximale d'environ 0 à 7 mètres. En le tournant dans le sens antihoraire, la portée de détection diminue, avec une distance minimale d'environ 0 à 3 mètres.

**Réglage du délai**

Tournez le bouton du potentiomètre de réglage du délai dans le sens horaire pour augmenter le délai de détection. Le délai maximal peut atteindre 300 secondes. À l'inverse, en tournant dans le sens antihoraire, vous pouvez réduire le délai à un minimum de 5 secondes.

**Deux modes de déclenchement**

Choisissez différents modes à l'aide du cavalier.

* **H** : Mode de déclenchement répétable. Après détection d'un corps humain, le module émet un signal de niveau haut. Pendant la période de délai, si quelqu'un entre dans la zone de détection, la sortie reste à un niveau haut.
* **L** : Mode de déclenchement non répétable. Le module émet un signal de niveau haut lorsqu'il détecte un corps humain. Après le délai, la sortie passe automatiquement de niveau haut à niveau bas.

.. Exemple
.. -------------------

.. :ref:`Intruder Alarm`


**Exemple**

* :ref:`py_pir` (pour les utilisateurs de MicroPython)
* :ref:`py_passage_counter` (pour les utilisateurs de MicroPython)
* :ref:`ar_pir` (pour les utilisateurs d'Arduino)
* :ref:`per_lucky_cat` (pour les utilisateurs de Piper Make)
