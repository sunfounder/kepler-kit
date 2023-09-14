.. _ar_tilt:

2.6 - 傾けてみよう！
==========================

|img_tilt|

この傾斜スイッチは中央に金属ボールが入っている2ピンのデバイスです。このスイッチを垂直に置くと、2つのピンが接続されます。スイッチを傾けると、2つのピンが切断されます。

**必要なコンポーネント**

このプロジェクトでは、以下のコンポーネントが必要です。

全体のキットを購入する方が間違いなく便利です。こちらがリンクです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットに含まれるアイテム
        - 購入リンク
    *   - ケプラーキット
        - 450以上
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
        - 1（10KΩ）
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_tilt`
        - 1
        - 

**回路図**

|sch_tilt|

スイッチを垂直に置くと、GP14はハイ状態になります。傾けた後、GP14はロー状態になります。

10KΩの抵抗の目的は、傾斜スイッチが傾いた状態のとき、GP14を安定したロー状態に保つことです。

* :ref:`cpn_tilt`

**配線**

|wiring_tilt|

**コード**

.. note::

   * ファイル ``2.6_tilt_it.ino`` は、パス ``kepler-kit-main/arduino/2.4_colorful_light`` の下にあります。
   * または、このコードを **Arduino IDE** にコピーしてください。

   * **アップロード** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と正確なポートを選択することを忘れないでください。

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/0421b002-a697-4f22-a965-0e62e8dc3abf/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

プログラムが動作すると、ブレッドボード（傾斜スイッチ）を傾けると、シェルに「スイッチが作動します！」と表示されます。
