.. note::

    Bonjour et bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Explorez plus en profondeur Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Assistance d'experts** : Résolvez vos problèmes après-vente et vos défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_led:

2.1 Bonjour, LED !
=======================================

Tout comme l'impression de "Hello, world!" est la première étape pour apprendre à programmer, utiliser un programme pour piloter une LED est la traditionnelle introduction à la programmation physique.

* :ref:`cpn_led`

**Composants requis**

Pour ce projet, nous aurons besoin des composants suivants.

Il est plus pratique d'acheter un kit complet, voici le lien :

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nom	
        - ÉLÉMENTS DANS CE KIT
        - LIEN
    *   - Kit Kepler	
        - 450+
        - |link_kepler_kit|

Vous pouvez également les acheter séparément via les liens ci-dessous.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - COMPOSANT	
        - QUANTITÉ
        - LIEN

    *   - 1
        - :ref:`cpn_pico_w`
        - 1
        - |link_picow_buy|
    *   - 2
        - Câble Micro USB
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Plusieurs
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_resistor`
        - 1(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|


**Schéma**

|sch_led|

Ce circuit fonctionne selon un principe simple, la direction du courant est indiquée dans la figure. La LED s'allumera après la résistance limitant le courant de 220 ohms lorsque GP15 émet un niveau haut (3,3V). La LED s'éteindra lorsque GP15 émettra un niveau bas (0V).

**Câblage**

|wiring_led|

Pour construire le circuit, suivez la direction du courant !

1. La LED est alimentée par la broche GP15 de la carte Pico W, et le circuit commence ici.
#. Pour protéger la LED, le courant doit passer par une résistance de 220 ohms. Une extrémité de la résistance doit être insérée dans la même rangée que la broche GP15 de la Pico W (rangée 20 dans mon circuit), et l'autre extrémité doit être insérée dans une rangée libre de la breadboard (rangée 24).

    .. note::
        L'anneau de couleur de la résistance de 220 ohms est rouge, rouge, noir, noir et brun.

#. Si vous prenez la LED, vous verrez que l'une de ses pattes est plus longue que l'autre. Connectez la patte longue à la même rangée que la résistance, et la patte courte à la même rangée de l'autre côté du milieu de la breadboard.

    .. note::
        La patte longue est l'anode, qui représente le côté positif du circuit ; la patte courte est la cathode, représentant le côté négatif.

        L'anode doit être connectée à la broche GPIO via une résistance ; la cathode doit être connectée à la broche GND.

#. Utilisez un câble de liaison mâle-mâle (M2M) pour connecter la patte courte de la LED au bus d'alimentation négatif de la breadboard.
#. Connectez la broche GND de la Pico W au bus d'alimentation négatif à l'aide d'un câble de liaison.

**Code**

.. note::

    * Ouvrez le fichier ``2.1_hello_led.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite. 

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime
    
    led = machine.Pin(15, machine.Pin.OUT)
    while True:
        led.value(1)
        utime.sleep(2)
        led.value(0)
        utime.sleep(2)

Une fois le code exécuté, vous verrez la LED clignoter.


**Comment ça fonctionne ?**

La bibliothèque ``machine`` est nécessaire pour utiliser les GPIO.

.. code-block:: python

    import machine

Cette bibliothèque contient toutes les instructions nécessaires pour permettre la communication entre MicroPython et la Pico W. 
Sans cette ligne de code, il ne sera pas possible de contrôler les GPIO.

La prochaine ligne importante à noter est la suivante :

.. code-block:: python

    led = machine.Pin(15, machine.Pin.OUT)

L'objet ``led`` est défini ici. Techniquement, il peut porter n'importe quel nom, comme x, y, banana, Michael_Jackson, ou tout autre caractère. 
Pour s'assurer que le programme reste facile à lire, il est préférable d'utiliser un nom qui décrit son rôle.

Dans la seconde partie de cette ligne (celle après le signe égal), nous appelons la fonction ``Pin`` de la bibliothèque ``machine``. Elle permet de dire aux broches GPIO de la Pico ce qu'elles doivent faire.
La fonction ``Pin`` prend deux paramètres : le premier (15) indique la broche à configurer ; 
le second paramètre (machine.Pin.OUT) précise que la broche doit être utilisée comme sortie plutôt que comme entrée.

Le code ci-dessus a configuré la broche, mais cela ne suffit pas pour allumer la LED. Pour cela, nous devons également "utiliser" la broche.

.. code-block:: python

    led.value(1)

La broche GP15 a été précédemment configurée et nommée ``led``. Cette instruction sert à définir la valeur de ``led`` à 1 pour allumer la LED.

En résumé, pour utiliser les GPIO, ces étapes sont nécessaires :

* **Importer la bibliothèque machine** : Cette étape est essentielle et n'est exécutée qu'une seule fois.
* **Configurer les GPIO** : Avant utilisation, chaque broche doit être configurée.
* **Utiliser** : Changez l'état de fonctionnement de la broche en lui attribuant une valeur.

Si nous suivons ces étapes pour écrire un exemple, voici le code obtenu :

.. code-block:: python

    import machine
    led = machine.Pin(15, machine.Pin.OUT)
    led.value(1)

Exécutez-le et vous verrez la LED s'allumer.

Ensuite, essayons d'ajouter une instruction pour l'éteindre :

.. code-block:: python

    import machine   
    led = machine.Pin(15, machine.Pin.OUT)
    led.value(1)
    led.value(0)

D'après ces lignes de code, le programme allumera d'abord la LED, puis l'éteindra. 
Cependant, lorsque vous l'exécutez, vous constaterez que ce n'est pas le cas. 
Aucune lumière ne s'échappe de la LED. Cela est dû à la vitesse d'exécution extrêmement rapide entre les deux lignes, bien plus rapide que la perception de l'œil humain. 
Quand la LED s'allume, nous ne percevons pas la lumière immédiatement. Ce problème peut être résolu en ralentissant l'exécution du programme.

La seconde ligne du programme devrait inclure l'instruction suivante :

.. code-block:: python

    import utime

De la même manière que ``machine``, la bibliothèque ``utime`` est importée ici, pour gérer tout ce qui concerne le temps.
Les délais que nous devons utiliser y sont inclus. Ajoutez une instruction de délai entre ``led.value(1)`` et ``led.value(0)`` et espacez-les de 2 secondes.

.. code-block:: python

    utime.sleep(2)

Voici à quoi le code devrait ressembler maintenant. 
Nous verrons que la LED s'allume d'abord, puis s'éteint lorsque nous l'exécutons :

.. code-block:: python

    import machine 
    import utime  
    led = machine.Pin(15, machine.Pin.OUT)
    led.value(1)
    utime.sleep(2)
    led.value(0)

Enfin, faisons clignoter la LED. 
Créez une boucle, réécrivez le programme, et vous obtiendrez ce que vous avez vu au début de ce chapitre.

.. code-block:: python

    import machine
    import utime
    
    led = machine.Pin(15, machine.Pin.OUT)
    while True:
        led.value(1)
        utime.sleep(2)
        led.value(0)
        utime.sleep(2)

* :ref:`py_syntax_while` 

**En savoir plus**


Il existe généralement un fichier API (Interface de Programmation d'Application) associé à la bibliothèque. 
Ce fichier contient toutes les informations nécessaires pour utiliser cette bibliothèque, y compris des descriptions détaillées des fonctions, classes, types de retour, types de paramètres, etc.

Dans cet article, nous avons utilisé les bibliothèques ``machine`` et ``utime`` de MicroPython, et nous pouvons trouver plus de façons de les utiliser ici :

* `machine.Pin <https://docs.micropython.org/en/latest/library/machine.Pin.html>`_

* `utime <https://docs.micropython.org/en/latest/library/utime.html>`_

Veuillez lire le fichier API pour bien comprendre cet exemple de clignotement de LED !

.. note::

    * Ouvrez le fichier ``2.1_hello_led_2.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite. 

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    led = machine.Pin(15, machine.Pin.OUT)
    while True:
        led.toggle()
        utime.sleep(1)