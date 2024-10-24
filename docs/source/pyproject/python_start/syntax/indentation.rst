.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans le monde des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes post-achat et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions spéciales durant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Indentation
=============

L'indentation fait référence aux espaces au début d'une ligne de code.
Comme les programmes Python standard, les programmes MicroPython s'exécutent généralement de haut en bas :
Ils parcourent chaque ligne à tour de rôle, l'exécutent dans l'interpréteur, puis passent à la ligne suivante,
Exactement comme si vous les tapiez ligne par ligne dans le Shell.
Un programme qui se contente de parcourir la liste des instructions ligne par ligne n'est pas très intelligent – c'est pourquoi MicroPython, tout comme Python, utilise l'indentation pour contrôler la séquence d'exécution de ses programmes.

Vous devez mettre au moins un espace avant print(), sinon un message d'erreur "Invalid syntax" apparaîtra. Il est généralement recommandé de standardiser les espaces en utilisant uniformément la touche Tab.

.. code-block:: python

    if 8 > 5:
    print("Eight is greater than Five!")

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 2
SyntaxError: invalid syntax

Vous devez utiliser le même nombre d'espaces dans le même bloc de code, sinon Python vous renverra une erreur.

.. code-block:: python

    if 8 > 5:
    print("Eight is greater than Five!")
            print("Eight is greater than Five")
            
>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 2
SyntaxError: invalid syntax
