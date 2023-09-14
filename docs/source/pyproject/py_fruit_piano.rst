.. _py_fruit_piano:

7.9 フルーツピアノ
============================

電気伝導性は多くの金属物体や人体、さらには果物にも存在します。
この性質を使って、ちょっとした楽しいプロジェクト、すなわちフルーツピアノを作成することができます。
言い換えれば、私たちは触れるだけで音楽を演奏できるキーボードに果物を変えます。

|fruit_piano|

**必要なコンポーネント**

このプロジェクトには、以下のコンポーネントが必要です。

一式をまとめて買う方が便利です、こちらがそのリンクです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットに含まれるアイテム
        - リンク
    *   - Kepler Kit	
        - 450+	
        - |link_kepler_kit|

以下のリンクから個別にも購入できます。

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - 品番
        - コンポーネント	
        - 数量
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
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 4(1-1KΩ, 1-330Ω, 2-220Ω)
        - |link_resistor_buy|
    *   - 7
        - パッシブ :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|
    *   - 8
        - :ref:`cpn_rgb`
        - 1
        - |link_rgb_led_buy|
    *   - 9
        - :ref:`cpn_mpr121`
        - 1
        - 

**回路図**

|sch_fruit_piano| 

フルーツをピアノのキーに変えるには、MPR121上の電極をフルーツ（例：バナナのハンドル）に接続する必要があります。

最初に、MPR121は初期化され、各電極は現在の電荷に基づいて値を取得します。導体（人体など）が電極に触れると、電荷が移動して再調整されます。
その結果、電極の値は初期値とは異なり、メインコントロールボードに触れられたことを知らせます。
このプロセス中に、各電極の配線が安定していることを確認し、初期化時にその電荷がバランスするようにしてください。

**配線図**

|wiring_fruit_piano| 

**コード**

.. note::

    * ``kepler-kit-main/micropython`` のパスの下で ``7.9_fruit_piano.py`` ファイルを開くか、Thonnyにこのコードをコピーして、「Run Current Script」をクリックするか、F5キーを押して実行してください。

    * 右下隅の「MicroPython（Raspberry Pi Pico）」インタプリタをクリックするのを忘れないでください。

    * 詳しいチュートリアルは、 :ref:`open_run_code_py` を参照してください。

    * ここでは、 ``mpr121.py`` というライブラリを使用する必要があります。Pico Wにアップロードされたかどうか確認してください。詳細なチュートリアルは、 :ref:`add_libraries_py` を参照してください。

.. code-block:: python

    from mpr121 import MPR121
    from machine import Pin, I2C
    import time
    import urandom

    # mpr121
    i2c = I2C(1, sda=Pin(6), scl=Pin(7))
    mpr = MPR121(i2c)

    # ブザー
    NOTE_A3 = 220
    NOTE_B3 = 247
    NOTE_C4 = 262
    NOTE_D4 = 294
    NOTE_E4 = 330
    NOTE_F4 = 349
    NOTE_G4 = 392
    NOTE_A4 = 440
    NOTE_B4 = 494
    NOTE_C5 = 523
    NOTE_D5 = 587
    NOTE_E5 = 659

    buzzer = machine.PWM(machine.Pin(15))
    note = [NOTE_A3, NOTE_B3, NOTE_C4, NOTE_D4, NOTE_E4, NOTE_F4, NOTE_G4, NOTE_A4, NOTE_B4, NOTE_C5, NOTE_D5, NOTE_E5]

    def tone(pin, frequency):
        pin.freq(frequency)
        pin.duty_u16(30000)

    def noTone(pin):
        pin.duty_u16(0)

    # RGB LED
    red = machine.PWM(machine.Pin(13))
    green = machine.PWM(machine.Pin(12))
    blue = machine.PWM(machine.Pin(11))
    red.freq(1000)
    green.freq(1000)
    blue.freq(1000)

    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def lightup():
        red.duty_u16(int(urandom.uniform(0, 65535)))
        green.duty_u16(int(urandom.uniform(0, 65535)))
        blue.duty_u16(int(urandom.uniform(0, 65535)))

    def dark():
        red.duty_u16(0)
        green.duty_u16(0)
        blue.duty_u16(0)

    # メインプロジェクト
    lastState = mpr.get_all_states()
    touchMills = time.ticks_ms()
    beat = 500

    while True:
        currentState = mpr.get_all_states()
        if currentState != lastState:
            for i in range(12):
                if i in list(currentState) and not i in list(lastState):
                    tone(buzzer, note[i])
                    lightup()
                    touchMills = time.ticks_ms()
        if time.ticks_diff(time.ticks_ms(), touchMills) >= beat or len(currentState) == 0:
            noTone(buzzer)
            dark()
        lastState = currentState

プログラムが動作する前に果物に触れないでください。初期化中に正確でない参照値を取得する可能性があります。
プログラムが動作した後、果物に優しく触れると、ブザーが対応する音を鳴らし、RGBライトがランダムに一回点滅します。
