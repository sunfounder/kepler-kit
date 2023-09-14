.. _ar_lcd:

3.4 - 液晶ディスプレイ
===============================

LCD1602は、文字型の液晶ディスプレイで、同時に32（16×2）文字を表示することができます。

ご存知のように、LCDやその他のディスプレイは人間と機械とのインタラクションを大いに豊かにしていますが、一つ共通の弱点があります。
それは、コントローラーに接続すると、多数のI/Oポートを占有し、コントローラーの他の機能に制限をかけてしまうことです。
そのため、この問題を解決するためにI2Cバスを備えたLCD1602が開発されました。

* :ref:`cpn_i2c_lcd`
* `Inter-Integrated Circuit - Wikipedia <https://en.wikipedia.org/wiki/I2C>`_

|pin_i2c|

ここでは、I2C0インターフェースを使用してLCD1602を制御し、テキストを表示します。

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
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|

**回路図**

|sch_lcd|

**配線**

|wiring_lcd|

**コード**

.. note::

    * ファイル ``3.4_liquid_crystal_display.ino`` は、 ``kepler-kit-main/arduino/3.4_liquid_crystal_display`` のパスで開くことができます。
    * または、このコードを **Arduino IDE** にコピーペーストしてください。
    * **アップロード** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と正確なポートを選択してください。
    * ここで使用されているライブラリは ``LiquidCrystal_I2C`` です。それをArduino IDEに追加する方法については、 :ref:`add_libraries_ar` を参照してください。

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/1f464967-5937-473a-8a0d-8e4577c85e7d/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


プログラムが実行された後、LCDに順番に2行のテキストが表示され、その後消えます。

.. note::
    コードと配線が正しくても、LCDが内容を表示しない場合は、背面のポテンショメータを回してコントラストを上げてみてください。

    
**どのように動作するか？**

ライブラリ ``LiquidCrystal_I2C.h`` を呼び出すことで、LCDを簡単に制御できます。

.. code-block:: arduino

    #include "LiquidCrystal_I2C.h"

**ライブラリ関数**

.. code-block:: arduino

    LiquidCrystal_I2C(uint8_t lcd_Addr,uint8_t lcd_cols,uint8_t lcd_rows)

Arduinoボードに接続された特定のLCDを表す ``LiquidCrystal_I2C`` クラスの新しいインスタンスを作成します。

- **lcd_Addr** : LCDのアドレスはデフォルトで0x27です。
- **lcd_cols** : LCD1602は16列です。
- **lcd_rows** : LCD1602は2行です。

.. code-block:: arduino

    void init()

LCDを初期化します。

.. code-block:: arduino

    void backlight()

（オプションの）バックライトをオンにします。

.. code-block:: arduino

    void nobacklight()

（オプションの）バックライトをオフにします。

.. code-block:: arduino

    void display()

LCDディスプレイをオンにします。

.. code-block:: arduino

    void nodisplay()

LCDディスプレイを素早くオフにします。

.. code-block:: arduino

    void clear()

ディスプレイをクリアし、カーソル位置をゼロに設定します。

.. code-block:: arduino

    void setCursor(uint8_t col,uint8_t row)

カーソル位置をcol,rowに設定します。

.. code-block:: arduino

    void print(data,BASE)

テキストをLCDに出力します。

- **data**: 出力するデータ（char、byte、int、long、またはstring）。

- **BASE（オプション）**: 数値を出力する際の基数：BIN（2進数）、DEC（10進数）、OCT（8進数）、HEX（16進数）。

**詳しくは**

Pico Wにコードをアップロードすると、シリアルモニターで入力した内容がLCDに表示されます。

.. note::

   * ファイル ``3.4_liquid_crystal_display_2.ino`` は、 ``kepler-kit-main/arduino/3.4_liquid_crystal_display_2`` のパスで開くことができます。
   * または、このコードを **Arduino IDE** にコピーペーストしてください。
   
   * **アップロード** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と正確なポートを選択してください。

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/631e0380-d594-4a8b-9bac-eb0688079b97/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Pico Wは、電子部品からのデータを読み取るだけでなく、シリアルポートモニターで入力されたデータも読み取れます。
そのため、 ``Serial.read()`` を回路実験のコントローラーとして使用できます。

``setup()`` でシリアル通信を実行し、データレートを9600に設定します。

.. code-block:: arduino

    Serial.begin(9600);

``loop()`` でシリアルポートモニターの状態を判断し、データが受信された場合のみ情報処理が行われます。

.. code-block:: arduino

    if (Serial.available() > 0){}

画面をクリアします。

.. code-block:: arduino

    lcd.clear();

シリアルポートモニターで入力値を読み取り、それを変数incomingByteに格納します。

.. code-block:: arduino

    char incomingByte = Serial.read();

各文字をLCDに表示し、改行文字はスキップします。

.. code-block:: arduino

    while (Serial.available() > 0) {
        char incomingByte=Serial.read();
        if(incomingByte==10){break;}// 改行文字をスキップ
        lcd.print(incomingByte);// 各文字をLCDに表示
    } 

* `Serial Read <https://www.arduino.cc/reference/en/language/functions/communication/serial/read/>`_
