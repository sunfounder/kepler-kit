.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

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

   * ここでは ``MFRC522`` ライブラリが使用されています。このライブラリは **Library Manager** からインストールできます。

      .. image:: img/lib_mfrc522.png

メイン機能は2つに分かれています：

* ``6.5_rfid_write`` でカード（またはキー）に情報を書き込む機能。

  .. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/b4f9156a-711a-442c-8271-329847e808dc/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

  実行後、シリアルモニタにメッセージを入力し、 ``#`` で終了します。次に、カード（またはキー）をMFRC522モジュールに近づけることで、メッセージがカードに書き込まれます。

* ``6.5_rfid_read`` でカード（またはキー）から情報を読み取る機能。

  .. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/df57b5cb-9162-4b4b-b28a-7f02363885c9/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

  実行後、カード（またはキー）に保存されたメッセージを読み取ることができます。

**どのように動作するのか？**

.. code-block:: arduino

    #include <MFRC522.h>

    #define RST_PIN         9
    #define SS_PIN          17

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
