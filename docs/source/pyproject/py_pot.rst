.. _py_pot:

2.11 ノブを回してみよう
===========================

以前のプロジェクトでは、Pico Wのデジタル入力を使用していました。
たとえば、ボタンでピンのレベルを低（オフ）から高（オン）に変えることができます。これはバイナリの動作状態です。

しかし、Pico Wは別のタイプの入力信号、すなわちアナログ入力も受け取ることができます。
完全に閉じている状態から完全に開いている状態まで、様々な値をとることができます。
アナログ入力により、マイクロコントローラは物理世界の光強度、音強度、温度、湿度などを感知することができます。

通常、マイクロコントローラにはアナログ入力を実装するための追加ハードウェア、すなわちアナログ-デジタルコンバータ（ADC）が必要です。
しかし、Pico W自体にはADCが組み込まれているので、直接使用することができます。

|pin_adc|

Pico Wにはアナログ入力が使用できるGPIOピンが3つあります：GP26、GP27、GP28。つまり、アナログチャンネル0、1、2です。
さらに、内蔵温度センサに接続された第4のアナログチャンネルもありますが、ここでは紹介しません。

このプロジェクトでは、ポテンショメータのアナログ値を読み取ることに挑戦します。

* :ref:`cpn_potentiometer`

**必要なコンポーネント**

このプロジェクトでは、以下のコンポーネントが必要です。

全体のキットを購入することは確かに便利です、以下がそのリンクです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットに含まれるアイテム
        - リンク
    *   - ケプラーキット
        - 450以上
        - |link_kepler_kit|

下記のリンクから別々にも購入することができます。

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
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
        - :ref:`cpn_resistor`
        - 1(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_potentiometer`
        - 1
        - |link_potentiometer_buy|


**回路図**

|sch_pot|

ポテンショメータはアナログデバイスであり、2つの異なる方向に回転させることができます。

ポテンショメータの中央のピンをアナログピンGP28に接続します。Raspberry Pi Pico Wは、マルチチャネル、16ビットのアナログ-デジタルコンバータを搭載しています。これにより、入力電圧が0から動作電圧（3.3V）の間で0から65535の整数値にマッピングされます。したがって、GP28の値の範囲は0から65535です。

計算式は以下の通りです。

    (Vp/3.3V) x 65535 = Ap

次に、GP28（ポテンショメータ）の値をGP15（LED）のPWM値としてプログラムします。
これにより、ポテンショメータを回転させると、LEDの明るさも同時に変化することがわかります。

**配線**

|wiring_pot|

**コード**

.. note::

    * ``kepler-kit-main/micropython`` のパスの下にある ``2.11_turn_the_knob.py`` ファイルを開くか、このコードをThonnyにコピーして、"Run Current Script"をクリックするかF5キーを押して実行します。

    * 右下隅にある"MicroPython（Raspberry Pi Pico）"インタプリタをクリックするのを忘れないでください。

    * 詳細なチュートリアルは、 :ref:`open_run_code_py` を参照してください。

.. code-block:: python

    import machine
    import utime

    potentiometer = machine.ADC(28)
    led = machine.PWM(machine.Pin(15))
    led.freq(1000)

    while True:
        value = potentiometer.read_u16()
        print(value)
        led.duty_u16(value)
        utime.sleep_ms(200)

プログラムが動作しているとき、シェルでGP28ピンが現在読み取っているアナログ値を確認できます。
ノブを回すと、その値は0から65535に変化します。
同時に、アナログ値が増加するにつれて、LEDの明るさも増加します。

**動作原理は？**

.. code-block:: python

    potentiometer = machine.ADC(28)

この例では、idによって識別されたソースに関連付けられたADCにアクセスします。この場合、それはGP28です。

.. code-block:: python

    potentiometer.read_u16()

アナログ読み取りを行い、0〜65535の範囲の整数を返します。返り値は、ADCによって取られた生の読み取り値を表し、最小値が0で最大値が65535になるようにスケーリングされています。

* `machine.ADC - MicroPython Docs <https://docs.micropython.org/en/latest/library/machine.ADC.html>`_

