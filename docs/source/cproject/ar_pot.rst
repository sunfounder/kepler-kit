.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des concours et promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ar_pot:

2.11 - Tournez le bouton
===========================

Dans les projets précédents, nous avons utilisé l'entrée numérique sur le Pico W.
Par exemple, un bouton peut changer la broche du niveau bas (éteint) au niveau haut (allumé). C'est un état de fonctionnement binaire.

Cependant, le Pico W peut également recevoir un autre type de signal d'entrée : l'entrée analogique.
Elle peut se situer dans n'importe quel état, de complètement fermé à complètement ouvert, avec une plage de valeurs possibles.
L'entrée analogique permet au microcontrôleur de percevoir l'intensité de la lumière, du son, la température, l'humidité, etc., du monde physique.

Habituellement, un microcontrôleur nécessite un matériel supplémentaire pour implémenter l'entrée analogique : le convertisseur analogique-numérique (ADC).
Mais le Pico W dispose lui-même d'un ADC intégré que nous pouvons utiliser directement.

|pin_adc|

Le Pico W possède trois broches GPIO capables de gérer des entrées analogiques : GP26, GP27, GP28. C'est-à-dire, les canaux analogiques 0, 1 et 2.
De plus, il existe un quatrième canal analogique, connecté au capteur de température intégré, qui ne sera pas présenté ici.

Dans ce projet, nous essayons de lire la valeur analogique du potentiomètre.

* :ref:`cpn_potentiometer`

**Composants requis**

Dans ce projet, nous avons besoin des composants suivants. 

Il est pratique d'acheter un kit complet, voici le lien : 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nom	
        - ARTICLES DANS CE KIT
        - LIEN D'ACHAT
    *   - Kit Kepler	
        - 450+
        - |link_kepler_kit|

Vous pouvez également les acheter séparément via les liens ci-dessous.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - N°
        - INTRODUCTION DES COMPOSANTS	
        - QUANTITÉ
        - LIEN D'ACHAT

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
        - 1 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_potentiometer`
        - 1
        - |link_potentiometer_buy|

**Schéma**

|sch_pot|

Le potentiomètre est un dispositif analogique, et lorsque vous le tournez dans deux directions différentes.

Connectez la broche centrale du potentiomètre à la broche analogique GP28. Le Raspberry Pi Pico W contient un convertisseur analogique-numérique multicanal de 16 bits. Cela signifie qu'il mappe la tension d'entrée entre 0 et la tension de fonctionnement (3,3V) à une valeur entière comprise entre 0 et 65535, donc la valeur de GP28 varie de 0 à 65535.

La formule de calcul est la suivante :

    (Vp/3.3V) x 65535 = Ap

Ensuite, programmez la valeur de GP28 (potentiomètre) comme valeur PWM de GP15 (LED).
De cette manière, vous remarquerez qu'en tournant le potentiomètre, la luminosité de la LED changera en même temps.

**Câblage**

|wiring_pot|

**Code**

.. note::

    * Vous pouvez ouvrir le fichier ``2.11_turn_the_knob.ino`` sous le chemin ``kepler-kit-main/arduino/2.11_turn_the_knob``. 
    * Ou copiez ce code dans l'**Arduino IDE**.
    * N'oubliez pas de sélectionner la carte (Raspberry Pi Pico) et le port correct avant de cliquer sur le bouton Upload.

Lorsque le programme est en cours d'exécution, nous pouvons voir la valeur analogique actuellement lue par la broche GP28 dans le moniteur série. 
Tournez le bouton, et la valeur variera de 0 à 1023.
En même temps, la luminosité de la LED augmentera au fur et à mesure que la valeur analogique augmentera.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/b3e3927a-bd1a-4756-83f2-141d47f99b1c/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>




**Comment ça marche ?**

Pour activer le moniteur série, vous devez démarrer la communication série dans ``setup()`` et définir le débit de données à 9600.

.. code-block:: arduino
    :emphasize-lines: 3

    void setup() {
        pinMode(ledPin, OUTPUT);
        Serial.begin(9600);
    }

* `Serial <https://www.arduino.cc/reference/en/language/functions/communication/serial/>`_

Dans la fonction loop, la valeur du potentiomètre est lue, puis la valeur est mappée de 0-1023 à 0-255 et finalement la valeur après le mappage est utilisée pour contrôler la luminosité de la LED.

.. code-block:: arduino

    void loop() {
        int sensorValue = analogRead(sensorPin);
        Serial.println(sensorValue);
        int brightness = map(sensorValue, 0, 1023, 0, 255);
        analogWrite(ledPin, brightness);
    }

* `analogRead() <https://www.arduino.cc/reference/en/language/functions/analog-io/analogread/>`_ est utilisée pour lire la valeur de la broche sensorPin (potentiomètre) et l'attribue à la variable ``sensorValue``.

.. code-block:: arduino

    int sensorValue = analogRead(sensorPin);

* Imprimez la valeur de ``sensorValue`` dans le moniteur série.

.. code-block:: arduino

    Serial.println(sensorValue);

* Ici, la fonction `map(value, fromLow, fromHigh, toLow, toHigh) <https://www.arduino.cc/reference/en/language/functions/analog-io/analogread/>`_ est requise car la valeur du potentiomètre lue est comprise entre 0-1023 et la valeur d'une broche PWM est comprise entre 0-255. Elle est utilisée pour re-mapper un nombre d'une plage à une autre.

.. code-block:: arduino

    int brightness = map(sensorValue, 0, 1023, 0, 255);

* Maintenant, nous pouvons utiliser cette valeur pour contrôler la luminosité de la LED.

.. code-block:: arduino

    analogWrite(ledPin,brightness);