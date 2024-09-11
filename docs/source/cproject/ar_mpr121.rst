.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _ar_mpr121:

4.3 - 電極キーボード
================================

多数のタッチスイッチをプロジェクトに追加したい場合、MPR121は優れた選択です。このモジュールは、導体で拡張可能な電極を備えています。
電極をバナナに接続すると、そのバナナをタッチスイッチに変えることができます。

* :ref:`cpn_mpr121`

**必要な部品**

このプロジェクトでは、以下のコンポーネントが必要です。

一式を購入することは非常に便利です、リンクはこちらです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットに含まれるアイテム
        - 購入リンク
    *   - Kepler Kit	
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
        - :ref:`cpn_mpr121`
        - 1
        - 

**回路図**

|sch_mpr121_ar|

**配線**

|wiring_mpr121_ar|



**コード**

.. note::

    * ファイル ``4.3_electrode_keyboard.ino`` は、パス ``kepler-kit-main/arduino/4.3_electrode_keyboard`` で開くことができます。
    * または、このコードを **Arduino IDE** にコピーペーストしてください。
    * **アップロード** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と正しいポートを選択してください。
    * ``Adafruit MPR121`` ライブラリがここで使用されます。このライブラリは **Library Manager** からインストールできます。

      .. image:: img/lib_mpr121.png

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/f31048b7-0f98-4d49-8c2e-26b3908e98cb/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

プログラムが動作すると、MPR121モジュール上の12個の電極に手で触れ、それらの電極のタッチ状態が12ビットのブーリアン型配列に記録され、シリアルモニターに出力されます。
最初と11番目の電極に触れると、 ``100000000010`` が出力されます。

電極を果物、ワイヤー、箔などの他の導体に接続して拡張することができます。これにより、これらの電極をトリガーする多くの方法が得られます。

**動作原理**

``MPR121`` オブジェクトを初期化します。この時点で、モジュールの電極の状態が初期値として記録されます。
電極を拡張する場合は、初期値をリセットするために例を再実行する必要があります。

.. code-block:: arduino

    #include "Adafruit_MPR121.h"

    Adafruit_MPR121 cap = Adafruit_MPR121();

    void setup() {
        Serial.begin(9600);
        int check = cap.begin(0x5A);
        if (!check) {
            Serial.println("MPR121 not found, check wiring?");
            while (1);
        }
        Serial.println("MPR121 found!");
    }

現在の電極の値を取得します。最初と11番目の電極に触れると、 ``100000000010`` が取得されます。

.. code-block:: arduino

    // Get the currently touched pads
    currtouched = cap.touched();

Determine if the electrode state has changed.

.. code-block:: arduino

    void loop() {
        currtouched = cap.touched();
        if (currtouched != lasttouched) {}

        // reset our state
        lasttouched = currtouched;
    }

電極の状態に変更が検出された場合、 ``currtouched`` の値が ``touchStates[12]`` 配列にビットごとに格納されます。最後に、配列が出力されます。

.. code-block:: arduino

    if (currtouched != lasttouched) {
        for (int i = 0; i < 12; i++) {
            if (currtouched & (1 << i)) touchStates[i] = 1;
            else touchStates[i] = 0;
        }
        for (int i = 0; i < 12; i++){
            Serial.print(touchStates[i]);
        }
        Serial.println();
    }
