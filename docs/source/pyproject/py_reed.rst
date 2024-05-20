.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _py_reed:

2.9 磁気を感じる
==============================

最も一般的なタイプのリードスイッチは、スイッチが開いているときに小さな隙間で分離された、磁化可能で柔軟な金属製のリードの一対を含んでいます。

電磁石または永久磁石からの磁場が、リード同士を引き寄せることで電気回路を完成させます。
磁場が消失すると、リードのバネ力によってそれらは分離し、回路が開きます。

リードスイッチの一般的な用途の一例は、セキュリティアラーム用にドアや窓が開いたことを検出することです。

* :ref:`cpn_reed`

**必要な部品**

このプロジェクトでは、以下の部品が必要です。

一式で購入する方が確実に便利です、リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットに含まれるアイテム
        - リンク
    *   - ケプラーキット	
        - 450+
        - |link_kepler_kit|

以下のリンクから個別に購入することもできます。

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
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_reed`
        - 1
        - 

**回路図**

|sch_reed|

デフォルトでは、GP14は低く、磁石がリードスイッチに近づくと高くなります。

10KΩの抵抗の目的は、磁石が近くにないときにGP14を安定した低レベルに保つことです。

**配線**

|wiring_reed|

**コード**

.. note::

    * ``kepler-kit-main/micropython`` のパスの下にある ``2.9_feel_the_magnetism.py`` ファイルを開くか、このコードをThonnyにコピーしてから、「Run Current Script」をクリックするか、単純にF5キーを押して実行してください。

    * 右下隅の「MicroPython（Raspberry Pi Pico）」インタープリターをクリックするのを忘れないでください。

    * 詳細なチュートリアルについては、 :ref:`open_run_code_py`  を参照してください。

.. code-block:: python

    import machine
    import utime
    reed = machine.Pin(14, machine.Pin.IN)
    while True:
        if reed.value() == 1:
            print("There are magnets here!!")
            utime.sleep(1)

コードが実行されると、リードスイッチに磁石が近づくとGP14が高くなり、そうでない場合は低くなります。 :ref:`py_button` チャプターのボタンと同様です。

**もっと詳しく**

今回は、スイッチの柔軟な使い方を試してみました：割り込み要求、またはIRQ（Interrupt Requests）。

例えば、あなたがプログラムがスレッドを実行しているかのように、ページごとに本を読んでいるとします。このとき、誰かが質問をしにきて、あなたの読書を中断しました。その人が割り込み要求を実行しています：あなたがやっていることをやめて、彼の質問に答え、その後で読書に戻らせます。

MicroPythonの割り込み要求も同じように動作します。それは、特定の操作がメインプログラムを中断できるようにします。

.. note::

    * ``kepler-kit-main/micropython`` のパスの下にある ``2.9_feel_the_magnetism_irq.py`` ファイルを開くか、このコードをThonnyにコピーしてから、「Run Current Script」をクリックするか、単純にF5キーを押して実行してください。

    * 右下隅の「MicroPython（Raspberry Pi Pico）」インタープリターをクリックするのを忘れないでください。

    * 詳細なチュートリアルについては、 :ref:`open_run_code_py` を参照してください。

.. code-block:: python

    import machine
    import utime

    reed_switch = machine.Pin(14, machine.Pin.IN)

    def detected(pin):
        print("Magnet!")

    reed_switch.irq(trigger=machine.Pin.IRQ_RISING, handler=detected)

ここではまず、コールバック関数 ``detected(pin)`` が定義されています。これを割り込みハンドラーと呼びます。割り込み要求がトリガーされたときに実行されます。次に、メインプログラムで割り込み要求が設定されています。これには二つの部分が含まれています： ``trigger`` と ``handler`` 。

このプログラムで ``trigger`` は ``IRQ_RISING`` です。これは、ピンの値が低から高に変わること（つまり、ボタンの押下）を示します。

``handler`` は、前に定義したコールバック関数 ``detected`` です。

* `machine.Pin.irq - Micropython Docs <https://docs.micropython.org/en/latest/library/machine.Pin.html#machine.Pin.irq>`_
