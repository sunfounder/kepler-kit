.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _py_micro:

2.8 やさしく押して
==========================

|img_micro_switch|

マイクロスイッチもまた3ピンのデバイスで、この3ピンの順序はC（共通ピン）、NO（通常開）およびNC（通常閉）です。

マイクロスイッチが押されていない場合、1（C）と3（NC）が接続され、押された場合は、1（C）と2（NO）が接続されます。

* :ref:`cpn_micro_switch`

**必要な部品**

このプロジェクトでは、以下の部品が必要です。

全ての部品が含まれるキットを購入するのは確かに便利です、リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットに含まれるアイテム
        - リンク
    *   - ケプラーキット
        - 450以上
        - |link_kepler_kit|


以下のリンクから部品を個別に購入することもできます。

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
        - :ref:`cpn_capacitor`
        - 1(104)
        - |link_capacitor_buy|
    *   - 7
        - :ref:`cpn_micro_switch`
        - 1
        - 

**回路図**

|sch_limit_sw|

デフォルトでは、GP14はローで、押されるとGP14はハイになります。

10Kの抵抗器の目的は、押している間にGP14を低く保つことです。

104セラミックキャパシターは、ジッターを除去するためにここで使用されます。

**配線**

|wiring_limit_sw|


**コード**

.. note::

    * ``kepler-kit-main/micropython`` パス下の ``2.8_micro_switch.py`` ファイルを開くか、このコードをThonnyにコピーして、「Run Current Script」をクリックするか、単にF5キーを押して実行してください。

    * 画面の右下隅にある "MicroPython (Raspberry Pi Pico)" インタープリタをクリックするのを忘れないでください。

    * 詳細なチュートリアルは、 :ref:`open_run_code_py` を参照してください。

.. code-block:: python

    import machine
    import utime
    button = machine.Pin(14, machine.Pin.IN)
    while True:
        if button.value() == 1:
            print("The switch works!")
            utime.sleep(1)

プログラムが実行された後、スライドスイッチを右に切り替えると、シェルに「The switch works!」と表示されます。
