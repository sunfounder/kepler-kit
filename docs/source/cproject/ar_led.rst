.. _ar_led:

2.1 - こんにちは、LED！
=======================================

「Hello, world!」を出力することがプログラミング学習の第一歩であるように、LEDを制御するプログラムを使用することは、物理的なプログラミングを学ぶ際の伝統的な入門です。

* :ref:`cpn_led`

**必要なコンポーネント**

このプロジェクトには、以下のコンポーネントが必要です。

全体のキットを購入するのが便利です、以下がリンクです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットに含まれるアイテム
        - 購入リンク
    *   - ケプラーキット
        - 450以上
        - |link_kepler_kit|

以下のリンクから個別にも購入可能です。

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - コンポーネントの説明
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

この回路の原理はシンプルであり、図には電流の方向が示されています。GP15が高レベル（3.3V）を出力すると、220Ωの電流制限抵抗を経てLEDが点灯します。GP15が低レベル（0V）を出力すると、LEDは消灯します。

**配線**

|wiring_led|

電流の方向に沿って回路を組み立てましょう！

1. ここでは、Pico WボードのGP15ピンからの電気信号を使用してLEDを動作させ、この回路はここから始まります。
#. 電流は220Ωの抵抗器（LEDを保護するために使用）を通過する必要があります。抵抗器の一方の端（どちらでもよい）をPico W GP15ピンと同じ行（私の回路では行20）に挿入し、もう一方の端をブレッドボードの空いている行（私の回路では行24）に挿入します。
#. LEDを取り上げると、一方のリードがもう一方よりも長いことに気づくでしょう。抵抗器の端と同じ行に長いリードを挿入し、短いリードをブレッドボードの中央のギャップを越えて同じ行に接続します。
#. 男性対男性（M2M）ジャンパーワイヤーをLEDの短いピンと同じ行に挿入し、次にそれをブレッドボードの負の電源バスに接続します。
#. ジャンパーを使用して、負の電源バスをPico WのGNDピンに接続します。

**コード**

.. note::

   * ファイル ``2.1_hello_led.ino`` は、パス ``kepler-kit-main/arduino/2.1_hello_led`` の下で開くことができます。
   * または、このコードを **Arduino IDE** にコピーしてください。
   
   * **アップロード** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と正確なポートを選択することを忘れないでください。



.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/898b8ba7-9bdf-468d-9181-ca8535e8dca6/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


コードが実行された後、LEDが点滅するのが見えます。

**仕組みは？**

ここでは、LEDをデジタルピン15に接続していますので、プログラムの最初で「ledPin」という名前のint変数を宣言し、その値として15を割り当てる必要があります。

.. code-block:: C

    const int ledPin = 15;


次に、 ``setup()`` 関数内でピンを初期化します。ここでは、ピンを ``OUTPUT`` モードに初期化する必要があります。

.. code-block:: C

    void setup() {
        pinMode(ledPin, OUTPUT);
    }

``loop()`` 内で、 ``digitalWrite()`` を使用してledPinに3.3Vの高レベル信号を供給します。これにより、LEDのピン間に電圧差が生じ、LEDが点灯します。

.. code-block:: C

    digitalWrite(ledPin, HIGH);

レベル信号がLOWに変更されると、ledPinの信号は0Vに戻り、LEDが消灯します。

.. code-block:: C

    digitalWrite(ledPin, LOW);

点灯と消灯の間には間隔が必要ですので、 ``delay(1000)`` コードを使用して、コントローラーが1000ms何もしないようにします。

.. code-block:: C

    delay(1000); 
