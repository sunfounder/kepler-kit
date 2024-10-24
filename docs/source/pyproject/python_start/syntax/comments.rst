.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans le monde des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes post-achat et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions spéciales durant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Commentaires
================

Les commentaires dans le code nous aident à comprendre le fonctionnement, rendent l'ensemble du code plus lisible et permettent de désactiver une partie du code lors des tests, pour que cette partie ne soit pas exécutée.

Commentaire sur une seule ligne
---------------------------------------

Les commentaires sur une seule ligne en MicroPython commencent par #, et le texte qui suit est considéré comme un commentaire jusqu'à la fin de la ligne. Les commentaires peuvent être placés avant ou après le code.

.. code-block:: python

    print("hello world") # Ceci est un commentaire

>>> %Run -c $EDITOR_CONTENT
hello world

Les commentaires ne sont pas nécessairement du texte explicatif. Vous pouvez également commenter une partie du code pour empêcher MicroPython de l'exécuter.

.. code-block:: python

    #print("Ne peut pas être exécuté！")
    print("hello world") # Ceci est un commentaire

>>> %Run -c $EDITOR_CONTENT
hello world

Commentaire sur plusieurs lignes
-------------------------------------

Si vous souhaitez ajouter des commentaires sur plusieurs lignes, vous pouvez utiliser plusieurs signes #.

.. code-block:: python

    # Ceci est un commentaire
    # écrit sur
    # plusieurs lignes
    print("Hello, World!")

>>> %Run -c $EDITOR_CONTENT
Hello, World!

Ou bien, vous pouvez utiliser des chaînes de caractères multi-lignes à la place.

Comme MicroPython ignore les littéraux de chaîne qui ne sont pas affectés à des variables, vous pouvez ajouter des chaînes de caractères multi-lignes (guillemets triples) au code pour y inclure des commentaires :

.. code-block:: python

    """
    This is a comment
    written in
    more than just one line
    """
    print("Hello, World!")

>>> %Run -c $EDITOR_CONTENT
Hello, World!

Tant que la chaîne n'est pas affectée à une variable, MicroPython l'ignorera après avoir lu le code et la traitera comme un commentaire multi-ligne.

