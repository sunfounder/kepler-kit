.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Avant-premières exclusives** : Profitez d'un accès anticipé aux annonces de nouveaux produits et aux aperçus en avant-première.
    - **Remises spéciales** : Bénéficiez de réductions exclusives sur nos nouveaux produits.
    - **Promotions et cadeaux festifs** : Participez à des promotions spéciales et à des tirages au sort pour les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _cpn_mpu6050:

Module MPU6050
===========================

**MPU6050**

|img_mpu6050|

Le MPU-6050 est un dispositif de suivi de mouvement à 6 axes (combinant un 
gyroscope à 3 axes et un accéléromètre à 3 axes).

Ses trois systèmes de coordonnées sont définis comme suit :

Placez le MPU6050 à plat sur une table, en veillant à ce que la face avec 
l'étiquette soit orientée vers le haut et qu'un point sur cette surface soit 
dans le coin supérieur gauche. La direction verticale ascendante correspond 
alors à l'axe Z du composant. La direction de gauche à droite est considérée 
comme l'axe X. Par conséquent, la direction de l'arrière vers l'avant est 
définie comme l'axe Y.

|img_mpu6050_a| 

**Accéléromètre 3 axes**

L'accéléromètre fonctionne selon le principe de l'effet piézoélectrique, 
c'est-à-dire la capacité de certains matériaux à générer une charge 
électrique en réponse à une contrainte mécanique appliquée.

Imaginez ici un boîtier cuboïde avec une petite bille à l'intérieur, comme 
sur l'image ci-dessus. Les parois de ce boîtier sont faites de cristaux 
piézoélectriques. Chaque fois que vous inclinez le boîtier, la bille est 
forcée de se déplacer dans la direction de l'inclinaison, en raison de la 
gravité. La paroi avec laquelle la bille entre en collision crée de petits 
courants piézoélectriques. Il y a trois paires de parois opposées dans le 
cuboïde. Chaque paire correspond à un axe dans l'espace 3D : X, Y et Z. En 
fonction du courant produit par les parois piézoélectriques, on peut déterminer 
la direction et l'intensité de l'inclinaison.

|img_mpu6050_a2|

Nous pouvons utiliser le MPU6050 pour détecter son accélération sur chaque 
axe de coordonnées (à l'état stationnaire, l'accélération de l'axe Z est de 
1 unité de gravité, et celle des axes X et Y est de 0). Si le module est 
incliné ou dans un état de pesanteur/normale, la lecture correspondante changera.

Il existe quatre types de plages de mesure pouvant être sélectionnés par 
programmation : +/-2g, +/-4g, +/-8g, et +/-16g (par défaut à 2g) correspondant 
à chaque précision. Les valeurs varient de -32768 à 32767.

La lecture de l'accéléromètre est convertie en valeur d'accélération en 
mappant la lecture à la plage de mesure.

Accélération = (Donnée brute de l'axe de l'accéléromètre / 65536 \* Plage 
d'accélération complète) g

Prenons l'axe X comme exemple, lorsque la donnée brute de l'axe X de 
l'accéléromètre est de 16384 et que la plage est définie à +/-2g :

**Accélération sur l'axe X = (16384 / 65536 \* 4) g = 1g**

**Gyroscope 3 axes**

Les gyroscopes fonctionnent sur le principe de l'accélération de Coriolis. 
Imaginez une structure en forme de fourche, en mouvement constant d'avant en 
arrière. Elle est maintenue en place par des cristaux piézoélectriques. 
Lorsque vous essayez d'incliner cette configuration, les cristaux ressentent 
une force dans la direction de l'inclinaison, causée par l'inertie de la 
fourche en mouvement. Les cristaux produisent ainsi un courant, amplifié 
selon l'effet piézoélectrique.

|img_mpu6050_g|

Le gyroscope dispose également de quatre plages de mesure : +/-250, +/-500, 
+/-1000, et +/-2000. La méthode de calcul et l'accélération sont essentiellement 
cohérentes.

La formule pour convertir la lecture en vitesse angulaire est la suivante :

Vitesse angulaire = (Donnée brute de l'axe du gyroscope / 65536 \* Plage complète du gyroscope) °/s

Prenons l'axe X, par exemple, avec une donnée brute de l'axe X du gyroscope 
de 16384 et une plage de +/-250°/s :

**Vitesse angulaire sur l'axe X = (16384 / 65536 \* 500)°/s = 125°/s**

**Exemple**

* :ref:`py_mpu6050` (pour les utilisateurs de MicroPython)
* :ref:`py_somato_controller` (pour les utilisateurs de MicroPython)
* :ref:`py_bubble_level` (pour les utilisateurs de MicroPython)
* :ref:`ar_mpu6050` (pour les utilisateurs d'Arduino)
