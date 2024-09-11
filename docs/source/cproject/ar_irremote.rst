.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _ar_irremote:

6.4 - IR リモートコントロール
================================

家庭用電子機器では、テレビやDVDプレーヤーなどのデバイスを操作するためにリモートコントロールが使用されます。
場合によっては、リモートコントロールによって手の届かない場所にあるデバイス、例えばセントラルエアコンを操作することも可能です。

IRレシーバーは、赤外線を受信するように調整されたフォトセルを持つ部品です。
ほとんどの場合、リモートコントロールの検出に使用されます。すべてのテレビやDVDプレーヤーの前面には、クリッカーからのIR信号を受信するためのものがあります。
リモートコントロールの内部には、テレビをオン、オフ、またはチャンネルを変更するように指示するIR LEDがあります。

* :ref:`cpn_ir_receiver`

**必要な部品**

このプロジェクトでは、以下の部品が必要です。

便利なのは、一式をまとめて購入することです。リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットに含まれるアイテム
        - 購入リンク
    *   - ケプラーキット
        - 450以上
        - |link_kepler_kit|

以下のリンクから個々にも購入できます。

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - 部品紹介
        - 個数
        - 購入リンク

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
        - :ref:`cpn_ir_receiver`
        - 1
        - |link_receiver_buy|

**回路図**

|sch_irrecv|

**配線**

|wiring_irrecv|

**コード**

.. note::

    * ファイル ``6.4_ir_remote_control.ino`` は、 ``kepler-kit-main/arduino/6.4_ir_remote_control`` のパスで開くことができます。
    * またはこのコードを **Arduino IDE** にコピーペーストしてください。
    * **アップロード** ボタンを押す前に、ボード（Raspberry Pi Pico）と正確なポートを選択してください。
    * ``IRremote`` ライブラリがここで使用されます。このライブラリは **Library Manager** からインストールできます。

      .. image:: img/lib_ir.png

.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/71f50561-d1ad-4d9e-9db2-8eb7727df0a4/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

新しいリモートコントロールには、内部のバッテリーを隔離するためのプラスチック片が端にあります。使用する際には、このプラスチック片を引き抜いてリモートコントロールに電源を供給してください。
プログラムが動作している間、リモートコントロールのボタンを押すと、シリアルモニターに押したキーが表示されます。

**動作原理**

このコードは、 ``IRremote`` ライブラリを使用して、赤外線（IR）リモコンと連携するように設計されています。以下はその概要です。

#. ライブラリのインクルードと定数の定義。まず、IRremoteライブラリがインクルードされ、IR受信機のピン番号が2として定義されます。

   .. code-block:: cpp
 
     #include <IRremote.h>
     const int IR_RECEIVE_PIN = 17;

#. 9600ボーの通信速度でシリアル通信を初期化します。指定されたピン（ ``IR_RECEIVE_PIN`` ）でIR受信機を初期化し、LEDフィードバックを有効にします（該当する場合）。

   .. code-block:: arduino

       void setup() {
           Serial.begin(9600);                                     // 9600ボーの通信速度でシリアル通信を開始
           IrReceiver.begin(IR_RECEIVE_PIN, ENABLE_LED_FEEDBACK);  // IR受信機を開始
       }

#. ループは連続して実行され、受信したIRリモコン信号を処理します。

   .. code-block:: arduino

      void loop() {
         if (IrReceiver.decode()) {  // IR受信機が信号を受信したかどうかを確認
            bool result = 0;
            String key = decodeKeyValue(IrReceiver.decodedIRData.command);
            if (key != "ERROR") {
              Serial.println(key);  // 読み取り可能なコマンドを表示
              delay(100);
            }
         IrReceiver.resume();  // 次の信号を受信するためにIR受信機を準備
        }
      }
   
   * IR信号が受信され、正常にデコードされたか確認します。
   * デコードされたIRコマンドをカスタムの ``decodeKeyValue()`` 関数を使用して ``decodedValue`` に保存します。
   * デコードされたIR値をシリアルモニターに表示します。
   * 次の信号を受信するために、IR信号受信を再開します。

   .. raw:: html

        <br/>

#. 受信したIR信号を対応するキーにマッピングするヘルパー関数

   .. image:: img/ir_key.png
      :align: center
      :width: 80%

   .. code-block:: arduino

      // Function to map received IR signals to corresponding keys
      String decodeKeyValue(long result) {
        // Each case corresponds to a specific IR command
        switch (result) {
          case 0x16:
            return "0";
          case 0xC:
            return "1";
          case 0x18:
            return "2";
          case 0x5E:
            return "3";
          case 0x8:
            return "4";
          case 0x1C:
            return "5";
          case 0x5A:
            return "6";
          case 0x42:
            return "7";
          case 0x52:
            return "8";
          case 0x4A:
            return "9";
          case 0x9:
            return "+";
          case 0x15:
            return "-";
          case 0x7:
            return "EQ";
          case 0xD:
            return "U/SD";
          case 0x19:
            return "CYCLE";
          case 0x44:
            return "PLAY/PAUSE";
          case 0x43:
            return "FORWARD";
          case 0x40:
            return "BACKWARD";
          case 0x45:
            return "POWER";
          case 0x47:
            return "MUTE";
          case 0x46:
            return "MODE";
          case 0x0:
            return "ERROR";
          default:
            return "ERROR";
        }
      }