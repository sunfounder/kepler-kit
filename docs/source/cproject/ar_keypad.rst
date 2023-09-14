.. _ar_keypad:

4.2 4x4キーパッド
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

|sch_keypad|

4つのプルダウン抵抗がマトリックスキーボードの各列に接続されています。これにより、キーが押されていないときにG6〜G9が安定したローレベルを取得します。

キーボードの行（G2〜G5）は、高い状態にプログラムされています。G6〜G9のうちの1つが高い状態で読み取られた場合、どのキーが押されたかを知ることができます。

例えば、G6が高い状態で読み取られた場合、数字キー1が押されています。これは、数字キー1の制御ピンがG2とG6であり、数字キー1が押されたときにG2とG6が接続され、G6も高い状態になるためです。

**配線**

|wiring_keypad|

配線を簡単にするために、上記の図では、マトリックスキーボードの列と10K抵抗が、同時にG6〜G9の位置にある穴に挿入されています。

**コード**

.. note::

    * ファイル ``4.2_4x4_keypad.ino`` は、 ``kepler-kit-main/arduino/4.2_4x4_keypad`` のパスで開くことができます。
    * またはこのコードを **Arduino IDE** にコピーペーストしてください。
    * **アップロード** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と正確なポートを選択してください。
    * ここで使われるライブラリは ``Keypad`` です。それをArduino IDEに追加する方法については、 :ref:`add_libraries_ar` を参照してください。

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/6c776dfc-cb74-49d7-8906-f1382e0e7b7b/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

プログラムが実行された後、シェルはキーパッドで押したキーを出力します。

**仕組み**

``Keypad.h`` ライブラリを呼び出すことで、簡単にキーパッドを使用できます。

.. code-block:: arduino

    #include <Keypad.h>

ライブラリ関数：

.. code-block:: arduino

    Keypad(char *userKeymap, byte *row, byte *col, byte numRows, byte numCols)

内部のキーマップを ``userKeymap`` と同じに初期化します。

``userKeymap`` ：キーパッドのボタン上のシンボル。

``row`` , ``col`` ：ピン設定。

``numRows`` , ``numCols`` ：キーパッドのサイズ。

.. code-block:: arduino

    char getKey()

押されているキーを返します（あれば）。この関数は非ブロッキングです。
