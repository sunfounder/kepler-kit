.. note::

    Bonjour et bienvenue dans la communauté SunFounder pour les passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions et concours festifs** : Participez aux concours et aux promotions de fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_transistor:

2.15 Deux types de transistors
==========================================

Ce kit est équipé de deux types de transistors, le S8550 et le S8050. Le premier est un PNP, et le second un NPN. Ils se ressemblent beaucoup, et il est nécessaire de vérifier attentivement leurs étiquettes pour les identifier.
Lorsqu'un signal de niveau haut traverse un transistor NPN, il est activé. En revanche, un transistor PNP nécessite un signal de niveau bas pour fonctionner. Les deux types de transistors sont fréquemment utilisés comme interrupteurs sans contact, comme dans cette expérience.

|img_NPN&PNP|

Utilisons une LED et un bouton pour comprendre comment utiliser un transistor !

:ref:`cpn_transistor`

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
        - :ref:`cpn_resistor`
        - 3(220Ω, 1KΩ, 10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_button`
        - 1
        - |link_button_buy|
    *   - 8
        - :ref:`cpn_transistor`
        - 1(S8050/S8550)
        - |link_transistor_buy|


**Connexion du transistor NPN (S8050)**

|sch_s8050|

Dans ce circuit, lorsque le bouton est pressé, GP14 est à un niveau haut.

En programmant GP15 pour émettre un signal de niveau haut, après une résistance de limitation de courant de 1k (pour protéger le transistor), le S8050 (transistor NPN) est autorisé à conduire, permettant ainsi à la LED de s'allumer.


|wiring_s8050|

**Connexion du transistor PNP (S8550)**

|sch_s8550|

Dans ce circuit, GP14 est par défaut à un niveau bas et passe à un niveau haut lorsque le bouton est pressé.

En programmant GP15 pour émettre un signal de niveau **bas**, après une résistance de limitation de courant de 1k (pour protéger le transistor), le S8550 (transistor PNP) est autorisé à conduire, permettant ainsi à la LED de s'allumer.

La seule différence que vous remarquerez entre ce circuit et le précédent est que, dans le circuit précédent, la cathode de la LED est connectée au **collecteur** du **S8050 (transistor NPN)**, tandis que dans celui-ci, elle est connectée à l'**émetteur** du **S8550 (transistor PNP)**.

|wiring_s8550|


**Code**

.. note::

    * Ouvrez le fichier ``2.15_transistor.py`` situé sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite. 

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.


.. code-block:: python

    import machine
    button = machine.Pin(14, machine.Pin.IN)
    signal = machine.Pin(15, machine.Pin.OUT)    

    while True:
        button_status = button.value()
        if button_status== 1:
            signal.value(1)
        elif button_status == 0:
            signal.value(0)



Les deux types de transistors peuvent être contrôlés avec le même code. Lorsque nous appuyons sur le bouton, Pico W enverra un signal de niveau haut au transistor ; lorsque nous le relâchons, il enverra un signal de niveau bas.
Nous pouvons observer que des phénomènes diamétralement opposés se produisent dans les deux circuits.

* Le circuit utilisant le S8050 (transistor NPN) s'allumera lorsque le bouton est pressé, ce qui signifie qu'il reçoit un circuit de conduction de niveau haut ;
* Le circuit utilisant le S8550 (transistor PNP) s'allumera lorsqu'il est relâché, ce qui signifie qu'il reçoit un circuit de conduction de niveau bas.
