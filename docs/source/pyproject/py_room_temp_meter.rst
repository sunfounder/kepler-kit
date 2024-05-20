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
    import machine
    import utime
    import math

    thermistor = machine.ADC(28)
    lcd = LCD()

    while True:
        temperature_value = thermistor.read_u16()
        Vr = 3.3 * float(temperature_value) / 65535
        Rt = 10000 * Vr / (3.3 - Vr)
        temp = 1/(((math.log(Rt / 10000)) / 3950) + (1 / (273.15+25)))
        Cel = temp - 273.15
        #Fah = Cel * 1.8 + 32
        #print ('Celsius: %.2f C  Fahrenheit: %.2f F' % (Cel, Fah))
        #utime.sleep_ms(200)

        string = " Temperature is \n    " + str('{:.2f}'.format(Cel)) + " C"
        lcd.message(string)
        utime.sleep(1)
        lcd.clear()

プログラムが実行された後、LCDには現在の環境の温度値が表示されます。

.. note::
    コードと配線が正しいのにもかかわらず、LCDが何も表示しない場合は、裏面のポテンショメーターを回してコントラストを調整できます。
