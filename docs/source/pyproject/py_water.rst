.. _py_water:

2.14 水位を感知する
=====================================

|img_water_sensor|

この水センサーは、雨量、水位、さらには液体漏れを検知するために設計されています。

このセンサーは、水滴/水量の大きさを測定するために一連の露出した平行なワイヤートレースを使用して水位を測定します。水量は簡単にアナログ信号に変換され、出力アナログ値は、水位警報効果を実現するためにメインコントロールボードで直接読み取ることができます。

.. warning:: 

    センサーは完全に水に浸けることはできません。十本のトレースがある部分だけを水に触れさせてください。また、湿度の高い環境でセンサーに電力を供給すると、プローブの腐食が加速し、センサーの寿命が短くなる可能性があります。したがって、読み取りを行う際にのみ電力を供給することをお勧めします。

* :ref:`cpn_water_level`

**必要なコンポーネント**

このプロジェクトには、以下のコンポーネントが必要です。

以下のリンクからキット全体を購入することが便利です：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットに含まれるアイテム
        - リンク
    *   - ケプラーキット	
        - 450+
        - |link_kepler_kit|

下記のリンクから個々に購入することもできます。

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
        - :ref:`cpn_water_level`
        - 1
        - 

**回路図**

|sch_water|


**配線**

|wiring_water|

**コード**

.. note::

    * ``kepler-kit-main/micropython`` のパスにある ``2.14_feel_the_water_level.py`` ファイルを開いて、このコードをThonnyにコピーします。その後、「Run Current Script」をクリックするかF5キーを押して実行します。

    * 画面の右下隅にある「MicroPython（Raspberry Pi Pico）」インタープリタをクリックするのを忘れないでください。

    * 詳細なチュートリアルは、 :ref:`open_run_code_py` を参照してください。

.. code-block:: python

    import machine
    import utime

    sensor = machine.ADC(28)

    while True:
        value = sensor.read_u16()
        print(value)
        utime.sleep_ms(200)

プログラムを実行した後、水センサーモジュールをゆっくりと水に浸けます。深さが増すと、シェルはより大きな値を出力します。

**詳しく学ぶ**

アナログ入力モジュールをデジタルモジュールとして使用する方法があります。

まず、水センサーの乾燥した環境での読み取り値を記録し、それを閾値として使用します。次に、プログラミングを完了し、水センサーの読み取り値を再度読み取ります。水センサーの読み取り値が乾燥した環境での読み取り値と大きくずれている場合、液体に触れています。つまり、このデバイスを水道管の近くに置くと、水道管が漏れているかどうかを検出できます。

.. note::

    * ``kepler-kit-main/micropython`` のパスにある ``2.14_water_level_threshold.py`` ファイルを開いて、このコードをThonnyにコピーします。その後、「Run Current Script」をクリックするかF5キーを押して実行します。

    * 画面の右下隅にある「MicroPython（Raspberry Pi Pico）」インタープリタをクリックするのを忘れないでください。

    * 詳細なチュートリアルは、 :ref:`open_run_code_py` を参照してください。

.. code-block:: python

    import machine
    import utime

    sensor = machine.ADC(28)
    threshold = 30000  # この値は環境に応じて修正する必要があります。

    while True:
        value = sensor.read_u16()
        if value > threshold:
            print("Liquid leakage!")
        utime.sleep_ms(200)

