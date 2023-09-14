.. _ar_fade:

2.3 - Fading LED
=====================

これまで、高レベルと低レベル（または1と0、ONとOFFとも呼ばれる）の2つの出力信号のみを使用しており、これをデジタル出力と呼びます。
しかし、実際の使用において、多くのデバイスは単純にON/OFFして動作するわけではありません。例えば、モーターの速度調整やデスクランプの明るさ調整などです。
以前は、抵抗を調整できるスライダーがこの目的を達成するために使用されていましたが、これは常に信頼性が低く非効率的です。
そのため、パルス幅変調（PWM）がこのような複雑な問題に対する実用的な解決策として登場しました。

高レベルと低レベルで構成されるデジタル出力をパルスと呼びます。これらのピンのパルス幅は、ON/OFFの速度を変更することで調整することができます。

簡単に言えば、短い期間（例えば20ms、ほとんどの人々の視覚保持時間）でLEDを点灯、消灯、再点灯させると、消灯したことに気づかないでしょうが、光の明るさはわずかに弱くなります。
この期間中にLEDが点灯している時間が多いほど、LEDの明るさが高くなります。
言い換えれば、サイクル内でパルスが広いほど、マイクロコントローラーによって出力される"電気信号強度"が大きくなります。
これがPWMがLEDの明るさ（またはモーターの速度）を制御する方法です。

* `パルス幅変調 - Wikipedia <https://ja.wikipedia.org/wiki/%E3%83%91%E3%83%AB%E3%82%B9%E5%B9%85%E5%A4%89%E8%AA%BF>`_

Pico WがPWMを使用する際に注意すべきいくつかの点があります。この画像を見てみましょう。

|pin_pwm|

Pico Wの各GPIOピンはPWMをサポートしていますが、実際には合計16個の独立したPWM出力（30個ではない）があり、左側のGP0からGP15までに分散されています。右側のGPIOのPWM出力は左側のコピーと同等です。

注意すべき点は、プログラミング中に異なる目的で同じPWMチャネルを設定しないようにすることです。（例えば、GP0とGP16は両方ともPWM_0Aです）

この知識を理解した後、Fading LEDの効果を実現してみましょう。

* :ref:`cpn_led`

**必要なコンポーネント**

このプロジェクトでは、以下のコンポーネントが必要です。

全体のキットを購入する方が確実に便利です。リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットに含まれるアイテム
        - 購入リンク
    *   - ケプラーキット
        - 450+
        - |link_kepler_kit|

以下のリンクから個別にも購入できます。

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - コンポーネントの紹介
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
        - 1(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|


**回路図**

|sch_led|

このプロジェクトは最初のプロジェクト :ref:`ar_led` と同じ回路ですが、信号タイプが異なります。最初のプロジェクトでは、GP15から直接デジタルの高レベルと低レベル（0&1）を出力してLEDを点灯または消灯させるのに対し、このプロジェクトではGP15からPWM信号を出力してLEDの明るさを制御します。

**配線**

|wiring_led|

**コード**

.. note::

   * ファイル ``2.3_fading_led.ino`` は、パス ``kepler-kit-main/arduino/2.3_fading_led``  の下で開くことができます。
   * またはこのコードを **Arduino IDE** にコピーペーストしてください。

   * **アップロード** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と正しいポートを選択することを忘れないでください。



.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/86807da4-4714-4d3c-b6af-0f1b9a62223b/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


プログラムが実行されるにつれて、LEDは徐々に明るくなります。

**動作原理**

ピン15をledPinとして宣言します。

.. code-block:: C

    const int ledPin = 15;

``loop()`` 内の ``analogWrite()`` は、ledPinに0から255までのアナログ値（PWM波）を割り当ててLEDの明るさを変更します。

.. code-block:: C

    analogWrite(ledPin, value);

forループを使用して、 ``analogWrite()`` の値を最小値（0）と最大値（255）の間で段階的に変更することができます。

.. code-block:: C

    for (int value = 0 ; value <= 255; value += 5) {
        analogWrite(ledPin, value);
    }

実験現象を明確に観察するために、forサイクルに ``delay(30)`` を追加して、明るさの変更時間を制御する必要があります。

.. code-block:: C

    for (int value = 0 ; value <= 255; value += 5) {
        analogWrite(ledPin, value);
        delay(30);
    }
