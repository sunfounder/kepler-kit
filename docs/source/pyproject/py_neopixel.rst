.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _py_neopixel:

3.3 RGB LED ストリップ
======================

WS2812は、制御回路とRGBチップが5050コンポーネントのパッケージ内に統合されたインテリジェントなLED光源です。
内部には、インテリジェントなデジタルポートデータラッチと信号再整形増幅駆動回路が含まれています。
さらに、高精度な内部オシレーターとプログラム可能な定電流制御部も内蔵しており、各ピクセルの色の一貫性が高く確保されています。

データ転送プロトコルは、単一のNZR通信モードを使用します。
ピクセルが電源投入リセット後、DINポートはコントローラからデータを受信し、最初のピクセルは初期の24ビットデータを収集して内部データラッチに送ります。その後、内部信号再整形増幅回路によって整形された他のデータは、DOポートを通じて次のカスケードピクセルに送られます。各ピクセルの送信後、信号は24ビット削減されます。
ピクセルは自動再整形送信技術を採用しており、ピクセルのカスケード数は信号転送速度にのみ依存します。

* :ref:`cpn_ws2812`

**必要な部品**

このプロジェクトには、以下の部品が必要です。

一式をまとめて購入するのが便利です、リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットに含まれるアイテム
        - リンク
    *   - ケプラーキット
        - 450以上
        - |link_kepler_kit|

以下のリンクから個々の部品も購入できます。

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - 項番
        - 部品
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
        - :ref:`cpn_ws2812`
        - 1
        - |link_ws2812_buy|

**回路図**

|sch_ws2812|

**配線**

|wiring_ws2812|

.. warning::
    注意すべき点は電流です。

    Pico Wで任意の数のLEDを使用することができますが、そのVBUSピンの電力は制限されています。
    ここでは、安全な8つのLEDを使用します。
    ただし、より多くのLEDを使用したい場合は、別途電源を追加する必要があります。

    
**コード**

.. note::

    * ``kepler-kit-main/micropython`` のパスの下にある ``3.3_rgb_led_strip.py`` ファイルを開くか、このコードをThonnyにコピーしてから、「Run Current Script」をクリックするか、単純にF5キーを押して実行してください。

    * 画面の右下隅の「MicroPython（Raspberry Pi Pico）」インタープリタをクリックするのを忘れないでください。

    * 詳細なチュートリアルについては、 :ref:`open_run_code_py` を参照してください。
    
    * ここでは ``ws2812.py`` というライブラリを使用する必要があります。Pico Wにアップロードされているかどうか確認してください。詳細なチュートリアルについては、 :ref:`add_libraries_py` を参照してください。


.. code-block:: python

    import machine 
    from ws2812 import WS2812

    ws = WS2812(machine.Pin(0), 8)

    ws[0] = [64, 154, 227]
    ws[1] = [128, 0, 128]
    ws[2] = [50, 150, 50]
    ws[3] = [255, 30, 30]
    ws[4] = [0, 128, 255]
    ws[5] = [99, 199, 0]
    ws[6] = [128, 128, 128]
    ws[7] = [255, 100, 0]
    ws.write()

お気に入りの色をいくつか選んで、RGB LEDストリップに表示しましょう！

**仕組み**

ws2812ライブラリでは、関連する関数をWS2812クラスに統合しています。

次の文を使用して、RGB LEDストリップを操作できます。

.. code-block:: python

    from ws2812 import WS2812

WS2812型のオブジェクトを「ws」という名前で宣言し、それが「pin」に接続されており、WS2812ストリップには「number」個のRGB LEDがあります。

.. code-block:: python

    ws = WS2812(pin, number)

wsは配列オブジェクトであり、各要素はWS2812ストリップ上の1つのRGB LEDに対応しています。例えば、ws[0]は最初のもので、ws[7]は8番目です。

各RGB LEDに色値を割り当てることができます。これらの値は、24ビットカラー（6桁の16進数で表される）または3つの8ビットRGBのリストでなければなりません。

例えば、赤の値は "0xFF0000" または "[255,0,0]" です。

.. code-block:: python

    ws[i] = color value

次に、この文を使用してLEDストリップの色を書き込み、点灯させます。

.. code-block:: python

    ws.write()

すべてのLEDを同じ色で点灯させるには、次の文を直接使用することもできます。

.. code-block:: python

    ws.write_all(color value)

**さらに学ぶ**

ランダムに色を生成し、カラフルな流れる光を作成することができます。

.. note::

    * ``kepler-kit-main/micropython`` のパスの下にある ``3.3_rgb_led_strip_2.py`` ファイルを開くか、このコードをThonnyにコピーしてから、「Run Current Script」をクリックするか、単純にF5キーを押して実行してください。

    * 画面の右下隅の「MicroPython（Raspberry Pi Pico）」インタープリタをクリックするのを忘れないでください。

    * 詳細なチュートリアルについては、 :ref:`open_run_code_py` を参照してください。

.. code-block:: python

    import machine 
    from ws2812 import WS2812
    import utime
    import urandom

    ws = WS2812(machine.Pin(0),8)

    def flowing_light():
        for i in range(7, 0, -1):
            ws[i] = ws[i - 1]
        ws[0] = int(urandom.uniform(0, 0xFFFFFF))  
        ws.write()
        utime.sleep_ms(80)

    while True:
        flowing_light()
        print(ws[0])
