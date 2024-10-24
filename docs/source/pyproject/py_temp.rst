.. note::

    Bonjour, bienvenue dans la communauté SunFounder des passionnés de Raspberry Pi, Arduino & ESP32 sur Facebook ! Approfondissez vos connaissances en matière de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions festives.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_temp:

2.13 Thermomètre
===========================

Un thermomètre est un dispositif qui mesure la température ou un gradient de température (le degré de chaleur ou de froid d'un objet). 
Un thermomètre comporte deux éléments importants : (1) un capteur de température (par exemple, le bulbe d'un thermomètre à mercure ou le capteur pyrométrique d'un thermomètre infrarouge) dans lequel un changement se produit avec la variation de température ; 
et (2) un moyen de convertir ce changement en une valeur numérique (par exemple, l'échelle visible d'un thermomètre à mercure ou l'affichage numérique d'un modèle infrarouge). 
Les thermomètres sont largement utilisés en technologie et dans l'industrie pour surveiller les processus, en météorologie, en médecine, et dans la recherche scientifique.

Un thermistor est un type de capteur de température dont la résistance dépend fortement de la température, et il en existe deux types :
Coefficient de Température Négatif (NTC) et Coefficient de Température Positif (PTC), également appelés NTC et PTC. La résistance d'un 
thermistor PTC augmente avec la température, tandis que celle d'un NTC diminue.

Dans cette expérience, nous utilisons un **thermistor NTC** pour fabriquer un thermomètre.

* :ref:`cpn_thermistor`

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
        - :ref:`cpn_resistor`
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_thermistor`
        - 1
        - |link_thermistor_buy|

**Schéma**

|sch_temp|

Dans ce circuit, la résistance de 10K et le thermistor sont connectés en série, et le courant qui les traverse est le même. La résistance de 10K agit comme une protection, et le GP28 lit la valeur après la conversion de tension du thermistor.

Lorsque la température augmente, la résistance du thermistor NTC diminue, ce qui réduit sa tension, et donc la valeur lue par GP28 diminue également. Si la température est suffisamment élevée, la résistance du thermistor sera proche de 0, et la valeur de GP28 sera proche de 0. À ce moment-là, la résistance de 10K joue un rôle protecteur, évitant que le 3,3V et le GND ne soient connectés ensemble, ce qui entraînerait un court-circuit.

Quand la température baisse, la valeur de GP28 augmente. Si la température est très basse, la résistance du thermistor sera pratiquement infinie et sa tension sera proche de 3,3V (la résistance de 10K étant négligeable), et la valeur de GP28 sera proche de la valeur maximale de 65535.

La formule de calcul est la suivante :

    (Vp/3.3V) x 65535 = Ap


**Câblage**

|wiring_temp|

.. #. Connectez les broches 3V3 et GND du Pico W au bus d'alimentation de la breadboard.
.. #. Connectez une borne du thermistor à la broche GP28, puis reliez cette même borne au bus positif avec une résistance de 10K ohms.
.. #. Connectez l'autre borne du thermistor au bus négatif.

.. note::
    * Le thermistor est noir et marqué 103.
    * Les anneaux de couleur de la résistance de 10K ohms sont rouge, noir, noir, rouge et marron.

**Code**

.. note::

    * Ouvrez le fichier ``2.13_thermometer.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite. 

    * Pour des tutoriels détaillés, veuillez consulter :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime
    import math

    thermistor = machine.ADC(28)  

    while True:
        temperature_value = thermistor.read_u16()
        Vr = 3.3 * float(temperature_value) / 65535
        Rt = 10000 * Vr / (3.3 - Vr)
        temp = 1/(((math.log(Rt / 10000)) / 3950) + (1 / (273.15+25)))
        Cel = temp - 273.15
        Fah = Cel * 1.8 + 32
        print ('Celsius: %.2f C  Fahrenheit: %.2f F' % (Cel, Fah))
        utime.sleep_ms(200)

Après l'exécution du programme, la console affichera les températures en degrés Celsius et Fahrenheit.

**Comment ça marche ?**

Chaque thermistor possède une résistance normale. Ici, elle est de 10k ohms, mesurée à 25 degrés Celsius.

Lorsque la température augmente, la résistance du thermistor diminue. La tension est alors convertie en valeurs numériques par l'adaptateur A/D.

La température en degrés Celsius ou Fahrenheit est affichée via le programme.

.. code-block:: python

    import math 

Il existe une bibliothèque de fonctions numériques permettant de réaliser des opérations mathématiques courantes.

* `math <https://docs.micropython.org/en/latest/library/math.html>`_

.. code-block:: python

    temperature_value = thermistor.read_u16()

Cette fonction lit la valeur du thermistor.

.. code-block:: python

    Vr = 3.3 * float(temperature_value) / 65535
    Rt = 10000 * Vr / (3.3 - Vr)
    temp = 1/(((math.log(Rt / 10000)) / 3950) + (1 / (273.15+25)))
    Cel = temp - 273.15
    Fah = Cel * 1.8 + 32
    print ('Celsius: %.2f C  Fahrenheit: %.2f F' % (Cel, Fah))
    utime.sleep_ms(200)

Ces calculs convertissent les valeurs du thermistor en degrés Celsius et Fahrenheit.

.. code-block:: python

    Vr = 3.3 * float(temperature_value) / 65535
    Rt = 10000 * Vr / (3.3 - Vr)

Dans les deux lignes de code ci-dessus, la tension est d'abord calculée à partir de la valeur analogique lue, puis on obtient Rt (la résistance du thermistor).

.. code-block:: python

    temp = 1/(((math.log(Rt / 10000)) / 3950) + (1 / (273.15+25)))

.. note::
    Voici la relation entre la résistance et la température :

    **RT =RN expB(1/TK – 1/TN)** 

    * RT est la résistance du thermistor NTC lorsque la température est TK. 
    * RN est la résistance du thermistor NTC sous la température nominale TN. Ici, RN vaut 10k. 
    * TK est la température en Kelvin. Ici, TK est de 273.15 + degrés Celsius. 
    * TN est une température nominale en Kelvin ; ici, TN est de 273.15 + 25.
    * B (bêta), la constante de matériau du thermistor NTC, également appelée indice de sensibilité thermique, a pour valeur 3950. 
    * exp est l'abréviation d'exponentielle, avec le nombre de base e, un nombre naturel valant environ 2,7. 

    Convertissez cette formule en TK=1/(ln(RT/RN)/B+1/TN) pour obtenir la température en Kelvin, puis soustrayez 273,15 pour obtenir les degrés Celsius.

    Cette relation est empirique. Elle est précise uniquement lorsque la température et la résistance se situent dans une plage effective.

Ce code consiste à insérer Rt dans la formule TK=1/(ln(RT/RN)/B+1/TN) pour obtenir la température en Kelvin.

.. code-block:: python

    temp = temp - 273.15 

Conversion de la température Kelvin en degrés Celsius.

.. code-block:: python

    Fah = Cel * 1.8 + 32 

Conversion des degrés Celsius en degrés Fahrenheit.

.. code-block:: python

    print ('Celsius: %.2f °C Fahrenheit: %.2f ℉' % (Cel, Fah)) 

Affichage en console des températures en degrés Celsius et Fahrenheit avec leurs unités respectives.
