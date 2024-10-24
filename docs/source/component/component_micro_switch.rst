.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Avant-premières exclusives** : Profitez d'un accès anticipé aux annonces de nouveaux produits et aux aperçus en avant-première.
    - **Remises spéciales** : Bénéficiez de réductions exclusives sur nos nouveaux produits.
    - **Promotions et cadeaux festifs** : Participez à des promotions spéciales et à des tirages au sort pour les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _cpn_micro_switch:

Microrupteur
========================

|img_micro_switch|

La construction d'un microrupteur est très simple. Les principales parties du commutateur sont :

|img_micro_switch2|

* 1. Poussoir (Actionneur)
* 2. Couvercle
* 3. Pièce mobile
* 4. Support
* 5. Boîtier
* 6. Borne NO : normalement ouverte
* 7. Borne NC : normalement fermée
* 8. Contact
* 9. Bras mobile

Après qu'un microrupteur entre en contact physique avec un objet, ses contacts changent de position. Le principe de fonctionnement de base est le suivant :

Lorsque le poussoir est en position relâchée ou au repos :

* Le circuit normalement fermé peut transporter du courant.
* Le circuit normalement ouvert est électriquement isolé.

Lorsque le poussoir est enfoncé ou activé :

* Le circuit normalement fermé est ouvert.
* Le circuit normalement ouvert est fermé.

|img_micro_switch1|

**Exemple**

* :ref:`py_micro` (pour les utilisateurs de MicroPython)
* :ref:`ar_micro` (pour les utilisateurs d'Arduino)
* :ref:`per_service_bell` (pour les utilisateurs de Piper Make)
