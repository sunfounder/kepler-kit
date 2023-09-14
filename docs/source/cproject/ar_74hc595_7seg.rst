.. _ar_74hc_7seg:

5.2 - 数字表示
=======================

LEDセグメントディスプレイは日常生活の至る所で見かけます。
例えば、エアコンでは温度を表示するため、交通信号ではタイマーを表示するために使用されます。

LEDセグメントディスプレイは、基本的に8つのLEDで構成された装置です。そのうち、7つのストリップ状のLEDが「8」の形を形成し、もう一つは少し小さい点状のLEDが小数点としてあります。これらのLEDはa, b, c, d, e, f, g, およびdpとマークされています。それぞれには独自のアノードピンがあり、カソードは共有されています。ピンの位置は以下の図で示されています。

|img_7seg_cathode|

これは、フル動作するために同時に8つのデジタル信号で制御する必要があることを意味し、74HC595でこれを行うことができます。

* :ref:`cpn_7_segment`


**必要なコンポーネント**

このプロジェクトでは、以下のコンポーネントが必要です。

一式を購入するのが便利です、リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットに含まれるアイテム
        - 購入リンク
    *   - Kepler Kit
        - 450+
        - |link_kepler_kit|

以下のリンクから個別に購入することもできます。

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
        - :ref:`cpn_7_segment`
        - 1
        - |link_7segment_buy|
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|

**回路図**

|sch_74hc_7seg|

**配線**

|wiring_74hc_7seg|


.. list-table:: 配線
    :widths: 15 25
    :header-rows: 1

    *   - :ref:`cpn_74hc595`
        - :ref:`cpn_led` セグメントディスプレイ
    *   - Q0
        - a
    *   - Q1
        - b
    *   - Q2
        - c
    *   - Q3
        - d
    *   - Q4
        - e
    *   - Q5
        - f
    *   - Q6
        - g
    *   - Q7
        - dp

**コード**

.. note::

   * ``kepler-kit-main/arduino/5.2_number_display`` のパスの下で ``5.2_number_display.ino`` ファイルを開くことができます。
   * または、このコードを **Arduino IDE** にコピーしてください。

   * **アップロード** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と正しいポートを選択することを忘れないでください。

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/a237801f-40d7-4920-80fb-a349307b1e05/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

プログラムが動作していると、LEDセグメントディスプレイが0~9までの数字を順番に表示するのが見えるでしょう。

**仕組みは？**

``shiftOut()`` は74HC595に8つのデジタル信号を出力させます。
最後のビットの二進数をQ0に、最初のビットの出力をQ7にします。言い換えると、二進数 "00000001" を書くと、Q0はハイレベルを出力し、Q1~Q7はローレベルを出力します。

7セグメントディスプレイが数字 "1" を表示する場合、b、cにハイレベルを書き、a、d、e、f、g、およびdgにローレベルを書きます。
つまり、二進数 "00000110" を書く必要があります。可読性のため、16進数表記 "0x06" を使用します。

* `16進数 <https://ja.wikipedia.org/wiki/16%E9%80%B2%E6%95%B0>`_

* `BinaryHex変換器 <https://www.binaryhexconverter.com/binary-to-hex-converter>`_

同様に、同じ方法でLEDセグメントディスプレイに他の数字を表示させることもできます。以下の表は、これらの数字に対応するコードを示しています。

.. list-table:: グリフコード
    :widths: 20 20 20
    :header-rows: 1

    *   - 数字
        - 二進数コード
        - 16進数コード
    *   - 0
        - 00111111
        - 0x3f
    *   - 1
        - 00000110
        - 0x06
    *   - 2
        - 01011011
        - 0x5b
    *   - 3
        - 01001111
        - 0x4f
    *   - 4
        - 01100110
        - 0x66
    *   - 5
        - 01101101
        - 0x6d
    *   - 6
        - 01111101
        - 0x7d
    *   - 7
        - 00000111
        - 0x07
    *   - 8
        - 01111111
        - 0x7f
    *   - 9
        - 01101111
        - 0x6f

これらのコードを ``shiftOut()`` に書き込むと、LEDセグメントディスプレイが対応する数字を表示します。
