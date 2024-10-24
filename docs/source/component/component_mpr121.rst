.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Avant-premières exclusives** : Profitez d'un accès anticipé aux annonces de nouveaux produits et aux aperçus en avant-première.
    - **Remises spéciales** : Bénéficiez de réductions exclusives sur nos nouveaux produits.
    - **Promotions et cadeaux festifs** : Participez à des promotions spéciales et à des tirages au sort pour les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _cpn_mpr121:

Module MPR121
===========================

|img_mpr121|

* **3.3V** : Alimentation
* **IRQ** : Broche de sortie d'interruption à collecteur ouvert, active à l'état bas
* **SCL** : Horloge I2C
* **SDA** : Données I2C
* **ADD** : Broche de sélection d'adresse I2C. Connectez la broche ADDR à la ligne VSS, VDD, SDA ou SCL ; les adresses I2C résultantes seront respectivement 0x5A, 0x5B, 0x5C et 0x5D.
* **GND** : Masse
* **0~11** : Électrodes 0~11, chaque électrode étant un capteur tactile. En général, les électrodes peuvent simplement être un morceau de métal ou un fil. Cependant, selon la longueur du fil ou le matériau sur lequel se trouve l'électrode, cela peut rendre le déclenchement du capteur difficile. Pour cette raison, le MPR121 permet de configurer les paramètres nécessaires pour déclencher ou relâcher une électrode.

**APERÇU DU MPR121**

Le MPR121 est la deuxième génération de contrôleurs de capteurs tactiles 
capacitifs après la série initiale MPR03x. Le MPR121 se distingue par une 
intelligence interne accrue, notamment grâce à l'augmentation du nombre 
d'électrodes, une adresse I2C configurable matériellement, un système de 
filtrage élargi avec anti-rebond, et des électrodes entièrement indépendantes 
avec auto-configuration intégrée. L'appareil dispose également d'un 13ème 
canal de détection simulé dédié à la détection de proximité grâce aux entrées 
de détection multiplexées.

* `MPR121 Datasheet <https://cdn-shop.adafruit.com/datasheets/MPR121.pdf>`_

**Caractéristiques**

* Fonctionnement à faible consommation
    • Alimentation de 1,71 V à 3,6 V
    • Courant de 29 μA à un intervalle de 16 ms
    • Courant de 3 μA en mode arrêt
* 12 entrées de détection de capacité
    • 8 entrées multifonctionnelles pour le pilotage de LED et GPIO
* Détection tactile complète
    • Auto-configuration pour chaque entrée de détection
    • Auto-calibration pour chaque entrée de détection
    • Seuils de toucher/retrait et anti-rebond pour la détection tactile
* Interface I2C avec sortie d'interruption
* Boîtier QFN 3 mm x 3 mm x 0,65 mm à 20 broches
* Plage de température de fonctionnement : -40°C à +85°C

**Exemple**

* :ref:`py_mpr121` (pour les utilisateurs de MicroPython)
* :ref:`py_fruit_piano` (pour les utilisateurs de MicroPython)
* :ref:`ar_mpr121` (pour les utilisateurs d'Arduino)
