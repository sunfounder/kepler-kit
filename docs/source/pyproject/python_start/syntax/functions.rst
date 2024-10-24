.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans le monde des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes post-achat et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions spéciales durant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Fonctions
==============

En MicroPython, une fonction est un ensemble de déclarations liées qui exécutent une tâche spécifique.

Les fonctions aident à diviser notre programme en blocs modulaires plus petits. À mesure que notre projet devient plus vaste, les fonctions le rendent plus organisé et plus facile à gérer.

De plus, elles évitent les duplications et rendent le code réutilisable.

Créer une Fonction
----------------------

.. code-block::

    def function_name(parameters): 
        """docstring"""
        statement(s)

* Une fonction est définie à l'aide du mot-clé ``def``

* Un nom de fonction pour identifier la fonction de manière unique. La règle de nommage des fonctions est la même que pour les variables, et suit les règles suivantes :
    
   * Peut uniquement contenir des chiffres, des lettres et des underscores.
   * Le premier caractère doit être une lettre ou un underscore.
   * Sensible à la casse.

* Les paramètres (arguments) par lesquels nous transmettons des valeurs à une fonction. Ils sont optionnels.

* Les deux-points (:) marquent la fin de l'en-tête de la fonction.

* Une docstring optionnelle, utilisée pour décrire la fonction ; on utilise généralement des guillemets triples pour que la docstring puisse s'étendre sur plusieurs lignes.

* Une ou plusieurs instructions MicroPython valides qui constituent le corps de la fonction. Les instructions doivent avoir le même niveau d'indentation (généralement 4 espaces).

* Chaque fonction a besoin d'au moins une instruction, mais si pour une raison quelconque il y a une fonction sans instruction, utilisez l'instruction pass pour éviter les erreurs.

* Une instruction ``return`` optionnelle pour renvoyer une valeur depuis la fonction.


Appeler une Fonction
------------------------

Pour appeler une fonction, ajoutez des parenthèses après le nom de la fonction.

.. code-block:: python

    def my_function():
        print("Your first function")

    my_function()

>>> %Run -c $EDITOR_CONTENT
Your first function

L'instruction return
-----------------------

L'instruction return est utilisée pour quitter une fonction et revenir à l'endroit où elle a été appelée.

**Syntaxe de return**

.. code-block:: python

    return [expression_list]

L'instruction peut contenir une expression qui est évaluée et renvoie une valeur. S'il n'y a pas d'expression dans l'instruction, ou si l'instruction ``return`` elle-même n'existe pas dans la fonction, la fonction renverra un objet ``None``.

.. code-block:: python

    def my_function():
            print("Your first function")

    print(my_function())

>>> %Run -c $EDITOR_CONTENT
Your first function
None

Ici, ``None`` est la valeur de retour, car l'instruction ``return`` n'est pas utilisée.

Arguments
-------------

Les informations peuvent être transmises à la fonction sous forme d'arguments.

Spécifiez les arguments entre parenthèses après le nom de la fonction. Vous pouvez ajouter autant d'arguments que nécessaire, il suffit de les séparer par des virgules.

.. code-block:: python

    def welcome(name, msg):
        """This is a welcome function for
        the person with the provided message"""
        print("Hello", name + ', ' + msg)

    welcome("Lily", "Welcome to China!")

>>> %Run -c $EDITOR_CONTENT
Bonjour Lily, Bienvenue en Chine !

Nombre d'Arguments
*************************

Par défaut, une fonction doit être appelée avec le bon nombre d'arguments. Cela signifie que si votre fonction attend 2 paramètres, vous devez appeler la fonction avec 2 arguments, ni plus, ni moins.

.. code-block:: python

    def welcome(name, msg):
        """This is a welcome function for
        the person with the provided message"""
        print("Hello", name + ', ' + msg)

    welcome("Lily", "Welcome to China!")

Ici, la fonction bienvenue() a 2 paramètres.

Comme nous avons appelé cette fonction avec deux arguments, elle s'exécute sans erreurs.

Si elle est appelée avec un nombre différent d'arguments, l'interpréteur affichera un message d'erreur.

Voici des appels à cette fonction avec un seul et aucun argument, ainsi que leurs messages d'erreur respectifs.

.. code-block::

    welcome("Lily")＃Only one argument

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
TypeError: function takes 2 positional arguments but 1 were given

.. code-block::

    welcome()＃No arguments

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
TypeError: function takes 2 positional arguments but 0 were given


Arguments par Défaut
*************************

En MicroPython, nous pouvons utiliser l'opérateur d'affectation (=) pour fournir une valeur par défaut à un paramètre.

Si nous appelons la fonction sans argument, elle utilisera la valeur par défaut.

.. code-block:: python

    def welcome(name, msg = "Welcome to China!"):
        """This is a welcome function for
        the person with the provided message"""
        print("Hello", name + ', ' + msg)
    welcome("Lily")

>>> %Run -c $EDITOR_CONTENT
Hello Lily, Welcome to China!

