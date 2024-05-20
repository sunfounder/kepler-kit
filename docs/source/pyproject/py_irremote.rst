.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _py_irremote:

6.4 IRリモートコントロール
================================

消費者向け電子機器では、テレビやDVDプレーヤーなどの機器を操作するためにリモートコントロールが使用されます。
場合によっては、リモートコントロールによって手の届かない場所にある機器、例えばセントラルエアコンを操作することもあります。

IRレシーバーは、赤外線を受信するように調整されたフォトセルを搭載したコンポーネントです。
このタイプのレシーバーはほぼ常にリモートコントロールの検出に使用されています。すべてのテレビやDVDプレーヤーの前面には、クリッカーからのIR信号を受信するためのものがあります。
リモートコントロールの内部には、テレビをオン/オフにしたりチャンネルを変更するためのIRパルスを発生する対応するIR LEDがあります。

* :ref:`cpn_ir_receiver`

**必要なコンポーネント**

このプロジェクトで必要なコンポーネントは以下の通りです。

便利なのは、全体のキットを購入することです。リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - キット内容
        - リンク
    *   - ケプラーキット	
        - 450以上
        - |link_kepler_kit|

以下のリンクから個別に購入することもできます。

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
        - :ref:`cpn_ir_receiver`
        - 1
        - |link_receiver_buy|

**回路図**

|sch_irrecv|

**配線**

|wiring_irrecv|

**コード**

.. note::

    * ``kepler-kit-main/micropython`` のパス内の ``6.4_ir_remote_control.py`` ファイルを開くか、このコードをThonnyにコピペして、"Run Current Script"をクリックするか、単にF5キーを押して実行してください。

    * 右下隅の "MicroPython (Raspberry Pi Pico)" インタープリターをクリックするのを忘れないでください。

    * 詳細なチュートリアルについては、 :ref:`open_run_code_py` を参照してください。
    
    * ここでは ``ir_rx`` フォルダ内のライブラリが必要です。Picoにアップロードされているか確認してください。詳細なチュートリアルは :ref:`add_libraries_py` を参照してください。


.. code-block:: python

    import time
    from machine import Pin, freq
    from ir_rx.print_error import print_error
    from ir_rx.nec import NEC_8

    pin_ir = Pin(17, Pin.IN)

    def decodeKeyValue(data):
        if data == 0x16:
            return "0"
        if data == 0x0C:
            return "1"
        if data == 0x18:
            return "2"
        if data == 0x5E:
            return "3"
        if data == 0x08:
            return "4"
        if data == 0x1C:
            return "5"
        if data == 0x5A:
            return "6"
        if data == 0x42:
            return "7"
        if data == 0x52:
            return "8"
        if data == 0x4A:
            return "9"
        if data == 0x09:
            return "+"
        if data == 0x15:
            return "-"
        if data == 0x7:
            return "EQ"
        if data == 0x0D:
            return "U/SD"
        if data == 0x19:
            return "CYCLE"
        if data == 0x44:
            return "PLAY/PAUSE"
        if data == 0x43:
            return "FORWARD"
        if data == 0x40:
            return "BACKWARD"
        if data == 0x45:
            return "POWER"
        if data == 0x47:
            return "MUTE"
        if data == 0x46:
            return "MODE" 
        return "ERROR"

    # User callback
    def callback(data, addr, ctrl):
        if data < 0:  # NEC protocol sends repeat codes.
            pass
        else:
            print(decodeKeyValue(data))

    ir = NEC_8(pin_ir, callback)  # Instantiate receiver
    ir.error_function(print_error)  # Show debug information

    try:
        while True:
            pass
    except KeyboardInterrupt:
        ir.close()

この新しいリモートコントロールには、バッテリーを隔離するためのプラスチック片が最後にあります。それを使用する際には、このプラスチック片を引き抜いてリモートを起動する必要があります。
プログラムが実行されているとき、リモートコントロールのボタンを押すと、Shellに押したキーが表示されます。

**仕組みは？**

このプログラムは少し複雑に見えますが、実際はIRレシーバーの基本機能を数行で実装しています。

.. code-block:: python

    import time
    from machine import Pin, freq
    from ir_rx.nec import NEC_8

    pin_ir = Pin(17, Pin.IN)

    # User callback
    def callback(data, addr, ctrl):
        if data < 0:  # NEC protocol sends repeat codes.
            pass
        else:
            print(decodeKeyValue(data))

    ir = NEC_8(pin_ir, callback)  # Instantiate receiver

ここでは ``ir`` オブジェクトがインスタンス化され、IRレシーバーによって取得された信号を常に読み取ります。

結果はコールバック関数の ``data`` に記録されます。

* `コールバック関数 - ウィキペディア <https://ja.wikipedia.org/wiki/%E3%82%B3%E3%83%BC%E3%83%AB%E3%83%90%E3%83%83%E3%82%AF_(%E6%83%85%E5%A0%B1%E5%B7%A5%E5%AD%A6)>`_

IRレシーバーが重複値（例：キーを押して離さない場合）を受け取ると、data < 0 となり、このデータはフィルタリングする必要があります。

そうでなければ、dataは使用可能な値であり、 ``decodeKeyValue(data)`` 関数がそれをデコードするために使用されます。

.. code-block:: python

    def decodeKeyValue(data):
        if data == 0x16:
            return "0"
        if data == 0x0C:
            return "1"
        if data == 0x18:
            return "2"
        if data == 0x5E:
            return "3"
        if data == 0x08:
            return "4"
        if data == 0x1C:
            return "5"
        if data == 0x5A:
            return "6"
        if data == 0x42:
            return "7"
        if data == 0x52:
            return "8"
        if data == 0x4A:
            return "9"
        if data == 0x09:
            return "+"
        if data == 0x15:
            return "-"
        if data == 0x7:
            return "EQ"
        if data == 0x0D:
            return "U/SD"
        if data == 0x19:
            return "CYCLE"
        if data == 0x44:
            return "PLAY/PAUSE"
        if data == 0x43:
            return "FORWARD"
        if data == 0x40:
            return "BACKWARD"
        if data == 0x45:
            return "POWER"
        if data == 0x47:
            return "MUTE"
        if data == 0x46:
            return "MODE" 
        return "ERROR"

**1** キーを押すと、IRレシーバーは ``0x0C`` のような値を出力する必要があり、それを特定のキーに対応させる必要があります。

次に、いくつかのデバッグ関数があります。これらは重要ですが、私たちが達成したい効果には関係ないため、プログラムに含めています。

.. code-block:: python

    from ir_rx.print_error import print_error

    ir.error_function(print_error) # Show debug information

最後に、主要なプログラムとして空のループを使用します。そして、try-exceptを使用してプログラムが ``ir`` オブジェクトを終了させるようにします。

.. code-block:: python

    try:
        while True:
            pass
    except KeyboardInterrupt:
        ir.close()


* `try文 - Python Docs <https://docs.python.org/ja/3/reference/compound_stmts.html#the-try-statement>`_

