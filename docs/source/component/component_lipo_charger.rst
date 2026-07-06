.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Avant-premières exclusives** : Profitez d'un accès anticipé aux annonces de nouveaux produits et aux aperçus en avant-première.
    - **Remises spéciales** : Bénéficiez de réductions exclusives sur nos nouveaux produits.
    - **Promotions et cadeaux festifs** : Participez à des promotions spéciales et à des tirages au sort pour les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _cpn_lipo_charger:

Module de chargeur Li-po
=================================================

|lipo_module|

Il s'agit d'un module de chargeur Li-po conçu pour Raspberry Pi Pico/Pico H/Pico W. Branchez simplement le module et le Pico sur la plaque de prototypage comme indiqué ci-dessous, puis connectez la batterie à l'autre extrémité, et vous êtes prêt à l'utiliser.

Lorsque vous connectez le Pico W à un ordinateur ou une prise via un câble USB, le voyant du module de chargeur Li-po s'allume, indiquant que la batterie est en charge. Lorsque vous débranchez le câble USB, le Pico W est alimenté par la batterie, ce qui permet à votre projet de continuer à fonctionner.

.. note::
    Pour certains ordinateurs de faible performance, il peut arriver que si vous branchez votre Pico W à votre ordinateur avec ce module de charge, l'ordinateur ne reconnaisse pas votre Pico W.

    La raison est qu'après le branchement, tout en chargeant la batterie, la tension du port USB est abaissée, ce qui entraîne une alimentation insuffisante pour que le Pico W soit reconnu par l'ordinateur.
    
    Dans ce cas, vous devez débrancher le module de charge Li-po puis rebrancher le Pico W.

|lipo_wire|

**Caractéristiques**

* Tension d'entrée : 5V
* Tension de sortie : 3,3V
* Taille : 20mm x 7mm
* Modèle d'interface : PH2.0
* Il y a un support de batterie 1A assorti ainsi qu'une Power Pack de 800mAh à utiliser ensemble.

**Schéma**

|sch_lipo_charger|