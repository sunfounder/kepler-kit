.. _py_passage_counter:

7.4 乗客カウンター
==============================

大型ショッピングモール、ショッピングセンター、チェーンストア、空港、駅、美術館、展示会場などの公共の場所で、乗客の流れは欠かせないデータです。

例えば、空港や駅では、人々の数を厳密に制御して、安全と円滑な流れを確保する必要があります。
また、ショッピングセンターやチェーンストアでは、より多くの訪問者がいる時間帯や、各ユーザーが生成できる注文数などを把握することが可能です。
その結果、人々の消費習慣を分析し、売上を向上させることができます。

乗客カウンターは、これらの公共の場所の運営を理解し、効率的に運営を整えるのに役立ちます。

このプロジェクトでは、PIRセンサーと4桁の7セグメントディスプレイを使用して、シンプルな乗客カウンターを作成します。


**必要なコンポーネント**

このプロジェクトでは、以下のコンポーネントが必要です。

全体のキットを購入するのが確かに便利です、リンクはこちらです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - キット内容
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
        - 4(220Ω)
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
        - :ref:`cpn_pir`
        - 1
        - |link_pir_buy|

**回路図**

|sch_passager_counter| 

* この回路は、 :ref:`py_74hc_4dig` を基にして、PIRモジュールが追加されています。
* 誰かが通過すると、PIRは約2.8秒間の高い信号を送ります。
* PIRモジュールには二つの可変抵抗があります：一つは感度を調整し、もう一つは検出距離を調整します。PIRモジュールをより効果的に動作させるためには、これらの両方を反時計回りに最後まで回す必要があります。

    |img_PIR_TTE|


**配線**

|wiring_passager_counter| 


**コード**

.. note::

    * ``kepler-kit-main/micropython`` パスの下にある ``7.4_passenger_counter.py`` ファイルを開くか、このコードをThonnyにコピーしてから、「Run Current Script」をクリックするか、単にF5キーを押して実行してください。

    * 画面の右下隅にある「MicroPython（Raspberry Pi Pico）」インタープリターをクリックすることを忘れないでください。

    * 詳細なチュートリアルは、 :ref:`open_run_code_py` を参照してください。


.. code-block:: python

    import machine
    import time

    pir_sensor = machine.Pin(16, machine.Pin.IN)

    SEGCODE = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]

    sdi = machine.Pin(18,machine.Pin.OUT)
    rclk = machine.Pin(19,machine.Pin.OUT)
    srclk = machine.Pin(20,machine.Pin.OUT)

    placePin = []
    pin = [10,13,12,11]
    for i in range(4):
        placePin.append(None)
        placePin[i] = machine.Pin(pin[i], machine.Pin.OUT)

    count = 0

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

    def motion_detected(pin):
        global count
        count = count+1

    pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=motion_detected)

    while True:
        #print(count)
        
        pickDigit(0)
        hc595_shift(SEGCODE[count%10])

        pickDigit(1)
        hc595_shift(SEGCODE[count%100//10])
        
        pickDigit(2)
        hc595_shift(SEGCODE[count%1000//100])
        
        pickDigit(3)
        hc595_shift(SEGCODE[count%10000//1000])

コードが実行されたとき、PIRモジュールの前を誰かが通過すると、4桁の7セグメントディスプレイ上の数字が1つ増加します。
