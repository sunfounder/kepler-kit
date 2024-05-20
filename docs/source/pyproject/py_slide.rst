.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _py_slide:

2.7 左右切り替え
====================================

|img_slide|

スライドスイッチは3ピンのデバイスで、ピン2（中央）が共通ピンです。スイッチを左に切り替えると、左側の2つのピンが接続され、右に切り替えると、右側の2つのピンが接続されます。

**必要なコンポーネント**

このプロジェクトには以下のコンポーネントが必要です。

一式をまとめて購入するのは非常に便利です。リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名称	
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
        - :ref:`cpn_resistor`
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_capacitor`
        - 1(104)
        - |link_capacitor_buy|
    *   - 7
        - :ref:`cpn_slide_switch`
        - 1
        - 

**回路図**

|sch_slide|

スライドスイッチを左右に切り替えると、GP14のレベルが変わります。

10Kの抵抗器の目的は、切り替え中にGP14を低く保つことです（左端には切り替えず、右端にも切り替えない）。

104のセラミックコンデンサは、ジッタを除去するために使用されています。

* :ref:`cpn_slide_switch`
* :ref:`cpn_capacitor`

**配線**

|wiring_slide|

**コード**

.. note::

    * ``kepler-kit-main/micropython`` のパス下にある ``2.7_slide_switch.py`` ファイルを開くか、このコードをThonnyにコピペして、「Run Current Script」をクリックまたはF5キーを押して実行します。

    * 右下隅の「MicroPython（Raspberry Pi Pico）」インタープリターをクリックして選択してください。

    * 詳細なチュートリアルは、 :ref:`open_run_code_py` を参照してください。

.. code-block:: python

    import machine
    import utime
    button = machine.Pin(14, machine.Pin.IN)
    while True:
        if button.value() == 0:
            print("The switch works!")
            utime.sleep(1)

プログラムが実行された後、スライドスイッチを右に切り替えると、シェルに「The switch works!」と表示されます。