Dans cette fonction, le paramètre ``nom`` n'a pas de valeur par défaut et est obligatoire lors de l'appel.

En revanche, la valeur par défaut du paramètre ``msg`` est "Bienvenue en Chine !". Il est donc optionnel lors de l'appel. Si une valeur est fournie, elle remplacera la valeur par défaut.

Un nombre quelconque de paramètres dans la fonction peut avoir une valeur par défaut. Cependant, dès qu'il y a un argument par défaut, tous les arguments à sa droite doivent également avoir des valeurs par défaut.

Cela signifie que les arguments non par défaut ne peuvent pas suivre les arguments par défaut.

Par exemple, si nous définissons l'en-tête de fonction ci-dessus comme :

.. code-block:: python

    def welcome(name = "Lily", msg):

We will receive the following error message:

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
SyntaxError: non-default argument follows default argument

Arguments Nommes
**************************

Lorsque nous appelons une fonction avec certaines valeurs, ces valeurs seront attribuées aux arguments en fonction de leur position.

Par exemple, dans la fonction bienvenue() ci-dessus, lorsque nous l'avons appelée comme bienvenue("Lily", "Bienvenue en Chine"), la valeur "Lily" est affectée au paramètre ``nom`` et de même "Bienvenue en Chine" au paramètre ``msg``.

MicroPython permet d'appeler des fonctions avec des arguments nommés. Lorsque nous appelons la fonction de cette manière, l'ordre (position) des arguments peut être modifié.

.. code-block:: python

    # keyword arguments
    welcome(name = "Lily",msg = "Welcome to China!")

    # keyword arguments (out of order)
    welcome(msg = "Welcome to China！",name = "Lily") 

    #1 positional, 1 keyword argument
    welcome("Lily", msg = "Welcome to China!")

Comme nous pouvons le voir, nous pouvons mélanger des arguments positionnels et nommés lors des appels de fonctions. Mais il faut se rappeler que les arguments nommés doivent venir après les arguments positionnels.

Avoir un argument positionnel après un argument nommé entraînera une erreur.

Par exemple, si l'appel de fonction est le suivant :

.. code-block:: python

    welcome(name="Lily","Welcome to China!")

Will result in an error:

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
SyntaxError: non-keyword arg after keyword arg

Arguments Arbitraires
**************************

Parfois, vous ne connaissez pas à l'avance le nombre d'arguments qui seront passés à la fonction.

Dans la définition de la fonction, nous pouvons ajouter un astérisque (*) avant le nom du paramètre.

.. code-block:: python

    def welcome(*names):
        """This function welcomes all the person
        in the name tuple"""
        #names is a tuple with arguments
        for name in names:
            print("Welcome to China!", name)
            
    welcome("Lily","John","Wendy")

>>> %Run -c $EDITOR_CONTENT
Welcome to China! Lily
Welcome to China! John
Welcome to China! Wendy

Ici, nous avons appelé la fonction avec plusieurs arguments. Ces arguments sont regroupés dans un tuple avant d'être transmis à la fonction.

Dans la fonction, nous utilisons une boucle for pour récupérer tous les arguments.

Récursion
----------------
En Python, nous savons qu'une fonction peut en appeler d'autres. Il est même possible pour une fonction de s'appeler elle-même. Ces types de constructions sont appelés fonctions récursives.

Cela permet de parcourir des données pour obtenir un résultat.

Le développeur doit être très prudent avec la récursion, car il est facile d'écrire une fonction qui ne se termine jamais ou qui utilise trop de mémoire ou de puissance de traitement. Cependant, lorsqu'elle est correctement écrite, la récursion peut être une approche très efficace et élégante sur le plan mathématique.

.. code-block:: python

    def rec_func(i):
        if(i > 0):
            result = i + rec_func(i - 1)
            print(result)
        else:
            result = 0
        return result

    rec_func(6)

>>> %Run -c $EDITOR_CONTENT
1
3
6
10
15
21

Dans cet exemple, fonction_rec() est une fonction que nous avons définie pour s'appeler elle-même ("récursion"). Nous utilisons la variable ``i`` comme donnée, et elle décrémente (-1) à chaque fois que nous faisons une récursion. Lorsque la condition n'est plus supérieure à 0 (c'est-à-dire 0), la récursion se termine.

Pour les nouveaux développeurs, il peut être difficile de comprendre comment cela fonctionne, et le meilleur moyen est de tester et de modifier le code.

**Avantages de la Récursion**

* Les fonctions récursives rendent le code propre et élégant.
* Une tâche complexe peut être décomposée en sous-problèmes plus simples grâce à la récursion.
* La génération de séquences est plus facile avec la récursion qu'avec des boucles imbriquées.


**Inconvénients de la Récursion**

* Parfois, la logique derrière la récursion est difficile à suivre.
* Les appels récursifs sont coûteux (inefficaces) car ils consomment beaucoup de mémoire et de temps.
* Les fonctions récursives sont difficiles à déboguer.

