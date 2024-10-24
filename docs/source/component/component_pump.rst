.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Avant-premières exclusives** : Profitez d'un accès anticipé aux annonces de nouveaux produits et aux aperçus en avant-première.
    - **Remises spéciales** : Bénéficiez de réductions exclusives sur nos nouveaux produits.
    - **Promotions et cadeaux festifs** : Participez à des promotions spéciales et à des tirages au sort pour les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _cpn_pump:

Pompe à Eau DC
================

|img_pump|

Cette pompe fonctionne essentiellement comme un moteur à courant continu, opérant à une tension de 3V et un courant de 100mA. Lorsqu'elle est alimentée, la pompe aspire l'eau par le bas de son boîtier en plastique et l'expulse par le tuyau de sortie. Elle doit toujours être immergée dans l'eau pour fonctionner correctement. Inverser la polarité ne la transformera pas en dispositif d'aspiration ; elle ne fera que pomper l'eau vers l'extérieur !

Elle est particulièrement adaptée aux débutants souhaitant créer un projet de fontaine ou d'arrosage de plantes avec cette pompe submersible, car elle est extrêmement facile à utiliser !

**Caractéristiques**

* **Plage de tension** : DC 3 ~ 4,5V
* **Courant de fonctionnement** : 120 ~ 180mA
* **Puissance** : 0,36 ~ 0,91W
* **Hauteur maximale d'eau** : 0,35 ~ 0,55M
* **Débit maximal** : 80 ~ 100 L/H
* **Durée de vie en fonctionnement continu** : 100 heures
* **Indice d'étanchéité** : IP68
* **Mode de fonctionnement** : DC, entraînement magnétique
* **Matériau** : Plastique technique
* **Diamètre extérieur de la sortie** : 7,8 mm
* **Diamètre intérieur de la sortie** : 6,5 mm
* C'est une pompe submersible et doit être utilisée en tant que telle. Elle a tendance à surchauffer si elle est allumée sans être immergée.
* Elle est fournie avec un câble mâle de 25 cm, permettant une insertion facile dans une breadboard.

**Exemple**

* :ref:`py_pump` (pour les utilisateurs de MicroPython)
* :ref:`ar_pump` (pour les utilisateurs d'Arduino)
