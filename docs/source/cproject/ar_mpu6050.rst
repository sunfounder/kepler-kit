.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _ar_mpu6050:

6.3 - 6軸モーショントラッキング
===================================

MPU-6050は、3軸ジャイロスコープと3軸加速度計を組み合わせた6軸モーショントラッキングデバイスです。

加速度計は、適切な加速度を測定するツールです。例えば、地球上で静止している加速度計は、地球の重力による加速度を直上方向に測定します。その値はおおよそ g ≈ 9.81 m/s2 です。

加速度計は産業や科学で多くの用途があります。例としては、航空機やミサイルの慣性航法システム、タブレットやデジタルカメラの画像を垂直に保つためなどがあります。

ジャイロスコープは、デバイスの方向や角速度を測定するために使用されます。ジャイロスコープの応用例としては、自動車の反転防止やエアバッグシステム、スマートデバイスのモーションセンシングシステム、ドローンの姿勢安定化システムなどがあります。

* :ref:`cpn_mpu6050`

**必要なコンポーネント**

このプロジェクトで必要なコンポーネントは以下の通りです。

一式をまとめて購入するのが便利です。詳細は以下のリンクを参照してください：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットに含まれるアイテム
        - 購入リンク
    *   - ケプラーキット	
        - 450+
        - |link_kepler_kit|

以下のリンクから個々に購入することもできます。

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - コンポーネント説明	
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
        - :ref:`cpn_mpu6050`
        - 1
        - 

**回路図**

|sch_mpu6050|

**配線**

|wiring_mpu6050|


**コード**

.. note::

    * ``kepler-kit-main/arduino/6.3_6axis_motion_tracking`` のパスにある ``6.3_6axis_motion_tracking.ino`` ファイルを開いてください。
    * または、このコードを **Arduino IDE** にコピーアンドペーストしてください。
    * **Upload** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と正確なポートを選択することを忘れないでください。
    * ここでは ``Adafruit_MPU6050`` ライブラリを使用しています。Arduino IDEに追加する方法については、 :ref:`add_libraries_ar` を参照してください。

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/318f62d3-1d7b-4ee6-a1a2-97e783cf2d5e/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

プログラムを実行した後、3軸加速度計の値と3軸ジャイロスコープの値が出力に順次表示されます。
この時点でMPU6050をランダムに回転させると、これらの値はそれに応じて変化するでしょう。
変化を容易に確認するために、出力ラインの一つをコメントアウトして、別のデータセットに焦点を当てることができます。

**動作原理**

``MPU6050`` オブジェクトをインスタンス化します。

.. code-block:: arduino

    #include <Adafruit_MPU6050.h>
    #include <Wire.h>

    Adafruit_MPU6050 mpu;


MPU6050を初期化し、その精度を設定します。

.. code-block:: arduino

    void setup(void) {
        Serial.begin(115200);
        while (!Serial)
            delay(10); // will pause Zero, Leonardo, etc until serial console opens

        Serial.println("Adafruit MPU6050 test!");

        // Try to initialize!
        if (!mpu.begin()) {
            Serial.println("Failed to find MPU6050 chip");
            while (1) {
            delay(10);
            }
        }
        Serial.println("MPU6050 Found!");

        // Set range
        mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
        mpu.setGyroRange(MPU6050_RANGE_500_DEG);
        mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);

        Serial.println("");
        delay(100);
    }

新しいセンサーイベントとその読み取り値を取得します。

.. code-block:: arduino

    sensors_event_t a, g, temp;
    mpu.getEvent(&a, &g, &temp);

これにより、データ ``a.acceleration.x`` 、 ``a.acceleration.y`` 、 ``a.acceleration.z`` 、 ``g.gyro.x`` 、 ``g.gyro.y`` 、 ``g.gyro.z`` でリアルタイムの加速度と角速度の値を取得できます。

.. code-block:: arduino

    Serial.print("Acceleration X: ");
    Serial.print(a.acceleration.x);
    Serial.print(", Y: ");
    Serial.print(a.acceleration.y);
    Serial.print(", Z: ");
    Serial.print(a.acceleration.z);
    Serial.println(" m/s^2");

    Serial.print("Rotation X: ");
    Serial.print(g.gyro.x);
    Serial.print(", Y: ");
    Serial.print(g.gyro.y);
    Serial.print(", Z: ");
    Serial.print(g.gyro.z);
    Serial.println(" rad/s");
