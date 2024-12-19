.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _projects_micropython:

MicroPythonプロジェクト
============================

このセクションでは、MicroPythonの基礎を学びます。歴史から始まり、Pico Wへのインストール、基本的な構文の習得、そしてステップバイステップで進める実践的なプロジェクトを通じてMicroPythonをマスターします。

学習効果を最大化するために、章を順番に読むことをお勧めします。  


**ソースコード**

* :download:`SunFounder Kepler Kit <https://github.com/sunfounder/kepler-kit/archive/refs/heads/main.zip>`

* または `Kepler Kit - GitHub <https://github.com/sunfounder/kepler-kit>`_ でコードを確認してください。


1. 始めましょう
------------------------
MicroPythonの基礎を学び、開発環境をセットアップします。Thonnyのインストール、Pico WへのMicroPythonのアップロード、基本的な構文の探索を含みます。  


.. toctree::
    :maxdepth: 1

    python_start/introduction_micropython
    python_start/install_thonny
    python_start/install_micropython_to_pico
    python_start/upload_libraries
    python_start/quick_guide_thonny
    python_start/syntax/micropython_basic_syntax



2. 出力＆入力
----------------------
LEDやボタン、センサーなどの出力デバイスと入力デバイスの扱い方を学びます。この章では、実践的なプロジェクトを通じてフィジカルコンピューティングの基礎を紹介します。  


.. toctree::
    :maxdepth: 1

    py_led
    py_led_bar
    py_fade
    py_rgb
    py_button
    py_tilt
    py_slide
    py_micro
    py_reed
    py_pir
    py_pot
    py_photoresistor
    py_temp
    py_water
    py_transistor
    py_relay

3. サウンド＆ディスプレイ＆ムーブメント
----------------------------------------
ブザー、NeoPixel LED、LCDスクリーン、モーター、ポンプ、サーボなどのモジュールを使いこなします。音、ビジュアル、動きを生み出すインタラクティブなプロジェクトを作成しましょう。  

.. toctree::
    :maxdepth: 1

    py_ac_buz
    py_pa_buz
    py_neopixel
    py_lcd
    py_motor
    py_pump
    py_servo

4. コントローラー
----------------------
ジョイスティック、キーパッド、タッチセンサーなどのコントローラーを使用して、プロジェクトにインタラクティブ性と複雑さを加えます。  

.. toctree::
    :maxdepth: 1

    py_joystick
    py_keypad
    py_mpr121

5. マイクロチップ
------------------

74HC595シフトレジスタを使用したマイクロチップベースのプロジェクトに取り組みます。LED、7セグメントディスプレイ、ドットマトリックスなどを高度な技術で制御します。  

.. toctree::
    :maxdepth: 1

    py_74hc595_led
    py_74hc595_7seg
    py_74hc595_4dig
    py_74hc595_matrix

6. 高度なプロジェクト
----------------------

超音波センサー、DHT11温湿度モジュール、MPU6050ジャイロスコープ、RFIDリーダーなどの高度なコンポーネントを使用してプロジェクトを次のレベルに引き上げます。  


.. toctree::
    :maxdepth: 1

    py_ultrasonic
    py_dht11
    py_mpu6050
    py_irremote
    py_rfid

7. 楽しいプロジェクト
----------------------
光テルミン、乗客カウンター、RFID音楽プレーヤー、体感コントローラーなど、スキルを活用してエキサイティングで実用的なアプリケーションを構築します。これらのプロジェクトは楽しく教育的です。  


.. toctree::
    :maxdepth: 1

    py_light_theremin
    py_room_temp_meter
    py_alarm_siren_lamp
    py_passenger_counter
    py_game_10_second
    py_traffic_light
    py_game_guess_number
    py_rfid_music_player
    py_fruit_piano
    py_reversing_aid
    py_somatosensory_controller
    py_digital_bubble_level

8. IoTプロジェクト
------------------------
Pico Wをインターネットに接続し、IoT（モノのインターネット）の世界を探検します。CheerLights、天気モニター、MQTTベースの通信システム、さらには植物モニタリングシステムなどのプロジェクトを構築します。  

.. toctree::
    :maxdepth: 1

    iotproject/1.access
    iotproject/2.cheerlight
    iotproject/3.ifttt_mail
    iotproject/4.openweather
    iotproject/5.mqtt_pub
    iotproject/6.mqtt_sub
    iotproject/7.web_page
    iotproject/8.anvil
    iotproject/9.sunfounder_controller
    iotproject/10.plant_monitor
