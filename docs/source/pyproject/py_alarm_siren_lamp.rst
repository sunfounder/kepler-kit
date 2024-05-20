.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _py_alarm_lamp:

7.3 警報サイレンランプ
=======================

警察の灯りは、実際の生活（または映画）でよく見かけます。通常、交通を整理するため、警告装置として、そして警察官、緊急車両、消防車、作業車の重要な安全装置として使用されます。その灯りや音を見聞きした場合、注意が必要です。それは、あなた（または周囲の人々）が危険にさらされている可能性があるからです。

ここでは、LEDとブザーを用いて小型の警告灯を作成し、スライドスイッチで起動します。

|sirem_alarm|


**必要なコンポーネント**

このプロジェクトでは、以下のコンポーネントが必要です。

全てを一つのキットで購入すると便利です。リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - キットの内容
        - リンク
    *   - ケプラーキット
        - 450+点
        - |link_kepler_kit|

以下のリンクから個別にも購入できます。

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
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 6
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 7
        - :ref:`cpn_resistor`
        - 3(1KΩ, 220Ω, 10KΩ)
        - |link_resistor_buy|
    *   - 8
        - パッシブ :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|
    *   - 9
        - :ref:`cpn_capacitor`
        - 1(104)
        - |link_capacitor_buy|
    *   - 10
        - :ref:`cpn_slide_switch`
        - 1
        - 


**回路図**

|sch_alarm_siren_lamp|

* GP17はスライダーの中央ピンに接続されており、10Kの抵抗と一緒にキャパシタ（フィルタ）がGNDに並列接続されています。これにより、スライダーは左右に切り替えられたときに安定した高いまたは低いレベルを出力します。
* GP15が高いとすぐに、NPNトランジスタが導通し、パッシブブザーが鳴り始めます。このパッシブブザーは、サイレン音を出すように周波数が徐々に増加するようにプログラムされています。
* LEDはGP16に接続されており、サイレンを模倣するように定期的に明るさを変えるようにプログラムされています。

**配線**

|wiring_alarm_siren_lamp|


**コード**

.. note::

    * ``kepler-kit-main/micropython`` フォルダ下の ``7.3_alarm_siren_lamp.py`` ファイルを開くか、このコードをThonnyにコピーしてから、「Run Current Script」をクリックするか、F5キーを押して実行してください。

    * 右下隅の「MicroPython（Raspberry Pi Pico）」インタープリタを選択することを忘れずに。

    * 詳細なチュートリアルについては、 :ref:`open_run_code_py` を参照してください。


.. code-block:: python

    import machine
    import time

    buzzer = machine.PWM(machine.Pin(15))
    led = machine.PWM(machine.Pin(16))
    led.freq(1000)

    switch = machine.Pin(17, machine.Pin.IN)

    def noTone(pin):
        pin.duty_u16(0)

    def tone(pin, frequency):
        pin.freq(frequency)
        pin.duty_u16(30000)

    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def toggle(pin):
        global bell_flag
        bell_flag = not bell_flag
        print(bell_flag)
        if bell_flag:
            switch.irq(trigger=machine.Pin.IRQ_FALLING, handler=toggle)
        else:
            switch.irq(trigger=machine.Pin.IRQ_RISING, handler=toggle)

    bell_flag = False
    switch.irq(trigger=machine.Pin.IRQ_RISING, handler=toggle)

    while True:
        if bell_flag == True:
            for i in range(0, 100, 2):
                led.duty_u16(int(interval_mapping(i, 0, 100, 0, 65535)))
                tone(buzzer, int(interval_mapping(i, 0, 100, 130, 800)))
                time.sleep_ms(10)
        else:
            noTone(buzzer)
            led.duty_u16(0)

プログラムが動作している状態で、スライドスイッチを左に切り替えると（あなたのスライドスイッチの配線によっては右かもしれません）、ブザーが段階的に警告音を発し、LEDの明るさもそれに応じて変わります。スライドスイッチを右に切り替えると、ブザーとLEDは動作を停止します。
