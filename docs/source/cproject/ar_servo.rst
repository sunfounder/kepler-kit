.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _ar_servo:

3.7 - サーボの揺れ動き
=======================

このキットには、LEDやパッシブブザーに加えて、PWM信号で制御されるデバイス、サーボも含まれています。

サーボは位置（角度）制御用のデバイスで、一定の角度の変更が必要な制御システムに適しています。飛行機、潜水艦の模型、リモコンロボットなどの高級リモコン玩具で広く使用されています。

さあ、サーボを揺らしてみましょう！

* :ref:`cpn_servo`

**必要なコンポーネント**

このプロジェクトでは、以下のコンポーネントが必要です。

全体のキットを購入すると非常に便利です。リンクはこちらです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットに含まれるアイテム
        - 購入リンク
    *   - ケプラーキット	
        - 450+
        - |link_kepler_kit|

以下のリンクから個別に購入することもできます。

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - コンポーネント紹介	
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
        - :ref:`cpn_servo`
        - 1
        - |link_servo_buy|

**回路図**

|sch_servo|

**配線**

|wiring_servo|

* オレンジ色のワイヤーは信号で、GP15に接続されています。
* 赤色のワイヤーはVCCで、VBUS(5V)に接続されています。
* 茶色のワイヤーはGNDで、GNDに接続されています。

**コード**

.. note::

   * ファイル ``3.7_swinging_servo.ino`` は、パス ``kepler-kit-main/arduino/3.7_swinging_servo`` で開くことができます。
   * または、このコードを **Arduino IDE** にコピーしてください。

   * **アップロード** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と正確なポートを選択してください。

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/d52a67be-be6b-4cbf-b411-810160f56928/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

プログラムが実行されていると、サーボアームが0°から180°まで前後に揺れ動くのが見られます。

**どうやって動くのか？**

``Servo.h`` ライブラリを呼び出すことで、簡単にサーボを制御できます。

.. code-block:: arduino

    #include <Servo.h> 

**ライブラリ関数**

.. code-block:: arduino

    Servo

サーボを制御するための **Servo** オブジェクトを作成。

.. code-block:: arduino

    uint8_t attach(int pin); 

ピンをサーボドライバーに変換。pinModeを呼び出す。失敗時は0を返す。

.. code-block:: arduino

    void detach();

サーボドライブからピンを解放。

.. code-block:: arduino

    void write(int value); 

サーボの角度を度で設定、0から180。

.. code-block:: arduino

    int read();

最後のwrite()で設定した値を返す。

.. code-block:: arduino

    bool attached(); 

サーボが現在接続されている場合は1を返す。
