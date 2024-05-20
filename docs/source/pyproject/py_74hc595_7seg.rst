.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _py_74hc_7seg:

5.2 数字表示
=======================

7セグメントディスプレイは日常生活で至るところで見かけます。
例えば、エアコンでは温度を表示するために使われ、交通信号機ではタイマーを表示するために用いられます。

7セグメントディスプレイは基本的に8つのLEDで構成されています。このうち7つの帯状のLEDが「8」の形を形成し、小さな点状のLEDが小数点として機能します。これらのLEDはa、b、c、d、e、f、g、およびdpとマークされています。各LEDは独自のアノードピンを持ち、カソードは共有されています。ピンの位置は以下の図で示されています。

|img_7seg_cathode|

これは、7セグメントディスプレイが完全に動作するためには同時に8つのデジタル信号で制御する必要があることを意味します。74HC595がこれを可能にします。

* :ref:`cpn_7_segment`

**必要な部品**

このプロジェクトでは以下の部品が必要です。

一式で購入すると便利です、そのリンクはこちらです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットに含まれるアイテム
        - リンク
    *   - ケプラーキット
        - 450+ 
        - |link_kepler_kit|

以下のリンクから個々の部品も購入することができます。

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - 部品
        - 数量
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

こちらの配線原理は基本的に :ref:`py_74hc_led` と同じで、唯一の違いはQ0~Q7が7セグメントディスプレイのa~gピンに接続されている点です。

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

**配線図**

|wiring_74hc_7seg|

**コード**

.. note::

    * ``kepler-kit-main/micropython`` のパス内にある ``5.2_number_display.py`` ファイルを開くか、このコードをThonnyにコピーしてから「Run Current Script」をクリックするか、F5を押して実行してください。

    * 右下隅の「MicroPython（Raspberry Pi Pico）」インタプリタをクリックすることを忘れないでください。

    * 詳細なチュートリアルは、 :ref:`open_run_code_py` を参照してください。

.. code-block:: python

    import machine
    import time

    SEGCODE = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]

    sdi = machine.Pin(0,machine.Pin.OUT)
    rclk = machine.Pin(1,machine.Pin.OUT)
    srclk = machine.Pin(2,machine.Pin.OUT)

    def hc595_shift(dat): 
        rclk.low()
        time.sleep_ms(5)
        for bit in range(7, -1, -1):
            srclk.low()
            time.sleep_ms(5)
            value = 1 & (dat >> bit)
            sdi.value(value)
            time.sleep_ms(5)
            srclk.high()
            time.sleep_ms(5)
        time.sleep_ms(5)
        rclk.high()
        time.sleep_ms(5)
        
    while True:
        for num in range(10):
            hc595_shift(SEGCODE[num])
            time.sleep_ms(500)

プログラムが実行されていると、LEDセグメントディスプレイが0〜9を順番に表示するのが確認できます。

**動作原理**

``hc595_shift()`` 関数によって74HC595は8つのデジタル信号を出力します。
この関数は、2進数の最後のビットをQ0に、最初のビットをQ7に出力します。つまり、2進数「00000001」を書き込むと、Q0は高レベルを、Q1〜Q7は低レベルを出力します。

7セグメントディスプレイが「1」と表示する場合、bとcに高レベルを書き込み、a、d、e、f、g、およびdgに低レベルを書き込む必要があります。

|img_1_segment|

すなわち、2進数「00000110」を書き込む必要があります。可読性のため、16進数表記「0x06」を使用します。

* `16進数 <https://ja.wikipedia.org/wiki/16%E9%80%B2%E6%95%B0>`_

* `BinaryHex変換器 <https://www.binaryhexconverter.com/binary-to-hex-converter>`_

同様にして、LEDセグメントディスプレイに他の数字を表示させることもできます。以下の表は、それぞれの数字に対応するコードを示しています。

.. list-table:: グリフコード
    :widths: 20 20 20
    :header-rows: 1

    *   - 数字
        - 2進数コード
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

これらのコードを ``hc595_shift()`` 関数に書き込むことで、LEDセグメントディスプレイが対応する数字を表示するようにできます。
