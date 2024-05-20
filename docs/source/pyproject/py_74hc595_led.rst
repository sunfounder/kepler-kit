.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _py_74hc_led:

5.1 マイクロチップ - 74HC595
===============================

集積回路（Integrated Circuit、IC）は、電子回路で"IC"として表されるミニチュア電子デバイスまたはコンポーネントの一種です。

特定のプロセスを用いて、トランジスタ、抵抗器、コンデンサ、インダクタなど、回路に必要なコンポーネントと配線を小型またはいくつかの小型の半導体ウェハーや誘電体基板上に作成し、それをパッケージに収めることで、必要な回路機能を持つマイクロ構造になります。全てのコンポーネントは一体となって構造化され、電子部品は微小化、低消費電力、高信頼性、および知能化に大きく前進しています。

集積回路の発明者は、ジャック・キルビー（ゲルマニウム（Ge）を基にした集積回路）とロバート・ノートン・ノイス（シリコン（Si）を基にした集積回路）です。

このキットには、GPIOピンの使用を大幅に節約できるIC、74HC595が装備されています。具体的には、8ビットの2進数を書き込むことで、デジタル信号出力のための8ピンを置き換えることができます。

* `2進数 - ウィキペディア <https://ja.wikipedia.org/wiki/%E4%BA%8C%E9%80%B2%E6%95%B0>`_

* :ref:`74HC595`

**必要なコンポーネント**

このプロジェクトでは、以下のコンポーネントが必要です。

全体のキットを購入するのが確実に便利です。リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットに含まれるアイテム
        - リンク
    *   - ケプラーキット	
        - 450以上
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
        - 8（220Ω）
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 8
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|

**回路図**

|sch_74hc_led|

* MR（ピン10）がハイレベルで、OE（ピン13）がローレベルの場合、SHcpの立ち上がりエッジでデータが入力され、SHcpの立ち上がりエッジを通じてメモリレジスタに移動します。
* 2つのクロックが一緒に接続されている場合、シフトレジスタは常にメモリレジスタよりも1パルス早いです。
* メモリレジスタには、シリアルシフト入力ピン（Ds）、シリアル出力ピン（Q）、および非同期リセットボタン（ローレベル）があります。
* メモリレジスタは、3つの状態で並列8ビットのバスを出力します。
* OEが有効化（ローレベル）された場合、メモリレジスタ内のデータがバス（Q0〜Q7）に出力されます。

**配線**

|wiring_74hc_led|

**コード**

.. note::

    * ``kepler-kit-main/micropython`` のパスの下にある ``5.1_microchip_74hc595.py`` ファイルを開くか、このコードをThonnyにコピーしてから、「Run Current Script」をクリックするか、単純にF5を押して実行します。
    
    * 画面右下の角にある「MicroPython（Raspberry Pi Pico）」のインタープリターをクリックするのを忘れないでください。
    
    * 詳細なチュートリアルについては、 :ref:`open_run_code_py` を参照してください。

.. code-block:: python

    import machine
    import time

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

    num = 0

    for i in range(16):
        if i < 8:
            num = (num<<1) + 1
        elif i>=8:
            num = (num & 0b01111111)<<1
        hc595_shift(num)
        print("{:0>8b}".format(num))
        time.sleep_ms(200)

プログラムが動作しているとき、 ``num`` は8ビットの2進数として74HC595チップに書き込まれ、8つのLEDのオンオフを制御します。
シェルで ``num`` の現在の値を確認できます。

**仕組み**

``hc595_shift()`` は、74HC595に8つのデジタル信号を出力させます。それは2進数の最後のビットをQ0に、最初のビットをQ7に出力します。言い換えれば、2進数「00000001」を書き込むと、Q0はハイレベルを出力し、Q1〜Q7はローレベルを出力します。
