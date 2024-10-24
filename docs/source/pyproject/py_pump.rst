.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino & ESP32 sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprenez & Partagez** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Aperçus exclusifs** : Profitez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Bénéficiez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_pump:

3.6 Pompage
=======================


Les petites pompes centrifuges sont idéales pour les projets d'arrosage automatique des plantes.
Elles peuvent également être utilisées pour créer de petites fontaines intelligentes.

Le composant de puissance de la pompe est un moteur électrique, piloté exactement de la même manière qu'un moteur classique.

* :ref:`cpn_pump`
* :ref:`cpn_motor`
* :ref:`cpn_ta6586`
* :ref:`cpn_power_module`

.. note::

    #. Connectez le tuyau à la sortie du moteur, immergez la pompe dans l'eau, puis mettez-la sous tension.
    #. Vous devez vous assurer que le niveau de l'eau est toujours plus haut que le moteur. Un fonctionnement à vide peut endommager le moteur à cause de la chaleur générée et produire également du bruit.
    #. Si vous arrosez des plantes, veillez à éviter que la terre ne soit aspirée, car cela pourrait boucher la pompe.
    #. Si l'eau ne sort pas du tuyau, il peut y avoir de l'eau résiduelle bloquant le flux d'air dans le tuyau, qu'il faut d'abord évacuer.

**Composants Requis**

Dans ce projet, nous aurons besoin des composants suivants.

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
        - :ref:`cpn_ta6586`
        - 1
        - 
    *   - 6
        - :ref:`cpn_lipo_charger`
        - 1
        -  
    *   - 7
        - Batterie 18650
        - 1
        -  
    *   - 8
        - Support de batterie
        - 1
        -  
    *   - 9
        - :ref:`cpn_pump`
        - 1
        -  

**Schéma**

|sch_pump|

**Câblage**

.. note::

    * Comme la pompe nécessite un courant élevé, nous utilisons un module chargeur Li-po pour alimenter le moteur par sécurité.
    * Assurez-vous que votre module chargeur Li-po est connecté comme indiqué sur le schéma. Sinon, un court-circuit pourrait endommager la batterie et le circuit.

|wiring_pump|

**Code**

.. note::

    * Ouvrez le fichier ``3.6_pumping.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite.

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    motor1A = machine.Pin(14, machine.Pin.OUT)
    motor2A = machine.Pin(15, machine.Pin.OUT)

    while True:
        motor1A.high()
        motor2A.low()

Après l'exécution du code, la pompe commence à fonctionner et vous verrez l'eau couler du tuyau en même temps.

.. note::

    * Si le moteur continue de tourner après avoir cliqué sur le bouton Stop, vous devez réinitialiser la broche **RUN** du Pico W avec un fil vers GND, puis débrancher ce fil pour relancer le code.
    * Cela est dû au fait que le moteur consomme un courant élevé, ce qui peut provoquer la déconnexion du Pico W de l'ordinateur.

    |wiring_run_reset|
