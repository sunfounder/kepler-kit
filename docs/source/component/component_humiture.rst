.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Avant-premières exclusives** : Profitez d'un accès anticipé aux annonces de nouveaux produits et aux aperçus en avant-première.
    - **Remises spéciales** : Bénéficiez de réductions exclusives sur nos nouveaux produits.
    - **Promotions et cadeaux festifs** : Participez à des promotions spéciales et à des tirages au sort pour les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _cpn_dht11:

Capteur de température et d'humidité DHT11
==============================================

Le capteur numérique de température et d'humidité DHT11 est un capteur composite qui fournit une sortie de signal numérique calibrée pour la température et l'humidité. 
La technologie de collecte numérique dédiée et la technologie de détection de température et d'humidité sont appliquées pour garantir une haute fiabilité et une excellente stabilité à long terme.

Le capteur comprend un composant résistif de détection d'humidité et un dispositif de mesure de température NTC, le tout relié à un microcontrôleur 8 bits haute performance.

.. Le schéma du module capteur de température et d'humidité est présenté ci-dessous : |img_Hum-sch| 

Seules trois broches sont disponibles : VCC, GND et DATA. 
Le processus de communication commence avec la ligne DATA envoyant un signal de départ au DHT11, qui le reçoit et renvoie un signal de réponse. 
Ensuite, l'hôte reçoit le signal de réponse et commence à recevoir 40 bits de données de température et d'humidité (8 bits pour l'humidité entière + 8 bits pour l'humidité décimale + 8 bits pour la température entière + 8 bits pour la température décimale + 8 bits pour la somme de contrôle).

|img_Dht11|

**Caractéristiques**

    #. Plage de mesure de l'humidité : 20 - 90%RH
    #. Plage de mesure de la température : 0 - 60℃
    #. Sortie de signaux numériques indiquant la température et l'humidité
    #. Tension de fonctionnement : DC 5V ; Taille du PCB : 2,0 x 2,0 cm
    #. Précision de la mesure de l'humidité : ±5%RH
    #. Précision de la mesure de la température : ±2℃

* `DHT11 Datasheet <http://wiki.sunfounder.cc/images/c/c7/DHT11_datasheet.pdf>`_

**Exemple**


* :ref:`py_dht11` (pour les utilisateurs de MicroPython)
* :ref:`ar_dht11` (pour les utilisateurs d'Arduino)
