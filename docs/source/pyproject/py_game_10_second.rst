.. _py_10_second:

7.5 GAME - 10秒ゲーム
=======================

集中力を試すために、次に私に続いてゲームデバイスを作りましょう。
傾きスイッチと棒を接続して魔法の杖を作成します。この杖を振ると、4桁のセグメントディスプレイがカウントを始め、再度振るとカウントが停止します。勝つためには、表示されるカウントを **10.00** に保つ必要があります。友達とこのゲームで時間の魔法使いが誰かを見つけることができます。

**必要な部品**

このプロジェクトで必要な部品は以下のとおりです。

一式をまとめて購入する方が確実に便利です、リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットのアイテム
        - リンク
    *   - ケプラーキット
        - 450以上
        - |link_kepler_kit|

以下のリンクから個々に購入することもできます。

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
        - 5（4-220Ω、1-10KΩ）
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_4_dit_7_segment`
        - 1
        - 
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|
    *   - 8
        - :ref:`cpn_tilt`
        - 1
        - 

**回路図**

|sch_10_second|

* この回路は、 :ref:`py_74hc_4dig` に傾きスイッチを追加したものです。
* GP16は、傾きスイッチが垂直のときに高く、傾いたときに低くなります。

**配線図**

|wiring_game_10_second| 

**コード**

.. note::

    * ``kepler-kit-main/micropython`` のパス下にある ``7.5_game_10_second.py`` ファイルを開くか、このコードをThonnyにコピーして、"Run Current Script"をクリックするかF5キーを押して実行してください。

    * 右下隅の"MicroPython（Raspberry Pi Pico）"インタープリターをクリックすることを忘れないでください。

    * 詳細なチュートリアルについては、 :ref:`open_run_code_py` を参照してください。


.. code-block:: python

    import machine
    import time

    SEGCODE = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]

    sdi = machine.Pin(18,machine.Pin.OUT)
    rclk = machine.Pin(19,machine.Pin.OUT)
    srclk = machine.Pin(20,machine.Pin.OUT)

    placePin = []
    pin = [10,13,12,11]
    for i in range(4):
        placePin.append(None)
        placePin[i] = machine.Pin(pin[i], machine.Pin.OUT)

    def pickDigit(digit):
        for i in range(4):
            placePin[i].value(1)
        placePin[digit].value(0)

    def clearDisplay():
        hc595_shift(0x00)

    def hc595_shift(dat):
        rclk.low()
        time.sleep_us(200)
        for bit in range(7, -1, -1):
            srclk.low()
            time.sleep_us(200)
            value = 1 & (dat >> bit)
            sdi.value(value)
            time.sleep_us(200)
            srclk.high()
            time.sleep_us(200)
        time.sleep_us(200)
        rclk.high()
        #time.sleep_us(200)

    def display(num):

        pickDigit(0)
        hc595_shift(SEGCODE[num%10])

        pickDigit(1)
        hc595_shift(SEGCODE[num%100//10])

        pickDigit(2)
        hc595_shift(SEGCODE[num%1000//100]+0x80)

        pickDigit(3)
        hc595_shift(SEGCODE[num%10000//1000])    

    tilt_switch = machine.Pin(16,machine.Pin.IN)

    count_flag = False

    def shake(pin):
        global timeStart,count_flag
        count_flag = not count_flag
        if count_flag == True:
            timeStart = time.ticks_ms()

    tilt_switch.irq(trigger=machine.Pin.IRQ_RISING, handler=shake)

    count = 0
    while True:
        if count_flag == True:
            count = int((time.ticks_ms()-timeStart)/10)
        display(count)

魔法の杖を振ると、4桁の7セグメントディスプレイがカウントを開始し、再度振るとカウントが停止します。
表示されたカウントが10.00になった場合、あなたの勝ちです。もう一度振るとゲームが続きます。
