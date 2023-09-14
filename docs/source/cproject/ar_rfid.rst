.. _ar_rfid:

6.5 - 無線周波数識別（RFID）
================================================

無線周波数識別（RFID）は、オブジェクト（またはタグ）と照会装置（またはリーダー）との間で無線通信を使用して、そのようなオブジェクトを自動的に追跡・識別するテクノロジーを指します。タグの伝送範囲はリーダーから数メートルに限られます。リーダーとタグの間には必ずしも直線的な視界が必要ではありません。

ほとんどのタグには、少なくとも一つの集積回路（IC）とアンテナが含まれています。
このマイクロチップは情報を格納し、リーダーとの無線周波数（RF）通信を管理しています。パッシブタグには独立したエネルギー源がなく、リーダーから提供される外部の電磁信号に依存して動作します。
アクティブタグには独立したエネルギー源、例えばバッテリーが含まれています。
したがって、これらは処理能力、伝送能力、および範囲が増加する可能性があります。

* :ref:`cpn_mfrc522`

**必要なコンポーネント**

このプロジェクトでは、以下のコンポーネントが必要です。

全体のキットを購入するのが便利です、リンクは以下の通りです：

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

    *   - 番号
        - コンポーネント紹介	
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
        - :ref:`cpn_mfrc522`
        - 1
        - |link_rfid_buy|

**回路図**

|sch_rfid|

**配線**

|wiring_rfid|


**コード**

.. note::

    * ファイル ``6.5_rfid_write.ino`` は、パス ``kepler-kit-main/arduino/6.5_rfid_write`` で開くことができます。
    * または、このコードを **Arduino IDE** にコピーしてください。
    * **アップロード** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と正しいポートを選択してください。
    * ここではライブラリ「MFRC522」が使用されています。Arduino IDEに追加する方法については、 :ref:`add_libraries_ar` を参照してください。

メインの関数は二つに分かれています：

* ``6.5_rfid_write.ino`` ：カード（またはキー）に情報を書き込むために使用されます。
* ``6.5_rfid_read.ino`` ：カード（またはキー）内の情報を読み取るために使用されます。

.. note::

   * ファイル ``6.5_rfid_write.ino`` は、パス ``kepler-kit-main/arduino/6.5_rfid_write`` で開くことができます。
   * または、このコードを **Arduino IDE** にコピーしてください。

   
   * **アップロード** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と正しいポートを選択してください。

実行後、シリアルモニターでメッセージを入力して、 ``#`` で終了した後、MFRC522モジュールに近づけることでカード（またはキー）にメッセージを書き込むことができます。

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/b4f9156a-711a-442c-8271-329847e808dc/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

.. note::

   * ファイル ``6.5_rfid_read.ino`` は、パス ``kepler-kit-main/arduino/6.5_rfid_read`` で開くことができます。
   * または、このコードを **Arduino IDE** にコピーしてください。

   
   * **アップロード** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と正しいポートを選択してください。

実行後、カード（またはキー）に保存されているメッセージを読み取ることができます。

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/df57b5cb-9162-4b4b-b28a-7f02363885c9/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

**どのように動作するのか？**

.. code-block:: arduino

    #include <MFRC522.h>

    #define RST_PIN         0
    #define SS_PIN          5

    MFRC522 mfrc522(SS_PIN, RST_PIN);

まず、 ``MFRC522()`` クラスをインスタンス化します。

使いやすさのために、 ``MFRC522`` ライブラリは以下の関数でさらにカプセル化されています。

* ``void simple_mfrc522_init()`` : SPI通信を開始し、mfrc522モジュールを初期化します。
* ``void simple_mfrc522_get_card()`` : カード（またはキー）が検出されるまでプログラムを一時停止し、カードのUIDとPICCタイプを表示します。
* ``void simple_mfrc522_write(String text)`` : カード（またはキー）に文字列を書き込みます。
* ``void simple_mfrc522_write(byte* buffer)`` : 通常はシリアルポートから来る情報をカード（またはキー）に書き込みます。
* ``void simple_mfrc522_write(byte section, String text)`` : 特定のセクターに文字列を書き込みます。 ``section`` が0の場合、セクター1-2に書き込みます; ``section`` が1の場合、セクター3-4に書き込みます。
* ``void simple_mfrc522_write(byte section, byte* buffer)`` : 通常はシリアルポートから来る情報を特定のセクターに書き込みます。 ``section`` が0の場合、セクター1-2に書き込みます; ``section`` が1の場合、セクター3-4に書き込みます。
* ``String simple_mfrc522_read()`` : カード（またはキー）内の情報を読み取り、文字列を返します。
* ``String simple_mfrc522_read(byte section)`` : 特定のセクター内の情報を読み取り、文字列を返します。 ``section`` が0の場合、セクター1-2を読み取ります; ``section`` が1の場合、セクター3-4を読み取ります。

``6.5_rfid_write.ino`` の例では、一般的なシリアル入力方法として ``Serial.readBytesUntil()`` 関数が使用されています。

* `Serial.readBytesUntil <https://www.arduino.cc/reference/en/language/functions/communication/serial/readbytesuntil/>`_
