.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans le monde des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes post-achat et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions spéciales durant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Variables
=============
Les variables sont des conteneurs utilisés pour stocker des valeurs de données.

Créer une variable est très simple. Il suffit de lui donner un nom et de lui attribuer une valeur. Vous n'avez pas besoin de spécifier le type de données de la variable lors de l'affectation, car la variable est une référence qui accède à des objets de différents types de données via l'affectation.

Les noms de variables doivent suivre les règles suivantes :

* Les noms de variables peuvent uniquement contenir des chiffres, des lettres et des underscores.
* Le premier caractère du nom de la variable doit être une lettre ou un underscore.
* Les noms de variables sont sensibles à la casse.

Créer une Variable
---------------------
Il n'y a pas de commande pour déclarer des variables en MicroPython. Les variables sont créées lorsque vous leur attribuez une valeur pour la première fois. Il n'est pas nécessaire d'utiliser une déclaration de type spécifique, et vous pouvez même changer le type après avoir défini la variable.

.. code-block:: python

    x = 8       # x is of type int
    x = "lily" # x is now of type str
    print(x)

>>> %Run -c $EDITOR_CONTENT
lily

Conversion de Type (Casting)
------------------------------------
Si vous souhaitez spécifier le type de données pour la variable, vous pouvez le faire par conversion (casting).

.. code-block:: python

    x = int(5)    # y will be 5
    y = str(5)    # x will be '5'
    z = float(5)  # z will be 5.0
    print(x,y,z)

>>> %Run -c $EDITOR_CONTENT
5 5 5.0

Obtenir le Type
-------------------
Vous pouvez obtenir le type de données d'une variable avec la fonction `type()`.

.. code-block:: python

    x = 5
    y = "hello"
    z = 5.0
    print(type(x),type(y),type(z))

>>> %Run -c $EDITOR_CONTENT
<class 'int'> <class 'str'> <class 'float'>

Guillemets Simples ou Doubles ?
------------------------------------
En MicroPython, vous pouvez utiliser des guillemets simples ou doubles pour définir des variables de chaîne de caractères.

.. code-block:: python

    x = "hello"
    # équivaut à
    x = 'hello'

Sensibilité à la Casse
--------------------------
Les noms de variables sont sensibles à la casse.

.. code-block:: python

    a = 5
    A = "lily"
    # A ne remplacera pas a
    print(a, A)

>>> %Run -c $EDITOR_CONTENT
5 lily


