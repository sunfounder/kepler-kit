.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _ar_neopixel:

3.3 WS2812 RGB ストリップ
==========================

WS2812は、制御回路とRGBチップが5050コンポーネントのパッケージ内に統合されているインテリジェントなLED光源です。
この中には、インテリジェントなデジタルポートデータラッチと信号整形増幅駆動回路が内蔵されています。
さらに、高精度の内部オシレーターとプログラム可能な定電流制御部も含まれており、ピクセルポイントの光色の高度な一貫性を効果的に確保します。

データ転送プロトコルは、シングルNZR通信モードを使用します。
ピクセルが電源投入リセット後、DINポートはコントローラからデータを受信し、最初のピクセルが初期の24ビットデータを収集して内部データラッチに送ります。その他のデータは、内部信号整形増幅回路によって整形され、DOポートを介して次のカスケードピクセルに送信されます。各ピクセルの伝送後、信号は24ビット減少します。
ピクセルは、自動的に形状を整える伝送技術を採用しており、ピクセルのカスケード数は信号伝送の速度にのみ依存しています。

* :ref:`cpn_ws2812`

**必要なコンポーネント**

このプロジェクトでは、以下のコンポーネントが必要です。

便利なのは、一式を購入することです。リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットに含まれるアイテム
        - 購入リンク
    *   - ケプラーキット	
        - 450以上
        - |link_kepler_kit|

以下のリンクから個別に購入することもできます。

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
        - :ref:`cpn_ws2812`
        - 1
        - |link_ws2812_buy|

**回路図**

|sch_ws2812|

**配線**

|wiring_ws2812|

.. warning::
    注目すべき一点は電流です。

    Pico Wで任意の数のLEDを使用することは可能ですが、そのVBUSピンの電力は限られています。
    ここでは、安全な範囲内である8つのLEDを使用します。
    ただし、より多くのLEDを使用したい場合は、別の電源を追加する必要があります。

    

**コード**

.. note::

    * ファイル ``3.3_rgb_led_strip.ino`` を ``kepler-kit-main/arduino/3.3_rgb_led_strip`` のパスで開けます。
    * または、このコードを **Arduino IDE** にコピーしてください。
    * **アップロード** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と正しいポートを選択してください。
    * ここではライブラリ ``Adafruit_NeoPixel`` を使用しています。Arduino IDEに追加する方法については、 :ref:`add_libraries_ar` を参照してください。

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/efe5d60f-ea0f-4446-bc5b-30c76197fedf/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

お気に入りの色を選んで、RGB LEDストリップで表示してみましょう！

**動作の仕組み**

Adafruit_NeoPixel型のオブジェクトを宣言し、 ``PIXEL_PIN`` に接続されています。
ストリップには ``PIXEL_COUNT`` 個のRGB LEDがあります。

.. code-block:: arduino

    #define PIXEL_PIN    0
    #define PIXEL_COUNT 8

    // Declare our NeoPixel strip object:
    Adafruit_NeoPixel strip(PIXEL_COUNT, PIXEL_PIN, NEO_GRB + NEO_KHZ800);
    // Argument 1 = Number of pixels in NeoPixel strip
    // Argument 2 = Arduino pin number (most are valid)
    // Argument 3 = Pixel type flags, add together as needed:
    //   NEO_KHZ800  800 KHz bitstream (most NeoPixel products w/WS2812 LEDs)
    //   NEO_KHZ400  400 KHz (classic 'v1' (not v2) FLORA pixels, WS2811 drivers)
    //   NEO_GRB     Pixels are wired for GRB bitstream (most NeoPixel products)
    //   NEO_RGB     Pixels are wired for RGB bitstream (v1 FLORA pixels, not v2)
    //   NEO_RGBW    Pixels are wired for RGBW bitstream (NeoPixel RGBW products)

ストリップオブジェクトを初期化し、すべてのピクセルを「オフ」に設定します。

関数

    * ``strip.begin()`` : NeoPixelストリップオブジェクトを初期化（必須）。
    * ``strip.setPixelColor(index, color)`` : ピクセルの色を設定（RAM内）。 ``color`` は単一の'パックされた' 32ビット値でなければなりません。
    * ``strip.Color(red, green, blue)`` : 単一の'パックされた' 32ビット値としての色。
    * ``strip.show()`` : 新しい内容でストリップを更新。

**さらに学ぶ**

ランダムに色を生成し、カラフルな流れる光を作成することができます。

.. note::

   * ファイル ``3.3_rgb_led_strip_flowing.ino`` を ``kepler-kit-main/arduino/3.3_rgb_led_strip_flowing`` のパスで開けます。
   * または、このコードを **Arduino IDE** にコピーしてください。
   
   * **アップロード** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と正しいポートを選択してください。

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/a3d7c520-b4f8-4445-9454-5fe7d2a24fd9/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

または、このWS2812 LEDストリップで色の輪（範囲65535）をサイクルさせることができます。

.. note::

   * ファイル ``3.3_rgb_led_strip_rainbow.ino`` を ``kepler-kit-main/arduino/3.3_rgb_led_strip_rainbow`` のパスで開けます。
   * または、このコードを **Arduino IDE** にコピーしてください。
   
   * **アップロード** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と正しいポートを選択してください。

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/47d84804-3560-48fa-86df-49f8e2f6ad63/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

* ``strip.getPixelColor(index)`` : 以前に設定されたピクセルの色をクエリします。
* ``strip.ColorHSV(pixelHue)`` : 色相、彩度、明度を ``setPixelColor()`` または他のRGB互換関数に渡すことができるパックされた32ビットRGB色に変換します。
* ``strip.gamma32()`` : 各ピクセルに割り当てる前に"より真実な"色を提供します。

