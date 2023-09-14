.. _ar_dht11:

6.2 - 温度・湿度
=======================================

湿度と温度は、物理量自体から日常生活に至るまで、密接に関連しています。
人々が生活する環境の温度と湿度は、人体の体温調節機能や熱伝達効果に直接影響を与えます。
さらには、思考活動や精神状態にも影響を与え、学習や仕事の効率にも関わってきます。

温度は国際単位系（SI）における7つの基本物理量の一つであり、物体の熱い・冷たい程度を測るために使用されます。
摂氏は、世界で広く使用されている温度の尺度の一つであり、「℃」という記号で表されます。

湿度とは、空気中に存在する水蒸気の濃度です。
相対湿度は、日常生活でよく使用されるものであり、%RHで表されます。相対湿度は温度と密接に関連しています。
密閉された一定量のガスにおいて、温度が高いほど相対湿度は低く、温度が低いほど相対湿度は高くなります。

|img_Dht11|

このキットには基本的なデジタル温度・湿度センサー、 **DHT11** が含まれています。
このセンサーは、周囲の空気の湿度と温度を測定するために、容量性湿度センサーとサーミスタを使用し、データピンでデジタル信号を出力します（アナログ入力ピンは不要です）。

* :ref:`cpn_dht11`

**必要なコンポーネント**

このプロジェクトでは、以下のコンポーネントが必要です。

全体のキットを購入する方が便利です、リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットに含まれるアイテム
        - 購入リンク
    *   - ケプラーキット
        - 450+
        - |link_kepler_kit|

以下のリンクから個別にも購入可能です。

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
        - :ref:`cpn_dht11`
        - 1
        - |link_dht22_buy|

**回路図**

|sch_dht11|

**配線**

|wiring_dht11|

**コード**

.. note::

    * ファイル ``6.2_dht11.ino`` は、パス ``kepler-kit-main/arduino/6.2_dht11`` の下で開くことができます。
    * または、このコードを **Arduino IDE** にコピーしてください。
    * **アップロード** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と正確なポートを選択することを忘れないでください。
    * ここでは ``SimpleDHT`` ライブラリが使用されています。Arduino IDEに追加する方法については、 :ref:`add_libraries_ar` を参照してください。

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/b9e96e99-59d4-48ca-b41f-c03577acfb8f/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

コードが実行された後、シリアルモニターが連続して温度と湿度を出力するようになり、プログラムが安定して動作するにつれて、これらの二つの値はより正確になります。

**動作原理は？**

DHT11オブジェクトを初期化します。このデバイスは、デジタル入力だけで使用できます。

.. code-block:: arduino

    int pinDHT11 = 16;
    SimpleDHT11 dht11(pinDHT11);

現在の温度と湿度を読み取り、それらは変数 ``temperature`` と ``humidity`` に保存されます。 ``err`` はデータの妥当性を判断するために使用されます。

.. code-block:: arduino

    byte temperature = 0;
    byte humidity = 0;
    int err = dht11.read(&temperature, &humidity, NULL);

無効なデータをフィルタリングします。

.. code-block:: arduino

    if (err != SimpleDHTErrSuccess) {
        Serial.print("Read DHT11 failed, err="); 
        Serial.print(SimpleDHTErrCode(err));
        Serial.print(","); 
        Serial.println(SimpleDHTErrDuration(err)); 
        delay(1000);
        return;
    }    

温度と湿度を出力します。

.. code-block:: arduino

    Serial.print((int)temperature); 
    Serial.print(" *C, "); 
    Serial.print((int)humidity); 
    Serial.println(" H");

最後に、DHT11のサンプリングレートは1HZであり、ループ内で ``delay(1500)`` が必要です。

.. code-block:: arduino

    delay(1500);
