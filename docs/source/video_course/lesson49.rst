.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Approfondissez vos connaissances en Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et découvrez des avant-goûts exclusifs.
    - **Réductions spéciales** : Bénéficiez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Leçon 49 : Améliorer les performances de l'IMU avec un filtre complémentaire
=================================================================================

Ce tutoriel explique comment améliorer la précision des mesures d'inclinaison en utilisant le capteur MPU6050 avec le Raspberry Pi Pico W :

* **Configuration** : Connectez le MPU6050 au Raspberry Pi Pico W.
* **Défis** : Les accéléromètres sont sujets au bruit, tandis que les gyroscopes souffrent de dérive.
* **Solution** : Utiliser un filtre complémentaire pour combiner les données de l'accéléromètre et du gyroscope.
* **Mise en œuvre** : Calculer le roulis et le tangage, puis les combiner à l'aide d'un filtre complémentaire pour obtenir des mesures précises et avec peu de bruit.
* **Résultats** : Obtenez des mesures d'inclinaison précises, réactives, avec un minimum de bruit et de dérive.
* **Devoir** : Implémentez et affinez la méthode, en explorant des moyens d'éliminer les erreurs en régime permanent.



**Vidéo**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/CFuEokTJn5s?si=ploRdiueh3f4mQBL" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
