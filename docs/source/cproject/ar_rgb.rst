.. _ar_rgb:

2.4 - カラフルな光
==============================================

私たちは知っているとおり、光は重ね合わせることができます。例えば、青い光と緑の光を混ぜるとシアン色の光ができ、赤い光と緑の光を混ぜると黄色の光ができます。
このことを「加法的色の混合」と呼びます。

* `加法的色 - ウィキペディア <https://en.wikipedia.org/wiki/Additive_color>`_

この方法に基づいて、異なる比重で三原色を混合することで、任意の色の可視光を作成することができます。例えば、赤を多く、緑を少なくすることでオレンジ色を作ることができます。

この章では、RGB LEDを使用して加法的色の混合の神秘を探究します！

RGB LEDは、赤、緑、青のLEDを一つのランプキャップの下に封入し、三つのLEDは共通のカソードピンを共有しています。
各アノードピンに電気信号が供給されるため、対応する色の光が表示されます。各アノードの電気信号の強度を変更することで、さまざまな色を生成することができます。

* :ref:`cpn_rgb`

**必要なコンポーネント**

このプロジェクトでは、以下のコンポーネントが必要です。

全体のキットを購入すると非常に便利です。リンクはこちらです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットに含まれるアイテム
        - 購入リンク
    *   - ケプラーキット	
        - 450+
        - |link_kepler_kit|

以下のリンクから個別に購入することもできます。

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - コンポーネント紹介	
        - 数量
        - 購入リンク

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
        - 3（1-330Ω, 2-220Ω）
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_rgb`
        - 1
        - |link_rgb_led_buy|

**回路図**

|sch_rgb|

PWMピンGP13、GP14、GP15はそれぞれRGB LEDの赤、緑、青のピンを制御し、共通のカソードピンをGNDに接続します。これにより、異なるPWM値でこれらのピンに光を重ね合わせることで、RGB LEDが特定の色を表示することができます。

**配線**

|img_rgb_pin|

RGB LEDには4本のピンがあります：最も長いピンが共通のカソードピンで、通常はGNDに接続され、最も長いピンの隣の左側のピンが赤で、右側の2本のピンが緑と青です。

|wiring_rgb|


**コード**

ここで、お気に入りの色を描画ソフトウェア（例：ペイント）で選択し、RGB LEDで表示させることができます。

.. note::

   * ファイル ``2.4_colorful_light.ino`` は、パス ``kepler-kit-main/arduino/2.4_colorful_light`` で開くことができます。
   * または、このコードを **Arduino IDE** にコピーしてください。

   * **アップロード** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と正確なポートを選択してください。

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/c869191c-026c-4aac-8396-09eaf6ee2204/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

|img_take_color|

``color_set()`` にRGB値を入力すると、RGBが希望する色に光るようになります。

**どうやって動くのか？**

この例では、RGBの三つのピンに値を割り当てるために使用される関数は、独立したサブ関数 ``color()`` にパッケージされています。

.. code-block:: C

    void color (unsigned char red, unsigned char green, unsigned char blue)
    {
        analogWrite(redPin, red);
        analogWrite(greenPin, green);
        analogWrite(bluePin, blue);
    }

``loop()`` 内では、RGB値が入力引数として ``color()`` 関数を呼び出すことで、RGBが異なる色を発するようになります。

.. code-block:: C

    void loop() 
    {    
        color(255, 0, 0); //  red 
        delay(1000); 
        color(0,255, 0); //  green  
        delay(1000);  
        color(0, 0, 255); //  blue  
        delay(1000);
    }
