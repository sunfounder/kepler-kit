.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans le monde des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes post-achat et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions spéciales durant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Types de Données
=========================

Types de Données Intégrés
-------------------------------
MicroPython dispose des types de données suivants :

* Type Texte : str
* Types Numériques : int, float, complex
* Types Séquentiels : list, tuple, range
* Type de Mappage : dict
* Types d’Ensembles : set, frozenset
* Type Booléen : bool
* Types Binaires : bytes, bytearray, memoryview

Obtenir le Type de Donnée
-----------------------------
Vous pouvez obtenir le type de donnée de n'importe quel objet en utilisant la fonction ``type()`` :

.. code-block:: python

    a = 6.8
    print(type(a))

>>> %Run -c $EDITOR_CONTENT
<class 'float'>

Définir le Type de Donnée
--------------------------------
En MicroPython, il n'est pas nécessaire de définir spécifiquement le type de donnée. Il est déterminé automatiquement lors de l'affectation d'une valeur à la variable.

.. code-block:: python

    x = "welcome"
    y = 45
    z = ["apple", "banana", "cherry"]

    print(type(x))
    print(type(y))
    print(type(z))

>>> %Run -c $EDITOR_CONTENT
<class 'str'>
<class 'int'>
<class 'list'>
>>> 

Définir un Type de Donnée Spécifique
---------------------------------------------

Si vous souhaitez spécifier un type de donnée, vous pouvez utiliser les fonctions de constructeur suivantes :

.. list-table:: 
    :widths: 25 10
    :header-rows: 1

    *   - Exemple
        - Type de Donnée
    *   - x = int(20)
        - int
    *   - x = float(20.5)
        - float
    *   - x = complex(1j)
        - complex
    *   - x = str("Hello World")
        - str
    *   - x = list(("apple", "banana", "cherry"))
        - list
    *   - x = tuple(("apple", "banana", "cherry"))
        - tuple
    *   - x = range(6)
        - range
    *   - x = dict(name="John", age=36)
        - dict
    *   - x = set(("apple", "banana", "cherry"))
        - set
    *   - x = frozenset(("apple", "banana", "cherry"))
        - frozenset
    *   - x = bool(5)
        - bool
    *   - x = bytes(5)
        - bytes
    *   - x = bytearray(5)
        - bytearray
    *   - x = memoryview(bytes(5))
        - memoryview

Vous pouvez en imprimer certains pour voir le résultat.

.. code-block:: python

    a = float(20.5)
    b = list(("apple", "banana", "cherry"))
    c = bool(5)

    print(a)
    print(b)
    print(c)

>>> %Run -c $EDITOR_CONTENT
20.5
['apple', 'banana', 'cherry']
True
>>> 

Conversion de Type
-----------------------
Vous pouvez convertir d'un type à un autre avec les méthodes int(), float(), et complex() :
Le casting en Python se fait donc en utilisant des fonctions de constructeur :

* int() - construit un nombre entier à partir d'un littéral entier, d'un littéral flottant (en supprimant les décimales) ou d'un littéral chaîne (si la chaîne représente un nombre entier)
* float() - construit un nombre flottant à partir d'un littéral entier, d'un littéral flottant ou d'un littéral chaîne (si la chaîne représente un flottant ou un entier)
* str() - construit une chaîne de caractères à partir d'une grande variété de types de données, y compris les chaînes, les littéraux entiers et les littéraux flottants

.. code-block:: python

    a = float("5")
    b = int(3.7)
    c = str(6.0)

    print(a)
    print(b)
    print(c)

Remarque : Vous ne pouvez pas convertir des nombres complexes en un autre type numérique.
