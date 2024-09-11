.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _ar_keypad:

4.2 - 4x4キーパッド
========================

4x4キーボード、またはマトリックスキーボードは、一つのパネル内で排除された16個のキーのマトリックスです。

キーパッドは、主にデジタル入力が必要なデバイス、例えば電卓、テレビのリモートコントロール、押しボタン式の電話、自動販売機、ATM、組み合わせロック、デジタルドアロックなどで見られます。

このプロジェクトでは、押されたキーを特定し、関連するキー値を取得する方法を学びます。

* :ref:`cpn_keypad`
* `E.161 - Wikipedia <https://en.wikipedia.org/wiki/E.161>`_

**必要な部品**

このプロジェクトには、以下の部品が必要です。

全体のキットを購入するのが便利です。リンクはこちら：

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
        - :ref:`cpn_resistor`
        - 4(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_keypad`
        - 1
        - |link_keypad_buy|

**回路図**

|sch_keypad_ar|

4つのプルダウン抵抗がマトリックスキーボードの各列に接続されています。これにより、キーが押されていないときにG6〜G9が安定したローレベルを取得します。

キーボードの行（G2〜G5）は、高い状態にプログラムされています。G6〜G9のうちの1つが高い状態で読み取られた場合、どのキーが押されたかを知ることができます。

例えば、G6が高い状態で読み取られた場合、数字キー1が押されています。これは、数字キー1の制御ピンがG2とG6であり、数字キー1が押されたときにG2とG6が接続され、G6も高い状態になるためです。

**配線**

|wiring_keypad_ar|

配線を簡単にするために、上記の図では、マトリックスキーボードの列と10K抵抗が、同時にG6〜G9の位置にある穴に挿入されています。

**コード**

.. note::

    * ファイル ``4.2_4x4_keypad.ino`` は、 ``kepler-kit-main/arduino/4.2_4x4_keypad`` のパスで開くことができます。
    * またはこのコードを **Arduino IDE** にコピーペーストしてください。
    * **アップロード** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と正確なポートを選択してください。
    * ``Adafruit Keypad`` ライブラリがここで使用されます。このライブラリは **Library Manager** からインストールできます。

      .. image:: img/lib_ad_keypad.png

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/6c776dfc-cb74-49d7-8906-f1382e0e7b7b/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

プログラムが実行された後、シェルはキーパッドで押したキーを出力します。

**仕組み**

1. ライブラリのインクルード

   最初に、キーパッドとのインターフェースを簡単にするための ``Adafruit_Keypad`` ライブラリをインクルードします。

   .. code-block:: arduino

     #include "Adafruit_Keypad.h"

2. キーパッドの設定

   .. code-block:: arduino

     const byte ROWS = 4;
     const byte COLS = 4;
     char keys[ROWS][COLS] = {
       { '1', '2', '3', 'A' },
       { '4', '5', '6', 'B' },
       { '7', '8', '9', 'C' },
       { '*', '0', '#', 'D' }
     };
     byte rowPins[ROWS] = { 2, 3, 4, 5 };
     byte colPins[COLS] = { 8, 9, 10, 11 };

   - ``ROWS`` と ``COLS`` 定数は、キーパッドの行と列の数を定義します。 
   - ``keys`` はキーパッドの各ボタンのラベルを保持する2次元配列です。
   - ``rowPins`` と ``colPins`` は、キーパッドの行と列に接続されたArduinoのピンを保持する配列です。

   .. raw:: html

      <br/>

3. キーパッドの初期化

   ``Adafruit_Keypad`` のインスタンス ``myKeypad`` を作成し、それを初期化します。

   .. code-block:: arduino

     Adafruit_Keypad myKeypad = Adafruit_Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

4. setup() 関数

   シリアル通信とカスタムキーパッドを初期化します。

   .. code-block:: arduino

     void setup() {
       Serial.begin(9600);
       myKeypad.begin();
     }

5. メインループ

   キーイベントをチェックし、それをシリアルモニターに表示します。

   .. code-block:: arduino

     void loop() {
       myKeypad.tick();
       while (myKeypad.available()) {
         keypadEvent e = myKeypad.read();
         Serial.print((char)e.bit.KEY);
         if (e.bit.EVENT == KEY_JUST_PRESSED) Serial.println(" pressed");
         else if (e.bit.EVENT == KEY_JUST_RELEASED) Serial.println(" released");
       }
       delay(10);
     }