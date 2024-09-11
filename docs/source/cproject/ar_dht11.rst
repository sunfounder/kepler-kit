.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

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
    * ``DHT sensor library`` ライブラリがここで使用されます。このライブラリは **Library Manager** からインストールできます。

      .. image:: img/lib_dht.png

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/b9e96e99-59d4-48ca-b41f-c03577acfb8f/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

コードが実行された後、シリアルモニターが連続して温度と湿度を出力するようになり、プログラムが安定して動作するにつれて、これらの二つの値はより正確になります。

**動作原理は？**

#. 必要なライブラリのインクルードと定数の定義。
   この部分では、DHTセンサライブラリをインクルードし、このプロジェクトで使用するピン番号とセンサの種類を定義します。

   .. code-block:: arduino
    
      #include <DHT.h>
      #define DHTPIN 16       // センサが接続されているピンを定義
      #define DHTTYPE DHT11  // 使用するセンサの種類を定義

#. DHTオブジェクトの作成。
   ここでは、定義されたピン番号とセンサの種類を使用してDHTオブジェクトを作成します。

   .. code-block:: arduino

      DHT dht(DHTPIN, DHTTYPE);  // DHTオブジェクトを作成

#. この関数はArduinoが起動したときに一度だけ実行されます。シリアル通信とDHTセンサをこの関数で初期化します。

   .. code-block:: arduino

      void setup() {
        Serial.begin(9600);
        Serial.println(F("DHT11テスト!"));
        dht.begin();  // DHTセンサを初期化
      }

#. メインループ。
   ``loop()`` 関数は、setup関数の後に連続して実行されます。ここでは、湿度と温度の値を読み取り、ヒートインデックスを計算し、これらの値をシリアルモニターに表示します。センサの読み取りに失敗した場合（NaNが返された場合）、エラーメッセージを表示します。

   .. note::
    
      |link_heat_index| は、気温と湿度を組み合わせて、外がどれだけ暑く感じるかを測定する方法です。これは「体感気温」または「見かけの気温」とも呼ばれます。

   .. code-block:: arduino

      void loop() {
        delay(2000);
        float h = dht.readHumidity();
        float t = dht.readTemperature();
        float f = dht.readTemperature(true);
        if (isnan(h) || isnan(t) || isnan(f)) {
          Serial.println(F("Failed to read from DHT sensor!"));
          return;
        }
        float hif = dht.computeHeatIndex(f, h);
        float hic = dht.computeHeatIndex(t, h, false);
        Serial.print(F("Humidity: "));
        Serial.print(h);
        Serial.print(F("%  Temperature: "));
        Serial.print(t);
        Serial.print(F("°C "));
        Serial.print(f);
        Serial.print(F("°F  Heat index: "));
        Serial.print(hic);
        Serial.print(F("°C "));
        Serial.print(hif);
        Serial.println(F("°F"));
      }
