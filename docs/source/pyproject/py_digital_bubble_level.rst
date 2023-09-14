.. _py_bubble_level:

7.12 デジタル水平器
============================

`水平器 <https://ja.wikipedia.org/wiki/水準器>`_ は、面が水平（レベル）か垂直（垂直）かを示すための計測器具です。大工、石工、レンガ職人、他の建築関連の作業者、測量士、精密機械工、そして一部の写真やビデオ作業にも使用されるさまざまな種類の水平器があります。

ここでは、MPU6050と8x8 LEDマトリックスを使用してデジタル水平器を作成します。MPU6050を傾けると、LEDマトリックス上のバブルも傾きます。

**必要なコンポーネント**

このプロジェクトで必要なコンポーネントは以下の通りです。

一式をまとめて購入する方が便利です。リンクはこちら：

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
        - :ref:`cpn_dot_matrix`
        - 1
        - 
    *   - 6
        - :ref:`cpn_74hc595`
        - 2
        - |link_74hc595_buy|
    *   - 7
        - :ref:`cpn_mpu6050`
        - 1
        - 

**回路図**

|sch_bubble_level|

MPU6050は、各方向の加速度値を取得し、姿勢角を計算します。
その結果、プログラムは、2つの74HC595チップからのデータに基づいて、ドットマトリックス上に2x2のドットを描画します。
姿勢角が変わると、プログラムは74HC595チップに異なるデータを送信し、ドットの位置が変わり、バブル効果が生まれます。

**配線**

|wiring_digital_bubble_level|

**コード**

.. note::

    * ``kepler-kit-main/micropython`` フォルダの ``7.12_digital_bubble_level.py`` ファイルを開いて実行するか、このコードをThonnyにコピーして「Run Current Script」をクリック、またはF5キーを押して実行してください。

    * 右下の角にある「MicroPython（Raspberry Pi Pico）」のインタープリターを選択することを忘れないでください。

    * 詳細なチュートリアルは、 :ref:`open_run_code_py` を参照してください。
    * ここでは ``imu.py`` と ``vector3d.py`` が必要です。Pico Wにアップロードされているかどうか確認してください。詳細なチュートリアルは :ref:`add_libraries_py` を参照してください。

.. code-block:: python

    import machine
    from machine import I2C, Pin
    import time
    import math
    from imu import MPU6050


    ### mpu6050
    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
    mpu = MPU6050(i2c)

    # get rotary angle
    def dist(a,b):
        return math.sqrt((a*a)+(b*b))

    def get_y_rotation(x,y,z):
        radians = math.atan2(x, dist(y,z))
        return -math.degrees(radians)

    def get_x_rotation(x,y,z):
        radians = math.atan2(y, dist(x,z))
        return math.degrees(radians)

    def get_angle():
        y_angle=get_y_rotation(mpu.accel.x, mpu.accel.y, mpu.accel.z) 
        x_angle=get_x_rotation(mpu.accel.x, mpu.accel.y, mpu.accel.z) 
        return x_angle,y_angle

    ### led matrix display
    sdi = machine.Pin(18,machine.Pin.OUT)
    rclk = machine.Pin(19,machine.Pin.OUT)
    srclk = machine.Pin(20,machine.Pin.OUT)

    def hc595_in(dat):
        for bit in range(7,-1, -1):
            srclk.low()
            time.sleep_us(30)
            sdi.value(1 & (dat >> bit))
            time.sleep_us(30)
            srclk.high()

    def hc595_out():
        rclk.high()
        time.sleep_us(200)
        rclk.low()

    def display(glyph):
        for i in range(0,8):
            hc595_in(glyph[i])
            hc595_in(0x80>>i)
            hc595_out()

    # data transformation
    def matrix_2_glyph(matrix):
        glyph= [0 for i in range(8)] # glyph code for display()
        for i in range(8):
            for j in range(8):
                glyph[i]+=matrix[i][j]<<j
        return glyph

    def clamp_number(val, min, max):
        return min if val < min else max if val > max else val

    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    # Calculate the position of the bubble
    sensitivity=4          # The higher the number, the more sensitive
    matrix_range=7         # The size of the matrix is 8, so the coordinate range is 0~7
    point_range=matrix_range-1     # The x, y value of the bubble's marker point (upper left point) should be between 0-6
    def bubble_position():
        x,y=get_angle()
        x=int(clamp_number(interval_mapping(x,-90,90,0-sensitivity,point_range+sensitivity),0,point_range))
        y=int(clamp_number(interval_mapping(y,-90,90,point_range+sensitivity,0-sensitivity),0,point_range))
        return [x,y]

    # Drop the bubble into empty matrix
    def drop_bubble(matrix,bubble):
        matrix[bubble[0]][bubble[1]]=0
        matrix[bubble[0]+1][bubble[1]]=0
        matrix[bubble[0]][bubble[1]+1]=0
        matrix[bubble[0]+1][bubble[1]+1]=0
        return matrix

    while True:
        matrix= [[1 for i in range(8)] for j in range(8)]  # empty matrix
        bubble=bubble_position() # bubble coordinate
        matrix=drop_bubble(matrix,bubble) # drop the bubble into empty matrix
        display(matrix_2_glyph(matrix)) # show matrix

プログラムを実行した後、ブレッドボードを水平な面に置いてください。
LEDマトリックスの中央にドットが表示されます（中央にない場合は、MPU6050が水平でない可能性があります）。
ブレッドボードを傾けると、ドットも傾けた方向に動きます。
