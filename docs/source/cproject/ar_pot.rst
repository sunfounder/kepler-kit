.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _ar_pot:

2.11 - ノブを回す
===========================

前回のプロジェクトでは、Pico Wのデジタル入力を使用しました。
たとえば、ボタンはピンを低レベル（オフ）から高レベル（オン）に変更できます。これは2値の動作状態です。

しかし、Pico Wは別のタイプの入力信号、つまりアナログ入力も受け取ることができます。
完全に閉じた状態から完全に開いた状態まで、任意の状態になることができ、可能な値の範囲があります。
アナログ入力によって、マイクロコントローラは物理世界の光強度、音強度、温度、湿度などを感知できます。

通常、マイクロコントローラにはアナログ入力を実装するための追加ハードウェア、すなわちアナログ-デジタル変換器（ADC）が必要です。
しかし、Pico W自体には直接使用できる内蔵ADCがあります。

|pin_adc|

Pico Wには、アナログ入力を使用できるGPIOピンが3つあります、GP26、GP27、GP28。すなわち、アナログチャンネル0、1、2です。
さらに、内蔵の温度センサーに接続された第4のアナログチャンネルもありますが、ここでは紹介しません。

このプロジェクトでは、ポテンショメータのアナログ値を読み取ろうとしています。

* :ref:`cpn_potentiometer`

**必要なコンポーネント**

このプロジェクトに必要なコンポーネントは以下の通りです。

一式をまとめて購入すると便利です、そのためのリンクはこちら：

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

ポテンショメータはアナログデバイスであり、2つの異なる方向に回すことができます。

ポテンショメータの中央のピンをアナログピンGP28に接続します。Raspberry Pi Pico Wには、マルチチャンネル、16ビットのアナログ-デジタル変換器が含まれています。これは、入力電圧を0から動作電圧（3.3V）の間で0から65535までの整数値にマッピングすることを意味します。したがって、GP28の値は0から65535までの範囲です。

以下に計算式を示します。

    (Vp/3.3V) x 65535 = Ap

次に、GP28（ポテンショメータ）の値をGP15（LED）のPWM値としてプログラムします。
このようにすると、ポテンショメータを回すことで、LEDの明るさも同時に変わることがわかります。

**配線**

|wiring_pot|



**コード**

.. note::

   * ファイル ``2.11_turn_the_knob.ino`` は、パス ``kepler-kit-main/arduino/2.11_turn_the_knob`` の下で開くことができます。
   * または、このコードを **Arduino IDE** にコピーしてください。

   * **Upload** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と正確なポートを選択することを忘れないでください。

プログラムが実行されているとき、シリアルモニターでGP28ピンによって現在読み取られているアナログ値を見ることができます。
ノブを回すと、値は0から1023まで変わります。
同時に、アナログ値が増加するにつれて、LEDの明るさも増加します。

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/b3e3927a-bd1a-4756-83f2-141d47f99b1c/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

**どのように動作するか？**

シリアルモニターを有効にするには、 ``setup()`` でシリアル通信を開始し、データレートを9600に設定する必要があります。

.. code-block:: arduino
    :emphasize-lines: 3

    void setup() {
        pinMode(ledPin, OUTPUT);
        Serial.begin(9600);
    }

* `Serial <https://www.arduino.cc/reference/en/language/functions/communication/serial/>`_

ループ関数では、ポテンショメータの値を読み取り、その値を0-1023から0-255にマッピングし、最終的にマッピング後の値を使用してLEDの明るさを制御します。

.. code-block:: arduino

    void loop() {
        int sensorValue = analogRead(sensorPin);
        Serial.println(sensorValue);
        int brightness = map(sensorValue, 0, 1023, 0, 255);
        analogWrite(ledPin, brightness);
    }

* `analogRead() <https://www.arduino.cc/reference/en/language/functions/analog-io/analogread/>`_  は、sensorPin（ポテンショメータ）の値を読み取り、変数 ``sensorValue`` に割り当てるために使用されます。

.. code-block:: arduino

    int sensorValue = analogRead(sensorPin);

* シリアルモニターでSensorValueの値を表示します。

.. code-block:: arduino

    Serial.println(sensorValue);

* ここで、 `map(value, fromLow, fromHigh, toLow, toHigh) <https://www.arduino.cc/reference/en/language/functions/analog-io/analogread/>`_ 関数が必要です。ポテンショメータで読み取られる値は0-1023の範囲であり、PWMピンの値は0-255の範囲です。この関数は、値を別の範囲に再マッピングするために使用されます。

.. code-block:: arduino

    int brightness = map(sensorValue, 0, 1023, 0, 255);

* これで、この値を使用してLEDの明るさを制御できます。

.. code-block:: arduino

    analogWrite(ledPin, brightness);
