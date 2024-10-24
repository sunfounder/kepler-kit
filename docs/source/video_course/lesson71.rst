.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux nouvelles annonces de produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et des promotions pendant les périodes festives.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Leçon 71 : Permettre au Thread de terminer la tâche avant l'arrêt
===================================================================================

Ce tutoriel explique comment terminer proprement un programme multi-threadé sur le Raspberry Pi Pico W :

* **Configuration des connexions** : Connectez le contrôle du servo au GPIO 17, l'alimentation au pin 40, et la masse au pin 38. Connectez le bouton au GPIO 16 et à la masse.
* **Implémentation du code** : Importez ``machine``, ``time``, ``_thread``, ``Servo``. Configurez les broches pour le bouton et le servo. Implémentez un interrupteur pour contrôler le mouvement du servo, en utilisant le multi-threading pour assurer une sortie propre.
* **Gestion d'une terminaison propre** : Utilisez une variable globale ``running`` pour gérer l'exécution de la boucle. Implémentez un verrou pour contrôler les sections critiques. Assurez-vous que le servo termine son mouvement avant l'arrêt du programme.
* **Devoir** : Modifiez le programme pour gérer plus de composants ou de capteurs, en garantissant une terminaison propre dans tous les cas.

**Vidéo**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/Xm3chr1-hkY?si=ITIUvlqKF6UdOsq2" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
