.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Avant-premières exclusives** : Profitez d'un accès anticipé aux annonces de nouveaux produits et aux aperçus en avant-première.
    - **Remises spéciales** : Bénéficiez de réductions exclusives sur nos nouveaux produits.
    - **Promotions et cadeaux festifs** : Participez à des promotions spéciales et à des tirages au sort pour les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _cpn_reed:

Interrupteur Reed
======================

|img_reed|

L'interrupteur Reed est un interrupteur électrique qui fonctionne par l'application d'un champ magnétique. Il a été inventé par Walter B. Ellwood des laboratoires Bell Telephone en 1936 et breveté aux États-Unis le 27 juin 1940 sous le numéro de brevet 2264746.

Le principe de fonctionnement d'un interrupteur Reed est très simple. Deux lamelles (généralement en fer et en nickel, deux métaux) qui se chevauchent aux extrémités sont scellées dans un tube en verre, avec un petit écart entre elles (d'environ quelques microns). Le tube en verre est rempli d'un gaz inerte de haute pureté (comme l'azote), et certains interrupteurs Reed sont conçus pour avoir un vide à l'intérieur afin d'améliorer leurs performances haute tension.

Les lamelles agissent comme des conducteurs de flux magnétique. Les deux lamelles ne sont pas en contact lorsqu'elles ne sont pas activées ; lorsqu'elles passent dans un champ magnétique généré par un aimant permanent ou une bobine électromagnétique, le champ appliqué induit des polarités opposées aux extrémités des lamelles. Lorsque la force magnétique dépasse la force de ressort propre aux lamelles, elles sont attirées l'une vers l'autre pour fermer le circuit ; lorsque le champ magnétique diminue ou disparaît, les lamelles se séparent grâce à leur propre élasticité, ouvrant ainsi le circuit.

|img_reed_sche|

* `Reed Switch - Wikipedia <https://en.wikipedia.org/wiki/Reed_switch>`_


**Exemple**

* :ref:`py_reed` (pour les utilisateurs de MicroPython)
* :ref:`ar_reed` (pour les utilisateurs d'Arduino)
