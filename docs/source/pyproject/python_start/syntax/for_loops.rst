.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans le monde des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes post-achat et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions spéciales durant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _syntax_forloop:

Boucles For
===============

La boucle ``for`` peut parcourir n'importe quelle séquence d'éléments, comme une liste ou une chaîne de caractères.

Le format de la syntaxe de la boucle for est le suivant :

.. code-block:: python

    for val in sequence:
        Body of for


Ici, ``val`` est une variable qui reçoit la valeur de chaque élément de la séquence à chaque itération.

La boucle continue jusqu'à ce que le dernier élément de la séquence soit atteint. Utilisez l'indentation pour séparer le corps de la boucle ``for`` du reste du code.


**Organigramme de la boucle for**

.. image:: img/for_loop.png

.. code-block:: python

    numbers = [1, 2, 3, 4]
    sum = 0

    for val in numbers:
        sum = sum+val
        
    print("The sum is", sum)

>>> %Run -c $EDITOR_CONTENT
La somme est 10

L'instruction break
-------------------------

Avec l'instruction break, nous pouvons arrêter la boucle avant qu'elle ne parcoure tous les éléments :

.. code-block:: python

    numbers = [1, 2, 3, 4]
    sum = 0

    for val in numbers:
        sum = sum+val
        if sum == 6:
            break
    print("The sum is", sum)

>>> %Run -c $EDITOR_CONTENT
The sum is 6

L'instruction continue
--------------------------------------------

Avec l'instruction ``continue``, nous pouvons arrêter l'itération en cours de la boucle et passer à la suivante :

.. code-block:: python

    numbers = [1, 2, 3, 4]

    for val in numbers:
        if val == 3:
            continue
        print(val)

>>> %Run -c $EDITOR_CONTENT
1
2
4

La fonction range()
--------------------------------------------

Nous pouvons utiliser la fonction range() pour générer une séquence de nombres. range(6) produira des nombres entre 0 et 5 (6 nombres).

Il est également possible de définir un point de départ, un point d'arrêt et une taille de pas comme range(start, stop, step_size). Si non précisée, la taille du pas par défaut est de 1.

En quelque sorte, l'objet range est "paresseux" car lorsqu'on le crée, il ne génère pas tous les nombres qu'il "contient". Cependant, ce n'est pas un itérateur car il prend en charge les opérations in, len et ``__getitem__``.

Cette fonction ne stocke pas toutes les valeurs en mémoire ; ce serait inefficace. Elle se souvient du début, de la fin, de la taille du pas et génère le prochain nombre au fur et à mesure.

Pour forcer cette fonction à afficher tous les éléments, nous pouvons utiliser la fonction list().

.. code-block:: python

    print(range(6))

    print(list(range(6)))

    print(list(range(2, 6)))

    print(list(range(2, 10, 2)))

>>> %Run -c $EDITOR_CONTENT
range(0, 6)
[0, 1, 2, 3, 4, 5]
[2, 3, 4, 5]
[2, 4, 6, 8]

Nous pouvons utiliser ``range()`` dans une boucle ``for`` pour parcourir une séquence de nombres. Elle peut être combinée avec la fonction len() pour utiliser l'indice et parcourir la séquence.

.. code-block:: python

    fruits = ['pear', 'apple', 'grape']

    for i in range(len(fruits)):
        print("I like", fruits[i])
        
>>> %Run -c $EDITOR_CONTENT
I like pear
I like apple
I like grape


Else dans une boucle For
--------------------------------

La boucle ``for`` peut également comporter un bloc ``else`` optionnel. Si les éléments de la séquence utilisée pour la boucle sont épuisés, la partie ``else`` est exécutée.

Le mot-clé ``break`` peut être utilisé pour arrêter la boucle ``for``. Dans ce cas, la partie ``else`` sera ignorée.

Par conséquent, si aucune interruption ne se produit, la partie ``else`` de la boucle ``for`` sera exécutée.

.. code-block:: python

    for val in range(5):
        print(val)
    else:
        print("Finished")

>>> %Run -c $EDITOR_CONTENT
0
1
2
3
4
Finished

Le bloc else ne sera PAS exécuté si la boucle est interrompue par une instruction break.

.. code-block:: python


    for val in range(5):
        if val == 2: break
        print(val)
    else:
        print("Finished")

>>> %Run -c $EDITOR_CONTENT
0
1

