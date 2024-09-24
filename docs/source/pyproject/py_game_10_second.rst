.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

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

    # 7-segment display codes for digits 0-9, using hexadecimal to represent LED segments
    SEGCODE = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]

    # Define pins for shift register communication (74HC595)
    sdi = machine.Pin(18, machine.Pin.OUT)   # Serial Data Input
    rclk = machine.Pin(19, machine.Pin.OUT)  # Register Clock (Latch)
    srclk = machine.Pin(20, machine.Pin.OUT) # Shift Register Clock

    # Initialize list to store 4 digit control pins
    placePin = []

    # Define control pins for each of the four digits (common anodes)
    pin = [10,13,12,11]  # Pin numbers for the 4-digit display
    for i in range(4):
        placePin.append(None)  # Reserve space in list
        placePin[i] = machine.Pin(pin[i], machine.Pin.OUT)  # Initialize pin as output

    # Function to select which digit (0-3) to display by controlling the common anode pins
    def pickDigit(digit):
        for i in range(4):
            placePin[i].value(1)  # Turn off all digits
        placePin[digit].value(0)  # Turn on the selected digit

    # Function to clear the display by sending '0x00' to the shift register
    def clearDisplay():
        hc595_shift(0x00)

    # Function to send data to the shift register (74HC595)
    def hc595_shift(dat):
        rclk.low()  # Pull latch low to prepare for data shifting
        time.sleep_us(200)  # Small delay for timing stability
        for bit in range(7, -1, -1):  # Loop through each bit (MSB first)
            srclk.low()  # Prepare to send the next bit
            time.sleep_us(200)
            value = 1 & (dat >> bit)  # Extract the current bit from the data
            sdi.value(value)  # Set the data line to the current bit value
            time.sleep_us(200)
            srclk.high()  # Pulse the shift clock to store the bit in the register
            time.sleep_us(200)
        time.sleep_us(200)
        rclk.high()  # Pulse the register clock to move the data to the output

    # Function to display a number on the 7-segment display
    # This function breaks down the number into its individual digits and displays them one at a time
    def display(num):
        pickDigit(0)  # Select the units place
        hc595_shift(SEGCODE[num % 10])  # Display units

        pickDigit(1)  # Select the tens place
        hc595_shift(SEGCODE[num % 100 // 10])  # Display tens

        pickDigit(2)  # Select the hundreds place
        hc595_shift(SEGCODE[num % 1000 // 100] + 0x80)  # Display hundreds (with decimal point)

        pickDigit(3)  # Select the thousands place
        hc595_shift(SEGCODE[num % 10000 // 1000])  # Display thousands

    # Initialize the tilt switch sensor on pin 16
    tilt_switch = machine.Pin(16, machine.Pin.IN)

    # Boolean flag to control whether the counting should continue
    count_flag = False

    # Interrupt handler for the tilt switch, toggles the counting flag on each trigger
    def shake(pin):
        global timeStart, count_flag
        count_flag = not count_flag  # Toggle the counting state
        if count_flag == True:
            timeStart = time.ticks_ms()  # Record the time when counting starts

    # Set up an interrupt on the tilt switch to detect shaking and call the shake() function
    tilt_switch.irq(trigger=machine.Pin.IRQ_RISING, handler=shake)

    # Initialize the count variable to zero
    count = 0

    # Main loop to continuously update the display based on the elapsed time since the tilt switch was triggered
    while True:
        if count_flag == True:
            count = int((time.ticks_ms() - timeStart) / 10)  # Calculate the count in tenths of a second
        display(count)  # Update the display with the current count
)

魔法の杖を振ると、4桁の7セグメントディスプレイがカウントを開始し、再度振るとカウントが停止します。
表示されたカウントが10.00になった場合、あなたの勝ちです。もう一度振るとゲームが続きます。
