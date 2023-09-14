.. _py_reversing_aid:

7.10 バックアップ支援
======================

このプロジェクトでは、LED、ブザー、および超音波モジュールを使用して、バックアップ支援システムを作成します。
これをリモートコントロールカーに取り付けて、ガレージに車をバックして入れる実際のプロセスをシミュレーションすることができます。

**必要なコンポーネント**

このプロジェクトには、以下のコンポーネントが必要です。

便利なのは、一式をまとめて購入することです。リンクはこちらです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットに含まれるアイテム
        - リンク
    *   - ケプラーキット	
        - 450以上
        - |link_kepler_kit|

以下のリンクからそれぞれ個別に購入することも可能です。

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
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 2(1KΩ、220Ω)
        - |link_resistor_buy|
    *   - 7
        - パッシブ :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|
    *   - 8
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 9
        - :ref:`cpn_ultrasonic`
        - 1
        - |link_ultrasonic_buy|

**回路図**

|sch_reversing_aid|


**配線**

|wiring_reversing_aid| 

**コード**

.. note::

    * ``kepler-kit-main/micropython`` のパスの下で ``7.10_reversing_aid.py`` ファイルを開くか、このコードをThonnyにコピーして、"Run Current Script"をクリックするか、単にF5キーを押して実行してください。

    * 右下隅の"MicroPython（Raspberry Pi Pico）"インタープリターをクリックするのを忘れないでください。

    * 詳細なチュートリアルについては、 :ref:`open_run_code_py` を参照してください。

.. code-block:: python

    import machine
    import time
    import _thread

    buzzer = machine.Pin(15, machine.Pin.OUT)
    led = machine.Pin(14, machine.Pin.OUT)

    TRIG = machine.Pin(17, machine.Pin.OUT)
    ECHO = machine.Pin(16, machine.Pin.IN)

    dis = 100

    def distance():
        timeout = 10000 * 5 / 340
        TRIG.low()
        time.sleep_us(2)
        TRIG.high()
        time.sleep_us(10)
        TRIG.low()
        timeout_start = time.ticks_ms()
        while not ECHO.value():
            waiting_time = time.ticks_ms()
            if waiting_time - timeout_start > timeout:
                return -1
        time1 = time.ticks_us()
        while ECHO.value():
            waiting_time = time.ticks_ms()
            if waiting_time - timeout_start > timeout:
                return -1
        time2 = time.ticks_us()
        during = time.ticks_diff(time2, time1)
        return during * 340 / 2 / 10000

    def ultrasonic_thread():
        global dis
        while True:
            dis = distance()

    _thread.start_new_thread(ultrasonic_thread, ())

    def beep():
        buzzer.value(1)
        led.value(1)
        time.sleep(0.1)
        buzzer.value(0)
        led.value(0)
        time.sleep(0.1)

    intervals = 10000000
    previousMills = time.ticks_ms()
    time.sleep(1)

    while True:
        if dis < 0:
            pass
        elif dis <= 10:
            intervals = 300
        elif dis <= 20:
            intervals = 500
        elif dis <= 50:
            intervals = 1000
        else:
            intervals = 2000
        if dis != -1:
            print('Distance: %.2f' % dis)
            time.sleep_ms(100)

        currentMills = time.ticks_ms()

        if time.ticks_diff(currentMills, previousMills) >= intervals:
            beep()
            previousMills = currentMills

* プログラムが動作するとすぐに、超音波センサーは前方の障害物までの距離を連続して読み取ります。シェル上で正確な距離値を確認できます。
* LEDとブザーは、距離値に応じて点滅とビープの頻度が変わり、障害物が近づいていることを示します。
* :ref:`py_ultrasonic` の記事で、超音波センサーが動作すると、プログラムが一時停止すると言及されています。
* この例でLEDやブザーのタイミングに干渉しないように、測定用に別のスレッドを作成しました。

