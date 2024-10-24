.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Avant-premières exclusives** : Profitez d'un accès anticipé aux annonces de nouveaux produits et aux aperçus en avant-première.
    - **Remises spéciales** : Bénéficiez de réductions exclusives sur nos nouveaux produits.
    - **Promotions et cadeaux festifs** : Participez à des promotions spéciales et à des tirages au sort pour les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _cpn_74hc595:

74HC595
===========

|img_74hc595|

Le 74HC595 est composé d'un registre à décalage 8 bits et d'un registre de stockage avec des sorties parallèles à trois états. Il permet de convertir une entrée série en sortie parallèle afin d'économiser les ports d'E/S d'un microcontrôleur.

* Lorsque MR (broche 10) est à un niveau haut et que OE (broche 13) est à un niveau bas, les données sont entrées sur le front montant de SHcp et passent au registre mémoire via le front montant de SHcp.
* Si les deux horloges sont connectées ensemble, le registre à décalage a toujours une impulsion d'avance par rapport au registre mémoire.
* Le registre mémoire dispose d'une broche d'entrée série (Ds), d'une broche de sortie série (Q) et d'un bouton de réinitialisation asynchrone (niveau bas).
* Le registre mémoire offre une sortie parallèle 8 bits en trois états.
* Lorsque OE est activé (niveau bas), les données du registre mémoire sont transférées sur le bus (Q0 ~ Q7).

* `74HC595 Datasheet <https://www.ti.com/lit/ds/symlink/cd74hc595.pdf?ts=1617341564801>`_

|img_74jc595_pin|

Broches du 74HC595 et leurs fonctions :

* **Q0-Q7** : Broches de sortie de données parallèles 8 bits, capables de contrôler directement 8 LEDs ou 8 broches d'un afficheur 7 segments.
* **Q7'** : Broche de sortie série, connectée à DS d'un autre 74HC595 pour enchaîner plusieurs 74HC595 en série.
* **MR** : Broche de réinitialisation, active à niveau bas ;
* **SHcp** : Entrée d'horloge du registre à décalage. Sur le front montant, les données du registre à décalage se décalent successivement d'un bit, c'est-à-dire que les données de Q1 se déplacent vers Q2, et ainsi de suite. Sur le front descendant, les données restent inchangées.
* **STcp** : Entrée d'horloge du registre de stockage. Sur le front montant, les données du registre à décalage sont transférées dans le registre mémoire.
* **CE** : Broche d'activation de la sortie, active à niveau bas.
* **DS** : Broche d'entrée de données série.
* **VCC** : Tension d'alimentation positive.
* **GND** : Masse.

.. Example
.. -------------------

.. :ref:`Microchip - :ref:`cpn_74hc595``

**Exemple**

* :ref:`py_74hc_led` (pour les utilisateurs de MicroPython)
* :ref:`py_74hc_7seg` (pour les utilisateurs de MicroPython)
* :ref:`py_74hc_4dig` (pour les utilisateurs de MicroPython)
* :ref:`py_74hc_788bs` (pour les utilisateurs de MicroPython)
* :ref:`py_passage_counter` (pour les utilisateurs de MicroPython)
* :ref:`py_10_second` (pour les utilisateurs de MicroPython)
* :ref:`py_traffic_light` (pour les utilisateurs de MicroPython)
* :ref:`py_bubble_level` (pour les utilisateurs de MicroPython)
* :ref:`ar_74hc_led` (pour les utilisateurs d'Arduino)
* :ref:`ar_74hc_7seg` (pour les utilisateurs d'Arduino)
* :ref:`ar_74hc_4dig` (pour les utilisateurs d'Arduino)
* :ref:`ar_74hc_788bs` (pour les utilisateurs d'Arduino)
