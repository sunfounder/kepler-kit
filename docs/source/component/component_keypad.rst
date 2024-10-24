.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Avant-premières exclusives** : Profitez d'un accès anticipé aux annonces de nouveaux produits et aux aperçus en avant-première.
    - **Remises spéciales** : Bénéficiez de réductions exclusives sur nos nouveaux produits.
    - **Promotions et cadeaux festifs** : Participez à des promotions spéciales et à des tirages au sort pour les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _cpn_keypad:

Clavier 4x4
========================

Dans les systèmes à microcontrôleur, lorsque l'on utilise un grand nombre de touches, comme pour un verrou électronique ou un clavier de téléphone, il y a généralement au moins 12 à 16 touches, souvent disposées en clavier matriciel.

Le clavier matriciel, aussi appelé clavier à rangées, est un clavier avec quatre lignes d'E/S en tant que lignes de rangées et quatre lignes d'E/S en tant que lignes de colonnes. Une touche est placée à chaque intersection des lignes de rangées et de colonnes, ce qui donne un clavier de 4*4. Cette structure de clavier en rangées et colonnes permet d'améliorer efficacement l'utilisation des ports d'E/S dans un système à microcontrôleur.

Les contacts de ces claviers sont accessibles via un connecteur adapté pour une connexion avec un câble ruban ou pour être insérés dans un circuit imprimé. 
Dans certains claviers, chaque bouton est connecté à un contact séparé dans le connecteur, tandis que tous les boutons partagent une masse commune.

|img_keypad|

Le plus souvent, les boutons sont codés en matrice, ce qui signifie que chacun d'eux relie une paire unique de conducteurs dans une matrice. 
Cette configuration est idéale pour être scannée par un microcontrôleur, qui peut être programmé pour envoyer une impulsion de sortie sur chacune des quatre lignes horizontales à tour de rôle. 
Pendant chaque impulsion, il vérifie les quatre lignes verticales restantes, afin de déterminer si l'une d'entre elles transmet un signal. 
Des résistances de pull-up ou de pull-down doivent être ajoutées aux fils d'entrée pour éviter que les entrées du microcontrôleur ne se comportent de manière imprévisible en l'absence de signal.

* `Keypad - Wikipedia <https://en.wikipedia.org/wiki/Keypad>`_

**Exemple**

* :ref:`py_keypad` (pour les utilisateurs de MicroPython)
* :ref:`py_guess_number` (pour les utilisateurs de MicroPython)
* :ref:`ar_keypad` (pour les utilisateurs d'Arduino)
