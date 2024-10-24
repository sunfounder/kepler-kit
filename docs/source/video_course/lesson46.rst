.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez au cœur de l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Aperçus exclusifs** : Recevez en avant-première les annonces de nouveaux produits et des avant-goûts exclusifs.
    - **Réductions spéciales** : Bénéficiez de remises exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Leçon 46 : Construire un inclinomètre à 2 axes avec affichage utilisant le MPU6050
======================================================================================

Ce tutoriel explique comment utiliser le capteur MPU6050 avec le Raspberry Pi Pico W pour créer un inclinomètre à deux axes :

* **Configuration** : Connectez le MPU6050 et l'OLED 1306 au Raspberry Pi Pico W.
* **Concept** : Mesurez l'inclinaison en utilisant les angles de tangage (pitch) et de roulis (roll), et affichez un niveau à bulle sur l'OLED.
* **Équations** : 
   - Tangage : \(\arctan\left(\frac{Y}{Z}\right)\)
   - Roulis : \(\arctan\left(\frac{X}{Z}\right)\)
   - Convertissez les radians en degrés.
* **Code** : Configurez les bibliothèques, mesurez les accélérations X, Y, Z, calculez les angles et affichez-les sur l'OLED.
* **Démonstration** : Testez l'inclinaison et ajustez le mouvement de la bulle pour plus de réactivité.
* **Avancé** : Stabilisez les lectures d'inclinaison pour éviter les erreurs dues aux accélérations ou aux vibrations.

**Vidéo**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/wYv39RMwXvU?si=6gJoFFIa1HSdGIFt" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
