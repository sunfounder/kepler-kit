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
    * ここでは ``IRsmallDecoder`` ライブラリが使用されています。 :ref:`add_libraries_ar` を参照して、Arduino IDEに追加してください。

.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/71f50561-d1ad-4d9e-9db2-8eb7727df0a4/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

新しいリモートコントロールには、内部のバッテリーを隔離するためのプラスチック片が端にあります。使用する際には、このプラスチック片を引き抜いてリモートコントロールに電源を供給してください。
プログラムが動作している間、リモートコントロールのボタンを押すと、シリアルモニターに押したキーが表示されます。

.. **動作原理**

