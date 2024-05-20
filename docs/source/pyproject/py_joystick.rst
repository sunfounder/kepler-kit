.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _py_joystick:

4.1 ジョイスティックの切り替え
================================

ビデオゲームをよくプレイするなら、ジョイスティックには非常に馴染みがあるでしょう。
このデバイスは主にキャラクターの移動や画面の回転などに使用されます。

ジョイスティックがコンピュータに対して私たちのアクションを読み取る仕組みは非常にシンプルです。
これは、直交する2つのポテンショメータから成り立っていると考えることができます。
これらのポテンショメータは、ジョイスティックの垂直および水平なアナログ値を測定し、平面直角座標系での値（x,y）を出力します。

このキットのジョイスティックには、ジョイスティックが押されたときに活性化するデジタル入力もあります。

* :ref:`cpn_joystick`

**必要なコンポーネント**

このプロジェクトでは、以下のコンポーネントが必要です。

一式を購入するのは確かに便利です、リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットに含まれるアイテム
        - リンク
    *   - ケプラーキット	
        - 450以上
        - |link_kepler_kit|

以下のリンクから個別にも購入可能です。

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
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
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_joystick`
        - 1
        - 

**回路図**

|sch_joystick|

SWピンは10Kのプルアップ抵抗に接続されています。その理由は、ジョイスティックが押されていないときにSWピン（Z軸）で安定した高レベルを得るためです。そうでないと、SWはサスペンド状態になり、出力値は0/1の間で変動する可能性があります。

**配線**

|wiring_joystick|

**コード**

.. note::

    * ``kepler-kit-main/micropython`` のパスの下にある ``4.1_toggle_the_joystick.py`` ファイルを開くか、このコードをThonnyにコピーしてから、「Run Current Script」をクリックするか、単にF5キーを押して実行します。

    * 右下隅にある「MicroPython（Raspberry Pi Pico）」のインタープリタをクリックするのを忘れないでください。

    * 詳細なチュートリアルについては、 :ref:`open_run_code_py` を参照してください。

.. code-block:: python

    import machine
    import utime

    x_joystick = machine.ADC(27)
    y_joystick = machine.ADC(26)
    z_switch = machine.Pin(22,machine.Pin.IN)

    while True:
        x_value = x_joystick.read_u16()
        y_value = y_joystick.read_u16()
        z_value = z_switch.value()
        print(x_value,y_value,z_value)
        utime.sleep_ms(200)    

プログラムを実行した後、Shellはジョイスティックのx, y, zの値を出力します。

* x軸とy軸の値は、0から65535までのアナログ値です。
* Z軸は、状態が1または0のデジタル値です。
