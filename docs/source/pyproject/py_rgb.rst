.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _py_rgb:

2.4 カラフルな光  
==============================================  
  
我々が知っているように、光は重ね合わせることができます。例えば、青い光と緑の光を混ぜるとシアン色の光が生まれ、赤い光と緑の光を混ぜると黄色の光が生まれます。  
これを「加法混色」と呼びます。

* `加法混色 - ウィキペディア <https://en.wikipedia.org/wiki/Additive_color>`_

この方法に基づいて、三原色を用いて、異なる比重に応じて任意の色の可視光を混合することができます。例えば、オレンジ色は赤色を多く、緑色を少なくして作ることができます。

この章では、RGB LEDを用いて加法混色の神秘を探求します！

RGB LEDは、赤いLED、緑のLED、青いLEDを一つのランプキャップの下に封入し、三つのLEDは一つのカソードピンを共有しています。  
各アノードピンに電気信号が供給されるため、対応する色の光が表示されます。各アノードの電気信号強度を変更することで、さまざまな色を生成することができます。

* :ref:`cpn_rgb`

**必要なコンポーネント**

このプロジェクトでは、以下のコンポーネントが必要です。

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

以下のリンクから個別に購入することも可能です。

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
        - マイクロUSBケーブル
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
        - :ref:`cpn_resistor`
        - 3(1-330Ω, 2-220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_rgb`
        - 1
        - |link_rgb_led_buy|


**回路図**

|sch_rgb|

PWMピンのGP13、GP14、およびGP15は、RGB LEDの赤、緑、青のピンをそれぞれ制御します。共通のカソードピンはGNDに接続されます。これにより、RGB LEDは異なるPWM値でこれらのピンに光を加算することで、特定の色を表示できます。

**配線**

|img_rgb_pin|

RGB LEDには4つのピンがあります：一番長いピンは共通のカソードピンで、通常はGNDに接続されます。この長いピンの隣にある左側のピンが赤で、右側にある2つのピンは緑と青です。

|wiring_rgb|

**コード**

.. note::

    * ``kepler-kit-main/micropython`` ディレクトリ内の ``2.4_colorful_light.py`` ファイルを開くか、このコードをThonnyにコピペして、「Run Current Script」をクリック、またはF5キーを押して実行します。
    
    * 右下角にある「MicroPython（Raspberry Pi Pico）」インタープリターをクリックして選択してください。

    * 詳細なチュートリアルは、 :ref:`open_run_code_py` を参照してください。

.. code-block:: python

    import machine
    import utime

    red = machine.PWM(machine.Pin(13))
    green = machine.PWM(machine.Pin(14))
    blue = machine.PWM(machine.Pin(15))
    red.freq(1000)
    green.freq(1000)
    blue.freq(1000)

    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def color_to_duty(rgb_value):
        rgb_value = int(interval_mapping(rgb_value, 0, 255, 0, 65535))
        return rgb_value

    def color_set(red_value, green_value, blue_value):
        red.duty_u16(color_to_duty(red_value))
        green.duty_u16(color_to_duty(green_value))
        blue.duty_u16(color_to_duty(blue_value))

    color_set(255, 128, 0)

こちらでは、描画ソフト（例：ペイント）で好みの色を選び、RGB LEDでその色を表示できます。

|img_take_color|

``color_set()`` 関数にRGB値を入力すると、選択した色でRGB LEDが点灯します。

**仕組みについて**

三原色を統合して機能するように、 ``color_set()`` 関数を定義しています。

現在、コンピュータのハードウェアピクセルは通常24ビットで表現されます。各基本色は8ビットに分けられ、色値は0から255までです。0を含めて各基本色に256の可能な組み合わせがあります。よって、256 x 256 x 256 = 16,777,216色が可能です。
``color_set()`` 関数も24ビット表記を使用しているため、色の選択が容易です。

そして、 ``duty_u16()`` の値域が0〜65535であるため、PWMを通じてRGB LEDに信号を出力する際には、 ``color_to_duty()`` と ``interval_mapping()`` 関数を用いて色値をduty値にマッピングしています。
