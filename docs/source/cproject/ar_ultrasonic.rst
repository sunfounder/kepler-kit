.. _ar_ultrasonic:

6.1 - 距離の測定
======================================

超音波センサーモジュールは、物体までの距離を決定するために、ソナーおよびレーダーシステムの原理に基づいて動作します。

* :ref:`cpn_ultrasonic`

**必要なコンポーネント**

このプロジェクトには、以下のコンポーネントが必要です。

全体のキットを購入する方が確実に便利です。リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットに含まれるアイテム
        - 購入リンク
    *   - ケプラーキット
        - 450+
        - |link_kepler_kit|

以下のリンクから個別にも購入できます。

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - コンポーネントの説明
        - 数量
        - 購入リンク
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
        - :ref:`cpn_ultrasonic`
        - 1
        - |link_ultrasonic_buy|

**回路図**

|sch_ultrasonic|

**配線**

|wiring_ultrasonic|

**コード**

.. note::

   * ファイル ``6.1_ultrasonic.ino`` は、パス ``kepler-kit-main/arduino/6.1_ultrasonic`` にあります。
   * または、このコードを **Arduino IDE** にコピーしてください。

   * **アップロード** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と適切なポートを選択してください。

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/631a1663-ce45-4d46-b8f0-7d10f32097a9/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

プログラムが動作していると、シリアルモニターには超音波センサーから先の障害物までの距離が表示されます。

**動作原理**

超音波センサーの適用については、サブ関数を直接確認できます。

.. code-block:: arduino

    float readSensorData(){// ...}

``PING`` は、2マイクロ秒以上のHIGHパルスでトリガーされます。（クリーンな ``HIGH`` パルスを確保するために、事前に短い ``LOW`` パルスを与えます。）

.. code-block:: arduino

    digitalWrite(trigPin, LOW); 
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH); 
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW); 

エコーピンは、PINGからの信号を読み取るために使用され、その期間は物体のエコーを受信するまでの時間（マイクロ秒単位）です。

.. code-block:: arduino

    microsecond=pulseIn(echoPin, HIGH);

音速は340 m/s、または1センチメートル当たり29マイクロ秒です。

これは、ピンによって移動した距離、往復を指し、障害物までの距離を得るために2で割ります。

.. code-block:: arduino

    float distance = microsecond / 29.00 / 2;  

超音波センサーが動作しているときにプログラムが一時停止することに注意してください。これは、複雑なプロジェクトを作成しているときに遅延を引き起こす可能性があります。
