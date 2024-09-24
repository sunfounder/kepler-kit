.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _py_room_temp:

7.2 室温計
======================================

サーミスターとI2C LCD1602を使って、室温計を作成できます。

このプロジェクトは非常にシンプルで、 :ref:`py_temp` に基づきI2C LCD1602で温度を表示します。

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
        - :ref:`cpn_thermistor`
        - 1
        - |link_thermistor_buy|
    *   - 7
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|

**回路図**

|sch_room_temp|

**配線**

|wiring_room_temp|

**コード**

.. note::

    * ``kepler-kit-main/micropython`` のパス下にある ``7.2_room_temperature_meter.py`` ファイルを開くか、このコードをThonnyにコピペして、「Run Current Script」をクリックまたはF5キーを押して実行します。

    * 右下角にある「MicroPython（Raspberry Pi Pico）」インタープリターをクリックして選択してください。

    * 詳細なチュートリアルは、 :ref:`open_run_code_py` を参照してください。

.. code-block:: python

    from lcd1602 import LCD
    from machine import I2C, Pin
    import utime
    import math

    # Initialize the thermistor (ADC on pin 28) and LCD display
    thermistor = machine.ADC(28)  # Analog input from the thermistor

    # Initialize I2C communication for the LCD1602 display
    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)

    # Create an LCD object for controlling the LCD1602 display
    lcd = LCD(i2c)

    # Main loop to continuously read temperature and display it
    while True:
        # Read raw ADC value from the thermistor
        temperature_value = thermistor.read_u16()

        # Convert the raw ADC value to a voltage (0-3.3V range)
        Vr = 3.3 * float(temperature_value) / 65535  # ADC value to voltage conversion

        # Calculate the thermistor resistance (using a voltage divider with a 10kOhm resistor)
        Rt = 10000 * Vr / (3.3 - Vr)  # Rt = thermistor resistance

        # Use the Steinhart-Hart equation to calculate the temperature in Kelvin
        # The values used are specific to the thermistor (3950 is the beta coefficient)
        temp = 1 / (((math.log(Rt / 10000)) / 3950) + (1 / (273.15 + 25)))  # Temperature in Kelvin

        # Convert temperature from Kelvin to Celsius
        Cel = temp - 273.15

        # Display the temperature on the LCD in Celsius
        string = " Temperature is \n    " + str('{:.2f}'.format(Cel)) + " C"  # Format string for the LCD
        lcd.message(string)  # Display the string on the LCD

        utime.sleep(1)  # Wait for 1 second
        lcd.clear()  # Clear the LCD for the next reading


プログラムが実行された後、LCDには現在の環境の温度値が表示されます。

.. note::
    コードと配線が正しいのにもかかわらず、LCDが何も表示しない場合は、裏面のポテンショメーターを回してコントラストを調整できます。
