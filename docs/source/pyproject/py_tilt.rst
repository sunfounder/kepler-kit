.. _py_tilt:

2.6 傾けてみよう！
==========================

|img_tilt|

この傾きスイッチは、中央に金属の玉がある2ピンのデバイスです。スイッチが垂直の場合、2つのピンが接続されています。それが傾いた場合、2つのピンが切断されます。

**必要なコンポーネント**

このプロジェクトでは、以下のコンポーネントが必要です。

便宜上、全体のキットを購入することもできます。リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットに含まれるアイテム
        - リンク
    *   - ケプラーキット	
        - 450以上
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
        - :ref:`cpn_resistor`
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_tilt`
        - 1
        - 

**回路図**

|sch_tilt|

垂直に置いた場合、GP14はハイレベルになります。傾けた後、GP14はローレベルになります。

10KΩの抵抗器の目的は、傾きスイッチが傾いた状態のときにGP14を安定したローレベル状態に保つことです。

* :ref:`cpn_tilt`

**配線**

|wiring_tilt|



**コード**

.. note::

    * ``kepler-kit-main/micropython`` のパスにある ``2.6_tilt_switch.py`` ファイルを開くか、このコードをThonnyにコピーしてから、"Run Current Script"をクリックするかF5を押して実行してください。

    * 右下隅の"MicroPython（Raspberry Pi Pico）"インタープリターをクリックするのを忘れないでください。

    * 詳細なチュートリアルは、 :ref:`open_run_code_py` を参照してください。

.. code-block:: python

    import machine
    import utime
    button = machine.Pin(14, machine.Pin.IN)
    while True:
        if button.value() == 0:
            print("The switch works!")
            utime.sleep(1)

プログラムが実行された後、ブレッドボード（傾きスイッチ）を傾けると、シェルに「The switch works!」と表示されます。
