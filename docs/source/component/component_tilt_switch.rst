.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _cpn_tilt:

Interrupteur à Inclinaison
=============================

|img_tilt| 

L'interrupteur à inclinaison utilisé ici est un modèle à bille avec une petite bille métallique à l'intérieur. Il est conçu pour détecter de légères inclinaisons.

Le principe est très simple. Lorsque l'interrupteur est incliné à un certain angle, la bille à l'intérieur roule et touche les deux contacts reliés aux broches extérieures, déclenchant ainsi les circuits. Sinon, la bille reste éloignée des contacts, interrompant ainsi les circuits.

|img_tilt_symbol|

* `SW520D Tilt Switch Datasheet <https://www.tme.com/Document/f1e6cedd8cb7feeb250b353b6213ec6c/SW-520D.pdf>`_

.. * :ref:`Lecture de la valeur du bouton`


**Exemple**

* :ref:`py_tilt` (pour les utilisateurs de MicroPython)
* :ref:`py_10_second` (pour les utilisateurs de MicroPython)
* :ref:`ar_tilt` (pour les utilisateurs d'Arduino)
* :ref:`per_flowing_leds` (pour les utilisateurs de Piper Make)
