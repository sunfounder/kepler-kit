.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _py_servo:

3.7 サーボの振動
===================

このキットには、LEDやパッシブブザーに加えて、PWM信号で制御されるデバイス、サーボも含まれています。

サーボは、位置（角度）制御が可能なデバイスであり、一定の角度変更が必要な制御システムに適しています。高級リモコン玩具、例えば飛行機、潜水艦モデル、リモコンロボットなどで広く利用されています。

それでは、サーボを振動させてみましょう！

* :ref:`cpn_servo`

**必要なコンポーネント**

このプロジェクトには以下のコンポーネントが必要です。

一式をまとめて購入するのは非常に便利です。リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名称	
        - このキットに含まれるアイテム
        - リンク
    *   - ケプラーキット	
        - 450+
        - |link_kepler_kit|

以下のリンクから個別に購入することもできます。

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - コンポーネント	
        - 個数
        - リンク

    *   - 1
        - :ref:`cpn_pico_w`
        - 1
        - |link_picow_buy|
    *   - 2
        - Micro USBケーブル
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - 数本
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_servo`
        - 1
        - |link_servo_buy|

**回路図**

|sch_servo|

**配線**

|wiring_servo|

* オレンジ色のワイヤーは信号で、GP15に接続されています。
* 赤色のワイヤーはVCCで、VBUS(5V)に接続されています。
* 茶色のワイヤーはGNDで、GNDに接続されています。

**コード**

.. note::

    * ``kepler-kit-main/micropython`` のパス下にある ``3.7_swinging_servo.py`` ファイルを開くか、このコードをThonnyにコピペして、「Run Current Script」をクリックまたはF5キーを押して実行します。

    * 右下角にある「MicroPython（Raspberry Pi Pico）」インタープリターをクリックして選択してください。

    * 詳細なチュートリアルは、 :ref:`open_run_code_py` を参照してください。

.. code-block:: python

    import machine
    import utime

    servo = machine.PWM(machine.Pin(15))
    servo.freq(50)

    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def servo_write(pin, angle):
        pulse_width = interval_mapping(angle, 0, 180, 0.5, 2.5)
        duty = int(interval_mapping(pulse_width, 0, 20, 0, 65535))
        pin.duty_u16(duty)

    while True:
        for angle in range(180):
            servo_write(servo, angle)
            utime.sleep_ms(20)
        for angle in range(180, -1, -1):
            servo_write(servo, angle)
            utime.sleep_ms(20)

プログラムが実行中のとき、サーボアームが0°から180°まで前後に振動するのが見えます。

``while True`` ループによってプログラムは絶えず動作していますので、プログラムを終了するにはStopボタンを押す必要があります。

**動作原理は？**

サーボを動かすために ``servo_write()`` 関数を定義しました。

この関数には二つのパラメーターがあります：

* ``pin`` 、サーボを制御するGPIOピン。
* ``Angle`` 、軸の出力角度。

この関数内で、 ``interval_mapping()`` が呼び出され、角度範囲0~180をパルス幅範囲0.5~2.5msにマッピングします。

.. code-block:: python

    pulse_width = interval_mapping(angle, 0, 180, 0.5, 2.5)

なぜ0.5~2.5なのか？これはサーボの動作モードによって決定されます。

* :ref:`cpn_servo`

次に、パルス幅を周期からデューティに変換します。 ``duty_u16()`` は小数点を持つことができない（値は浮動小数点型であってはならない）ので、 ``int()`` を用いてデューティを整数型に強制変換します。

.. code-block:: python

    duty = int(interval_mapping(pulse_width, 0, 20, 0, 65535))

最後に、デューティ値を ``duty_u16()`` に書き込みます。
