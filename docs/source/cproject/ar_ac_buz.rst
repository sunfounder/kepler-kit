.. _ar_ac_buz:

3.1 - ビープ音
==================
アクティブ・ブザーは、LEDを点灯させるのと同じくらい簡単に使える典型的なデジタル出力デバイスです！

* :ref:`cpn_buzzer`

**必要なコンポーネント**

このプロジェクトでは、以下のコンポーネントが必要です。

全体のキットを購入するのが確かに便利です、リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットのアイテム
        - 購入リンク
    *   - ケプラーキット
        - 450+
        - |link_kepler_kit|

以下のリンクから個々に購入することもできます。

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
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 1(1KΩ)
        - |link_resistor_buy|
    *   - 7
        - アクティブ :ref:`cpn_buzzer`
        - 1
        - 

**回路図**

|sch_buzzer|

GP15の出力が高い場合、1Kの電流制限抵抗を経て（トランジスタを保護するため）、S8050（NPNトランジスタ）は導通し、ブザーが音を出します。

S8050（NPNトランジスタ）の役割は、電流を増幅してブザーの音を大きくすることです。実際、GP15に直接ブザーを接続することもできますが、ブザーの音は小さくなるでしょう。

**配線**

キットには2種類のブザーが含まれています。
アクティブブザーが必要です。裏返して、密封された背面（露出したPCBではない）が必要なものです。

|img_buzzer|

ブザーは動作時にトランジスタを使用する必要があります。ここでは、S8050（NPNトランジスタ）を使用します。

|wiring_beep|

**コード**

.. note::

   * ファイル ``3.1_beep.ino`` は、 ``kepler-kit-main/arduino/3.1_beep`` のパスの下で開くことができます。
   * または、このコードを **Arduino IDE** にコピペしてください。

   * ボード（Raspberry Pi Pico）と正確なポートを選択したら、 **アップロード** ボタンをクリックする前に設定を忘れないでください。

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/62bf2c5d-9890-4f3a-b02a-119c2f6b0bf1/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

コードが実行された後、1秒ごとにビープ音が聞こえます。
