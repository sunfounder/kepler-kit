.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez au cœur de l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Aperçus exclusifs** : Recevez en avant-première les annonces de nouveaux produits et des aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Leçon 47 : Améliorer les données des capteurs avec un filtre passe-bas
=============================================================================

Ce tutoriel explique comment utiliser le capteur MPU6050 avec le Raspberry Pi Pico W pour créer un inclinomètre à deux axes stable en implémentant un filtre passe-bas :

* **Configuration** : Connectez le MPU6050 au Raspberry Pi Pico W.
* **Concept** : Mesurez l'inclinaison en utilisant les données de l'accéléromètre tout en corrigeant les erreurs dues à l'accélération.
* **Filtre passe-bas** : Implémentez un filtre pour lisser les données en utilisant l'équation : ``\(\text{nouvelle valeur} = \text{confiance} \times \text{mesure} + (1 - \text{confiance}) \times \text{ancienne valeur}\)``.
* **Code** : Mesurez les axes X, Y, Z, appliquez le filtre aux angles de tangage (pitch) et de roulis (roll), et affichez les résultats.
* **Devoir** : Testez le filtre passe-bas et expérimentez avec différentes valeurs de confiance.

**Vidéo**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/3YqGIg4crEk?si=rwiDFcJ98nlj_Sg3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
