.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Avant-premières exclusives** : Profitez d'un accès anticipé aux annonces de nouveaux produits et aux aperçus en avant-première.
    - **Remises spéciales** : Bénéficiez de réductions exclusives sur nos nouveaux produits.
    - **Promotions et cadeaux festifs** : Participez à des promotions spéciales et à des tirages au sort pour les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _cpn_i2c_lcd:

I2C LCD1602
==================

|i2c_lcd1602|

* **GND** : Masse
* **VCC** : Alimentation, 5V
* **SDA** : Ligne de données série. Connecter à VCC via une résistance de pull-up.
* **SCL** : Ligne d'horloge série. Connecter à VCC via une résistance de pull-up.

Comme nous le savons tous, bien que les écrans LCD et d'autres affichages enrichissent considérablement l'interaction homme-machine, ils partagent une faiblesse commune. Lorsqu'ils sont connectés à un contrôleur, plusieurs E/S sont occupées, ce qui limite les autres fonctions du contrôleur, surtout si celui-ci ne dispose pas de nombreux ports externes.

C'est pourquoi le LCD1602 avec un module I2C a été développé pour résoudre ce problème. Le module I2C intègre une puce PCF8574 qui convertit les données série I2C en données parallèles pour l'affichage sur le LCD.

* `PCF8574 Datasheet <https://www.ti.com/lit/ds/symlink/pcf8574.pdf?ts=1627006546204&ref_url=https%253A%252F%252Fwww.google.com%252F>`_

**Adresse I2C**

L'adresse par défaut est généralement 0x27, mais dans certains cas, elle peut être 0x3F.

En prenant l'adresse par défaut 0x27 comme exemple, l'adresse du périphérique peut être modifiée en reliant les points A0/A1/A2 ; à l'état par défaut, A0/A1/A2 est à 1, et si le point de connexion est relié, A0/A1/A2 passe à 0.

|i2c_address|

**Rétroéclairage/Contraste**

Le rétroéclairage peut être activé via un cavalier ; retirez le cavalier pour désactiver le rétroéclairage. Le potentiomètre bleu au dos sert à ajuster le contraste (le rapport de luminosité entre le blanc le plus lumineux et le noir le plus foncé).

|back_lcd1602|

* **Cavalier** : Le rétroéclairage peut être activé avec ce cavalier, retirez-le pour désactiver le rétroéclairage.
* **Potentiomètre** : Il permet de régler le contraste (la clarté du texte affiché), qui augmente dans le sens horaire et diminue dans le sens antihoraire.

**Exemple**

* :ref:`py_lcd` (pour les utilisateurs de MicroPython)
* :ref:`py_room_temp` (pour les utilisateurs de MicroPython)
* :ref:`py_guess_number` (pour les utilisateurs de MicroPython)
* :ref:`ar_lcd` (pour les utilisateurs d'Arduino)
