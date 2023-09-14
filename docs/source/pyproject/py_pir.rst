.. _py_pir:

2.10 人間の動きを検出
========================================

受動型赤外線センサー（PIRセンサー）は、視野内の物体が放出する赤外線（IR）光を測定できる一般的なセンサーです。
簡単に言えば、体から放出される赤外線を受け取り、人や他の動物の動きを検出します。
具体的には、誰かが部屋に入ったとメインコントロールボードに通知します。

:ref:`cpn_pir`

**必要なコンポーネント**

このプロジェクトで必要なコンポーネントは以下のとおりです。

全体のキットを購入する方が確実に便利です、リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットに含まれるアイテム
        - リンク
    *   - ケプラーキット
        - 450以上
        - |link_kepler_kit|

以下のリンクから個々に購入することもできます。

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - S/N
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
        - :ref:`cpn_pir`
        - 1
        - |link_pir_buy|


**回路図**

|sch_pir|

PIRモジュールが通過する人を検出すると、GP14は高くなり、それ以外の場合は低くなります。

.. note::
    PIRモジュールには二つの可変抵抗があります：一つは感度を調整し、もう一つは検出距離を調整します。PIRモジュールをより効果的に動作させるには、両方を反時計回りに最後まで回してください。

    |img_PIR_TTE|

**配線**

|wiring_pir|

**コード**

.. note::

    * ``kepler-kit-main/micropython`` のパス下の ``2.10_detect_human_movement.py`` ファイルを開くか、このコードをThonnyにコピーして、"Run Current Script"をクリックするかF5を押して実行してください。

    * 右下隅の"MicroPython（Raspberry Pi Pico）"インタプリターをクリックするのを忘れないでください。

    * 詳細なチュートリアルについては、 :ref:`open_run_code_py` を参照してください。

.. code-block:: python

    import machine
    import utime

    pir_sensor = machine.Pin(14, machine.Pin.IN)

    def motion_detected(pin):
        print("Somebody here!")

    pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=motion_detected)

プログラムが実行された後、PIRモジュールが近くに誰かを検出すると、シェルに「Somebody here!」と表示されます。

**もっと詳しく**

PIRは非常に敏感なセンサーです。使用環境に適応させるために調整が必要です。2つの可変抵抗がある側を向けて、両方の可変抵抗を反時計回りに最後まで回し、Lと中央のピンにジャンパーキャップを挿入してください。

.. note::

    * ``kepler-kit-main/micropython`` のパス下の ``2.10_pir_adjustment.py`` ファイルを開くか、このコードをThonnyにコピーして、"Run Current Script"をクリックするかF5を押して実行してください。

    * 右下隅の"MicroPython（Raspberry Pi Pico）"インタプリターをクリックするのを忘れないでください。

    * 詳細なチュートリアルについては、 :ref:`open_run_code_py` を参照してください。

.. code-block:: python

    import machine
    import utime

    pir_sensor = machine.Pin(14, machine.Pin.IN)

    global timer_delay
    timer_delay = utime.ticks_ms()
    print("start")

    def pir_in_high_level(pin):
        global timer_delay    
        pir_sensor.irq(trigger=machine.Pin.IRQ_FALLING, handler=pir_in_low_level)    
        intervals = utime.ticks_diff(utime.ticks_ms(), timer_delay)
        timer_delay = utime.ticks_ms()
        print("the dormancy duration is " + str(intervals) + "ms")

    def pir_in_low_level(pin):
        global timer_delay    
        pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_in_high_level) 
        intervals2 = utime.ticks_diff(utime.ticks_ms(), timer_delay)
        timer_delay = utime.ticks_ms()        
        print("the duration of work is " + str(intervals2) + "ms")

    pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_in_high_level) 

調整方法と実験結果を一緒に解析しましょう。

|img_pir_back|

1. トリガーモード

   コーナーのジャンパーキャップがあるピンを見てみましょう。
   それによってPIRは、リピート可能なトリガーモードまたは非リピート可能なトリガーモードに入ります。

   現在、ジャンパーキャップは中央のピンとLピンを接続しており、PIRは非リピート可能なトリガーモードになっています。
   このモードでは、PIRが生体の動きを検出すると、約2.8秒間メインコントロールボードに高レベルの信号を送信します。
   印刷されたデータで見ると、作業の継続時間は常に約2800ms前後になります。

   次に、下のジャンパーキャップの位置を変更して、中央のピンとHピンを接続し、PIRをリピート可能なトリガーモードにします。
   このモードでは、PIRが生体の動きを検出する（センサーの前で静止しているのではなく、動いていることに注意）と、生体が検出範囲内で動き続ける限り、PIRはメインコントロールボードに高レベルの信号を送り続けます。
   印刷されたデータで見ると、作業の継続時間は不確かな値になります。

#. 遅延調整

   左側の可変抵抗は、二つの作業の間隔を調整するために使用されます。
   
   現在、反時計回りに最後まで回してありますので、PIRは高レベルの作業を送信し終えた後、約5秒のスリープ時間が必要です。この期間中、PIRは目標エリアでの赤外線放射を検出しません。
   印刷されたデータで見ると、休眠期間は常に5000ms以上になっています。

   可変抵抗を時計回りに回すと、スリープ時間も増加します。それを時計回りに最後まで回すと、スリープ時間は最大で300秒になります。

#. 距離調整

   中央の可変抵抗は、PIRの感知距離範囲を調整するために使用されます。

   距離調整の可変抵抗のノブを **時計回り** に回すと、感知距離範囲が増加し、最大感知距離範囲は約0-7メートルです。
   **反時計回り** に回すと、感知距離範囲が減少し、最小感知距離範囲は約0-3メートルです。
