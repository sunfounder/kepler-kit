.. _py_somato_controller:

7.11 体感コントローラー
=============================

ロボット映画をよく観ているなら、このような光景を見たことがあるでしょう。
主人公が手首をひねると、巨大なロボットがそれに応じて動き、主人公が拳を振ると、ロボットもそれに続く。非常にクールです。

この技術の使用は、すでに大学や研究機関で一般的であり、5Gの到来によってその応用範囲は大いに拡大しています。
「外科ロボットダ・ヴィンチ」の遠隔手術は典型的な例です。

この種のロボットシステムは、通常、人間の動きをキャプチャするモジュールとロボットアームを駆動するモジュール（一部の応用シナリオにはデータ通信モジュールも含まれる）の2つのモジュールで構成されています。

ここでは、MPU6050を用いて人間の動きをキャプチャ（グローブに取り付ける）し、サーボを用いてロボットアームの動きを表現しています。

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
        - :ref:`cpn_mpu6050`
        - 1
        - 
    *   - 6
        - :ref:`cpn_servo`
        - 1
        - |link_servo_buy|

**回路図**

|sch_somato|

MPU6050は各方向の加速度値に基づいて姿勢角を計算します。

プログラムは、姿勢角が変わるにつれて、サーボを対応する偏角で制御します。

**配線**

|wiring_somatosensory_controller|

**コード**

.. note::

    * ``kepler-kit-main/micropython`` のパス下にある ``7.11_somatosensory_controller.py`` ファイルを開くか、このコードをThonnyにコピペして、"Run Current Script"をクリックまたはF5キーを押して実行します。
    * 右下の「MicroPython（Raspberry Pi Pico）」インタープリターをクリックして選択してください。
    * 詳細なチュートリアルは、 :ref:`open_run_code_py` を参照してください。
    * こちらでは ``imu.py`` と ``vector3d.py`` が必要です。Pico Wにアップロードされているか確認してください。詳細なチュートリアルは :ref:`add_libraries_py` を参照してください。

.. code-block:: python


    from imu import MPU6050
    from machine import I2C, Pin
    import time
    import math

    # mpu6050
    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
    mpu = MPU6050(i2c)

    # servo
    servo = machine.PWM(machine.Pin(15))
    servo.freq(50)


    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min



    # get rotary angle
    def dist(a,b):
        return math.sqrt((a*a)+(b*b))

    def get_y_rotation(x,y,z):
        radians = math.atan2(x, dist(y,z))
        return -math.degrees(radians)

    def get_x_rotation(x,y,z):
        radians = math.atan2(y, dist(x,z))
        return math.degrees(radians)

    # servo work
    def servo_write(pin,angle):
        pulse_width=interval_mapping(angle, 0, 180, 0.5,2.5)
        duty=int(interval_mapping(pulse_width, 0, 20, 0,65535))
        pin.duty_u16(duty)

    times=25
    while True:
        total=0 
        for i in range(times):
            angle=get_y_rotation(mpu.accel.x, mpu.accel.y, mpu.accel.z) #get rotation value
            total+=angle
        average_angle=int(total/times) # make the value smooth
        servo_write(servo,interval_mapping(average_angle,-90,90,0,180))



プログラムが動作すると、MPU6050を傾ける（またはグローブに取り付けた場合は手首を回す）と、サーボが左右に回転します。
