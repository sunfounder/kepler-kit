.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Avant-premières exclusives** : Profitez d'un accès anticipé aux annonces de nouveaux produits et aux aperçus en avant-première.
    - **Remises spéciales** : Bénéficiez de réductions exclusives sur nos nouveaux produits.
    - **Promotions et cadeaux festifs** : Participez à des promotions spéciales et à des tirages au sort pour les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _cpn_ir_receiver:

Récepteur Infrarouge
=================================

Récepteur IR
----------------------------

|img_irrecv|

* S: Signal output
* +: VCC
* -: GND

Un récepteur infrarouge est un composant qui reçoit les signaux infrarouges et peut capter indépendamment les rayons infrarouges en produisant des signaux compatibles avec le niveau TTL. Il a une taille similaire à celle d'un transistor classique en plastique et convient à tous types de télécommandes et de transmissions infrarouges.

La communication infrarouge, ou IR, est une technologie de communication sans fil populaire, économique et facile à utiliser. La lumière infrarouge possède une longueur d'onde légèrement plus longue que celle de la lumière visible, ce qui la rend imperceptible à l'œil humain - idéale pour la communication sans fil. Une méthode courante de modulation pour la communication infrarouge est la modulation à 38KHz.

* Capteur récepteur IR HX1838, haute sensibilité
* Peut être utilisé pour le contrôle à distance
* Alimentation : 3.3~5V
* Interface : Numérique
* Fréquence de modulation : 38KHz


Télécommande
-------------------------

|img_controller|

Il s'agit d'une mini télécommande infrarouge sans fil fine avec 21 boutons de fonction et une portée de transmission pouvant atteindre 8 mètres, adaptée pour commander une large gamme de dispositifs dans une chambre d'enfant.

* Taille : 85x39x6mm
* Portée de la télécommande : 8-10m
* Pile : pile bouton lithium-manganèse 3V
* Fréquence porteuse infrarouge : 38KHz
* Matériau de surface : 0.125mm PET
* Durée de vie effective : plus de 20 000 utilisations

**Exemple**

* :ref:`py_irremote` (pour les utilisateurs de MicroPython)
* :ref:`ar_irremote` (pour les utilisateurs d'Arduino)
