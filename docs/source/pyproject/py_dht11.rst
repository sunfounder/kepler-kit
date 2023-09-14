.. _py_dht11:

6.2 温度・湿度センサー
=======================================

湿度と温度は、物理量自体から日常生活まで密接に関連しています。
人間の環境の温度と湿度は、体温調節機能や熱伝達の効果に直接影響を与えます。
さらに、これは思考活動や精神状態にも影響を与え、学習や仕事の効率にも影響を与えます。

温度は、国際単位系（SI）での7つの基本的な物理量の一つであり、物体の熱さや寒さを測るために使用されます。
摂氏度は、世界でよく使用される温度の尺度の一つで、"℃"という記号で表されます。

湿度は、空気中に存在する水蒸気の濃度です。
一般的には相対湿度が使用され、%RHで表されます。相対湿度は温度に密接に関連しています。
密閉された一定量のガスに対して、温度が高いほど相対湿度は低く、温度が低いほど相対湿度は高くなります。

|img_Dht11|

このキットには基本的なデジタル温度・湿度センサー、 **DHT11** が付属しています。
このセンサーは、周囲の空気の温度と湿度を測るために、容量性湿度センサーとサーミスターを使用し、データピンでデジタル信号を出力します（アナログ入力ピンは不要です）。

* :ref:`cpn_dht11`

**必要なコンポーネント**

このプロジェクトでは、以下のコンポーネントが必要です。

一式をまとめて購入すると便利です、リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットに含まれるアイテム
        - リンク
    *   - ケプラーキット	
        - 450+
        - |link_kepler_kit|

以下のリンクから個別にも購入できます。

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
        - いくつか
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_dht11`
        - 1
        - |link_dht22_buy|

**回路図**

|sch_dht11|

**配線**

|wiring_dht11|

**コード**

.. note::

    * ``kepler-kit-main/micropython`` フォルダ内の ``6.2_temperature_humidity.py`` ファイルを開くか、このコードをThonnyにコピーしてから、「Run Current Script」をクリックするか、F5キーを押して実行してください。

    * 右下の角にある「MicroPython（Raspberry Pi Pico）」のインタープリターを選択することを忘れないでください。

    * 詳細なチュートリアルは、 :ref:`open_run_code_py` を参照してください。

    * ここでは ``dht.py`` というライブラリを使用する必要があります。Pico Wにアップロードされているか確認してください。詳細なチュートリアルは :ref:`add_libraries_py` を参照してください。

.. code-block:: python

    from machine import Pin, I2C
    import utime as time
    from dht import DHT11, InvalidPulseCount

    pin = Pin(16, Pin.IN, Pin.PULL_UP)
    sensor = DHT11(pin)
    time.sleep(5)  # 初期遅延

    while True:
        try:
            sensor.measure()
            string = "Temperature:{}\nHumidity: {}".format(sensor.temperature, sensor.humidity)
            print(string)
            time.sleep(4)

        except InvalidPulseCount as e:
            print('Bad pulse count - retrying ...')

コードを実行すると、シェルには温度と湿度が継続して表示され、プログラムが安定して動作するにつれて、これらの値はますます正確になります。

**仕組み**

dhtライブラリでは、関連する機能を ``DHT11`` クラスに統合しています。

.. code-block:: python

    from dht import DHT11, InvalidPulseCount

``DHT11`` オブジェクトを初期化します。このデバイスは、デジタル入力だけで使用できます。

.. code-block:: python

    pin = Pin(16, Pin.IN, Pin.PULL_UP)
    sensor = DHT11(pin)

``sensor.measure()`` を使用して現在の温度と湿度を読み取り、 ``sensor.temperature`` 、 ``sensor.humidity`` に保存されます。
それらはその後、出力されます。
最後に、DHT11のサンプリングレートは1HZなので、ループ内で ``time.sleep(1)`` が必要です。

.. code-block:: python

    while True:
        try:
            sensor.measure()
            string = "Temperature:{}\nHumidity: {}".format(sensor.temperature, sensor.humidity)
            print(string)
            time.sleep(4)

        except InvalidPulseCount as e:
            print('Bad pulse count - retrying ...')

