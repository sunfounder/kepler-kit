.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez au cœur des univers Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Remises spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et cadeaux** : Participez à des promotions spéciales et à des tirages au sort festifs.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _cpn_ta6586:

TA6586 - Puce de commande de moteur
=======================================

|img_ta6586|

Le TA6586 est un CI monolithique conçu pour piloter des moteurs à courant 
continu bidirectionnels. Il dispose de deux broches d'entrées logiques 
permettant de contrôler la direction du moteur, en marche avant et arrière. 
Le circuit offre une bonne performance anti-interférence, un faible courant 
de veille et une faible chute de tension de saturation en sortie. Il intègre 
une diode de protection pour compenser l'impact du courant de décharge des 
charges inductives, garantissant ainsi un usage sûr et fiable pour le pilotage 
de relais, moteurs à courant continu, moteurs pas à pas ou pour la gestion 
d'alimentations de commutation. Le TA6586 est idéal pour les véhicules jouets, 
les moteurs d'avions télécommandés, les moteurs de vannes automatiques, les 
entraînements de serrures électromagnétiques, les instruments de précision et 
d'autres circuits.

**Caractéristiques**

* Faible courant de veille : ≦2uA
* Large plage de tension d'alimentation
* Fonction de frein intégrée
* Protection contre la surchauffe
* Limitation de courant et protection contre les courts-circuits
* Boîtier DIP8 sans plomb

**Fonction des broches**

|img_ta6586_pin|


**Table de vérité des entrées**

|img_ta6586_priciple|


**Exemple**

* :ref:`py_motor` (pour les utilisateurs de MicroPython)
* :ref:`ar_motor` (pour les utilisateurs d'Arduino)
* :ref:`py_pump` (pour les utilisateurs de MicroPython)
* :ref:`ar_pump` (pour les utilisateurs d'Arduino)
* :ref:`per_smart_fan` (pour les utilisateurs de Piper Make)
