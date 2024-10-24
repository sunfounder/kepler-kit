.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Avant-premières exclusives** : Profitez d'un accès anticipé aux annonces de nouveaux produits et aux aperçus en avant-première.
    - **Remises spéciales** : Bénéficiez de réductions exclusives sur nos nouveaux produits.
    - **Promotions et cadeaux festifs** : Participez à des promotions spéciales et à des tirages au sort pour les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _cpn_potentiometer:

Potentiomètre
==================

|img_pot|

Le potentiomètre est également un composant de résistance à trois bornes dont la valeur de résistance peut être ajustée en fonction d'une variation régulière.

Les potentiomètres existent sous différentes formes, tailles et valeurs, mais ils ont tous les points communs suivants :

* Ils possèdent trois bornes (ou points de connexion).
* Ils ont un bouton, une vis ou un curseur qui peut être déplacé pour faire varier la résistance entre la borne centrale et l'une des bornes extérieures.
* La résistance entre la borne centrale et l'une des bornes extérieures varie de 0 Ω à la résistance maximale du potentiomètre lorsque le bouton, la vis ou le curseur est déplacé.

Voici le symbole de circuit du potentiomètre.

|img_pot_symbol|


Les fonctions du potentiomètre dans le circuit sont les suivantes :

#. Servir de diviseur de tension

    Le potentiomètre est une résistance réglable en continu. Lorsque vous ajustez l'arbre ou la poignée coulissante du potentiomètre, le contact mobile glisse sur la résistance. À ce moment-là, une tension peut être délivrée en fonction de la tension appliquée au potentiomètre et de l'angle de rotation du bras mobile ou de la course qu'il a parcourue.

#. Servir de rhéostat

    Lorsqu'il est utilisé comme rhéostat, connectez la broche centrale et l'une des deux autres broches au circuit. Vous obtiendrez ainsi une valeur de résistance qui varie de manière fluide et continue sur toute la course du contact mobile.

#. Servir de contrôleur de courant

    Lorsqu'il agit comme contrôleur de courant, la borne de contact coulissant doit être connectée comme l'une des bornes de sortie.

Pour en savoir plus sur les potentiomètres, consultez : `Potentiometer - Wikipedia <https://en.wikipedia.org/wiki/Potentiometer.>`_

.. Exemple
.. -------------------

.. * :ref:`Turn the Knob` (pour les utilisateurs de MicroPython)
.. * :ref:`Table Lamp` (pour les utilisateurs de C/C++(Arduino))


**Exemple**

* :ref:`py_pot` (pour les utilisateurs de MicroPython)
* :ref:`ar_pot` (pour les utilisateurs d'Arduino)
* :ref:`per_swing_servo` (pour les utilisateurs de Piper Make)
