.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _ar_button:

2.5 - ボタン値の読み取り
==============================================

GPIO（General-purpose input/output、汎用入出力）という名前からわかるように、これらのピンには入力と出力の両方の機能があります。
前のレッスンでは出力機能を使用しましたが、この章では入力機能を使用してボタンの値を読み取ります。

* :ref:`cpn_button`

**必要なコンポーネント**

このプロジェクトでは、以下のコンポーネントが必要です。

全体のキットを購入するのが便利です、リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットに含まれるアイテム
        - 購入リンク
    *   - ケプラーキット	
        - 450+
        - |link_kepler_kit|

以下のリンクから個々にも購入できます。

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - コンポーネントの紹介
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
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_button`
        - 1
        - |link_button_buy|

**回路図**

|sch_button|

ボタンのピンの一方は3.3vに接続され、もう一方のピンはGP14に接続されているため、ボタンが押されると、GP14は高くなります。しかし、ボタンが押されていないとき、GP14は未定義の状態にあり、高いか低いかが不明です。ボタンが押されていないときに安定した低レベルを得るために、GP14は10Kプルダウン抵抗を介してGNDに再接続する必要があります。

**配線**

|wiring_button|

.. note::
    4本足のボタンはH型のボタンと考えることができます。その左（右）の2本の足は接続されており、中央の仕切り線をまたぐと、同じ行番号の2つの半行が接続されます（例えば、私の回路では、E23とF23が接続されています。E25とF25も同様です）。

    ボタンが押される前は、左右は互いに独立しており、一方から他方への電流は流れません。


**コード**

.. note::

    * ファイル ``2.5_reading_button_value.ino`` は、 ``kepler-kit-main/arduino/2.5_reading_button_value`` のパスにあります。
    * または、このコードを **Arduino IDE** にコピーしてください。

    * アップロードボタンをクリックする前に、ボード（Raspberry Pi Pico）と正確なポートを選択することを忘れないでください。

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/6fcb7cac-e866-4a2d-8162-8e0c6fd17660/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

コードが実行された後、Arduino IDEの右上角にある虫眼鏡アイコン（シリアルモニタ）をクリックしてください。

.. image:: img/open_serial_monitor.png

これで、ボタンを押すと、シリアルモニタに「You pressed the button!」と表示されます。

**動作原理は？**

シリアルモニタを有効にするには、 ``setup()`` でシリアル通信を開始し、データレートを9600に設定する必要があります。

.. code-block:: arduino

    Serial.begin(115200);

* `Serial <https://www.arduino.cc/reference/en/language/functions/communication/serial/>`_

ボタンには、その値を取得できるようにモードを ``INPUT`` に設定する必要があります。

.. code-block:: arduino

    pinMode(buttonPin, INPUT);

``buttonPin`` の状態を ``loop()`` で読み取り、変数 ``buttonState`` に割り当てます。

.. code-block:: arduino

    buttonState = digitalRead(buttonPin);

* `digitalRead() <https://www.arduino.cc/reference/en/language/functions/digital-io/digitalread/>`_

``buttonState`` がHIGHであれば、LEDが点滅し、シリアルモニタに「You pressed the button!」と表示されます。

.. code-block:: arduino

    if (buttonState == HIGH) {
        Serial.println("You pressed the button!");
    }


**プルアップ動作モード**

次に、ボタンがプルアップ動作モードでの配線とコードです、試してみてください。

|wiring_button_pullup|

.. 1. Pico Wの3V3ピンをブレッドボードの正の電源バスに接続します。
.. #. ボタンをブレッドボードに挿入し、中央の仕切り線をまたぐようにします。
.. #. ジャンパワイヤーを使用して、ボタンのピンの一つを**負**のバスに接続します（私の場合は右上のピンです）。
.. #. もう一方のピン（左上または左下）をGP14にジャンパワイヤーで接続します。
.. #. 10Kの抵抗器を使用して、ボタンの左上隅のピンと**正**のバスを接続します。
.. #. ブレッドボードの負の電源バスをPicoのGNDに接続します。

プルダウンモードとの唯一の違いは、10Kの抵抗器が3.3Vに接続され、ボタンがGNDに接続されているため、ボタンを押すとGP14は低レベルになることです。これは、プルダウンモードで得られる値とは逆です。
したがって、このコードを ``if (buttonState == LOW)`` に変更するだけです。
