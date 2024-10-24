.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Avant-premières exclusives** : Profitez d'un accès anticipé aux annonces de nouveaux produits et aux aperçus en avant-première.
    - **Remises spéciales** : Bénéficiez de réductions exclusives sur nos nouveaux produits.
    - **Promotions et cadeaux festifs** : Participez à des promotions spéciales et à des tirages au sort pour les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _cpn_mfrc522:

Module MFRC522
====================

|img_mfrc522|

Le MFRC522 est une puce intégrée de lecture et écriture de cartes, couramment 
utilisée dans la radio à 13,56 MHz. Lancée par la société NXP, il s'agit d'une 
puce de carte sans contact à basse tension, peu coûteuse et de petite taille, 
idéale pour les instruments intelligents et les appareils portables.

Le MFRC522 utilise un concept avancé de modulation et de démodulation qui couvre 
entièrement tous les types de méthodes et protocoles de communication sans contact 
passifs à 13,56 MHz. En outre, il prend en charge l'algorithme de chiffrement 
rapide CRYPTO1 pour la vérification des produits MIFARE. Le MFRC522 supporte 
également les communications haute vitesse de la série MIFARE, avec un taux de 
transmission de données bidirectionnel pouvant atteindre 424 kbit/s. En tant que 
nouveau membre de la série de lecteurs de cartes hautement intégrés à 13,56 MHz, 
le MFRC522 est similaire aux modèles existants MF RC500 et MF RC530, mais présente 
également des différences notables. Il communique avec la machine hôte de manière 
sérielle, nécessitant moins de câblage. Vous pouvez choisir entre les modes SPI, 
I2C et UART série (similaire au RS232), ce qui permet de simplifier la connexion, 
d'économiser de l'espace sur la carte PCB (format plus compact) et de réduire les coûts.

* `MFRC522 Data sheet <https://www.nxp.com/docs/en/data-sheet/MFRC522.pdf>`_


**Exemple**


* :ref:`py_rfid` (pour les utilisateurs de MicroPython)
* :ref:`py_music_player` (pour les utilisateurs de MicroPython)
* :ref:`ar_rfid` (pour les utilisateurs d'Arduino)
