.. _py_mpu6050:

6.3 6軸モーショントラッキング
=====================================

MPU-6050は6軸（3軸ジャイロスコープ、3軸加速度計）のモーショントラッキングデバイスです。

加速度計は、適切な加速度を測定するツールです。例えば、地球上で静止している加速度計は、地球の重力による上向きの加速度[3]（定義上）を約9.81 m/s²として測定します。

加速度計は、産業や科学で多くの用途があります。例としては、航空機やミサイルの慣性航法システム、タブレットやデジタルカメラの画像を縦に保つためなどがあります。

ジャイロスコープは、デバイスまたは機器の方向と角速度を測定するために使用されます。
ジャイロスコープの応用例としては、自動車の反転防止とエアバッグシステム、スマートデバイスのモーションセンシングシステム、ドローンの姿勢安定化システムなどがあります。

* :ref:`cpn_mpu6050`

**必要な部品**

このプロジェクトには、以下の部品が必要です。

全てを一つのキットで購入するのも便利です、リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットに含まれるアイテム
        - リンク
    *   - ケプラーキット
        - 450以上
        - |link_kepler_kit|

もちろん、以下のリンクから個々の部品を購入することもできます。

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - 項番
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
        - :ref:`cpn_mpu6050`
        - 1
        - 

**回路図**

|sch_mpu6050|

**配線**

|wiring_mpu6050|

**コード**

.. note::

    * ``kepler-kit-main/micropython`` パス下の ``6.3_6axis_motion_tracking.py`` ファイルを開くか、このコードをThonnyにコピーして、「Run Current Script」をクリックするか、単にF5キーを押して実行してください。

    * 画面の右下隅にある "MicroPython (Raspberry Pi Pico)" インタープリタをクリックするのを忘れないでください。

    * 詳細なチュートリアルは、 :ref:`open_run_code_py` を参照してください。

    * このプロジェクトでは ``imu.py`` と ``vector3d.py`` が必要です。Pico Wにアップロードされているか確認してください。詳細なチュートリアルは :ref:`add_libraries_py` を参照してください。

.. code-block:: python

    from imu import MPU6050
    from machine import I2C, Pin
    import time

    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
    mpu = MPU6050(i2c)

    while True:
        print("x: %s, y: %s, z: %s"%(mpu.accel.x, mpu.accel.y, mpu.accel.z))
        time.sleep(0.1)
        print("A: %s, B: %s, Y: %s"%(mpu.gyro.x, mpu.gyro.y, mpu.gyro.z))
        time.sleep(0.1)

プログラムを実行すると、3軸加速度計の値と3軸ジャイロスコープの値が出力で循環します。
この時点でMPU6050を自由に回転させると、これらの値もそれに応じて変わるでしょう。
変更を容易に確認するために、print文の一つをコメントアウトして、他のデータセットに集中することもできます。

**仕組みは？**

imuライブラリでは、関連する関数を ``MPU6050`` クラスに統合しています。
MPU6050はI2Cモジュールであり、初期化のためにI2Cピンのセットを定義する必要があります。

.. code-block:: python

    from imu import MPU6050
    from machine import I2C, Pin

    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
    mpu = MPU6050(i2c)

その後、 ``mpu.accel.x`` 、 ``mpu.accel.y`` 、 ``mpu.accel.z`` 、 ``mpu.gyro.x`` 、 ``mpu.gyro.y`` 、 ``mpu.gyro.z`` でリアルタイムの加速度と角速度の値を取得できます。

.. code-block:: python

    while True:
        print("x: %s, y: %s, z: %s"%(mpu.accel.x, mpu.accel.y, mpu.accel.z))
        time.sleep(0.1)
        print("A: %s, B: %s, Y: %s"%(mpu.gyro.x, mpu.gyro.y, mpu.gyro.z))
        time.sleep(0.1)
