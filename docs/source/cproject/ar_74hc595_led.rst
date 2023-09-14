.. _ar_74hc_led:

5.1 マイクロチップ - 74HC595
===============================

集積回路（integrated circuit）は、回路内で「IC」という文字で表されるミニチュア電子デバイスまたはコンポーネントです。

トランジスタ、抵抗器、コンデンサ、インダクタなど、回路で必要なコンポーネントと配線を特定のプロセスで相互接続し、小型またはいくつかの小型半導体ウェハーまたは誘電体基板上に製造し、それをパッケージに封装することで、必要な回路機能を持つ微細構造になります。全てのコンポーネントは一体化されており、これにより電子部品は微細化、低消費電力、知能化、高信頼性に大きく前進しています。

集積回路の発明者は、Jack Kilby（ゲルマニウム（Ge）ベースの集積回路）とRobert Norton Noyce（シリコン（Si）ベースの集積回路）です。

このキットには、GPIOピンの使用を大幅に節約できるIC、74HC595が装備されています。
具体的には、8ビットの2進数を書き込むことで、デジタル信号出力のための8ピンを置き換えることができます。

* `2進数 - Wikipedia <https://ja.wikipedia.org/wiki/2%E9%80%B2%E6%95%B0>`_

* :ref:`74HC595`

**必要な部品**

このプロジェクトでは、以下の部品が必要です。

便利なのは、一式を購入することです。こちらがそのリンクです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットに含まれるアイテム
        - 購入リンク
    *   - Kepler Kit
        - 450以上
        - |link_kepler_kit|

以下のリンクから個別に購入することも可能です。

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - コンポーネントの説明
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
        - 8（220Ω）
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 8
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|

**回路図**

|sch_74hc_led|

* MR（ピン10）がハイレベルで、OE（ピン13）がローレベルの場合、SHcpの立ち上がりエッジでデータが入力され、SHcpの立ち上がりエッジを介してメモリレジスタに移動します。
* 2つのクロックが一緒に接続されている場合、シフトレジスタは常にメモリレジスタよりも1パルス早いです。
* メモリレジスタには、シリアルシフト入力ピン（Ds）、シリアル出力ピン（Q）、および非同期リセットボタン（ローレベル）があります。
* メモリレジスタは、3つの状態で8ビットの並列バスを出力します。
* OEが有効（ローレベル）の場合、メモリレジスタ内のデータがバス（Q0〜Q7）に出力されます。

**配線**

|wiring_74hc_led|

**コード**

.. note::

   * ``kepler-kit-main/arduino/5.1_microchip_74hc595`` のパスの下で ``5.1_microchip_74hc595.ino`` ファイルを開くことができます。
   * または、このコードを **Arduino IDE** にコピーしてください。

   * **アップロード** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と正しいポートを選択することを忘れないでください。

.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/71854882-0c1b-4d09-b3e7-5ef7272f7293/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

プログラムが動作していると、LEDが順番に点灯しているのが見えます。

**仕組みは？**

配列を宣言し、74HC595で制御される8つのLEDの作動状態を変更するために使用されるいくつかの8ビットの2進数を格納します。

.. code-block:: arduino

    int datArray[] = {0b00000000, 0b00000001, 0b00000011, 0b00000111, 0b00001111, 0b00011111, 0b00111111, 0b01111111, 0b11111111};

まず ``STcp`` をローレベルに設定し、次にハイレベルに設定します。これにより、  ``STcp`` の立ち上がりエッジパルスが生成されます。

.. code-block:: arduino

    digitalWrite(STcp,LOW); 

``shiftOut()`` は、1ビットずつデータのバイトをシフトアウトするために使用されます。つまり、DSピンを使ってdatArray[num]のデータバイトをシフトレジスタにシフトします。MSBFIRSTは高ビットから動かすことを意味します。

.. code-block:: arduino

    shiftOut(DS,SHcp,MSBFIRST,datArray[num]);

``digitalWrite(STcp,HIGH)`` が実行された後、STcpは立ち上がりエッジになります。この時点で、シフトレジスタ内のデータがメモリレジスタに移動します。

.. code-block:: arduino

    digitalWrite(STcp,HIGH);

8回後に、1バイトのデータがメモリレジスタに転送されます。その後、メモリレジスタのデータがバス（Q0-Q7）に出力されます。例えば、 ``B00000001`` をシフトアウトすると、Q0で制御されるLEDが点灯し、Q1〜Q7で制御されるLEDは消灯します。
