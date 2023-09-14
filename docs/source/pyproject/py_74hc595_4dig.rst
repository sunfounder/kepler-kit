.. _py_74hc_4dig:

5.3 時間カウンター
================================

4桁の7セグメントディスプレイは、4つの7セグメントディスプレイが連動して動作するものです。

この4桁の7セグメントディスプレイは独立して動作します。それは、人間の視覚の残像効果の原理を使って、各7セグメントの文字を高速でループ表示し、連続した文字列を形成します。

例えば、「1234」と表示された場合、最初の7セグメントには「1」が表示され、それ以降「234」は表示されません。一定の時間が経過すると、次の7セグメントに「2」が表示され、1つ目、3つ目、4つ目の7セグメントは何も表示されない、といった具体です。このプロセスは非常に短い（一般に5ms程度）であり、視覚の残像効果と残像の原理により、我々は同時に4つの文字を見ることができます。

**必要な部品**

このプロジェクトでは、以下のコンポーネントが必要です。

一式をまとめて購入すると確実に便利です、リンクはこちらです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - キット内容
        - リンク
    *   - Keplerキット
        - 450+ 
        - |link_kepler_kit|

以下のリンクからも個別に購入することができます。

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

**回路図**

|sch_4dig|

ここでの配線の原理は、 :ref:`py_74hc_led` と基本的に同じで、唯一の違いは、Q0～Q7が4桁の7セグメントディスプレイのa〜gピンに接続されている点です。

そして、G10〜G13がどの7セグメントディスプレイが動作するかを選択します。

**配線**

|wiring_4dig|


**コード**

.. note::

    * ``kepler-kit-main/micropython`` パスの下で ``5.3_time_counter.py`` ファイルを開くか、このコードをThonnyにコピーして、"Run Current Script"をクリックするかF5キーを押して実行します。

    * 忘れずに右下の「MicroPython（Raspberry Pi Pico）」インタプリタをクリックしてください。

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

    timerStart=time.ticks_ms()

    def timer1():
        return int((time.ticks_ms()-timerStart)/1000)

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
        time.sleep_us(200)

    while True:
        count = timer1()
        #print(count)
        
        pickDigit(0)
        hc595_shift(SEGCODE[count%10])

        pickDigit(1)
        hc595_shift(SEGCODE[count%100//10])
        
        pickDigit(2)
        hc595_shift(SEGCODE[count%1000//100])
        
        pickDigit(3)
        hc595_shift(SEGCODE[count%10000//1000])  

プログラムが実行されると、4桁の7セグメントディスプレイがカウンターになり、数字が1秒ごとに1増えます。

**どのように動作するのか？**

各7セグメントディスプレイに信号を書き込む処理は、 :ref:`py_74hc_7seg` と同様に、 ``hc595_shift()`` 関数を使用しています。
4桁の7セグメントディスプレイの要点は、各7セグメントディスプレイを選択的に活性化することです。この関連するコードは以下の通りです。

.. code-block:: python

    placePin = []
    pin = [13, 12, 11, 10]
    for i in range(4):
        placePin.append(None)
        placePin[i] = machine.Pin(pin[i], machine.Pin.OUT)

    def pickDigit(digit):
        for i in range(4):
            placePin[i].value(1)
        placePin[digit].value(0)

    while True:
        hc595_shift(SEGCODE[count % 10])
        pickDigit(0)
        
        hc595_shift(SEGCODE[count % 100 // 10])
        pickDigit(1)
        
        hc595_shift(SEGCODE[count % 1000 // 100])
        pickDigit(2)
        
        hc595_shift(SEGCODE[count % 10000 // 1000])
        pickDigit(3)

ここでは、4つのピン（GP10、GP11、GP12、GP13）が4桁の7セグメントディスプレイの各ビットを個々に制御するために使用されています。
これらのピンの状態が ``0`` であれば、対応する7セグメントディスプレイは活性化されます。状態が ``1`` であれば、その逆です。

``pickDigit(digit)`` 関数は、すべての桁を無効化した後、特定の桁だけを個別に有効にするために使用されます。
その後、 ``hc595_shift()`` 関数で、7セグメントディスプレイに対応する8ビットのコードが書き込まれます。

4桁の7セグメントディスプレイは、連続的に交互に活性化する必要があり、それによって4つの数字が同時に表示されるように見えます。
しかし、この例ではタイミング機能も追加する必要があります。 ``sleep(1)`` を追加すると、それが一目瞭然になります。
そのため、 ``time.ticks_ms()`` 関数を使用することが、この問題に対する優れた解決策です。

.. code-block:: python

    import time

    timerStart=time.ticks_ms()

    def timer1():
        return int((time.ticks_ms()-timerStart)/1000)

    while True:
        count = timer1()

``time.ticks_ms()`` 関数で取得する時間は（非明示的な）もので、最初に取得した時間値を ``timerStart`` として記録します。
その後、時間が必要な場合には、再度 ``time.ticks_ms()`` 関数を呼び出し、その値から ``timerStart`` を引いて、プログラムがどれくらい動いているか（ミリ秒単位で）を計算します。

最後に、この時間値を4桁の7セグメントディスプレイに変換して出力し、完成です。

* `Time - MicroPython Docs <https://docs.micropython.org/en/latest/library/time.html>`_
