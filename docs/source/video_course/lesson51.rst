.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Approfondissez vos connaissances en Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et promotions spéciales durant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Leçon 51 : Le gadget ultime pour mesurer le tangage et le roulis avec le MPU6050
====================================================================================

Ce tutoriel explique comment créer un inclinomètre précis à l'aide du capteur MPU6050 et du Raspberry Pi Pico W :

* **Configuration** : Connectez le MPU6050 et l'écran OLED 1306 au Raspberry Pi Pico W.
* **Défis** : Les données de l'accéléromètre sont bruitées et celles du gyroscope dérivent avec le temps.
* **Solution** : Utiliser un filtre complémentaire pour combiner les données de l'accéléromètre et du gyroscope, avec correction des erreurs de l'état stable.
* **Mise en œuvre** : Initialisez les capteurs et l'écran OLED. Collectez et filtrez les données, en affichant l'inclinaison à la fois sous forme de niveau à bulle et en degrés sur l'écran OLED.
* **Démonstration** : Testez pour obtenir des mesures stables de tangage et de roulis, avec une alimentation portable par batterie.
* **Améliorations supplémentaires** : Envisagez un suivi sans fil ou la création d'un boîtier imprimé en 3D pour plus de portabilité.

**Vidéo**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/afQyZl2hkd0?si=4Dg4Uvr5yVC4f60Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
