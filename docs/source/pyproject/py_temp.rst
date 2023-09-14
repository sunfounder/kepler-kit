.. _py_temp:

2.13 温度計
===========================

温度計は、温度または温度勾配（物体の熱さや冷たさの度合い）を測定する装置です。
温度計には2つの重要な要素があります：(1) 温度センサー（例えば、水銀温度計の球根や赤外線温度計の焦電センサー）で、これには温度の変化に伴い何らかの変化が生じます；
そして（2）この変化を数値に変換する何らかの手段（例えば、水銀温度計にマークされた目盛りまたは赤外線モデルのデジタル表示）。
温度計は、テクノロジーや産業でプロセスを監視するため、気象学、医学、科学研究で広く使用されています。

サーミスターは、温度に強く依存する抵抗値を持つ温度センサーの一種で、2つのタイプがあります：
負温度係数（NTC）と正温度係数（PTC）、別名NTCおよびPTCです。PTCサーミスターの抵抗は温度とともに増加し、NTCの状態はそれと逆です。

この実験では、 **NTCサーミスター** を用いて温度計を作成します。

* :ref:`cpn_thermistor`

**必要なコンポーネント**

このプロジェクトでは、以下のコンポーネントが必要です。

一式をまとめて購入するのは便利です。リンクはこちら：

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

**回路図**

|sch_temp|

この回路では、10Kの抵抗とサーミスターが直列に接続されており、両方を通る電流は同じです。10Kの抵抗は保護として機能し、GP28はサーミスターの電圧変換後の値を読み取ります。

温度が上昇すると、NTCサーミスターの抵抗値は減少し、その電圧も減少するため、GP28からの値も減少します。温度が十分に高い場合、サーミスターの抵抗はほぼ0に近く、GP28の値もほぼ0に近くなります。このとき、10Kの抵抗は保護として働き、3.3VとGNDが直結し短絡することを防ぎます。

温度が下がると、GP28の値は増加します。温度が十分に低い場合、サーミスターの抵抗は無限大になり、その電圧はほぼ3.3Vに近くなります（10Kの抵抗は無視できます）、GP28の値は最大値の65535に近くなります。

計算式は以下の通りです。

    (Vp/3.3V) x 65535 = Ap


**配線**

|wiring_temp|



.. note::
    * サーミスターは黒く、103とマークされています。
    * 10Kオームの抵抗器のカラーリングは赤、黒、黒、赤、茶です。

**コード**

.. note::

    * ``kepler-kit-main/micropython`` のパスにある ``2.13_thermometer.py`` ファイルを開くか、このコードをThonnyにコピーして、"Run Current Script"をクリックするかF5キーを押して実行します。

    * 右下隅の"MicroPython（Raspberry Pi Pico）"インタープリターを忘れずにクリックしてください。

    * 詳細なチュートリアルについては、 :ref:`open_run_code_py` を参照してください。

.. code-block:: python

    import machine
    import utime
    import math

    thermistor = machine.ADC(28)  

    while True:
        temperature_value = thermistor.read_u16()
        Vr = 3.3 * float(temperature_value) / 65535
        Rt = 10000 * Vr / (3.3 - Vr)
        temp = 1/(((math.log(Rt / 10000)) / 3950) + (1 / (273.15+25)))
        Cel = temp - 273.15
        Fah = Cel * 1.8 + 32
        print ('Celsius: %.2f C  Fahrenheit: %.2f F' % (Cel, Fah))
        utime.sleep_ms(200)

プログラムが実行された後、シェルは摂氏と華氏の温度を出力します。

**仕組みは？**

各サーミスターには通常の抵抗値があります。ここでは、それは10kオームであり、25度摂氏で測定されます。

温度が高くなると、サーミスターの抵抗が減少します。その後、A/Dアダプターによって電圧データがデジタル量に変換されます。

プログラミングを介して摂氏または華氏での温度が出力されます。

.. code-block:: python

    import math 

これは、一般的な数学的演算と変換を計算する一連の関数を宣言する数値ライブラリです。

* `math <https://docs.micropython.org/en/latest/library/math.html>`_

.. code-block:: python

    temperature_value = thermistor.read_u16()

この関数は、サーミスターの値を読み取るために使用されます。

.. code-block:: python

    Vr = 3.3 * float(temperature_value) / 65535
    Rt = 10000 * Vr / (3.3 - Vr)
    temp = 1/(((math.log(Rt / 10000)) / 3950) + (1 / (273.15+25)))
    Cel = temp - 273.15
    Fah = Cel * 1.8 + 32
    print ('Celsius: %.2f C  Fahrenheit: %.2f F' % (Cel, Fah))
    utime.sleep_ms(200)

これらの計算は、サーミスターの値を摂氏度と華氏度に変換します。

.. code-block:: python

    Vr = 3.3 * float(temperature_value) / 65535
    Rt = 10000 * Vr / (3.3 - Vr)

上記の2行のコードでは、まず読み取ったアナログ値を使用して電圧を計算し、次にRt（サーミスターの抵抗）を取得します。

.. code-block:: python

    temp = 1/(((math.log(Rt / 10000)) / 3950) + (1 / (273.15+25))) 

.. note::
    ここでは、抵抗と温度の関係が以下のようになっています：

    **RT = RN expB(1/TK – 1/TN)**

    * RTは、温度がTKのときのNTCサーミスターの抵抗です。
    * RNは、定格温度TN下でのNTCサーミスターの抵抗です。ここでは、RNの数値値は10kです。
    * TKはケルビン温度で、単位はKです。ここでは、TKの数値値は273.15 + 摂氏度です。
    * TNも定格ケルビン温度であり、単位もKです。ここでは、TNの数値値は273.15+25です。
    * B（ベータ）はNTCサーミスターの材料定数であり、熱感度指数とも呼ばれ、数値値は3950です。
    * expは指数の略であり、基数eは自然数で、約2.7に等しいです。

    この関係は、実用的な公式です。温度と抵抗が有効範囲内にある場合にのみ正確です。

このコードは、ケルビン温度を取得するために、Rtを式TK=1/(ln(RT/RN)/B+1/TN)に代入しています。

.. code-block:: python

    temp = temp - 273.15 

ケルビン温度を摂氏度に変換します。

.. code-block:: python

    Fah = Cel * 1.8 + 32 

摂氏度を華氏度に変換します。

.. code-block:: python

    print ('Celsius: %.2f °C Fahrenheit: %.2f ℉' % (Cel, Fah)) 

シェルに摂氏度、華氏度、およびそれらの単位を出力します。
