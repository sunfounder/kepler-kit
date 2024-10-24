.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _cpn_ultrasonic:

Module Ultrasonique
================================

|ultrasonic_pic|

* **TRIG** : Entrée du signal de déclenchement
* **ECHO** : Sortie du signal d'écho
* **GND** : Masse
* **VCC** : Alimentation 5V

Il s'agit du capteur de distance ultrasonique HC-SR04, offrant une mesure sans contact de 2 cm à 400 cm avec une précision de l'ordre de 3 mm. Le module inclut un émetteur ultrasonique, un récepteur et un circuit de contrôle.

Vous n'avez besoin de connecter que 4 broches : VCC (alimentation), Trig (déclencheur), Echo (récepteur) et GND (masse) pour l'utiliser facilement dans vos projets de mesure.

**Caractéristiques**

* Tension de fonctionnement : DC 5V
* Courant de fonctionnement : 16mA
* Fréquence de fonctionnement : 40Hz
* Portée maximale : 500 cm
* Portée minimale : 2 cm
* Signal d'entrée de déclenchement : impulsion TTL de 10µs
* Signal de sortie d'écho : signal TTL proportionnel à la distance
* Connecteur : XH2.54-4P
* Dimensions : 46 x 20,5 x 15 mm

**Principe**

Les principes de base sont les suivants :

* Utilisation du déclencheur IO pour un signal de niveau haut d'au moins 10µs.

* Le module émet une rafale de 8 cycles d'ultrasons à 40 kHz et détecte si un signal de retour est reçu.
* Echo produira un niveau haut si un signal est retourné ; la durée du niveau haut correspond au temps écoulé entre l'émission et le retour.
* Distance = (temps du niveau haut x vitesse du son (340m/s)) / 2

|ultrasonic_prin|

Formule :

* µs / 58 = distance en centimètres
* µs / 148 = distance en pouces
* distance = temps de niveau haut x vitesse (340m/s) / 2

.. note::

    Ce module ne doit pas être connecté sous tension ; si nécessaire, veillez à connecter d'abord la GND du module. Sinon, cela pourrait affecter le fonctionnement du module.

    La zone de l'objet à mesurer doit être d'au moins 0,5 mètre carré et aussi plate que possible. Sinon, les résultats risquent d'être affectés.


**Exemple**

* :ref:`py_ultrasonic` (pour les utilisateurs de MicroPython)
* :ref:`py_reversing_aid` (pour les utilisateurs de MicroPython)
* :ref:`ar_ultrasonic` (pour les utilisateurs d'Arduino)
* :ref:`per_reversing_system` (pour les utilisateurs de Piper Make)
