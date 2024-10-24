.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez au cœur de l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Aperçus exclusifs** : Recevez en avant-première les annonces de nouveaux produits et des aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Leçon 48 : Mesurer la rotation avec les gyroscopes du MPU6050
=============================================================================

Ce tutoriel explique comment utiliser le capteur MPU6050 avec le Raspberry Pi Pico W pour créer un inclinomètre stable en combinant les données de l'accéléromètre et du gyroscope :

* **Configuration** : Connectez le MPU6050 au Raspberry Pi Pico W.
* **Concept** : Mesurez l'inclinaison en utilisant les données de l'accéléromètre et du gyroscope, en traitant le bruit et la dérive.
* **Filtre passe-bas** : Appliquez un filtre pour lisser les données de l'accéléromètre et réduire le bruit.
* **Intégration du gyroscope** : Utilisez la vitesse de rotation pour calculer et mettre à jour le tangage, le roulis et le lacet.
* **Combinaison des données** : Fusionnez les données de l'accéléromètre et du gyroscope pour minimiser les erreurs.
* **Devoir** : Implémentez et peaufinez la méthode pour obtenir une mesure d'inclinaison stable.

**Vidéo**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/XZIJasvCB44?si=hx0Ulyd0pTnro8sd" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
