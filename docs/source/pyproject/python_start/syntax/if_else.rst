.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans le monde des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes post-achat et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions spéciales durant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

If Else
=============

La prise de décision est nécessaire lorsque nous voulons exécuter un code uniquement si une certaine condition est remplie.

if
--------------------
.. code-block:: python

    if test expression:
        statement(s)

Ici, le programme évalue l'``expression de test`` et exécute l'``instruction`` uniquement lorsque l'``expression de test`` est True.

Si l'``expression de test`` est False, alors les ``instruction(s)`` ne seront pas exécutées.

En MicroPython, l'indentation définit le corps de l'instruction ``if``. Le corps commence avec une indentation et se termine à la première ligne non indentée.

Python interprète les valeurs non nulles comme "True". None et 0 sont interprétés comme "False".

**Organigramme de l'instruction if**

.. image:: img/if_statement.png

**Exemple**

.. code-block:: python

    num = 8
    if num > 0:
        print(num, "is a positive number.")
    print("End with this line")

>>> %Run -c $EDITOR_CONTENT
8 is a positive number.
End with this line



if...else
-----------------------

.. code-block:: python

    if test expression:
        Body of if
    else:
        Body of else

L'instruction ``if..else`` évalue l'``expression de test`` et exécutera le corps du ``if`` uniquement lorsque la condition est ``True``.

Si la condition est ``False``, le corps du ``else`` est exécuté. L'indentation est utilisée pour séparer les blocs.

**Organigramme de l'instruction if...else**

.. image:: img/if_else.png

**Exemple**

.. code-block:: python

    num = -8
    if num > 0:
        print(num, "is a positive number.")
    else:
        print(num, "is a negative number.")

>>> %Run -c $EDITOR_CONTENT
-8 is a negative number.



if...elif...else
--------------------

.. code-block:: python

    if test expression:
        Body of if
    elif test expression:
        Body of elif
    else: 
        Body of else

``Elif`` est l'abréviation de ``else if``. Il permet de vérifier plusieurs expressions.

Si la condition du ``if`` est False, la condition du bloc elif suivant est vérifiée, et ainsi de suite.

Si toutes les conditions sont ``False``, le corps du ``else`` est exécuté.

Un seul des blocs ``if...elif...else`` est exécuté en fonction des conditions.

Le bloc ``if`` ne peut avoir qu'un seul ``else``. Mais il peut avoir plusieurs ``elif``.

**Organigramme de l'instruction if...elif...else**

.. image:: img/if_elif_else.png

**Exemple**

.. code-block:: python

    x = 10
    y = 9

    if x > y:
        print("x is greater than y")
    elif x == y:
        print("x and y are equal")
    else:
        print("x is greater than y")

>>> %Run -c $EDITOR_CONTENT
x is greater than y


If imbriqué
---------------------

Nous pouvons imbriquer une instruction if dans une autre, ce que l'on appelle alors un if imbriqué.

**Exemple**

.. code-block:: python

    x = 67

    if x > 10:
        print("Above ten,")
        if x > 20:
            print("and also above 20!")
        else:
            print("but not above 20.")

>>> %Run -c $EDITOR_CONTENT
Above ten,
and also above 20!