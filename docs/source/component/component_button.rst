.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Avant-premières exclusives** : Profitez d'un accès anticipé aux annonces de nouveaux produits et aux aperçus en avant-première.
    - **Remises spéciales** : Bénéficiez de réductions exclusives sur nos nouveaux produits.
    - **Promotions et cadeaux festifs** : Participez à des promotions spéciales et à des tirages au sort pour les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _cpn_button:

Bouton
==========

|img_button|

Les boutons sont des composants courants utilisés pour contrôler les dispositifs électroniques. Ils servent généralement de commutateurs pour ouvrir ou fermer des circuits. Bien que les boutons existent en diverses tailles et formes, celui utilisé ici est un mini-bouton de 6 mm comme illustré sur les images ci-dessous.
La broche 1 est connectée à la broche 2 et la broche 3 à la broche 4. Vous n'avez donc qu'à relier l'une des broches 1 ou 2 à la broche 3 ou 4.

Voici la structure interne d'un bouton. Le symbole situé en bas à droite est couramment utilisé pour représenter un bouton dans les schémas électroniques.

|img_button_symbol|

Puisque la broche 1 est connectée à la broche 2, et la broche 3 à la broche 4, lorsque le bouton est enfoncé, les 4 broches se connectent, fermant ainsi le circuit.

|img_button2|

.. Examples
.. -------------------

.. :ref:`Lecture de la valeur du bouton`

**Exemple**

* :ref:`py_button` (pour les utilisateurs de MicroPython)
* :ref:`ar_button` (pour les utilisateurs d'Arduino)
* :ref:`per_button` (pour les utilisateurs de Piper Make)
* :ref:`per_rainbow_light` (pour les utilisateurs de Piper Make)
* :ref:`per_drum_kit` (pour les utilisateurs de Piper Make)
* :ref:`per_reaction_game` (pour les utilisateurs de Piper Make)
