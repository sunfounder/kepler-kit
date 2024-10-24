.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ar_dht11:

6.2 - Température - Humidité
=======================================

L'humidité et la température sont étroitement liées, que ce soit en tant que grandeurs physiques ou dans notre vie quotidienne.
La température et l'humidité de notre environnement influencent directement la régulation thermique et le transfert de chaleur du corps humain.
Cela peut également affecter notre activité mentale et notre état d'esprit, et par conséquent, l'efficacité de nos études et de notre travail.

La température est l'une des sept grandeurs physiques de base dans le Système international d'unités, utilisée pour mesurer le degré de chaleur d'un objet.
Le Celsius est l'une des échelles de température les plus utilisées dans le monde, exprimée par le symbole "℃".

L'humidité désigne la concentration de vapeur d'eau présente dans l'air.
L'humidité relative de l'air est couramment utilisée au quotidien et est exprimée en %RH. L'humidité relative est étroitement liée à la température.
Pour un volume de gaz fermé, plus la température est élevée, plus l'humidité relative est faible, et plus la température est basse, plus l'humidité relative est élevée.

|img_Dht11|

Un capteur numérique de température et d'humidité de base, le **DHT11**, est fourni dans ce kit.
Il utilise un capteur d'humidité capacitif et une thermistance pour mesurer l'air ambiant et fournit un signal numérique sur les broches de données (aucune broche d'entrée analogique n'est nécessaire).

* :ref:`cpn_dht11`

**Composants requis**

Dans ce projet, nous avons besoin des composants suivants.

Il est plus pratique d'acheter un kit complet, voici le lien :

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
        - :ref:`cpn_dht11`
        - 1
        - |link_dht22_buy|

**Schéma**

|sch_dht11|

**Câblage**

|wiring_dht11|

**Code**

.. note::

    * Vous pouvez ouvrir le fichier ``6.2_dht11.ino`` sous le chemin ``kepler-kit-main/arduino/6.2_dht11``. 
    * Ou copiez ce code dans l'**Arduino IDE**.
    * Ensuite, sélectionnez la carte Raspberry Pi Pico et le port correct avant de cliquer sur le bouton Upload.
    * La bibliothèque ``DHT sensor library`` est utilisée ici, vous pouvez l'installer via le **Gestionnaire de Bibliothèques**.

      .. image:: img/lib_dht.png

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/b9e96e99-59d4-48ca-b41f-c03577acfb8f/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Après l'exécution du code, vous verrez le Moniteur Série afficher en continu la température et l'humidité, et au fur et à mesure que le programme fonctionne de manière stable, ces deux valeurs deviendront de plus en plus précises.

**Comment ça fonctionne ?**

#. Inclusion des bibliothèques nécessaires et définition des constantes.
   Cette partie du code inclut la bibliothèque du capteur DHT et définit le numéro de broche et le type de capteur utilisés dans ce projet.

   .. code-block:: arduino
    
      #include <DHT.h>
      #define DHTPIN 16       // Définir la broche utilisée pour connecter le capteur
      #define DHTTYPE DHT11  // Définir le type de capteur

#. Création de l'objet DHT.
   Ici, nous créons un objet DHT en utilisant le numéro de broche et le type de capteur définis.

   .. code-block:: arduino

      DHT dht(DHTPIN, DHTTYPE);  // Créer un objet DHT

#. Cette fonction est exécutée une fois lorsque l'Arduino démarre. Nous initialisons la communication série et le capteur DHT dans cette fonction.

   .. code-block:: arduino

      void setup() {
        Serial.begin(9600);
        Serial.println(F("DHT11 test!"));
        dht.begin();  // Initialiser le capteur DHT
      }

#. Boucle principale.
   La fonction ``loop()`` s'exécute en continu après la fonction setup. Ici, nous lisons les valeurs d'humidité et de température, calculons l'indice de chaleur, et affichons ces valeurs sur le moniteur série. Si la lecture du capteur échoue (retourne NaN), un message d'erreur est imprimé.

   .. note::
    
      L'|link_heat_index| est une manière de mesurer la sensation de chaleur extérieure en combinant la température de l'air et l'humidité. On l'appelle également la "température ressentie" ou "température apparente".

   .. code-block:: arduino

      void loop() {
        delay(2000);
        float h = dht.readHumidity();
        float t = dht.readTemperature();
        float f = dht.readTemperature(true);
        if (isnan(h) || isnan(t) || isnan(f)) {
          Serial.println(F("Failed to read from DHT sensor!"));
          return;
        }
        float hif = dht.computeHeatIndex(f, h);
        float hic = dht.computeHeatIndex(t, h, false);
        Serial.print(F("Humidity: "));
        Serial.print(h);
        Serial.print(F("%  Temperature: "));
        Serial.print(t);
        Serial.print(F("°C "));
        Serial.print(f);
        Serial.print(F("°F  Heat index: "));
        Serial.print(hic);
        Serial.print(F("°C "));
        Serial.print(hif);
        Serial.println(F("°F"));
      }
