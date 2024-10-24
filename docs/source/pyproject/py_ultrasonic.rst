.. note::

    Bonjour et bienvenue dans la communauté SunFounder pour les passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions et concours festifs** : Participez aux concours et aux promotions de fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_ultrasonic:

6.1 Mesure de la distance
======================================

Le module de capteur ultrasonique fonctionne selon le principe des systèmes sonar et radar pour déterminer la distance d'un objet.

* :ref:`cpn_ultrasonic`

**Composants requis**

Pour ce projet, nous aurons besoin des composants suivants.

Il est bien sûr plus pratique d'acheter un kit complet, voici le lien : 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nom	
        - ARTICLES DANS CE KIT
        - LIEN
    *   - Kit Kepler	
        - 450+
        - |link_kepler_kit|

Vous pouvez également les acheter séparément via les liens ci-dessous.


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - N°
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
        - :ref:`cpn_ultrasonic`
        - 1
        - |link_ultrasonic_buy|


**Schéma**

|sch_ultrasonic|

**Câblage**

|wiring_ultrasonic|

**Code**

.. note::

    * Ouvrez le fichier ``6.1_measuring_distance.py`` situé sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite. 

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import time

    TRIG = machine.Pin(17,machine.Pin.OUT)
    ECHO = machine.Pin(16,machine.Pin.IN)

    def distance():
        TRIG.low()
        time.sleep_us(2)
        TRIG.high()
        time.sleep_us(10)
        TRIG.low()
        while not ECHO.value():
            pass
        time1 = time.ticks_us()
        while ECHO.value():
            pass
        time2 = time.ticks_us()
        during = time.ticks_diff(time2,time1)
        return during * 340 / 2 / 10000

    while True:
        dis = distance()
        print ('Distance: %.2f' % dis)
        time.sleep_ms(300)

Une fois le programme lancé, la console affichera la distance détectée par le capteur ultrasonique par rapport à l'obstacle situé en face.

**Comment ça marche ?**

Les capteurs ultrasoniques produisent des ondes sonores de haute fréquence (ultrasons) émises par la sonde émettrice. Lorsque cette onde ultrasonique rencontre un objet, elle est réfléchie sous forme d'écho, détecté par la sonde réceptrice. En calculant le temps écoulé entre l'émission et la réception, on peut déterminer la distance.
Sur cette base, la fonction ``distance()`` peut être définie.

.. code-block:: python

    def distance():
        TRIG.low()
        time.sleep_us(2)
        TRIG.high()
        time.sleep_us(10)
        TRIG.low()
        while not ECHO.value():
            pass
        time1 = time.ticks_us()
        while ECHO.value():
            pass
        time2 = time.ticks_us()
        during = time.ticks_diff(time2,time1)
        return during * 340 / 2 / 10000

* Parmi ces lignes, les premières servent à transmettre une onde ultrasonique de 10 µs.

.. code-block:: python

    TRIG.low()
    time.sleep_us(2)
    TRIG.high()
    time.sleep_us(10)
    TRIG.low()

* Ensuite, le programme se met en pause et enregistre l'heure actuelle après l'émission de l'onde ultrasonique.

.. code-block:: python

        while not ECHO.value():
            pass
        time1 = time.ticks_us()

* Par la suite, le programme se suspend à nouveau. Après avoir reçu l'écho, l'heure actuelle est enregistrée une seconde fois.

.. code-block:: python

        while ECHO.value():
            pass
        time2 = time.ticks_us()

* Enfin, en fonction de la différence de temps entre les deux enregistrements, la vitesse du son (340 m/s) est multipliée par le temps pour obtenir le double de la distance entre le module ultrasonique et l'obstacle (c'est-à-dire un aller-retour des ondes ultrasoniques entre le module et l'obstacle). En convertissant les unités en centimètres, nous obtenons la valeur de retour souhaitée.

.. code-block:: python

        during = time.ticks_diff(time2,time1)
        return during * 340 / 2 / 10000

Notez que le capteur ultrasonique met en pause le programme lorsqu'il fonctionne, ce qui peut entraîner des ralentissements lorsqu'on écrit des projets plus complexes.

