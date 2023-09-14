.. _ar_joystick:

4.1 - ジョイスティックの切り替え
================================

ビデオゲームをよくプレイするなら、ジョイスティックに非常に慣れているはずです。
通常、キャラクターを動かしたり、画面を回転させたりするために使用されます。

ジョイスティックがコンピュータに私たちの行動を読み取らせる仕組みは非常にシンプルです。
これは、直交する2つのポテンショメーターで構成されていると考えることができます。
これら2つのポテンショメーターは、ジョイスティックの垂直および水平のアナログ値を測定し、平面直角座標系での値（x,y）を生成します。

このキットのジョイスティックには、ジョイスティックが押されたときに作動するデジタル入力もあります。

* :ref:`cpn_joystick`

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
        - :ref:`cpn_resistor`
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_joystick`
        - 1
        - 

**回路図**

|sch_joystick|

SWピンは10Kのプルアップ抵抗に接続されています。これは、ジョイスティックが押されていないときにSWピン（Z軸）で安定した高レベルを得るためです。それ以外の場合、SWは一時停止状態にあり、出力値は0/1の間で変動する可能性があります。

**配線**

|wiring_joystick|

**コード**

.. note::

   * ファイル ``4.1_toggle_the_joyostick.ino`` は、 ``kepler-kit-main/arduino/4.1_toggle_the_joyostick`` のパスで開くことができます。
   * またはこのコードを **Arduino IDE** にコピーペーストしてください。
   * **アップロード** ボタンを押す前に、ボード（Raspberry Pi Pico）と正確なポートを選択してください。

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/dfe53878-7cb4-4543-bb97-7f5ef5aad15a/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

プログラムが実行された後、シェルはジョイスティックのx,y,z値を出力します。

* x軸とy軸の値は0から65535まで変動するアナログ値です。
* Z軸は、状態が1または0のデジタル値です。
