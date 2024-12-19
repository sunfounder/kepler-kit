.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _projects_arduino:

Arduinoプロジェクト
======================

このセクションでは、Pico Wを使用したArduinoプログラミングを紹介します。Arduino IDEの設定、必要なライブラリのインストール、そしてエキサイティングなプロジェクトの構築までをガイドします。詳細な説明とハンズオン演習を通じて、基本的なArduinoのハードウェアプログラミングから高度なスキルまでを習得できます。

**ソースコード**

* :download:`SunFounder Kepler Kit <https://github.com/sunfounder/kepler-kit/archive/refs/heads/main.zip>`

* または `Kepler Kit - GitHub <https://github.com/sunfounder/kepler-kit>`_ でコードを確認してください。


1. 始めましょう
------------------------
Arduino IDEを設定し、Pico Wをプログラミングする準備を整えましょう。IDEのインストール方法、Pico Wボードの設定、プロジェクトに必要なライブラリの追加方法を学びます。  

.. toctree::
    :maxdepth: 1

    arduino_start/install_arduino_ide
    arduino_start/introduce_ide
    arduino_start/install_pico_w
    arduino_start/add_libraries_ar 

2. 出力＆入力
-----------------------
LED、センサー、スイッチを使用して、出力デバイスの制御や物理的な世界からの入力の収集の基本を学びます。これらの基礎的な演習は、Arduinoプログラミングの堅実な基盤を築きます。  

.. toctree::
    :maxdepth: 1

    ar_led
    ar_led_bar
    ar_fade
    ar_rgb
    ar_button
    ar_tilt
    ar_slide
    ar_micro
    ar_reed
    ar_pir
    ar_pot
    ar_photoresistor
    ar_temp
    ar_water
    ar_transistor
    ar_relay

3. サウンド＆ディスプレイ＆ムーブメント
----------------------------------------


音を作り出し、データを表示し、動きを制御する方法を学びます。この章では、ブザー、NeoPixel LED、LCDスクリーン、モーター、ポンプ、サーボを使用したプロジェクトが含まれ、ハードウェアに命を吹き込みます。  

.. toctree::
    :maxdepth: 1

    ar_ac_buz
    ar_pa_buz
    ar_neopixel
    ar_lcd
    ar_motor
    ar_pump
    ar_servo


4. コントローラー
---------------------
ジョイスティック、キーパッド、タッチセンサーなどのコントローラーを使用して、プロジェクトにインタラクティブな機能を追加します。これらのデバイスからの入力を処理し、それを創造的な出力に変換する方法を学びます。  

.. toctree::
    :maxdepth: 1

    ar_joystick
    ar_keypad
    ar_mpr121

5. マイクロチップ
---------------------
LED制御の高度な技術や、7セグメントディスプレイ、ドットマトリックスモジュールの扱い方を学びます。この章では、少ないピンで複数の出力を効率的に処理する技術をカバーします。  

.. toctree::
    :maxdepth: 1

    ar_74hc595_led
    ar_74hc595_7seg
    ar_74hc595_4dig
    ar_74hc595_matrix

6. 高度なプロジェクト
-----------------------
超音波距離測定、DHT11を使った環境センシング、MPU6050を使った動きの追跡、RFIDやIRリモコンを使った無線通信など、高度なモジュールと概念に踏み込みます。  

.. toctree::
    :maxdepth: 1

    ar_ultrasonic
    ar_dht11
    ar_mpu6050
    ar_irremote
    ar_rfid
