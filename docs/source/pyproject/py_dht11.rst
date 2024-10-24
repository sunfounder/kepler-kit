.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions spéciales durant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_dht11:

6.2 Température - Humidité
=======================================

L'humidité et la température sont étroitement liées, tant en termes de 
quantités physiques qu'en impact sur la vie quotidienne. La température 
et l'humidité de l'environnement humain influencent directement la régulation 
thermique et le transfert de chaleur du corps humain. Cela peut également 
affecter l'activité mentale et l'état d'esprit, influençant ainsi l'efficacité 
de nos études et de notre travail.

La température est l'une des sept grandeurs physiques fondamentales du Système 
international d'unités, utilisée pour mesurer le degré de chaleur ou de froid 
d'un objet. Le degré Celsius est l'une des échelles de température les plus 
couramment utilisées dans le monde, exprimée par le symbole "℃".

L'humidité est la concentration de vapeur d'eau présente dans l'air. L'humidité 
relative de l'air est généralement utilisée au quotidien et est exprimée en %RH. 
L'humidité relative est étroitement liée à la température. Pour un volume de gaz 
scellé donné, plus la température est élevée, plus l'humidité relative est faible ; 
et plus la température est basse, plus l'humidité relative est élevée.

|img_Dht11|

Un capteur numérique de base pour la température et l'humidité, le **DHT11**, est inclus dans ce kit. Il utilise un capteur capacitif d'humidité et une thermistance pour mesurer l'air ambiant et transmet un signal numérique via les broches de données (aucune broche d'entrée analogique n'est requise).

* :ref:`cpn_dht11`

**Composants Requis**

Pour ce projet, nous avons besoin des composants suivants : 

Il est plus pratique d'acheter un kit complet, voici le lien : 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nom	
        - ARTICLES DANS CE KIT
        - LIEN
    *   - Kepler Kit	
        - 450+
        - |link_kepler_kit|

Vous pouvez également les acheter séparément via les liens ci-dessous :

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
        - :ref:`cpn_dht11`
        - 1
        - |link_dht22_buy|

**Schéma**

|sch_dht11|

**Câblage**

|wiring_dht11|

**Code**

.. note::

    * Ouvrez le fichier ``6.2_temperature_humidity.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Exécuter le script actuel" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite. 

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`. 
    
    * Vous devez utiliser la bibliothèque appelée ``dht.py``, vérifiez si elle a été téléchargée sur le Pico W. Pour un tutoriel détaillé, référez-vous à :ref:`add_libraries_py`.

.. code-block:: python

    from machine import Pin
    import utime as time
    from dht import DHT11, InvalidPulseCount

    pin = Pin(16, Pin.IN)
    sensor = DHT11(pin)
    time.sleep(5)  # délai initial

    while True:
        try:
            sensor.measure()
            string = "Temperature:{}\nHumidity: {}".format(sensor.temperature, sensor.humidity)
            print(string)
            time.sleep(4)

        except InvalidPulseCount as e:
            print('Bad pulse count - retrying ...')




Après l'exécution du code, vous verrez le Shell afficher en continu la température et l'humidité, et à mesure que le programme fonctionne de manière stable, ces deux valeurs deviendront de plus en plus précises.

**Comment ça marche ?**

Dans la bibliothèque dht, les fonctionnalités pertinentes ont été intégrées dans la classe ``DHT11``.

.. code-block:: python

    from dht import DHT11, InvalidPulseCount

Initialisez l'objet ``DHT11``. Ce dispositif ne nécessite qu'une entrée numérique pour être utilisé.

.. code-block:: python

    pin = Pin(16, Pin.IN)
    sensor = DHT11(pin)

Utilisez ``sensor.measure()`` pour lire la température et l'humidité actuelles, 
qui seront stockées dans ``sensor.temperature`` et ``sensor.humidity``. Elles 
sont ensuite imprimées à l'écran. Enfin, le taux d'échantillonnage du DHT11 est 
de 1HZ, il faut donc un ``time.sleep(1)`` dans la boucle.

.. code-block:: python

    while True:
        try:
            sensor.measure()
            string = "Temperature:{}\nHumidity: {}".format(sensor.temperature, sensor.humidity)
            print(string)
            time.sleep(4)

        except InvalidPulseCount as e:
            print('Bad pulse count - retrying ...')
