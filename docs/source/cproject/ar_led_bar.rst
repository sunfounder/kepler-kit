.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _ar_led_bar:

2.2 - レベル表示
=============================

最初のプロジェクトはLEDを点滅させる単純なものです。このプロジェクトでは、LEDバーグラフを使用しましょう。これは、10個のLEDがプラスチックケースにパッケージされており、一般的には電力や音量レベルを表示するために使用されます。

|img_led_bar_pin|

* :ref:`cpn_led_bar`

**必要なコンポーネント**

このプロジェクトで必要なコンポーネントは以下の通りです。

全体のキットを購入するのが便利です。以下がリンクです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットに含まれるアイテム
        - 購入リンク
    *   - ケプラーキット	
        - 450以上
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
        - :ref:`cpn_resistor`
        - 10(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led_bar`
        - 1
        - 

**回路図**

|sch_ledbar|

LEDバーグラフには10個のLEDがあり、それぞれが個別に制御可能です。ここでは、10個のLEDのアノードはGP6〜GP15に接続され、カソードは220Ωの抵抗器を介してGNDに接続されています。

**配線**

|wiring_ledbar|

**コード**

.. note::

   * ファイル ``2.2_display_the_level.ino`` は ``kepler-kit-main/arduino/2.2_display_the_level`` のパスで開くことができます。
   * または、このコードを **Arduino IDE** にコピーペーストしてください。

    * **アップロード** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と正確なポートを選択してください。

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/ae60e723-430e-4a58-ac39-566b9d1828e8/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

プログラムが動作すると、LEDバーグラフのLEDが順番に点灯し、次に消灯します。

**動作原理**

LEDバーの各LEDはピンで制御する必要があります。つまり、これらの10個のピンを定義する必要があります。

``setup()`` 内のコードはforループを使用して、順番にピン6〜15を出力モードに初期化します。

.. code-block:: C

    for(int i=6;i<=15;i++)
    {
        pinMode(i,OUTPUT);
    }   

``loop()`` 内でforループを使用して、LEDを順番に点滅させます（0.5秒点灯、次に0.5秒消灯）。

.. code-block:: C

    for(int i=6;i<=15;i++)
    {
        digitalWrite(i,HIGH);
        delay(500);
        digitalWrite(i,LOW);
        delay(500);    
    }
