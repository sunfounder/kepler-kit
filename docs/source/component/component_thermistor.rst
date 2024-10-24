.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _cpn_thermistor:

Thermistance
===============

|img_thermistor|

Une thermistance est un type de résistance dont la valeur de résistance dépend fortement de la température, bien plus que dans les résistances standard. Le mot "thermistance" est une combinaison de "thermique" et "résistance". Les thermistances sont largement utilisées comme limiteurs de courant d'appel, capteurs de température (de type NTC à coefficient de température négatif, typiquement), protecteurs contre les surintensités réinitialisables et éléments chauffants autorégulants (de type PTC à coefficient de température positif, typiquement).

* `Thermistor - Wikipedia <https://en.wikipedia.org/wiki/Thermistor>`_

Voici le symbole électronique de la thermistance.

|img_thermistor_symbol|

Les thermistances se déclinent en deux types fondamentaux opposés :

* Avec les thermistances NTC, la résistance diminue à mesure que la température augmente, généralement en raison d'une augmentation des électrons de conduction activés par l'agitation thermique à partir de la bande de valence. Un NTC est couramment utilisé comme capteur de température, ou en série avec un circuit comme limiteur de courant d'appel.
* Avec les thermistances PTC, la résistance augmente à mesure que la température augmente, généralement en raison d'agitations thermiques accrues dans le réseau cristallin, notamment celles des impuretés et des imperfections. Les thermistances PTC sont couramment installées en série avec un circuit, et utilisées pour protéger contre les conditions de surintensité, comme des fusibles réarmables.

Dans ce kit, nous utilisons une thermistance de type NTC. Chaque thermistance a une résistance nominale. Ici, elle est de 10k ohms, mesurée à 25 degrés Celsius.

Voici la relation entre la résistance et la température :

    RT = RN * expB(1/TK - 1/TN)   

* **RT** est la résistance de la thermistance NTC lorsque la température est TK. 
* **RN** est la résistance de la thermistance NTC à la température nominale TN. Ici, la valeur numérique de RN est de 10k.
* **TK** est une température en Kelvin, l'unité est K. Ici, la valeur numérique de TK est 273,15 + degrés Celsius.
* **TN** est une température nominale en Kelvin ; l'unité est également K. Ici, la valeur numérique de TN est 273,15 + 25.
* Et **B (bêta)**, la constante du matériau de la thermistance NTC, est aussi appelée indice de sensibilité thermique, avec une valeur numérique de 3950.
* **exp** est l'abréviation d'exponentiel, et le nombre de base e est un nombre naturel, environ égal à 2,7.

Convertissez cette formule TK=1/(ln(RT/RN)/B+1/TN) pour obtenir la température en Kelvin, dont vous soustrayez 273,15 pour obtenir la température en degrés Celsius.

Cette relation est une formule empirique. Elle est précise uniquement lorsque la température et la résistance sont dans la plage effective.

.. Exemple
.. -------------------

.. :ref:`Thermomètre`


**Exemple**

* :ref:`py_temp` (pour les utilisateurs de MicroPython)
* :ref:`py_room_temp` (pour les utilisateurs de MicroPython)
* :ref:`ar_temp` (pour les utilisateurs d'Arduino)
